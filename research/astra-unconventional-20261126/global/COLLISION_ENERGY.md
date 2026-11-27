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

## A signed modulus-eight test with forced positive drift on escape

Let $\Phi(u)=u^2/(1+u)$. On odd integers define the fixed mean-zero periodic function
\[
 W(y)=\tfrac34-{\bf1}_{v_2(3y+1)\ge2}-{\bf1}_{v_2(3y+1)\ge3}.
\]
Its values on $y=1,3,5,7\pmod8$ are $-1/4,3/4,-5/4,3/4$, respectively. Set $\delta=3/4-\log_2(3/2)>0$. There is a quantitative signed obstruction with no integer-orbit test in its finite left side:
\[
 \liminf_{k\to\infty}\frac1k\sum_{\substack{0<y<2\cdot3^k\\y\ {\rm odd}}}
 W(y)\Phi\!\left(\frac{3^k p_k(y\bmod3^k)}{y}\right)
 \ \ge\ \delta\sum_{C\ {\rm escaping}}\Phi(H_C). \tag{11}
\]
If there is no escape the signed expression tends to zero by (10). An upper bound of zero along a subsequence would therefore rule out every ordinary escaping orbit under the named inputs. This only asks for cancellation of one fixed arithmetic test on the clipped original-law trace.

For the proof, on an escaping ray put $e_n=v_2(3a_n+1)$, $A_N=\sum_{n<N}e_n$. Corrected heights give $2^{A_N}P(a_N)=3^N P(a_0)$ and $P(a_N)\ge1$. Consequently $A_N/N\le\log_2 3+O(1/N)$. For each $e\ge1$, ${\bf1}_{e\ge2}+{\bf1}_{e\ge3}\le e-1$. It follows directly that
\[
 \sum_{n<N}W(a_n)\ge N(7/4)-A_N\ge \delta N-O_{a_0}(1). \tag{12}
\]
On every fixed escaping tail, the two-sided limits in (3) let one replace $\Phi(g_k(a_n))$ by $\Phi(H_C)$ throughout $0\le n\le k$ with total error $o(k)$, since $W$ is bounded. For $n>k$, the first-power bound (2), $\Phi(u)\le u^2$ and the positive-lag limit give a total $o(k)$ just as for (4). The fixed periodic and transient sites contribute $o(k)$. Outside the orbits through $M$, $\Phi(g_k)\ll M^{-\delta_0}g_k$ for the positive exponent $\delta_0$ of the complementary layer estimate. Its signed normalized contribution is thus $O(M^{-\delta_0})$ in absolute value. Use (12) for each of the finitely many remaining escaping tails, let $M\to\infty$, and finally use (8) and the global Lipschitz bound for $\Phi$ to replace $g_k$ by $u_k$. This proves (11).

The same arithmetic test can be read from dyadic target lifts. If $y$ is odd, $j\ge0$ and $k\ge1$, then $u_k(2^j y)$ is the ordinary harmonic fibre at $y$ restricted to sources whose last exponent exceeds $j$. Reconstructing an inverse word ending at $2^j y$ adds $j$ to its final exponent to get a word ending at $y$, leaving $3^k2^{-A}/(2^j y)$ equal to the latter word's harmonic weight. In particular there is no assumption of unbiased parity at these lifts. Weaver's solenoid equidistribution concerns dyadic pushforwards of the stationary joint real/ternary law, with an explicitly exceptional ordinary integer diagonal. It gives no estimate of the signed finite sums in (11). [Weaver, Paper 19, §§9–10.6](https://rstation.ai/problems/collatz/papers/19)

### A counterexample to cancellation from ternary regularity alone

There is an explicit probability density $f$ on the $3$-adic units whose finite Haar conditional densities $f_k$ have all the following properties. They have a uniform positive unit floor, exponentially fast $L^1$ convergence, a finite limit at each fixed positive ordinary integer, maximum of order $(3/2)^k$, and Haar quadratic energy of order $k$. The limiting $f$ is in weak $L^2$ and in every $L^p$ for $1\le p<2$, and has infinite second moment. Nevertheless
\[
 \liminf_k\frac1k\sum_{0<y<2\cdot3^k,\ y\ {\rm odd}}
 W(y)\Phi(f_k(y)/y)>0. \tag{13}
\]
This separates (11)'s missing cancellation from strong absolute and harmonic regularity for consistent ternary reductions. The constructed density is a different law from the Syracuse affine fixed point.

Here are the construction and bounds. Choose $z_n=24n+7$ for $n\ge6$ and put $B_n=z_n+3^n\mathbb Z_3$. These are unit cylinders with $z_n<3^n$, and $W(z_n)=3/4$. The positive spikes
\[
 b(z)=\sum_{n\ge6}z_n{\bf1}_{B_n}(z)
\]
lie in every finite $L^p$ by $\sum z_n3^{-n/p}<\infty$, with exponential conditional-expectation approximation in each such space. Disjointness is unnecessary. For $n\le k$ the bump is already resolved. Its normalized contributions at the other positive odd lifts in the representative window have $\ell^2$ norm at most $C z_n/3^n$, by summing the squares over $y=z_n+2j3^n$, $j\ge1$. If $n>k$ and $z_n<2\cdot3^k$, its sole positive odd representative is $z_n$. If $z_n\ge2\cdot3^k$, its averaged height is $z_n3^{k-n}$, and the sum of these heights is bounded uniformly in $k$ and tends to zero. It follows by the $\ell^2$ triangle inequality that on all sites with $W<0$ the vector $b_k(y)/y$ has uniformly bounded squared sum. Each $z_n$ with $6\le n\le k$ has $b_k(z_n)/z_n\ge1$. At a fixed positive integer, only finitely many resolved bumps meet it, and the unresolved ones through that integer eventually have $z_n\ge 3^k-O_y(1)$, hence their contribution vanishes. Also $\|b_k\|_\infty=O(k^2)$ by summing the first $k$ bump heights and their averaged tail.

To supply the exact critical integrability threshold and maximal exponential growth, put $\eta=\log_2(4/3)$. In the first $j$ least-significant ternary positions, allow digits $1,2$ at exactly $\lfloor\eta j\rfloor$ positions and require digit $2$ at all others. One consistent choice makes position $j$ free when $\lfloor\eta j\rfloor>\lfloor\eta(j-1)\rfloor$. Let $L(z)$ be the length of the initial admissible segment. With Haar probability,
\[
 m\{L\ge j\}=3^{-j}2^{\lfloor\eta j\rfloor}\asymp(4/9)^j.
\]
Set $s(z)=(3/2)^{L(z)}$ on units and zero on nonunits. Its Haar tail is comparable to $t^{-2}$. On an admissible depth-$k$ cylinder, $s_k$ is comparable to $(3/2)^k$ because the conditional probability of surviving a further $j$ levels is at most $2(4/9)^j$. Elsewhere it equals $s$. The squared expectation of $s_k$ is of order $k$, since for $j<k$ the probability of $L=j$ is comparable to $(4/9)^j$, and each such level contributes order one. Its $L^1$ approximation error is $O((2/3)^k)$. At every positive integer $y$ with $j$ initial admissible digits, $y\ge(3^j-1)/2$ because every admissible digit is at least one. Therefore $s_k(y)\ll(1+y)^{\log_3(3/2)}$ uniformly in $k$. This exponent is less than $1/2$, so $\sum_{y\ge1}(s_k(y)/y)^2=O(1)$ uniformly.

Finally set $f=({\bf1}_{\mathbb Z_3^\times}+c b+s)/Z$, normalized to total mass one. Choose the fixed $c\ge1$ so that $c\int b$ exceeds the mass of the other two summands. Then $f$ puts more than half its mass on $1\bmod3$ because every bump lies there. The Syracuse law puts exactly $1/3$ there, the probability of an even first exponent. Thus the exact affine recursion already fails on the first quotient. Its lower floor, critical index, maximum, energy, convergence, and fixed positive traces follow from the preceding bounds. On $W<0$ sites the total clipped contribution stays bounded because $\Phi(u)\le u^2$. The $k-5$ distinct marked sites contribute at least $(3/4)(k-5)\Phi(1/Z)$, proving (13). Any proof of cancellation through the exact Syracuse transfer must use structure beyond these matched properties.

The counterexample can also match arbitrarily many exact Syracuse quotients. Fix $d\ge1$, put $g=b+s$, and let $g_d$ be its depth-$d$ conditional expectation. For sufficiently small $\epsilon>0$ the density $f^{(d)}=\rho_d+\epsilon(g-g_d)$ has $\rho_d-\epsilon g_d\ge\rho_d/2$ on units and is zero on nonunits. Its reductions through $d$ are exactly the original Syracuse reductions, so its integral is one. Beyond $d$ the density consists of a bounded, nonnegative baseline and $\epsilon g$. All the bounds above persist, with constants allowed to depend on $d,\epsilon$, and (13) still holds by replacing the marked-site lower bound with $\Phi(\epsilon)>0$. Since $g-g_d$ is nonzero, distinct $\epsilon$ give distinct densities. At most one can satisfy the full Syracuse affine recursion: its projection at depth $k$ is uniquely the original $k$-word law, as the first $k$ ternary digits of the iterated affine recursion are independent of the remaining seed. Thus one can select $\epsilon$ for which an affine quotient identity fails strictly beyond $d$.

A one-depth perturbation quantifies the precision loss at the actual finite law. Use specifically Paper 12, §2, Input D, which imports a single $\alpha>0$ with $\rho_j(r)\ge\alpha$ for **every** $j\ge1$ and every ternary unit residue. Fix $\epsilon>0$, $q=3^k$, and choose $m=k-\lceil\log_3(Ck)\rceil$, where $C$ is a fixed sufficiently large constant depending on $\epsilon/\alpha$. Write $N=3^{k-m}$. For $1\le i\le k$ put $z_i=24i+7$. At sufficiently large $k$ these are distinct unit classes modulo $3^m$, all below $3^m$. Perturb the genuine depth-$k$ density by
\[
 \widetilde\rho_k(r)=\rho_k(r)+\epsilon\sum_{i=1}^k z_i
 \left({\bf1}_{r=z_i\bmod q}-N^{-1}{\bf1}_{r=z_i\bmod3^m}\right).
\]
Each parent has unchanged total, so every original quotient law through $m$ is exact. Each subtraction is at most $\epsilon(24k+7)/N\le\alpha/2$, which gives a probability law. The total variation distance is $O_\epsilon(k^2/3^k)$ by summing the added masses. At every marked positive lift $z_i$ the normalized amplitude increases by $\epsilon(1-N^{-1})$. Convexity and $\Phi(0)=0$ imply $\Phi(u+a)-\Phi(u)\ge\Phi(a)$ on $u,a\ge0$. Away from those marked lifts, the total absolute loss in the signed clipped sum is bounded by the Lipschitz constant times
\[
 \|W\|_\infty\frac{\epsilon}{N}\sum_{i=1}^k z_i
     \sum_{j=1}^{N-1}\frac1{z_i+2j3^m}
 \ll_\epsilon \frac{k^2\log(2N)}{3^k}=o(1).
\]
Thus the change in the signed sum divided by $k$ has liminf at least $(3/4)\Phi(\epsilon)>0$, despite exponentially small total variation error and exact agreement until the final $O(\log k)$ levels. This is an instability of replacing the exact fine quotient by a nearby law. The triangular array does not satisfy the complete affine recursion. [Uniform all-residue atom floor as imported in Paper 12](https://rstation.ai/problems/collatz/papers/12)

In fact this array converges in $L^1$ to the true stationary ternary density and satisfies the one-step affine recursion to $O_\epsilon(k^2 3^{-k})$ in total variation, because the affine pushforward is a total-variation contraction and the original finite laws satisfy that recursion exactly. Every fixed quotient is eventually exact. The signed discrepancy persists in this array because exact refinement at its changing finest levels is absent.

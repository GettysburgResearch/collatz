# The stationary trace on every proportional ordinary interval

Write $U(n)=(3n+1)/2^{v_2(3n+1)}$ on positive odd integers, $D=\log(4/3)$, $\kappa=D/2$, $I_Y=[Y,\lambda Y]\cap(2\mathbb N+1)$ for fixed $\lambda>1$, and $\eta=1/64$. All unsubscripted logarithms are natural. Use additive Haar probability $\nu$ on $\mathbb Z_3$. The canonical stationary trace $h(n)$ is evaluated at the *actual integer* before sampling. Valbuena's greatest lower semicontinuous stationary density $E$ has $E(n)=h(n)$ and $\int E\,d\nu=1$. The locally constant infima $e_k(z)=\inf_{n\ge1,\ n\equiv z\bmod 3^k}h(n)$ increase to $E$. For a nonperiodic odd unit $n$ the trace has $h(n)=\kappa n\beta_n$, with $0\le\beta_n\le d_n$, where $d_n$ is the relative natural density among odd sources of the full predecessor basin $B_n$. Odd multiples of three have $h(n)=d_n=0$. [Valbuena, stationary envelope, pin a7275d5](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex) · [Weaver 102/v1, §6 (26)–(29)](https://rstation.ai/problems/collatz/papers/102).

**Theorem.** Fix $0<s<\eta$. For every prescribed $w(n)\to\infty$ with $w(n)\le n^s$ eventually,
\[
       \sum_{n\in I_Y}\frac{\min\{h(n),w(n)\}}n
               \longrightarrow \tfrac12\log\lambda .                  \tag{1}
\]
In fact, let $L=\lfloor Y^{1-\eta}\rfloor$, $F$ the positive odds through $L$, $V(F)=\bigcup_{f\in F,i\ge0}\{U^if\}$, $K=\lfloor(\log Y)/2\rfloor$, and $\tau_F$ the first entrance grade, allowing grade zero and infinite waiting time. Then
\[
 \begin{split}
  G_Y&=\{n\in I_Y:n\notin V(F),\ \tau_F(n)\le K\},\qquad
  |I_Y\setminus G_Y|=O_\lambda(Y^{1-\eta}\log Y),\\
  &\sum_{n\in G_Y}\frac{h(n)}n\longrightarrow\tfrac12\log\lambda .
 \end{split}                                                           \tag{2}
\]
The second sum is *uncapped*. Its complement specifies where an untruncated excess can survive.

With uniform natural sampling on $I_Y$, the joint law of $(n/Y,n,h(n))$ on $[1,\lambda]\times\mathbb Z_3\times[0,\infty]$ converges to $(V,Z,E(Z))$, where $V$ is uniform on $[1,\lambda]$ and independent of Haar $Z$. With normalization by $\sum_{n\in I_Y}1/n$ and harmonic sampling, $V$ instead has density $(v\log\lambda)^{-1}$. Both samplings have capped first mean tending to $1$ and uncapped $p$-moment tending to $\int E^p\,d\nu$ for $0<p<1/128$. Uniform sampling of the positive odds through $X$ gives the same conclusions, with $V=n/X$ asymptotically uniform on $[0,1]$. All statements are source-qualified written deductions.

## The ordinary exception count

Put $N=\log Y$. For the native shortcut map $T$, set $k=\lceil\log_2(\lambda Y)\rceil$. The elementary two-case parity count bounds $|T^k([1,\lambda Y]\cap\mathbb N)|\ll_\lambda Y^{49/50}$. Indeed the starts with more than $3k/5$ odd steps number at most $(5/2)^k(2/3)^{3k/5}$, by binary parity coding and an exponential weight. The remaining images are at most $3^{3k/5}+(3/2)^k$ by the affine iterate formula. The three exponential bases are at most $2^{49/50}$. For any finite family of complete shortcut orbits the number of their distinct sites through height $\lambda Y$ is at most this image size plus $2k$ per seed. To see this, add the orbits one by one, decomposing each newly added part into a simple path stopped on entering previously added vertices, or a tail and its own cycle, or an infinite simple path. Cycles act bijectively under $T^k$. Delete at most the last $k$ positions of each finite path so that the retained positions have distinct $k$-step images in their own piece. The bound follows by restricting to starting positions of the indicated height. Each odd orbit is contained in its native shortcut orbit. Therefore
\[
             |V(F)\cap I_Y|\ll_\lambda Y^{49/50}+L\log Y.
\]
[Elementary one-orbit compression, PR212 at 3131111](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md) · [Weaver 178/v1, §5 following (14), union of complete orbits](https://rstation.ai/problems/collatz/papers/178/v1).

Let $G_i^*$ be independent geometric gaps with $\Pr(G_i^*=e)=2^{-e}$ for $e\ge1$, and $V_j^*=\sum_{i=1}^j(G_i^*\log2-\log3)$, including $V_0^*=0$. Set $b=\lfloor0.9\log_2Y\rfloor$. An odd source chosen uniformly from $I_Y$ has its first $K$ genuine gaps coupled to these independent gaps except with probability $O_\lambda(Y^{-1/50})$. The uniform odd residues mod $2^{b+1}$ determine all gaps when their total is at most $b$; each odd gap word of total $g$ occupies one odd residue mod $2^{g+1}$, with relative mass $2^{-g}$. Odd residues of uniform sources in $I_Y$ deviate in total variation by $O_\lambda(2^b/Y)$. The iid overflow has probability at most $(5/3)^K(4/5)^b$ since $\mathbb E(5/4)^{G_1^*}=5/3$. Its exponent $\frac12\log(5/3)-0.9\log(5/4)/\log2$ is below $-1/50$.

If a source $n$ misses $F$ through grade $K$, its affine log correction through that grade is at most $K/(3L)$. On successful coupling,
\[
 V_K^*\le\log(n/L)+K/(3L)\le\eta N+O_\lambda(1).
\]
Since $\mathbb E e^{-V_1^*/2}=\sqrt3/(2\sqrt2-1)<19/20$, exponential Markov bounds this event by $O_\lambda(Y^{\eta/2-1/40})$. Here $1/40-\eta/2>\eta$. This proves the count in (2).

## Transfer of complete good-site occupation to a nearby ordinary source

Set $B=\lceil2\lambda Y\rceil$. For a positive odd landing label $z\le B$, let $\Phi(z)$ count distinct visits to $G_Y$ from $z$ before its first entry into $F$. Set $\Phi(\infty)=0$. No orbit avoiding $F$ forever can visit $G_Y$. From the first eligible visit, entrance into $F$ occurs within $K$ further steps. An eligible site can never be visited after that entrance, since it lies outside $V(F)$. Hence $0\le\Phi\le K+1$ throughout. For every source above $B$ its entire lifetime count of distinct visits to $G_Y$ equals $\Phi$ of its first odd landing through $B$, including failure. An orbit hitting a periodic $n$ and subsequently $F$ would put $n$ in $V(F)$, so all eligible sites are nonperiodic.

Use the smooth odd source $\mathbf U_X$ with mass proportional to $\rho(\log_2(n/X))$, where $\rho$ is the fixed smooth bump of Weaver's input, supported on $[X/2,4X]$ in physical coordinates. For fixed $Y$, finite additivity of expectation, partial summation, and the genuine odd densities give
\[
    \lim_{X\to\infty}\mathbb E\Phi(\operatorname{Pass}_B(\mathbf U_X))
         =\sum_{n\in G_Y}d_n .                                        \tag{3}
\]
Use $\gamma=1.001$ from that input. Fix $\gamma<\xi_1<\xi_2<\gamma^2$, and take $X=B^\xi$ with $\xi_1\le\xi\le\xi_2$. Then $x=X^{1/\gamma}>B$. Weaver's stopped-set comparison (20), iterated at $x,x^\gamma,x^{\gamma^2},\dots$, compares the landing law from this $\mathbf U_X$ to the law at every successive ladder scale. For all increasing $Y$ the cumulative variation bound, uniformly in this interval of $\xi$, is
\[
  O\!\left(\sum_{j\ge0} e^{-c(\log\log x+j\log\gamma)^2}\right)
       =O_A((\log Y)^{-A})
\]
for every fixed $A$. The estimate includes failure; the finite-set estimate suffices directly for the nonnegative test that vanishes at failure. Apply it to the $K+1$-bounded test and then send the far ladder index to infinity in (3) at each fixed $Y$. Thus uniformly in the reference interval
\[
     \sum_{n\in G_Y} d_n
        =\mathbb E\Phi(\operatorname{Pass}_B(\mathbf U_X))+o(1).
                                                                         \tag{4}
\]
This use of first-landing variation tests actual deterministic subsequent visits. The finite bound on their number is essential. [Weaver 102/v1, smooth source (11)–(12), §4 Lemma 5 (20)–(21) and ladder sum (24)](https://rstation.ai/problems/collatz/papers/102).

## The averaged real window

For these nearby $X$, couple $\mathbf U_X$ to $\log X+\log v$ in logarithmic height and to the independent gaps of the preceding section. Here $v$ has the compactly supported continuous density proportional to $\rho(\log_2 v)$ on $[1/2,4]$, independent of the gaps and its source scale. For details take a uniform odd residue mod $2^{b+1}$, independent of $v$, and round $Xv$ to the closest integer in this residue. Its mass on each lattice point differs in total variation from $\mathbf U_X$ by $O(2^b/X)$: integration over its cell of length $2^{b+1}$ replaces the Lipschitz weight by its central value at relative scale $O(2^b/X)$ in total absolute mass, including the support boundary. The discrete smooth normalizing sum is $X/2$ times the continuous integral plus $O(1)$. Couple the residue to an infinite random odd binary integer extending it, so that its gaps are iid and independent of $v$. Outside the overflow and total variation events the actual first $K$ gaps agree and $|\log\mathbf U_X-\log X-\log v|=O(2^b/X)$.

A source missing $F$ through $K$ has $V_K^*\le(\eta+\gamma^2-1)N+O_\lambda(1)$ on the coupling. Its probability is $O_\lambda(Y^{-c_1})$ for some $c_1>0$, by the same exponential Markov estimate since $(\eta+\gamma^2-1)/2<1/40$. Up to its first entry in $F$ the affine log correction is at most $K/(3L)$. All eligible visits from a coupled source entering $F$ by $K$ therefore occur at indices $j\le K$ with
\[
   \log X+\log v-V_j^*\in
   [\log Y-\delta_Y,\ \log(\lambda Y)+\delta_Y],
       \qquad \delta_Y=O(2^b/Y+K/L)=o(1).
\]
Each coupling or entrance failure costs at most $K+1$ in the actual occupation, for a total $o(1)$. The reference sources all exceed $B$ for large $Y$. This gives an upper bound for the right side of (4) by the expected number of visits of the ideal walk to this widened band, counting all $j\ge0$, plus $o(1)$.

Now average $\log X$ uniformly from $\xi_1\log B$ to $\xi_2\log B$. Put $a=\xi_1\log B-\log Y$, $c=\xi_2\log B-\log Y$. Both endpoints and their difference are positive fixed multiples of $N$ to leading order. At a given $j$, intersection of the eligible $\log X$ interval with the averaging interval has length at most $\log\lambda+2\delta_Y$ and can be nonempty only if $V_j^*\in[a-C_0,c+C_0]$ for some $C_0=C_0(\lambda)$. By independence, the averaged expectation is bounded by
\[
 \frac{\log\lambda+2\delta_Y}{c-a}
        \sum_{j\ge0}\Pr(V_j^*\in[a-C_0,c+C_0])+o(1).
\]
The sum is $(c-a)/D+o(N)$. Indeed the increments have mean $D$ and exponential moments near zero. For $j$ up to a sufficiently large constant multiple of $N$, deviation from $Dj$ by more than $\epsilon N$ costs $O_\epsilon(e^{-c_\epsilon N})$ by either exponential tilt. The indices whose means lie in the two edge strips of width $2\epsilon N$ number $O(\epsilon N+1)$. For $j$ above that multiple of $N$, a fixed negative tilt bounds the probability by $O(e^{-c'j})$. Squeezing the bulk and sending $\epsilon$ to zero gives the assertion. In particular
\[
                \limsup_{Y\to\infty}\sum_{n\in G_Y}d_n
                       \le\frac{\log\lambda}{D}.                         \tag{5}
\]

## Matching lower bounds, moments, and the remaining orbit

Equation (5) times $\kappa$ is the desired upper bound for the good sum. Each fixed $e_k$ is bounded, below $h$ and, eventually, below every admissible cap. Its harmonic mean on $I_Y$ tends to its Haar mean, by summing the finitely many residue classes. Omitting the exceptional sites changes its harmonic sum by $o(1)$. Monotone convergence gives $\int e_k\,d\nu\uparrow1$, proving the lower bound in (2). On the exceptional set the $w$-capped harmonic sum is $O_\lambda(Y^{s-\eta}\log Y)=o(1)$, which proves (1).

On every subinterval $[aY,bY]$ with $0<a<b$ fixed, (1) gives the limiting integral $(\log(b/a))/2$. This identifies the weak limit of the capped harmonic measures in the physical coordinate; weighting by the continuous coordinate $n/Y$ gives the natural measure. The joint law follows from the same common-minorant argument on each such interval. The spatial and ternary coordinates alone have independent limits by finite progressions. In any subsequential joint limit the trace coordinate $H$ exceeds each continuous $e_k(Z)$ almost surely. For every fixed finite $M$, the limiting mean of $H\wedge M$ is at most one by (1). Thus $H=E(Z)$ almost surely. Writing $\rho_k=\mathbb E_\nu[E\mid z\bmod 3^k]$, the physical mean of $|\min(h,w)-\rho_k|$ has iterated limsup at most $2(1-\int e_k\,d\nu)$, since $e_k$ is below both functions eventually. This also gives physical $L^1$ approximation by the actual finite rows as $k\to\infty$.

For an odd periodic unit, the product on its least lap is at most $3n/(3n+1)$ because the lap includes the factor at $n$. The full trace formula hence gives $h(n)\le\kappa n(3n+1)$ there, also valid at all other odd sites. Thus the raw exceptional $p$-moment costs $O_\lambda(Y^{2p-\eta}\log Y)=o(1)$ for $2p<\eta$. On $G_Y$, its tail past $h>M$ is bounded in harmonic mean by $M^{p-1}$ times the bounded good first mean. Uniform integrability and the joint weak law prove the raw moment statement, including bounded continuous physical and ternary factors. For natural sampling up to $X$, use fixed proportional subintervals of $[\epsilon X,X]$. The contribution from $[1,\epsilon X]$ is $O(\epsilon)$ after normalization, by summing dyadic octaves with their uniformly bounded capped or $p$-moment means. This proves the endpoint assertion. [Valbuena, first-hit and full-lap trace formula, pin a7275d5](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex).

On a fixed escaping ray $r_i$ the original profile has $h(r_i)/r_i\to H_C>0$. Once its fixed seed belongs to $F$, every site of that ray lies in $V(F)$. For $s<1/64<1-49/50$, the entire ray has finite harmonic mass after the site cap $n^s$, by the uniform single-path packing and dyadic summation. Thus the growing physical cap in (1) and the exact bulk calculation in (2) leave open all post-floor returns on that fixed ray. A bound on those untruncated returns would require an additional input. [PR212, spatial trace profile, pin 3131111](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-global-20261128/escape/SPATIAL_TRACE_TAIL.md).

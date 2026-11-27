# First-crossing budgets with an integer parameter

For each proposed nonnegative integer $r$, there is an explicit program, containing only $r$, which attains the defect rate in [the escape flux identity](../phase9/ESCAPE_FLUX.md) if the number of ordinary escaping components equals $r$. In that case its marked set contains exactly $r$ vertices in every sufficiently high dyadic octave. This removes the need to hard-code a representative seed from each component. The parameter's correct value and the onset of the octave count are unknown.

For integer $k\ge1$ and $0\le N\le k$, let $G_k(N)$ be the set of different first crossings of $2^k$ from the ordinary seeds $1,\ldots,N$. A seed contributes its first physical iterate at least $2^k$ when it has one. A repeat below threshold ends its finite search with no crossing. Every seed is below $2^k$; each crossing belongs to $[2^k,(3/2)2^k)$, and membership in $G_k(N)$ is decidable. Define
\[
      f_r(k)=\max\{0\le N\le k:\ |G_k(N)|\le r\}.
\]
The empty seed list is admissible, so this is a total, computable integer. The gate count is nondecreasing in $N$. For fixed $N$, it is nonincreasing in $k$ whenever $k\ge\max(1,N)$: each higher crossing lies on the future of one preceding crossing, and each preceding crossing yields at most one crossing of the next threshold. Consequently $f_r(k)$ is nondecreasing in $k$.

For each finite $N$, the eventual value of $|G_k(N)|$ equals the number of escaping components represented by $1,\ldots,N$. Each bounded seed ultimately drops out; escaping seeds in the same component merge at a finite ordinary state, after which their first crossings are identical above their respective pre-merger peaks. Distinct escaping components have disjoint trajectories. Therefore, for the true number $c$ of escaping components, allowing infinity,
\[
                  f_r(k)\longrightarrow\infty
                     \quad\Longleftrightarrow\quad c\le r .              \tag{1}
\]
Indeed if $c\le r$, every fixed $N$ is eventually admissible. If $c>r$, choose $N$ covering $r+1$ distinct escaping components; for all sufficiently large $k$ this $N$ is inadmissible and every larger candidate fails as well.

Mark the set
\[
                       E_r=\bigcup_{k\ge1}G_k(f_r(k)).
\]
It is decidable by the one indicated finite-level computation per ordinary input; there are at most $r$ marks per octave. If $c\le r$, (1) ensures every escaping seed is included at every sufficiently large level and hence reaches marks arbitrarily far along its own orbit. The program for $B_{E_r}$ searches from its input until a mark or a first repeat and takes the maximal true slope product up to that time, including the empty product. Thus $u_r=B_{E_r}^{-2}$ is a total, strictly positive rational function under this hypothesis. Monotonicity of $f_r$ ensures the next octave of every marked seed is also monitored. The first-passage estimate from the main theorem gives maximum one-edge positive log defect $2\log3$, with all violations supported on $E_r$.

Suppose $c=r<\infty$. Above some level, $f_r(k)$ includes representative seeds $s_1,\ldots,s_r$ from every escaping component. Their $r$ distinct crossings already exhaust the allowed budget. From that level on the only marks are the crossing states of those selected trajectories, one in each component. For consecutive marks $y_{i,k},y_{i,k+1}$ on any one trajectory, the positive log defect at $y_{i,k}$ is at most $2\log(y_{i,k+1}/y_{i,k})$ by first passage. The finitely many earlier marks contribute a finite constant. The upper estimate telescopes and the finite simple-path lower estimate in the main theorem gives
\[
 \sum_{n\le X} [\log(a(n)^2u_r(n)/u_r(Tn))]_+
                =2r\log X+O(1),\qquad
            \#(E_r\cap[1,X])=r\log_2 X+O(1).
\]
The second equality counts marked sites; some marks need have no positive defect. For $r=0=c$, the empty marked set and repeated-path stopping give the same statements directly.

For $r<c$ the function $f_r$ eventually becomes constant. Its finite prefix of seeds can represent at most $r$ escaping components, by eventual stabilization of their crossing count. A missing escaping component contains no marks at sufficiently high levels. Since its path is simple, advancing along that path past the finitely many low marks gives an input from which the stopping program never returns. Thus the guarantee of totality is itself conditional on $c\le r$. Formula (1) does not provide an algorithm to recognize an unbounded computable sequence, find $c$, or establish universal ordinary convergence.

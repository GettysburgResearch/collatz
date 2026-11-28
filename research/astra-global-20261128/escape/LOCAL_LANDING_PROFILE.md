# A local profile for the complete first-landing labels

**Source-qualified written theorem.** The transfer from arbitrary distant ordinary octaves uses the uniform relative first-landing estimate of [PR213, equation (1)](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md). The positive floor on the ternary units imports the controlled landing theorem of Weaver, Paper 12. The unrestricted ternary density used to write the recursion for every $t>0$ follows from Tao, Proposition 1.14. The analytic inputs and limiting profile are written proofs. Weaver already studies the stationary ternary density restricted by the maximum prefix multiplier. His fixed-cap $O(n^2)$ maximum-density approximation and every-order $L^1$ error imply every finite moment at a fixed cap. Here the actual-label total-variation template, its record-time identification with this family, and the limiting ordinary entropy constant connect the earlier ternary bounds to first landings. [Weaver, Paper 146, §§1–2](https://rstation.ai/problems/collatz/papers/146).

Let $\lambda_3$ be normalized Haar measure on $\mathbb Z_3$, and let $\mu_B$ record the limiting first odd landing at or below the integer $B$, with a cemetery value on failure. There is a probability density $G$ on $[0,1]\times\mathbb Z_3$, for Lebesgue measure times $\lambda_3$. It belongs to $L^p$ for every finite $p\ge1$. Its relation to the actual integer labels is stronger than weak convergence. For each $\epsilon>0$ there is a nonnegative function $g(u,z)$ which is constant on finitely many intervals in $u$ and residue classes modulo a fixed power of three in $z$, such that $\|g-G\|_1<\epsilon$ and
\[
 \limsup_{B\to\infty}\left[\mu_B(\dagger)+\sum_{y\le B\ {\rm odd}}
       \left|\mu_B(y)-\frac2B g(y/B,y)\right|\right]<\epsilon .        \tag{1}
\]
The same statement holds on every sequence of actual source octaves $[X,2X)$ with $B\to\infty$ and $X/B\to\infty$. Formula (1) tests **every bounded function of the integer label**, even if it depends on its entire future or varies with $B$. The fixed templates can be evaluated at individual ordinary integers. An arbitrary Lebesgue–Haar representative of $G$ itself need not have meaningful values on that countable sampling set.

The entropy, in nats, has a common finite constant term:
\[
      \mathsf H(\mu_B)=\log(B/2)-\int G\log G\,du\,d\lambda_3+o(1).   \tag{2}
\]
This also holds for each of the actual source sequences just specified. The construction uses [the pinned relative landing theorem and bounded information moments](FIRST_LANDING_ENTROPY.md). No numerical value for the constant is asserted here.

## A finite template from a fresh octave

Fix a sufficiently large $v>0$, start from uniform positive odds in $[Be^v,2Be^v)$, and retain precisely the paths with first odd landing of grade $j\le L=\lceil C_0v\rceil$ and total physical clock at most $4L$. By the fresh-source estimate in [the entropy proof](FIRST_LANDING_ENTROPY.md) their missing mass is $O(e^{-cv}+B^{-c})$ as $B\to\infty$ for fixed $v$. For each of the finitely many words $w$ of these sizes, use forward order from source to target and denote its affine map by $x\mapsto J_w x+R_w$, $J_w=3^j2^{-S_w}$. An odd target $y$ has its unique positive odd ancestor for this word exactly when $y\equiv R_w\pmod{3^j}$. This is the successive inverse integer test. Let $\mathcal C_w$ be that ternary cylinder.

An allowed $u=y/B$ satisfies $u\le1$. Requiring the source to lie in the fresh octave amounts to
\[
              J_w e^v+R_w/B\le u<2J_we^v+R_w/B .
\]
For each nonempty suffix $w'$ of the word, the earlier odd state mapping to $y$ through this suffix must exceed $B$. Its condition is $u>J_{w'}+R_{w'}/B$. These inequalities specify the entire first-passage event. Define $I_w\subseteq[0,1]$ by setting the terms $R_{w'}/B$ and $R_w/B$ to zero, preserving the indicated inequalities. The empty word has empty interval here since $v>0$. Set
\[
            g_v(u,z)=e^{-v}\sum_w 1_{I_w}(u)1_{\mathcal C_w}(z).       \tag{3}
\]
Every legal word supplies exactly one distinct original source at a chosen target, with probability $2e^{-v}/B+O_v(B^{-2})$. Replacing those finitely many shifted interval endpoints changes $O_v(1)$ integer counts per word. The variation distance in (1) between the retained fresh probabilities and the sampled template tends to zero for fixed $v$. This reasoning also permits an interval that collapses to a point after the shifts are removed.

The relative landing comparison from the fresh octave to $\mu_B$ is $O(v^{-1/9})$ in sum norm for large $v$. Indeed the comparison is uniform on events, and two probability measures have sum norm twice their maximal event discrepancy. The preceding exceptional mass and normalization therefore give
\[
 \limsup_{B\to\infty}\left[\mu_B(\dagger)+
  \sum_{y\le B\ {\rm odd}}|\mu_B(y)-(2/B)g_v(y/B,y)|\right]
       \le C v^{-1/9}.                                                \tag{4}
\]
For any two fixed such templates the corresponding ordinary sample sum of their absolute difference tends to their $L^1(du\,d\lambda_3)$ distance. Each interval cut and ternary residue uses the elementary count of positive odds in that arithmetic progression. Hence (4) makes $g_v$ a Cauchy family in $L^1$ as $v\to\infty$. Its limit $G$ is nonnegative, has integral one and satisfies (1). For distant actual octaves apply the same uniform event comparison at their actual separation. The construction identifies the whole marked distribution of $(y/B,y\bmod3^m)$ at every fixed $m$. A fixed binary residue or any other fixed modulus coprime to six can also be adjoined: the template is constant on those classes at each fixed ternary residue, and the ordinary Riemann sums give their independent uniform law on the possible classes. In particular binary equidistribution refers to the fresh digits at the landing, not to conditional behavior after an arbitrarily growing number of future steps.

The limiting profile is zero at ternary multiples of three: a positive-depth odd landing is always a unit. The controlled near-first-landing theorem gives $\mu_B(y)\ge c/B$ at each odd unit $y\le B$ for sufficiently large $B$. Indeed its fresh source lower count $cX/B$ persists on taking the distant-source limit. An indicator of any fixed rectangle then gives $G\ge c/2$ almost everywhere on the unit trits by approximation. [Controlled first landing, anchored at every odd unit](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/critical-orbit-mellin/LOCAL_FIRST_LANDING.md) · [Weaver, paper 12, Theorem 14](https://rstation.ai/problems/collatz/papers/12).

## Integrability and the constant entropy deficit

For a finite union of interval–cylinder rectangles $E$, the physical labels $(y/B,y)\in E$ have count $(B/2)|E|+o(B)$ and limiting probability $\int_EG$. Apply the arbitrary-set estimate (1) of [the entropy theorem](FIRST_LANDING_ENTROPY.md). This gives $\int_E G\le C_\eta |E|^\eta$ for every $\eta<1$. By approximation in both finite measures it holds for every measurable $E$. Testing $E=\{G>s\}$ gives $|E|\le (C_\eta/s)^{1/(1-\eta)}$. Taking $\eta$ arbitrarily close to one proves $G\in L^p$ for every fixed finite $p$.

For (2) write $f_B(y)=(B/2)\mu_B(y)$ on the ordinary grid, using weight $2/B$ there. The positive tails of $f_B\log f_B$ are uniformly integrable under these grid measures by any information moment of order greater than one. The negative part near zero is uniformly negligible since $-s\log s\to0$ as $s\downarrow0$ and the grid has bounded total measure. The cemetery's contribution to the entropy correction $\mu_B(\dagger)\log((B/2)\mu_B(\dagger))$ tends to zero by its every-order bound (with $0\log0=0$). Approximate $s\log s$ by a bounded Lipschitz function which agrees on $[\delta,K]$ and vanishes at zero; for instance truncate outside this interval linearly or constantly. Equation (4) and the Lipschitz bound compare the grid average with its integral against $g_v$ under the product reference measure, with the Riemann limit taken first. Then let $v\to\infty$, use $L^1$ convergence, and remove the two truncations using the uniform integrability already given and $G\in L^2$. This proves (2) and the same argument for distant actual sources.

This representation keeps the true post-landing donor label and a lower bound on all unit labels. A sparse set of last exits has small first-landing probability. Its full predecessor set inside the floor can have order $B$ elements, including a positive fraction of all inputs if an escaping component exists. The first-to-last excursion through the low states remains unpriced by (1).

## A record-time formula and a recursive equation

Let $(E_i)_{i\in\mathbb Z}$ be independent with $\Pr(E_i=e)=2^{-e}$ for $e=1,2,\ldots$. Put $D=2\log 2-\log 3$, and form the backwards sums, positive record increment and stationary ternary phase
\[
 W_r=\sum_{i=0}^{r-1}(E_{-i}\log2-\log3),\qquad
 L=(\inf_{r\ge1} W_r)_+,\qquad
 Z=\sum_{r\ge1}3^{r-1}2^{-\sum_{i=0}^{r-1}E_{-i}}\ \in\mathbb Z_3.
\]
The last series converges in the ternary metric. The full ordinary first-landing profile in (1) satisfies
\[
 \int f(u,z) G(u,z)\,du\,d\lambda_3(z)
   =D^{-1}\mathbb E\int_0^L f(e^{-s},Z)\,ds .                         \tag{5}
\]
In particular $\mathbb E L=D$. A longer positive record increment receives proportionally more mass, with the logarithmic overshoot uniform inside it. The same past increments generate the ternary phase and the record increment, so the formula retains their dependence.

For the proof, start the uncorrected multiplicative model at $e^vU$ with $U$ uniform on $[1,2]$, and with an independent Haar ternary source. At each iid increment $E_i=e$, multiply the real coordinate by $3/2^e$ and send the ternary coordinate $z$ to $(3z+1)/2^e$. At its first real crossing of height one, truncate by the same $j,S$ as (3). On a fixed word the output real density is $e^{-v}/J_w$ on $I_w$ and the ternary distribution is normalized Haar on $\mathcal C_w$. Since the word probability is $2^{-S_w}$ and $\lambda_3(\mathcal C_w)=3^{-j}$, their product is exactly (3). Its missing mass tends to zero as $v\to\infty$ by (4) and unit total mass. The strong law gives almost sure crossing for this model. Thus the expectations of every bounded continuous $f$ at its crossing converge to the left side of (5). Their averages over $0\le v\le V$ have the same limit.

Write $S_0=0$ and $S_n=\sum_{i=1}^n(E_i\log 2-\log3)$, and let $Z_n$ be the ternary state after $n$ steps. In the average over levels, replacing $v+\log U$ by $v$ costs at most $2\|f\|_\infty\log2/V$, by a shift of integration endpoints on every sample path. A new record time $n$ first crosses precisely the levels between the old maximum $\max_{0\le j<n}S_j$ and $S_n$, apart from boundary points of zero length. Its contribution is $\int_0^{L_n} f(e^{-s},Z_n)\,ds$, where $L_n=(S_n-\max_{0\le j<n}S_j)_+$. Write $\tau(V)=\min\{n:S_n\ge V\}$. The final incomplete record costs at most $\|f\|_\infty\max_{n\le\tau(V)} E_n\log 2$ before division by $V$. The strong law gives $\tau(V)/V\to D^{-1}$, and the geometric tail gives $\max_{n\le N}E_n/N\to0$ almost surely.

Extend the walk to all negative times by the given iid increments. Its negative-time levels tend to minus infinity, so their finite maximum is eventually exceeded. Thereafter $L_n$ equals the stationary record increment made from all the increments before and including $n$. For $f$ depending on $z$ modulo $3^m$, the stationary ternary state agrees modulo $3^m$ with $Z_n$ once $n\ge m$. Birkhoff's theorem for the iid shift, with integrable envelope $\|f\|_\infty E_0\log2$, now gives (5) pathwise for the normalized full level integral. That integral is bounded by $\|f\|_\infty$, so expectation converges too. Uniform approximation of continuous $f$ by functions depending on finitely many trits extends the identity, and equality of finite measures gives it for bounded measurable $f$.

Put $J_e=3/2^e$ and $K=\sup_{r\ge1} e^{-W_r}$. It is finite and attained almost surely. For $t>0$ let $h_t$ be the ternary density of $\Pr(Z\in dz,K<t)$. These submeasures are dominated by the unrestricted law of $Z$, whose density exists by the oscillation estimate of Tao, Proposition 1.14: the ternary truncations have the Syracuse random-variable laws and their compatible Haar densities are Cauchy in $L^1$ by (1.26)–(1.27). [Tao, Almost all orbits of the Collatz map attain almost bounded values](https://arxiv.org/abs/1909.03562). One may take jointly measurable versions via conditional expectation. Changing variables $u=e^{-s}$ in (5) and peeling the final increment gives
\[
 G(u,z)=\frac{h_u(z)}{D u}\quad(0<u<1),\qquad
 h_t(z)=\sum_{\substack{e\ge1:\ 2^ez\equiv1\pmod3\\ J_e<t}}
      J_e\,h_{t/J_e}\!\left((2^ez-1)/3\right).                        \tag{6}
\]
The first relation holds almost everywhere in the product measure; the second is a Haar density identity for each fixed $t>0$. Indeed $Z=2^{-E_0}(1+3 Z')$ and $K=J_{E_0}\max(1,K')$ for the shifted pair $(Z',K')$. The image of a Haar ternary density on its eligible trit has density multiplied by $3$. Multiplying this by $2^{-e}$ gives the coefficient $J_e$. Also $h_t\uparrow d\Pr(Z\in dz)/d\lambda_3$ in $L^1$ as $t\uparrow\infty$.

For $0<t\le1$, every admissible term for $h_{t/2}$ has $e\ge2$. Lower its index by one in (6). This gives the exact scaling and its integrated height consequence
\[
     h_{t/2}(z)=\tfrac12 h_t(2z),\qquad
     G(u/2,z)=G(u,2z),\qquad
     \Pr_G(u\le t/2)=\tfrac12\Pr_G(u\le t).                            \tag{7}
\]
Multiplication by two preserves ternary Haar measure. In particular $\Pr_G(u\le2^{-k})=2^{-k}$ for all $k\ge0$. There is also a direct deduction of the continuum finite moments from the prior fixed-cap estimate. On $1/2\le u\le1$, (6) gives $G(u,z)\le (2/D)\sigma_2(z)$, where $\sigma_2$ is the density of the event $\max(1,K)\le2$ in Weaver, Paper 146. Its finite-depth approximants have $L^\infty$ norm $O(n^2)$ and $L^1$ error $O_M(n^{-M})$ for every $M$, so $\sigma_2$ has all finite moments by truncation. Equation (7) transfers the resulting bounds to the remaining dyadic intervals. The discrete information estimates used in (2) control the sampled ordinary labels in addition to this continuum integrability. [Weaver, Paper 146, §2](https://rstation.ai/problems/collatz/papers/146).

The real marginal density is $\Pr(K<u)/(D u)$ and is bounded by $2/D$ on $[1/2,1]$, hence essentially everywhere by (7). These iid formulae describe the first-landing limit of actual distant source octaves through (1). They give exterior source statistics on each fixed landing floor and allow its future labels as tests in (1); a law conditioned on climbing out after passing through a common low ancestor still requires the corresponding return probabilities.

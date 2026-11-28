# Joint physical grade fluctuations at multiplicatively distinct ordinary sources

Let $r\ge2$ and fix positive odd integers $A_1,\ldots,A_r$ such that $A_i/A_j\notin 3^{\mathbb Z}$ for every distinct pair. Let $n$ have Haar law on $\mathbb Z_2$. Write $k_m(x)$ for the number of odd shortcut departures during the first $m$ physical steps from $x$. Consider the linearly interpolated process whose values at the grid dates $m/N$ are
\[
      M^{(N)}(m/N)_i=\frac{2k_m(A_i n)-m}{\sqrt N}.
\]
Each marginal has the usual simple-walk limit. Jointly, on any bounded time interval, the laws are tight. Every subsequential limit is a continuous martingale $M$ with absolutely continuous bracket. Its bracket derivative $Q_t$ has trace $r$, and at almost every time its rank is at least
\[
                          d_r=1+\lceil\log_2 r\rceil.                    \tag{1}
\]
Its $d_r$-th largest eigenvalue is bounded below by a constant depending only on $r$. For $r=2,3$, this gives uniform positive definiteness in all directions, and at every fixed positive time every open ball in $\mathbb R^r$ receives positive mass uniformly over the possible subsequential limits. For all $r$ and $t>0$,
\[
  \sup_z\Pr(|M_t-z|\le\epsilon)
       \le C_r(\epsilon/\sqrt t)^{3r/(2r+1)}.                            \tag{2}
\]
In particular no rectifiable curve carries positive limiting mass. These statements use the true same-input parity paths and permit dependence of the limiting covariance on the path. The [dyadic line-incidence and entropy argument](MULTIPLIER_BERNOULLI_JOINING.md) separately identifies a unique joint limit with independent Brownian coordinates. The arguments below retain a direct native uniform-ellipticity test without invoking that additional rigidity.

For ordinary uniform sources on $[X,2X)$ the same conclusions apply up to a moving horizon $N\to\infty$ with $2^N=o(X)$, on rescaled time $[0,1]$. For any hypothetical positive integer cycle all of its distinct odd sites are units prime to three, so (1) applies with those sites as multipliers. Thus the simultaneous multiplicative perturbations of a cycle with $p\ge2$ odd sites have at least $1+\lceil\log_2 p\rceil$ diffusive clock directions. The multipliers and the cycle are fixed before sending the observation horizon to infinity. This assertion about their whole family of dilations gives no direct bound on the exceptional source $n=1$ or on physical first-hit clocks past the binary observation horizon.

## Both kinds of departures occupy every macroscopic interval

Use the binary source filtration $\mathcal F_m$ just before revealing bit $m$, starting with bit zero. Conditional on the prefix, each physical state has the form $c_i+a_i u$ in a common fresh Haar variable $u$, with $a_i=A_i3^{k_m(A_i n)}$ odd. Thus the signed grade increment vector is $v_m$ or $-v_m$ with equal probability, for a predictable $v_m\in\{-1,1\}^r$. A common change of sign does not affect $v_mv_m^{\mathsf T}$.

Fix two coordinates, and let $H_m$ count their mixed (opposite-parity) departures by time $m$. In [the physical Hamming theorem](MULTIPLIER_PARITY_SEPARATION.md), $\tau_j$ is the time just after the $j$th mixed departure, $W_j=\tau_{j+1}-\tau_j$, and $S_j$ is the grade difference there. Its proof establishes on the same probability-one set
\[
  \sum_{j<l}(W_j-\mathbb E_j W_j)=o(l),\qquad
  \mathbb E_j W_j\le 2+v(S_j),\qquad
  \sum_{j<l}v(S_j)=\bar v l+o(l),
\]
where $\bar v=3/2$ or $5/2$ as specified there. The second case uses the cited Bugeaud–Laurent two-adic logarithm estimate. If $R_l=o(l)$ then $\max_{l\le N}|R_l|=o(N)$. Subtract the two partial-sum formulas at two endpoints, retaining the one-sided expectation bound term by term on the interval. This gives, uniformly for $0\le j\le k\le N+1$,
\[
       \tau_k-\tau_j\le (2+\bar v)(k-j)+o(N).
\]
Thus for $0\le a\le b\le N$, using $\tau_{H_a}\le a$ and $b<\tau_{H_b+1}$, we obtain
\[
           H_b-H_a\ge (b-a)/(2+\bar v)-o(N)                             \tag{3}
\]
uniformly over both physical endpoints. This uses the predictable waiting envelope, not subtraction of two lower bounds on $H_m$.

There is a separate uniform lower for common departures. With input coordinate $x=c_i+a_i u$, write the other as $y=A x+B$ with $A$ an odd two-adic unit. If the current departures are mixed then $B$ is odd. When $x$ is even the next relation has slope $3A$ and intercept $(3B+1)/2$. When $x$ is odd the next slope is $A/3$ and its intercept is $(A+B)/2-2A/3$. The two children can both remain mixed only if $A\equiv B\equiv3\pmod4$. In that case both new slopes are one modulo four, so from either child at least one of its own two equiprobable children is common. Therefore at least one of the current date and the next two is common with conditional probability at least one half, for every starting prefix. The next-bit split is equiprobable since $a_i$ is odd, also when input parities are taken in the order of the $x$ coordinate.

Partition physical time into disjoint triples and count the indicator that each triple contains a common departure. Its conditional expectation given the initial prefix of the triple is at least one half. The bounded martingale difference strong law, followed by subtraction of its $o(N)$ partial sums uniformly in the endpoints, shows that every physical interval $[a,b)$ contains at least $(b-a)/6-o(N)$ common departures. Partial triples cost at most four sites. Together with (3), for all the finitely many pairs we have uniformly in $0\le a\le b\le N$,
\[
    \frac{b-a}{6}-o(N)\le H_b-H_a\le \frac{5(b-a)}6+o(N).              \tag{4}
\]
The mixed lower in (3) is actually at least $2(b-a)/9-o(N)$.

## Brackets and rank

The scaled predictable bracket is the interpolation of $N^{-1}\sum_{j<m}v_jv_j^{\mathsf T}$. Write it $V^{(N)}$. Its entries are uniformly Lipschitz. Tightness of $M^{(N)}$ follows from the fourth-moment bound $\mathbb E|M^{(N)}(b/N)-M^{(N)}(a/N)|^4\le C_r(b-a)^2/N^2$. Each individual signed increment sequence consists of independent fair signs, by the fresh bits and predictable coordinate signs; apply its exact fourth moment and $|x|^4\le r\sum_i x_i^4$. Linear interpolation gives the continuous-time tightness criterion on every fixed time interval. Joint subsequences therefore exist. In a limit $(M,V)$, each $M_i$ and each $M_iM_j-V_{ij}$ is a martingale for the joint filtration: test increments against bounded continuous functions of finitely many past values, pass to the limit by the fourth-moment bound and use a monotone-class argument. Interpolation errors at the test dates vanish in the corresponding expectations. Thus $V=\langle M\rangle$.

For any rational time interval the normalized increment of $V$ belongs to the convex hull of the sign outer products. Equation (4) bounds all of its off-diagonal entries in absolute value by $2/3$. One may pass these simultaneous constraints to any weak limit since the errors divided by $N$ vanish almost surely, hence in probability. Lipschitz continuity and differentiation show that $Q_t=dV/dt$ belongs almost everywhere to the compact set
\[
 \mathcal K_r=\{Q\in\operatorname{conv}\{vv^{\mathsf T}:v\in\{-1,1\}^r\}:\
                         |Q_{ij}|\le2/3\ (i\ne j)\}.
\]
Every $Q$ here has diagonal one. Write it as a positive combination of its supporting sign outer products, and put $d=\operatorname{rank}Q$. The supporting sign vectors span a space of dimension $d$. Choose $d$ independent support vectors as columns. Among the $r$ coordinate rows, no two sign patterns in these columns can be equal up to sign. That would make those two coordinates equal up to a fixed sign on the full support, giving $|Q_{ij}|=1$. At most $2^{d-1}$ sign rows are available up to sign, proving (1). Ordered eigenvalues are continuous on $\mathcal K_r$, so the positive $d_r$-th eigenvalue has a positive minimum there. Also the row-sum estimate gives
\[
             \lambda_{\max}(Q)\le \Lambda_r=(2r+1)/3.                   \tag{5}
\]

## Spatial concentration and support

Fix a terminal time $t>0$, centre $z\in\mathbb R^r$ and radius $\epsilon>0$. For $s\ge0$ set
\[
 u(s,x)=e^{1/(2\Lambda_r)}\epsilon^{2\beta}
 (s+\epsilon^2)^{-\beta}
 \exp\bigl(-|x-z|^2/(2\Lambda_r(s+\epsilon^2))\bigr),
 \qquad \beta=r/(2\Lambda_r).
\]
For every $Q\in\mathcal K_r$, $\partial_su-\tfrac12 Q:\nabla^2u\ge0$. Indeed the constant term in the derivative divided by $u$ is $[-\beta+\operatorname{tr}(Q)/(2\Lambda_r)]/(s+\epsilon^2)=0$, and the remaining numerator is proportional to $\Lambda_r|x-z|^2-(x-z)^{\mathsf T}Q(x-z)\ge0$. Itô's formula for $u(t-s,M_s)$ therefore bounds its final expectation by its initial value. At time parameter zero the function majorizes the required ball indicator, proving (2). In particular (2) gives zero mass to all sets of Hausdorff dimension strictly below $3r/(2r+1)$ by ball coverings. The uniform-in-centre limiting bound also gives a limsup bound for the finite physical laws, by tightness, compactness of the possible centres of balls of nonvanishing mass, and a slight enlargement of the radius.

For $r=2,3$ let $\eta I\le Q\le\Lambda_r I$ be the uniform bounds just proved. For completeness a bounded change of drift gives the uniform positive lower for an arbitrary open ball. Stop at $\tau_R=\inf\{s:|M_s-z|\ge R\}$ with $R>|z|$. Change measure using the stochastic exponential with integrand $Q_s^{-1}K(z-M_s)\mathbf1_{s\le\tau_R}$ against $M$. Its quadratic energy is at most $K^2R^2t/\eta$, so it is a probability density with second moment at most $\exp(K^2R^2t/\eta)$. Under the changed measure the process is a martingale $M'$ plus drift $K(z-M_s)$ until the stop and zero drift afterward; the martingale still has bracket $V$. The stopped quadratic distance identity gives $\Pr'(\tau_R\le t)\le(|z|^2+rt)/R^2$. On no exit, $M_t-z$ is equal to
\[
        -e^{-Kt} z+\int_0^t e^{-K(t-s)}dM'_s,
\]
whose unconditional second moment under the changed measure is at most $e^{-2Kt}|z|^2+r/(2K)$. Choose $R$ and $K$ so that the exit probability and the probability that this last expression is outside the requested radius are each below one quarter. Then the ball has changed probability at least one half, hence original probability at least $\tfrac14\exp(-K^2R^2t/\eta)$ by Cauchy–Schwarz. This proof requires ellipticity only for the two- and three-source assertions.

Finally the complete grade path to date $N$ is determined by the source modulo $2^N$. The discrepancy in total variation between a rounded ordinary octave and the Haar prefix law is $O(2^N/X)$, so the stated ordinary transfer costs no unproved bivariate clock approximation.

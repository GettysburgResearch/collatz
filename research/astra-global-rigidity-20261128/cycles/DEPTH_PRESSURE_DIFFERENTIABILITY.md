# Differentiability at every tilt for the untruncated depth pressure

Use the pinned model and uniform pressure theorem of [the full-range word theorem](FULL_CORRECTION_WORD_ENTROPY.md). This proves the remaining differentiability assertion in Polson–Sokolov R8, including at the depinning threshold. The argument works with the physical irrational rotation, allows all depths, and uses no random-environment assumption. [Polson–Sokolov, R8, pinned source](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex)

Let $T v=\{v+\alpha\}$ on the circle with normalized Lebesgue measure $dv$, $\theta=\log_2 3$, $\alpha=\theta-1$, $a_t=2^{-T^t v}$, and $c_t=\lfloor T^t v+\alpha\rfloor\in\{0,1\}$. The pinned paths have $j_0=j_n=0$ and $0\le j_{t+1}\le j_t+c_t$. Their reward is $\Phi=\sum_{t<n}r_t$, where $r_t=a_t2^{-j_t}$. Write $Z_n(\lambda,v)$ for the sum of $e^{\lambda\Phi}$ and $H=P(0)=\theta\log\theta-\alpha\log\alpha$. Uniform convergence of $n^{-1}\log Z_n$ to $P$ at every phase and on compact tilt intervals, and exact pinned supermultiplicativity, are the inputs from the full-range theorem.

**Theorem.** There is a number $0<\lambda_c<\infty$ such that $P=H$ on $[0,\lambda_c]$, $P'_+(\lambda_c)=0$, and $P$ is locally $C^{1,1}$ on $(\lambda_c,\infty)$. In particular $P$ is continuously differentiable on the entire nonnegative tilt axis. Combined with the uniform pressure theorem, this answers R8 for the valuation-word model. It asserts no exclusion of integer cycles.

## A positive delocalized interval

Let $p=1/\theta$, $q=1-p$, and take $k\ge1$ with probability $p q^{k-1}$. The real heights $y_t=j_t+T^t v$ change by $X=\theta-k$, a centered increment. Killing at a negative height imposes precisely the path constraint. Every length-$n$ word pinned at $v_n=T^n v$ has free probability $p^n q^{\lfloor v+n\theta\rfloor-n}=\exp(-nH+O(1))$, uniformly in the phase. Its reward is $\sum2^{-y_t}$.

Write $L$ for the killed free expectation in one step. Fix $0<a<\log 2$ (in particular $qe^a<1$). On the real line define $h(y)=C+y-e^{-ay}$. For $y\ge0$, strict convexity and $\mathbb E X=0$ give
\[
 h(y)-\mathbb E h(y+X)=(\mathbb E e^{-aX}-1)e^{-ay}>0.
\]
Given $y+X<0$, the overshoot $-(y+X)$ is a shifted geometric variable whose additive shift lies in $[0,1]$, by memorylessness. Its mean and $a$-exponential moment are uniformly bounded. Choose $C$ so that $h\ge1$ on the half-line and $\mathbb E[h(y+X)\mid y+X<0]\ge0$. Hence $h-Lh\ge c e^{-ay}$. Since $(C+y)2^{-y}\ll_a e^{-ay}$, for sufficiently small $\lambda>0$ this implies $e^{\lambda2^{-y}}Lh(y)\le h(y)$. Iterating bounds the killed, weighted free-word sum, including the pinned subset, uniformly for $v\in[0,1)$. Thus $P(\lambda)\le H$, and monotonicity gives equality. Also $P(\lambda)\ge\lambda\mu$, where $\mu=1/(2\log2)$, from the all-zero depth path. Convexity gives the stated finite, positive endpoint $\lambda_c=\sup\{\lambda\ge0:P(\lambda)=H\}$.

## A positive excursion has half the interior tilt

Let $K_l(\lambda,v)$ be the partition sum over pinned paths with $j_t>0$ for $0<t<l$, including the starting reward and excluding the terminal reward. For $l\ge2$ it vanishes unless $c_0=1$, and its first interior depth is then one. Subtract one from every positive interior depth and append a terminal zero. This injects the excursions into the pinned length-$(l-1)$ paths starting at $Tv$. The original interior reward is exactly half the resulting reward. Therefore, for $\lambda\ge0$,
\[
 K_l(\lambda,v)\le e^\lambda Z_{l-1}(\lambda/2,Tv).                 \tag{1}
\]
If $\lambda>\lambda_c$, convexity and $P(\lambda)>H$ imply $P(\lambda)>P(\lambda/2)$. Uniform pressure convergence yields $K_l/Z_l\le C e^{-\kappa l}$, uniformly over phases and over tilts in a compact neighborhood of each such $\lambda$. In any finite pinned bridge, conditional on a zero at each of two specified times $b,b+l$, the probability of no internal zero is exactly $K_l(\lambda,T^bv)/Z_l(\lambda,T^bv)$. This identity follows by replacing the intervening word with any pinned bridge. The chance of no zero on $[i,j]$ is at most $C' e^{-\kappa'(j-i)}$: sum this ratio over the two possible nearest bracketing zero positions, with at most $l+1$ choices per length $l\ge j-i$. If an interval contains a pinned boundary the chance is zero.

To control covariance take two independent replicas $x,y$ of the same finite bridge. For $i\le t<j$ call the edge usable if
\[
 \max(x_{t+1},y_{t+1})\le\min(x_t,y_t)+c_t.
\]
Then the two tails after $t$ can be exchanged. The first usable edge is determined by the unordered pair of heights at each position. The exchange is a weight-preserving involution and negates $(r_i(x)-r_i(y))(r_j(x)-r_j(y))$. If both replicas have a zero in $[i,j]$, their order must change or their heights must agree at some site there. An equality gives a usable adjoining edge in $[i,j)$, and a strict crossing gives a usable crossing edge by the displayed inequality and legality of the two original edges. Thus for $i<j$ the absolute covariance is at most $C e^{-\kappa'|i-j|}$. Indeed twice the covariance is the mean of the displayed product, bounded by one before cancellation. It follows that $\operatorname{Var}(\Phi)\le Cn$ on each of these compact tilt neighborhoods. The second derivative of $n^{-1}\log Z_n$ is $\operatorname{Var}(\Phi)/n$. Passing to the limit using centered second differences and convexity yields $P\in C^{1,1}_{\rm loc}((\lambda_c,\infty))$.

## The critical pinned state if the derivative jumps

We give details of the infinite-volume construction to keep the phase and the unbounded heights in the argument. For a fixed phase sequence and tilt, pin at zero at the two endpoints of a finite interval. These path measures are positively associated and are stochastically increasing in either boundary height whenever the prescribed boundary pair is feasible. They are stochastically decreasing in $\lambda$. Here the order is the coordinatewise order on depths. To verify the assertions, a one-site heat-bath update at $t$ draws an integer $j$ in
\[
 [\max(0,j_{t+1}-c_t),\ j_{t-1}+c_{t-1}]
\]
with weight proportional to $\exp(\lambda a_t2^{-j})$. Its quantile is increasing in both neighbors, and decreasing in positive tilt by the likelihood-ratio order. The finite heat-bath chain with deterministic cyclic scans converges to the stated Gibbs law. Each state can be reduced to the least admissible path by choosing its least permissible value successively from right to left; the reverse changes are admissible, and unchanged updates have positive probability. This proves irreducibility for repeated scans and aperiodicity. The least path's interior heights are $\max(0,j_{\rm right}-\sum_{s=t}^{\rm right-1}c_s)$, which respect feasibility of the fixed left boundary. Coupling the updates by independent uniforms proves the monotonicity assertions. At each finite scan the coordinates started from the least path are increasing functions of independent uniforms, hence are positively associated by the product-measure correlation inequality. Association passes to the limiting bridge law. In particular decreasing indicators of zeros are positively correlated.

On intervals increasing to $\mathbb Z$, the zero-pinned laws restricted to any fixed set of sites increase stochastically: in the larger interval condition on the two heights at the smaller interval's boundaries and use boundary monotonicity. In the compact ordered space $\overline{\mathbb N}_0=\mathbb N_0\cup\{\infty\}$ the finite-dimensional laws therefore have a unique weak limit $\mu_v^\lambda$. For instance the probabilities of rectangles specified by upper bounds on any finite list of coordinates decrease and determine the limit. It is measurable in phase, shift equivariant, independent of the expanding interval exhaustion, and retains association for zero events. The laws decrease stochastically in $\lambda$.

At each $\lambda>\lambda_c$ the phase-averaged reward of this family is $P'(\lambda)$. Indeed the normalized finite derivative averages the one-site rewards. For a site distant by at least $L$ from both pinned endpoints its expectation is between that for the whole-line state (lower bound) and that for a $[-L,L]$ zero-pinned window centered at that site (upper bound), by the ordering just proved. Integrate the initial phase over Haar measure, use its rotation invariance, send $n\to\infty$ and then $L\to\infty$. Finite derivatives of the integrated convex pressures converge to the derivative of their differentiable limit. Bounded convergence on the compact height space applies to $2^{-j}$ with $2^{-\infty}=0$.

Suppose now $P'_+(\lambda_c)>0$. As $\lambda_j\downarrow\lambda_c$ from the localized side, their infinite-volume laws increase to a shift-equivariant family $\nu_v$ with strictly positive phase-averaged reward. Conditional on finite specified heights at the endpoints of any fixed interval the exact filling law is the critical finite Gibbs bridge. This follows first at finite volume by splitting the path weight, then twice by limits: finite boundary-height events are clopen, and the finite left height bounds all the intermediate heights. Also the following unconditional replacement identity passes directly to both limits for every $n$:
\[
 \nu_v(j_0=0,\ j_t>0\ (0<t<n),\ j_n=0)
 = \nu_v(j_0=j_n=0)\ K_n(\lambda_c,v)/Z_n(\lambda_c,v).              \tag{2}
\]
The finite lists of zero events and of their complements are clopen, including at infinity.

Write $p_0(v)=\nu_v(j_0=0)$. Then $p_0(v)>0$ almost everywhere. Indeed any finite height forces the next height finite since the possible increase is at most one. The phase-integrated law is stationary, so finiteness is almost surely constant over all sites. Its conditional probability is rotation invariant, hence a positive constant almost everywhere by ergodicity and the positive reward. On almost every path having finite heights there are arbitrarily remote future returns to some bounded height set, by recurrence applied to the countably many sets $\{j_0\le J\}$. Thus for almost every phase there is positive probability of some finite pair $j_{-1}=b$, $j_L=d$ with $d\le\sum_{t=0}^{L-1}c_t$, since that sum grows as $\alpha L+O(1)$. On those boundary data a path with $j_0=0$ is feasible: it can drop to zero initially and then rise by available increments up to $d$. Its conditional finite filling probability is positive. Countability and the filling identity prove the claim.

## Inducing the pressure at eligible contacts

Take a measurable set $E$ of positive Haar measure such that $c_0=1$ and $p_0(v)\ge\delta>0$ everywhere on $E$, after removal of any null exceptions. This exists because the eligible interval has measure $\alpha$. Denote by $t_k(v)$ the $k$th positive return of the rotation to $E$ and by $\mathbb E_E$ integration against normalized Haar measure there. Its induced transformation preserves this measure, and Kac's return formula gives $\mathbb E_E t_k=k/|E|$.

The raw unweighted strict excursion estimate is, uniformly at every eligible $v$ and $n\ge2$,
\[
                        K_n(\lambda_c,v)\ge C e^{Hn} n^{-3/2}.       \tag{3}
\]
For $n\ge3$ prescribe $j_1=j_{n-1}=1$, insert any pinned length-$(n-2)$ bridge raised by one between those times, then drop to the terminal zero. All its critical weights are at least one. For any phase $w$ and length $m$, among the positive compositions of $M=\lfloor w+m\theta\rfloor$ into $m$ parts, at least $1/m$ of their number are pinned paths, by rotating after a maximum of $K_t-t M/m$. Indeed $tM/m\le t\theta+w$ for $t\le m$. Stirling's estimate for the binomial coefficient, uniform in $M=m\theta+O(1)$, gives $Z_m(0,w)\ge c m^{-3/2}e^{Hm}$. The remaining lengths, including $n=2$, follow from the eligible path. This proves (3).

Induced supermultiplicativity gives, for each fixed $k\ge1$,
\[
           \mathbb E_E \log Z_{t_k(v)}(\lambda_c,v)\le H\mathbb E_E t_k.
                                                                         \tag{4}
\]
To see this concatenate $m$ consecutive groups of $k$ returns. The expectation of the sum of their log partition functions is $m$ times the left side of (4). It is bounded above by $\mathbb E_E\log Z_{t_{mk}}(\lambda_c,v)$. For arbitrarily small $\eta>0$ and all large $m$, uniform all-phase pressure at critical and $t_{mk}\ge mk$ bound this by $(H+\eta)mk/|E|$. Divide by $m$ and send $\eta$ to zero. Every expectation is finite by the linear word bound and Kac's identity. This is where all-phase pressure removes any need to assume a stationary eigenfunction or to estimate phase-wise boundary normalizers.

For $v\in E$ and $n=t_k(v)$ association gives $\nu_v(j_0=j_n=0)\ge p_0(v)p_0(T^n v)\ge\delta^2$. Multiply (2) by $n$ and use (3). For $k\ge2$, Jensen's inequality, (4) and concavity of the logarithm yield
\[
 \mathbb E_E\left[\frac{t_k^{-1/2}e^{H t_k}}{Z_{t_k}(\lambda_c,v)}\right]
 \ge \exp\!\left[-\tfrac12\mathbb E_E\log t_k+H\mathbb E_E t_k
                    -\mathbb E_E\log Z_{t_k}(\lambda_c,v)\right]
 \ge (k/|E|)^{-1/2}.                                                 \tag{5}
\]
The return lengths at each phase are distinct. Equations (2)–(5) force the phase integral of $\sum_{n\ge1} n\nu_v(j_0=0,\text{ next zero at }n)$ to diverge. For every stationary point process of zero times on the integers this integral is at most one: the disjoint intervals from each zero up to its next zero send one unit of mass per covered integer, or equivalently apply Kac to the zero event in the stationary path space. This contradiction excludes a positive right derivative at $\lambda_c$. The left derivative is zero by the plateau. Convexity gives continuity of the derivative wherever it exists, including the transition. Together with the preceding localized estimate and the positive plateau, the argument covers every nonnegative tilt.

The proof concerns the book's exact correction-word ensemble. A low-density collection of these words may still contain an exceptional ordinary cycle.

## Review and verification boundary

Root independently reconstructed every part of this written proof, including
finite heat-bath association, the usable-edge involution, the positive
supersolution, the critical finite-height component and its zero contacts,
the induced pressure inequality, and the Jensen/Kac contradiction. The
half-tilt map is in fact a bijection when the initial step is eligible;
the displayed upper bound is enough for the proof. This is internal
mathematical review, not external peer review.

[The exact finite checker](check_depth_pressure.py) verifies 24 phase/length
cases, 67 strict excursions, 9,512 unordered replica pairs and 250,252
intervals. It checks the full rational reward polynomial of the half-tilt
bijection, min/max lattice closure and reward preservation, 229,513 legal
involutive tail exchanges, 30,000 cases with equality only at the right
endpoint, and 169,522 cases in which two zero visits force an exchange.
It includes 20,739 intervals where no exchange is available. Both Python
modes agree. No numerical Gibbs approximation is used.

[DepthBridge.lean](DepthBridge.lean) proves ten finite lattice, swap,
order-propagation, zero-contact and half-tilt weight lemmas. The infinite
Gibbs construction, pressure differentiability and critical return-time
argument remain written mathematics. The finite audit does not certify
those analytic conclusions by itself.

# A tilted parity count forces nonsmooth companions toward the fair grade

Fix positive odd integers $A,B$ with $B/A\notin3^{\mathbb Z}$ and fixed integer offsets $a,b$. Set $x=An+a$, $y=Bn+b$, and write $k_t$ for the number of odd shortcut departures by date $t$. Fix $0<p<1$ with $p\ne1/2$. Let $\mu_{p,x}$ be the unique source law on the common $n\in\mathbb Z_2$ under which the physical parity sequence of $x$ is iid Bernoulli of mean $p$. The ordinary one-coordinate construction is the parity pullback of a biased Bernoulli law. The odd affine map from $n$ to $x$, followed by native parity coding, bijects depth-$t$ cylinders at every $t$. [Prior construction of the biased Collatz measure, Paper 170](https://rstation.ai/problems/collatz/papers/170)

There are $\eta>0$ and $c,C>0$, depending on the fixed parameters, such that for large $t$
\[
 \mu_{p,x}\left(\left|k_t(y)/t-1/2\right|>
                (1-\eta)|p-1/2|\right)
           \le C\exp[-ct/(\log(2+t))^4].                              \tag{1}
\]
In particular every subsequential limiting physical grade of $y$ is strictly closer to $1/2$ than the actual first-source grade $p$, almost surely. The constants can be kept uniform with $p$ in a fixed compact subinterval of $(0,1/2)$ or $(1/2,1)$. When $B/A\equiv5,7\bmod8$ the right side can be replaced by $Ce^{-ct}$. The general case uses the fixed-ratio Bugeaud–Laurent two-adic logarithm bound. The fair source is treated separately by the [physical Bernoulli joining](MULTIPLIER_BERNOULLI_JOINING.md).

**True ordinary slices.** Let $t=t(X)\to\infty$, $2^t=o(X)$, and let the integer $k=k(X)$ satisfy $k/t\to p$. Give $n\in[X,2X)$ equal weight conditioned on the exact, generally exponentially rare event $k_t(x)=k$. Then except on relative probability $O(\exp[-c't/(\log(2+t))^4])$ one has
\[
          |k_t(y)/t-1/2|\le (1-\eta')|p-1/2|.                          \tag{2}
\]
This holds simultaneously for each fixed finite list of companions whose ratio to $A$ is outside $3^{\mathbb Z}$, without restrictions on the ratios between companions. The $5,7$ residue cases retain an exponential exceptional bound. For the critical density $p=\log 2/\log 3$, the actual size of the selected $x$ changes by a factor $\exp(o(t))$ while each companion's size decreases by at least an exponential factor $\exp(c_0t)$ outside the same exceptional set. This concerns final size after exactly $t$ actual steps and places no condition on later fate.

**Mutual singularity.** For any $q\in(0,1)$, the two source laws $\mu_{p,x}$ and $\mu_{q,y}$ are mutually singular. If $q=1/2$, the second law is Haar and has first-source grade $1/2$ almost surely. For $q\ne1/2$, take the probability-one set for the first law on which its own grade tends to $p$ and (1) holds eventually, and symmetrically the set for the second law. If both actual limits $p,q$ exist at a point of intersection, they would force both $|q-1/2|<|p-1/2|$ and its reverse. Thus the two full-measure sets are disjoint. This includes equal biased parameters. Translations and the excluded powers of three need separate analysis.

## The mixed-departure chain under the changed source law

At every date the earlier $t$ physical parities of $x$ and the lower $t$ source bits determine each other. Conditional on any such prefix the next first-source parity has probability $p$ of being odd and is independent of past parities. At the same date the two true states, as functions of the fresh binary tail, have affine slopes $A3^{k_t(x)}$ and $B3^{k_t(y)}$. Their agreement or disagreement in parity is already known from the prefix. In case of disagreement the grade difference $D_t=k_t(y)-k_t(x)$ increases by one if $x$ is even, an event of probability $1-p$, and decreases by one otherwise. All statements hold at finite prefix stopping times by their cylinder partition.

Let $S_j$ be $D$ just after the $j$th mixed departure, starting at zero. Let $W_j$ be the number of additional physical dates through and including the next such departure. Set
\[
      v(d)=v_2(B3^d-A),\qquad s_p=\max(p,1-p)<1 .
\]
The difference of the two states at this prefix is an affine function of the unread binary tail with nonzero coefficient of valuation $v(S_j)$. The length of the run of common parities is its valuation, since common steps multiply the difference by $1/2$ or $3/2$. If the intercept has valuation less than $v(S_j)$ the wait is deterministic and shorter. Otherwise requiring at least $l$ extra common steps beyond $v(S_j)$ specifies one residue for the fresh tail modulo $2^l$. It specifies a unique next $l$-parity word of the first source and has conditional probability at most $s_p^l$. Consequently
\[
  \Pr(W_j>1+v(S_j)+l\mid\mathcal F_{\tau_j})\le s_p^l\qquad(l\ge0).
\]
There are infinitely many mixed dates almost surely. Their signs are independent with the probabilities just found, since at the next predictable mixed departure the fresh first-source parity still has parameter $p$. Thus $S_j$ is a biased nearest-neighbor walk. For small fixed $h>0$ the conditional exponential moments of $(W_j-1-v(S_j))_+$ are bounded by $C_p$. Iteration and exponential Markov give
\[
 \Pr\!\left(\sum_{j<m}W_j>\sum_{j<m}v(S_j)+C'_pm\right)\le e^{-c_pm}. \tag{3}
\]

## Occupation of arithmetic waiting costs

In the residue classes $5,7$ the valuations are bounded by two. In general the [fixed-slope evaluation](MULTIPLIER_PARITY_SEPARATION.md) gives $v(d)\le C_{A,B}\log^2(2+|d|)$. It follows from Bugeaud–Laurent Theorem 3 on the two rational units $3,A/B$ or their reciprocal as appropriate. They are multiplicatively independent by unique factorization. For $k\ge3$ each nonempty set $v(d)\ge k$ is a single exponent class modulo $2^{k-2}$ by the order of three modulo $2^k$. Therefore
\[
   \sum_{|d|\le m}v(d)\le C m+O_{A,B}(\log^2(2+m)),                   \tag{4}
\]
by summing $O(1+m2^{-k})$ through the maximum valuation. [Bugeaud and Laurent, Theorem 3](https://irma.math.unistra.fr/~bugeaud/travaux/logpadicdef.pdf)

Suppose first $p>1/2$, so $S$ drifts downwards; the other case is its reflection, using $v(-d)$. Put $f_m(d)=v(d)\mathbf1_{|d|\le m}$, $\delta=2p-1$, $\rho=(1-p)/p$. For the biased walk kernel $P$ define
\[
 U_m(s)=\delta^{-1}\left(\sum_{d\le s}f_m(d)+\sum_{d>s}\rho^{d-s}f_m(d)\right).
\]
Direct substitution gives $(I-P)U_m=f_m$: the kernel is constant on $s\ge d$, geometric on $s<d$, with a unit source at $d$. Its nearest-neighbor differences are bounded by $C_p\|f_m\|_\infty$ by differencing the geometric sum. It is nonnegative, and $U_m(0)\le\delta^{-1}\sum f_m\ll_p m$ for all sufficiently large $m$ by (4). Telescoping gives
\[
 \sum_{j<m}v(S_j)=U_m(0)-U_m(S_m)
                +\sum_{j<m}\bigl(U_m(S_{j+1})-PU_m(S_j)\bigr).
\]
Here $|S_j|\le m$ makes the truncation exact through these dates. The final sum is a martingale with increment bounded by $2C_p\|f_m\|_\infty$. Azuma's inequality therefore bounds the chance of an occupation cost above $C''_p m$ by $\exp[-c_{p,A,B}m/(\log(2+m))^4]$. Using (3) at $m=\lfloor\alpha t\rfloor$ with sufficiently small fixed $\alpha>0$ proves that at least $\alpha t/2$ of the first $t$ dates are mixed off an exceptional set of the order in (1). The bound is $O(e^{-ct})$ when all the valuations are bounded.

A uniform proportion are common as well. In each block of three physical dates there is conditional probability at least $\epsilon_p=\min(p,1-p)^2$ of at least one common date: if the current date is mixed, the [native three-date calculation](MULTIPLIER_DIFFUSION_RANK.md) either allows a common date after a one-bit choice or reaches a prefix with such a choice on the second following bit. Each specified length-two first-coordinate parity continuation has conditional probability at least $\epsilon_p$. The indicators of success minus their conditional expectations are bounded martingale differences over disjoint length-three blocks. Thus at least $\epsilon_p t/8$ dates are common off an exponentially small set for large $t$. For the mixed count $H_t$ we have shown
\[
      \alpha'\le H_t/t\le1-\beta'                                    \tag{5}
\]
with the asserted failure rates and positive constants.

## The grade and the ordinary conditional ensemble

The increments of $D_t-(1-2p)H_t$ are bounded martingale differences in physical time. Thus any fixed linear tolerance has an exponentially small probability of failure. The first-source grade likewise differs from $pt$ by a fixed linear tolerance only with exponentially small probability. Consequently
\[
 \frac{k_t(y)}t-\frac12
     =(p-1/2)(1-2H_t/t)+O(\varepsilon)
\]
outside an exponentially small set, for any prescribed $\varepsilon>0$. Use (5) and choose $\varepsilon$ small compared with $|p-1/2|\min(\alpha',\beta')$ to obtain (1). Borel–Cantelli proves the almost-sure assertion. Every constant and probability estimate above is uniform for $p$ in the stated compact intervals; $A,B,a,b$ remain fixed.

For (2) put $p_t=k/t$. Tilting the first-source law at depth $t$ by $p_t$ gives every parity word in the exact grade-$k$ slice the same mass $p_t^k(1-p_t)^{t-k}$. Conditional on that slice the law consequently equals the unweighted uniform binary residue law on the slice. Its slice probability under the tilt is $\binom tk p_t^k(1-p_t)^{t-k}\gg_p t^{-1/2}$ by Stirling. Thus conditioning costs at most $O_p(\sqrt t)$ in (1), absorbed by decreasing $c$. Every individual binary residue modulo $2^t$ is represented in the octave with count $X/2^t+O(1)$. Therefore the ordinary conditional probability of *any* subcollection of the slice differs by a **relative** factor $1+O(2^t/X)$ from its uniform-slice value when nonempty. The small unconditional Haar mass of the slice makes no loss here. Letting $p_t\to p$ and slightly decreasing the contraction constant proves (2).

Finally, throughout the first $t$ dates every ordinary physical state starting at either fixed affine input is $\gg_{A,B}X2^{-t}\to\infty$. The exact log-size change per step at time $t$ is
\[
   t^{-1}\log(T^t x/x)= (k_t(x)/t)\log3-\log2+O_{A,B,a,b}(2^t/X),
\]
and similarly for $y$, by summing the true corrections $\log(1+1/(3z))$ at odd sites $z$. At the specified critical tilt the first change is $o(1)$ and (2) puts the other below a fixed negative constant. This proves the physical endpoint comparison for actual positive integers.

[Finite native prefix and exact-slice checks](check_critical_dilations.py) · [Output](../../../reports/astra-global-20261128/cycles/CRITICAL_DILATIONS.json)

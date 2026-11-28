# A positive fraction of all prime-factor additions change the orbit test

Write $p_1<\cdots<p_{\omega(n)}$ for the distinct prime factors of $n$ and $s_i=\prod_{j\le i}p_j^{v_{p_j}(n)}$, with $s_0=1$. For a binary test $F$ let $V_F(n)=\sum_{i\ge1}|F(s_i)-F(s_{i-1})|$, ending at $s_{\omega(n)}=n$. If $F$ is a fixed union of eventual Collatz components or the indicator of a visit to a fixed odd target, and its ordinary natural density $d$ belongs to $(0,1)$, then for some $c_F>0$
\[
                V_F(n)\ge c_F\,\omega(n)
               \quad\text{on a set of natural density one}.             \tag{1}
\]
Indeed $V_F(n)\gg_F\log\log n$ there. Every change counted in (1) occurs when one adds one of the actual prime powers of $n$. The proof uses the dimension-one fundamental lemma and counted neighbor-pair synchronization with arbitrary offsets. It requires neither RH nor a relative short-interval theorem for a sparse multiplicative function. It does not require a mixing limit for the entire factor band.

This applies, for example, to visits to $5$: the physically disjoint predecessor sets of $5$ and $85$ both have positive density under the all-unit predecessor input. If a single positive orbit misses $1$, the analogous conclusion applies to visits to $1$. [Full smooth-signature approximation, exact factor bands and source qualification](SMOOTH_DIVISOR_FATES.md) · [Counted fusion, Paper 209/v1, Theorem 4.2](https://rstation.ai/problems/collatz/papers/209) · [All-unit predecessor densities, Paper 12/v1, Theorem 1 under Inputs C–D](https://rstation.ai/problems/collatz/papers/12/v1)

## A fixed-ratio factor band with a constant probability of mixing

Let $V(z)=\prod_{p\le z}(1-1/p)$. In the independent geometric signature model each valuation has law $(1-1/p)p^{-v}$. For $R$ a large fixed constant, set $w=z^{1/R}$ and let $M$ be the product of all prime powers in $(w,z]$. If $\sqrt z<m\le z$, its upper prime cutoff holds automatically. Thus exactly on this interval
\[
            \Pr(M=m)=\frac{V(z)}{V(w)m}\,1_{P^-(m)>w}.                   \tag{2}
\]
Crucially the harmonic mass of this one interval is comparable to one, however large the fixed $R$ is. We use only this portion of the band to force a change.

Fix $K\ge2$. For every earlier multiplier $d_0$ with $\log d_0\le K\log w$ set $D=d_0/2^{v_2(d_0)}$. The physical events in (1) satisfy $F(2^a u)=F(u)$ for all $a,u$: each intervening state is even, so visits to an odd target are preserved, and the eventual component is unchanged. Thus one may test $F(Dm)$ with an **odd** multiplier, even if the actual signature has a large dyadic part. For $b\in\{0,1\}$ put $f=1_{F=b}$ and $d_b=\lim_{X\to\infty}\mathbb E_{I_X}f$, with $I_X=(X,2X]$. We claim uniformly over these multipliers that
\[
 \Pr(F(d_0 M)=b,\ \sqrt z<M\le z)
  = \tfrac12 e^{-\gamma_{\rm E}}d_b+
              O\!\left(\sqrt{K/R+R^{-1/2}}+e_R\right)+o_{R,K}(1),       \tag{3}
\]
where $e_R\to0$ and $\gamma_{\rm E}$ is Euler's constant. The first implied constant is absolute for the normalized binary test. The $z\to\infty$ limit is taken with $R,K$ fixed. An analogous one-sided estimate holds for any fixed orbit event of this type.

For $z^{1/4}\le T\le z$ put $H=\lfloor T^{1/\sqrt R}\rfloor$, $t=\lfloor(\log_2 T)/10\rfloor$, $Q=2^t$ and $b_w(m)=1_{P^-(m)>w}$. In *every* interval of length $H$ the mean of $b_w$ is $V(w)(1+O(e_R)+o_{R,K}(1))$. Use the fundamental lemma with sieve level $\sqrt H$ and $s=\log(\sqrt H)/\log w\ge\sqrt R/9$ for large $z$. Its divisor remainders sum to $O(\sqrt H)$, which is $o_R(HV(w))$. The long octave has the same estimate. In every odd residue class modulo $Q$, ordinary $w$-rough numbers in the octave enlarged by $H$ number at most $CT V(w)/Q$ for an absolute $C$. Apply the upper sieve to its progression with level $\sqrt{T/Q}$; omission of the prime two multiplies its main product by two. These conclusions are uniform in intervals and residues. [Ford, *Sieve methods*, Theorem 3.6(a), p. 38](https://ford126.web.illinois.edu/sieve2023.pdf)

For $j\le H$ compare $f(Dm)$ with $f(D(m-j))$ using the true offset $Dj$. The unsuccessful binary cells occupy relative fraction $O(\sqrt{(1+\log(DH))/t})$. The affine map from the residue of $m$ to the lower source permutes the residues. The rough upper bound therefore gives relative weighted error $O(\sqrt{K/R+R^{-1/2}})+o_{R,K}(1)$. A fixed odd visit target is below all states before the fusion date, since $T^{t}x\ge x2^{-t}$ and the same lower bound holds at earlier dates. Average over shifts, with edge cost $O(H/(TV(w)))=o_R(1)$. The uniform rough interval estimate then removes the weight. Tiling by $Du+j'$, $0\le j'<D$, compares the remaining dilated ordinary mean to the full octave $I_{DT}$ with error $O(\sqrt{K/R})+o_{R,K}(1)$, by the same cylinder estimate without a sieve weight. Natural density of $f$ gives $\mathbb E_{I_{DT}}f\to d_b$ uniformly here, since $DT\ge z^{1/4}$. We have proved
\[
  (TV(w))^{-1}\sum_{m\in I_T} b_w(m)f(Dm)
            =d_b+O(\sqrt{K/R+R^{-1/2}}+e_R)+o_{R,K}(1).
\]
For $Y\in[\sqrt z,z]$ sum from $Y$ down in dyadic octaves until scale $z^{1/4}$, paying $O(z^{1/4})$ for the remaining count. Partial summation converts the estimate to the reciprocal sum on $[\sqrt z,z]$; the discarded endpoints cost $o_R(1)$ after multiplication by $V(z)/V(w)$. Its main coefficient is $V(z)\log z/2\to e^{-\gamma_{\rm E}}/2$ by Mertens. The bounded limiting factor $V(z)\log z$ leaves the same absolute error. This proves (3).

## Typical history and empirical changes

Choose $K=10$ and then a finite $R=R_F$ sufficiently large that (3) yields, for both $b$, a lower probability $\eta_F>0$ on all sufficiently large scales. For instance one may take $\eta_F=e^{-\gamma_{\rm E}}\min(d,1-d)/4$ by increasing $R$. On one independent geometric probability space let $\log z_j=R^j$ and $S_j=\prod_{p\le z_j}p^{v_p}$. A stage $j$ is good if $\log S_{j-1}\le K\log z_{j-1}$. Let $Z_j=(\log S_j)/\log z_j$. Then
\[
 \mathbb E Z_j\to1,\qquad
 \operatorname{Var}(\log S_j)=\sum_{p\le z_j}(\log p)^2\frac{p}{(p-1)^2}
                                      \ll (\log z_j)^2.
\]
The expectation uses $\sum_{p\le u}(\log p)/(p-1)=\log u+O(1)$ and the variance bound follows by partial summation. Independence of disjoint prime bands gives $|\operatorname{Cov}(Z_i,Z_j)|\ll R^{-|i-j|}$. Hence $k^{-1}\sum_{j<k} Z_j\to1$ in $L^2$. The proportion of bad stages is at most this average divided by $K$, apart from a vanishing endpoint term. With probability tending to one, at least $1-2/K$ of the stages are good.

Conditional on all earlier valuations, the chance $F(S_j)\ne F(S_{j-1})$ is at least $\eta_F$ on each sufficiently large good stage by (3), whichever bit the previous state carries. Subtract the conditional expectations from these switch indicators. The resulting bounded martingale differences have variance at most $k$ in sum, so the empirical switch proportion is at least $(1-2/K)\eta_F-o_{\mathbb P}(1)$. These are true changes irrespective of the marks on the other portion of each band.

Now sample an ordinary $n\in I_X$, $L=\log X$, and take $k$ maximal with $\log z_k\le L/\log L$. Then $k\sim (\log\log X)/\log R$. The complete small-prime signature of $n$ through $z_k$ is within $o(1)$ in total variation of the geometric model by the full-signature proof, since $\log z_k=o(\log X)$. All cutoffs are deterministic functions of that one signature. Every sampled switch requires one or more actual canonical prime-power additions, proving the asserted positive lower bound in units of $\log\log n$. The normal order $\omega(n)/\log\log n\to1$ in natural probability proves (1). It also follows directly from the same geometric comparison: the indicators of positive valuation have independent variances $\ll1/p$, while factors above $z_k$ occur $o(\log\log X)$ times in ordinary probability by Mertens and Markov. Dyadic summation passes from all large octaves to natural density.

For any fixed finite word of prescribed positive-density events of the stated kind, a positive multiple of $\log\log n$ disjoint blocks of canonical additions realize that word as an ordered subsequence, on a density-one set. Take blocks of as many consecutive bands as there are letters. From a good initial history impose the moderate-size requirement $\sqrt z<M\le z$ and the desired label at each stage. The next history remains good, because its logarithm is at most $(K/R+1)\log z\le K\log z$. Iteration gives a fixed positive success probability on every initially good block. The covariance calculation also applies to the spaced block-start indices, and the bounded martingale-difference argument applies to the disjoint block indicators. The restriction $M>1$ ensures distinct divisors in each successful block. Intermediate prime-power links can occur between the prescribed labels.

## Density-zero sets on canonical divisors

There is a transfer for exceptional sets that uses no orbit theorem. For every ordinary set $E$ of natural density zero, let $N_E(n)=\#\{1\le j\le\omega(n):s_j\in E\}$. Then
\[
                   N_E(n)/(1+\omega(n))\longrightarrow0
                         \quad\text{in natural probability}.            \tag{4}
\]
This concerns almost all the *canonical* divisors. It does not assert that an arbitrary divisor chosen after inspection avoids $E$.

In the geometric model through $z$, write $S_{p^-}$ for the earlier signature. The expected number of selected post-prime sites in $E$ is
\[
 \sum_{p\le z}\sum_{a\ge1}(1-1/p)p^{-a}\,
                \Pr(p^aS_{p^-}\in E).
\]
The terms with $a\ge2$ sum to $O(1)$. Fix $K\ge2$. In the $a=1$ contribution, $\log S_{p^-}>K\log p$ costs $O((1+\log\log z)/K)$ in total by $\mathbb E\log S_{p^-}\ll\log p$. On the remainder put $m=p S_{p^-}$. The prime $p$ is uniquely its largest prime, and $m\le p^{K+1}$. Its weight is at most $V(p^-)/m\ll(K+1)/(m\log m)$, with $V(p^-)=\prod_{q<p}(1-1/q)$. The whole contribution is at most
\[
             C(K+1)\sum_{2\le m\le z^{K+1}}\frac{1_E(m)}{m\log m}
                            =o_K(\log\log z).
\]
The last equality follows by partial summation from the assumed natural density zero. Let $K\to\infty$. Markov gives $N_E(S_z)/\log\log z\to0$ in probability. This is a null-set statement: the sampling weight at a post-prime site involves its largest prime.

Choose $z=\exp(L/\log L)$ at ordinary octave scale. The complete signature TV approximation transfers this probability conclusion. The number of higher prime factors has expectation bounded by
\[
      \sum_{z<p\le2X}(1/p+O(1/X))=O(1+\log\log X-\log\log z)
                                      =o(\log\log X).
\]
These factors contribute at most that many additional exceptional sites, in expectation. Since $\log\log z\sim\log\log X$ and $\omega(n)$ has the stated normal order, (4) follows.

## A computable dichotomy at a logarithmic orbit deadline

Fix $b>\mu=2/\log(4/3)$ and define the total finite test
\[
        G_b(n)=1_{\{T^t n=1\text{ for some }0\le t\le\lfloor b\log n\rfloor\}} .
\]
An integer-only version takes deadline $5(1+\lfloor\log_2 n\rfloor)$, which exceeds $(\mu+\varepsilon)\log n$ for some fixed positive $\varepsilon$ and large $n$. The fixed-target first-hit clock theorem says that the ordinary set where the true visit indicator $F=1_{\{\text{visits }1\}}$ differs from either finite test has natural density zero: on the hit population the first clock is centered at $\mu\log n$ with square-root logarithmic fluctuations. The same reasoning applies at any fixed odd unit target using its corresponding clock input. [PR 215, fixed-target clock and cited sources](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/phase2/MOVING_CLOCKS.md) · [Paper 233, integer five-steps-per-bit test](https://rstation.ai/problems/collatz/papers/233)

Changing one vertex label alters the variation by at most two. Applying (4) to the disagreement set gives
\[
                |V_{G_b}(n)-V_F(n)|/(1+\omega(n))\longrightarrow0
                          \quad\text{in natural probability}.           \tag{5}
\]
Thus there are two alternatives for quantities computable from the finite factorization and finitely many forward steps of the individual prefix divisors.

* If every positive orbit visits one, $V_{G_b}(n)/(1+\omega(n))\to0$ in natural probability.
* If any positive orbit misses one, then for some $c>0$, $V_{G_b}(n)/(1+\omega(n))\ge c$ on a set of natural density one.

In the second case the ordinary density of visits to one is strictly between zero and one by positive unit predecessor densities, so (1) and (5) apply. Equivalently under these inputs, universal convergence holds exactly when the bounded statistic $V_{G_b}(n)/(1+\omega(n))$ has lower limiting ordinary mean zero. The same dichotomy holds for the stated integer-only deadline. The computation of this ratio at any individual source terminates without knowing its eventual fate. The present work gives no upper bound establishing the zero-mean alternative.

Even without an extra-cycle hypothesis, testing visits to five with this finite logarithmic deadline changes value on a positive proportion of all canonical prime-factor additions for density-one ordinary integers, by (1), (4) and the fixed-target clock. The previously obtained full-frequency law at severely separated cutoffs and its $\log\log\log n$ lower bound use a full band limit. The present fixed-ratio argument obtains a positive proportion with a one-sided minorization and a typical-history estimate.

## Exact mean occupancy of all prime-factor sites

Mark one of the noninitial sites $s_1,\ldots,s_{\omega(n)}$ uniformly after choosing an ordinary uniform source $n\in I_X$. The conditional convention at $\omega(n)=0$ is immaterial. For every fixed component union or odd-target visit event $F$ as above, the mean probability that the marked site satisfies $F$ tends **exactly** to its ordinary density $d$. This conclusion concerns sampling one link; it makes no assertion that every individual typical chain has empirical frequency tending to $d$.

In the independent geometric model through $z$, let $C_F$ count all post-prime sites satisfying $F$. The exact identity for every bounded nonnegative test is
\[
 \mathbb E C_F =
     \sum_{m>1:\,P^+(m)\le z}\frac{V(P^+(m))}{m}F(m).                  \tag{6}
\]
Indeed $m=p^a d_0$ with $p=P^+(m)$, $a\ge1$, and $P^+(d_0)<p$ is a unique representation. Its mass at that prime link is $(1-1/p)p^{-a}V(p^-)/d_0=V(p)/m$. In particular $\mathbb E C_1=\sum_{p\le z}1/p$.

Removing $m>z$ in (6) costs only $O(1)$ uniformly for $0\le F\le1$. Conditional on $v_p>0$, the mean of $\log(p^{v_p}S_{p^-})$ is $O(\log p)$. Markov and $\sum_{p\le z}(\log p)/p\ll\log z$ give the bound. Removing $m>(P^+m)^K$ similarly costs $O((1+\log\log z)/K)$. For dyadic $T$ and $m\in I_T$ use the simpler cutoff $P^+m\ge T^{1/K}$, whose removed mass has this same bound since $m>T$. On the retained portion write $W_T(m)=(\log T)V(P^+m)1_{P^+m\ge T^{1/K}}$. It is a function of the largest prime with total variation and supremum $O(K)$, including its jump at the cutoff.

Every threshold $1_{P^+m\le v}$ is a bounded real multiplicative function (give $m=1$ value one). The published Matomäki–Radziwiłł short-interval theorem together with the cited counted-fusion estimate therefore implies, uniformly over $v$,
\[
 |\mathbb E_{I_U}[(F-\mathbb E_{I_U}F)1_{P^+m\le v}]|
                           \ll (\log U)^{-1/150}.
\]
This precise consequence for true future tests is already written in PR 213. Stieltjes summation over thresholds gives $|\mathbb E_{I_U}[(F-d)W_T]|\le C K((\log U)^{-1/150}+|\mathbb E_{I_U}F-d|)$. Here $W_T$ is fixed while $U$ varies, including $U\ge\sqrt T$. Summing dyadic octaves down from any $y\in[T,2T]$ and bounding the remaining $O(\sqrt T)$ initial terms proves a uniform $o_K(T)$ cumulative bound on $\sum_{m\le y}(F(m)-d)W_T(m)$. Partial summation then gives $o_K(1)$ for the reciprocal sum on any subinterval of $I_T$. Restoring $1/\log T$ and summing over dyadic $T\le z$ gives $o_K(\log\log z)$ for the retained part of $\mathbb E(C_F-d C_1)$. The discarded terms cost $O((1+\log\log z)/K+1)$. Let $K\to\infty$. [PR 213, real multiplicative observables including largest-prime thresholds](https://github.com/GettysburgResearch/collatz/blob/f2fb6bd2ed9dd4172d9e2040ca6b9ca012ca8ae0/research/astra-global-rigidity-20261128/mersenne/REAL_MULTIPLICATIVE_OBSERVABLES.md) · [Matomäki–Radziwiłł, Annals 183 (2016), Theorem 1](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf)

The number $C_1$ of geometric links is a sum of independent Bernoulli variables with variance $O(1+\log\log z)$, so $C_1/\log\log z\to1$ in $L^1$. Since $0\le C_F\le C_1$, replacing the deterministic denominator $\log\log z$ by $\max(1,C_1)$ changes the mean by $o(1)$. This last ratio is bounded; the full-signature total-variation comparison transfers its expectation to the ordinary truncated chain at $z=\exp(L/\log L)$. The omitted high prime factors are $o(\log\log X)$ in probability as above, so the ordinary full-chain bounded ratio has the same limiting expectation. The preceding-site marginal is the same, since replacing the terminal vertex by the initial vertex changes the count by at most one. Thus each mean endpoint marginal of the canonical prime links equals $d$, while (1) forces a positive frequency of transitions across any fixed nontrivial binary orbit test.

Finally the exact Euler-sum calculation in [the earlier complete-signature proof](SMOOTH_DIVISOR_FATES.md) together with the stronger lower bound (1) gives
\[
 \liminf_{z\to\infty}\frac{1}{\sum_{p\le z}1/p}
 \sum_{p\le z}\frac1p\Pr(F(pS_{p^-})\ne F(S_{p^-}))>0\quad(0<d<1).
\]
To use the geometric argument directly, take all fixed-ratio cutoffs below $z$; there are $\asymp_F\log\log z$ and their changes already have a positive expected fraction. Exponents $a\ge2$ contribute $O(1)$ as before. Consequently a set of primes of positive lower harmonic density has a change probability bounded away from zero on its corresponding genuine small-prime prefix law.

[Exact finite canonical clock comparisons and largest-prime Euler incidences](check_prime_variation.py) · [Recorded counts](../../../reports/astra-global-20261128/cycles/PRIME_VARIATION.json)

The [typical-band and tagged-prime proof](PRIME_BAND_OCCUPATION.md) strengthens the mean endpoint marginal to convergence in natural probability of the full-chain empirical occupancy, including full component TV under its stated ordinary-law input.

# Statistical information in a supplied ternary Syracuse residue

For \(0<\theta<1\), let independent positive gaps have probabilities \(p_\theta(e)=\theta(1-\theta)^{e-1}\). Put
\[
 A_e(y)=2^{-e}(1+3y),\quad S_n=\sum_{i=1}^ne_i,\qquad
 Z_n=A_{e_1}\cdots A_{e_n}(0)\bmod3^n .
\]
Write \(\mu_{\theta,n}\) for the law of \(Z_n\). The physical inverse at a supplied source is \(I_e(x)=(2^ex-1)/3\). Let \(K_n(z)\) be the least total of an \(n\)-gap word coding the *observed* cell \(z\bmod3^n\). Put \(\alpha=\log_3 2\), \(g=1/\alpha=\log_2 3\), and define \(a_*=1/\theta_*\) by \(H(a_*)=\log3\), where \(H(a)=a\log a-(a-1)\log(a-1)\). Use \(H(1)=0\). Logarithms below are natural.

**1. The whole geometric parameter experiment can be recovered.** For every compact interval \(J\subset(\alpha,1)\), there is one randomized decoder \(R_n\), independent of the unknown \(\theta\in J\), with
\[
 \sup_{\theta\in J}\big\|\mathcal L_\theta(Z_n,R_n(Z_n))-
                 \mathcal L_\theta(Z_n,(e_1,\ldots,e_n))\big\|_{\rm TV}
                      =O_J(n^{-1/2}).                                      \tag{1}
\]
The decoded word always belongs to the supplied cell. Thus observing the ternary residue and observing the whole iid gap sample are asymptotically equivalent statistical experiments throughout this parameter interval. For each fixed parameter and any diverging terminal allowance \(m_n\le n\), the same decoder also reproduces the actual *first* \(n-m_n\) gaps with probability tending to one; the last gaps can differ. The finite-sample Fisher information lost is bounded uniformly in \(n\) and \(\theta\in J\). So is the conditional Shannon entropy of the entire word given the residue. In particular \(K_n\) has the same central limit and all intermediate moderate-deviation rates as the iid total.

**2. Exact moment growth in a biased parameter region.** Write \(r=1-\theta\). For any \(q>1\), the following implication holds.
\[
 r^q\le \frac{(3/2)^{q-1}-1}{3^{q-1}-1},
 \quad\Longrightarrow\quad
 \lim_{n\to\infty}\frac1n\log\sum_z\mu_{\theta,n}(z)^q
                   = \log\frac{\theta^q}{1-r^q}.                         \tag{2}
\]
In particular this covers *every* \(q>1\) at every \(\theta\ge\alpha\), and every \(q\ge2\) at every \(\theta\ge1/2\). The most likely individual cell has probability \(\theta^{n+o(n)}\) for \(\theta\ge1/2\). The fair law's moment spectrum was already known.

**3. Minimum-cost deviations and discrimination.** For \(\theta\ge\alpha\), all \(1\le b\le a_*\) have the same local large-deviation rate for \(K_n/n\) as for the iid total:
\[
 \lim_{\varepsilon\downarrow0}\limsup_n\frac1n\log
     \Pr_\theta(|K_n/n-b|<\varepsilon)
 =\lim_{\varepsilon\downarrow0}\liminf_n\frac1n\log
     \Pr_\theta(|K_n/n-b|<\varepsilon)
 =-I_\theta(b),\qquad I_\theta(b)=D(p_{1/b}\Vert p_\theta).              \tag{3}
\]
At \(b=1\) use the point mass at gap one. Each fixed pair of distinct tilts in \([\alpha,1)\) has the identical optimal exponential testing rate from the single ternary residue as from the whole word, attained by a threshold in \(K_n\); each direction of the projected relative entropy also loses only \(o(n)\). In the additional band reaching down to \(\theta_*\), one direction continues without a real-moment hypothesis:
\[
 \lim_n n^{-1}D(\mu_{\beta,n}\Vert\mu_{\theta,n})
   =D(p_\beta\Vert p_\theta)
 \quad\text{if }\theta>\beta\ge\theta_*,
 \quad\text{or if }\theta,\beta\ge\alpha.                               \tag{4}
\]
The typical supplied source under *every* \(\mu_\beta\), \(\beta\ge\theta_*\), satisfies \(K_n/n\to1/\beta\) almost surely, with exponentially small fixed linear deviations.

**4. The entropy-critical code has a square-root obstruction to recovering its realized trajectory.** Draw the words at \(\theta_*\), observe \(n\) trits, and allow a list of candidate prefixes for the actual first \(n-m\) gaps. For any \(m=O(\sqrt n)\) and list size \(\exp(t\sqrt n+o(\sqrt n))\), \(t\ge0\),
\[
 \limsup_n\Pr(\text{the true prefix is listed})\le
              2\Phi(t/\sigma_*)-1,\qquad
 \sigma_*^2=\operatorname{Var}_{\theta_*}(\log(3p_{\theta_*}(e))).       \tag{10}
\]
This permits randomized lists depending on the entire observed residue. In particular even subexponentially many candidates on the square-root scale have asymptotically zero success. Full infinite-source decoding is compatible with this obstruction on a growing finite prefix.

All statements about normalized costs also hold for the true unit-terminal minimum \(C_n(x)\) at any full lift of the observed root. Indeed
\[
              K_n(x\bmod3^n)\le C_n(x)\le K_n(x\bmod3^n)+2.              \tag{5}
\]
In a word coding the observed cell the first \(n-1\) inverse children are already units, from the first trit of the remaining suffix. The last inverse division is integral. If its quotient \(v\) is divisible by three, raising the last exponent by two gives the unit \(4v+1\). The statement includes odd positive integer representatives of each finite cell.

## Clock ambiguity and the randomized inverse

For a word \(w\) with clock \(s\), write its offset as \(2^{-s}B_w\), and put
\[
 B_w=\sum_{i=1}^n 3^{i-1}2^{s-S_i},\qquad V_w=B_w/3^n.
\]
At fixed \((n,s)\), \(B_w\) uniquely determines \(w\), by [binary decoding](SPARSE_EDIT_INVERSE_REUNION.md). Within any one ternary cell the positive values \(V_w\) are consequently spaced at least one apart. Reversing the iid gaps gives \(V_w\) the law of
\[
           \frac13\sum_{j=0}^{n-1}\prod_{i=1}^j(2^{e_i}/3).             \tag{6}
\]
Uniformly on \(J\), \(\mathbb E_\theta\log(2^e/3)<-c_J<0\). Continuity of the geometric moment-generating function near zero, uniformly on this compact interval, gives \(0<t\le1\) and \(\sup_J\mathbb E_\theta (2^e/3)^t<1\). Subadditivity of the \(t\)th power and (6) give \(\sup_{n,J}\mathbb E V_w^t<\infty\).

Write \(D_n=S_n-K_n(Z_n)\ge0\). Fix \(k\ge1\) and a real cutoff \(L\ge1\). Whenever \(D_n\ge k\), some word \(u\) codes the same cell and costs \(j\ge k\) less than the observed word. For fixed \(u,j\) there are at most \(1+L\) possible observed words of that clock with \(V_w\le L\), by the spacing. Each has probability \(r^j p_\theta(u)\). Summing first over \(u\), then over \(j\), gives
\[
    \Pr_\theta(D_n\ge k)\le\Pr_\theta(V_w>L)+(1+L)r^k/(1-r)
                              \le C_J e^{-c'_J k}.                      \tag{7}
\]
For the last step take \(L=e^{\delta k}\) with fixed small \(\delta>0\). In particular a positive exponential moment of \(D_n\) is bounded uniformly.

Given \((Z_n,S_n)\), the additional nonnegative integer \(\lfloor V_w\rfloor\) specifies the word by the same spacing. Its entropy is bounded by comparison to a probability on integers proportional to \((1+j)^{-2}\), since (6) bounds \(\mathbb E\log(1+\lfloor V_w\rfloor)\). Given \(Z_n\), the entropy of \(S_n\) is bounded by that of \(D_n\), bounded by (7). The entropy chain rule proves the word-entropy assertion. The full sample score in parameter \(\theta\) is \(n/\theta-(S_n-n)/(1-\theta)\). The score of its observed cell is its conditional expectation, by termwise differentiation (geometric tails). Total variance shows the lost Fisher information equals
\[
    \frac{\mathbb E\operatorname{Var}(S_n\mid Z_n)}{(1-\theta)^2}
     \le \frac{\mathbb E D_n^2}{(1-\theta)^2}=O_J(1);
\]
the full information is \(n/[\theta^2(1-\theta)]\).

For (1) estimate the parameter by clipping \(n/K_n(Z_n)\) to \(J\). Write \(\eta=\log(1-\theta)\) and \(\widehat\eta=\log(1-\widehat\theta)\). Both the logarithm on \(J\) and \(a\mapsto1/a\) on \([1,\infty)\) are Lipschitz there. The iid total variance is \(O_J(n)\), so (7) gives \(\mathbb E(\widehat\eta-\eta)^2=O_J(1/n)\). At the given cell sample its exact word posterior at \(\widehat\theta\). Given \(Z_n=z\), that posterior is the posterior at the true \(\theta\) reweighted by \(L=\exp((\widehat\eta-\eta)D_n)\) and normalized. For a probability \(P\), the triangle inequality through the unnormalized measure \(LP\) gives \(\|P-LP/P(L)\|_{\rm TV}\le P|1-L|\). If \(|\widehat\eta-\eta|\le c\), the latter is at most
\[
  |\widehat\eta-\eta|\,\mathbb E[D_n e^{c D_n}\mid Z_n=z].
\]
Choose \(c>0\) small enough for \(\sup_{n,J}\mathbb E[D_n^2e^{2c D_n}]<\infty\). Averaging and Cauchy–Schwarz give \(O_J(n^{-1/2})\); Chebyshev bounds the complementary event by \(O_J(1/n)\). This proves (1) for a decoder preserving the actual observed cell. It is an existence construction with countable posterior support, without a runtime assertion. Finally (7) gives \(D_n/\sqrt n\to0\) in probability; at scales \(v_n/\sqrt n\to\infty\), \(v_n/n\to0\), the event \(D_n>\varepsilon v_n\) is superexponentially small on the moderate-deviation speed \(v_n^2/n\). The classical iid central limit and geometric moderate-deviation results transfer directly.

There is also agreement on the realized trajectory. Write \(h_j(\theta)=H_\theta(e_1\mid Z_j)\). Given the true first \(i\) letters, the affine map from the independent suffix residue of depth \(n-i\) to the full residue is one-to-one on its image. The conditional chain rule therefore gives
\[
 H_\theta(e_1,\ldots,e_n\mid Z_n)=\sum_{j=1}^n h_j(\theta),\qquad
 H_\theta(e_1,\ldots,e_{n-m}\mid Z_n)=\sum_{j=m+1}^n h_j(\theta).
\]
The full-word entropy bound makes this nonnegative series summable at every fixed \(\theta\in J\). Two independent posterior samples at the true parameter disagree on the first \(n-m\) symbols with conditional probability at most the corresponding conditional entropy: for probabilities \(v_i\), \(1-\sum v_i^2\le-\sum v_i\log v_i\). Replacing the second sample by the fitted posterior costs at most its mean conditional total variation from (1). Thus the mismatch probability is at most \(\sum_{j>m}h_j(\theta)+O_J(n^{-1/2})\), proving the asserted fixed-parameter trajectory recovery. No uniform tail of the series over the parameter interval is used.

## Positive moment growth

For each total \(s\) and cell \(z\), let \(N_s(z)\) count its words. In order of increasing \(V_w\), the rank of each such word is at most \(1+V_w\). For \(N\ge1\), \(N^q\le q\sum_{i=1}^N i^{q-1}\) by integration. Thus \(N_s(z)^q\le q\sum_{w:s,z}(1+V_w)^{q-1}\). All words of this clock have the same mass \(p_s=\theta^n r^{s-n}\). Hölder with any sufficiently small \(\delta>0\) gives
\[
\begin{aligned}
 \sum_z\mu_{\theta,n}(z)^q
 &\le \left(\sum_{s\ge1}e^{-\delta s/(q-1)}\right)^{q-1}
                \sum_{z,s}e^{\delta s}p_s^q N_s(z)^q\\
 &\le c_{q,\delta} M(\delta)^n\,
             \mathbb E_{Q_\delta}(1+V_w)^{q-1},
 \quad M(\delta)=\sum_{e\ge1}p_\theta(e)^q e^{\delta e},
 \quad Q_\delta(e)=p_\theta(e)^qe^{\delta e}/M(\delta).
\end{aligned}                                                            \tag{8}
\]
Set \(u=q-1>0\), \(m(\delta)=\mathbb E_{Q_\delta}(2^e/3)^u\). For each fixed \(\delta\) where the moment is finite, (6) and either subadditivity for \(u\le1\) or Minkowski for \(u\ge1\) bound the last expectation in (8) by a polynomial in \(n\) times \(\max(1,m(\delta))^n\). With \(Q_0(e)=(1-r^q)r^{q(e-1)}\),
\[
             m(0)=\frac{(2/3)^u(1-r^q)}{1-2^u r^q}.
\]
The condition in (2) implies the denominator is positive and \(m(0)\le1\) (multiply the stated threshold by \(2^u\) to see it is strictly below one). Small \(\delta>0\) remain in the domain of finiteness. Taking the limsup in (8) and then \(\delta\downarrow0\) gives at most \(\log M(0)\). The opposite bound is exact at each depth: merging positive word probabilities increases their summed \(q\)th power, so \(\sum_z\mu_{\theta,n}(z)^q\ge M(0)^n\).

To check the first parameter range, let \(r_0=\log(3/2)/\log 3=1-\alpha<1/2\). Then
\[
 \frac{(3/2)^u-1}{3^u-1}
 =r_0\frac{\int_0^1 (3/2)^{ut}\,dt}{\int_0^1 3^{ut}\,dt}
 \ge r_0 2^{-u} \ge r_0^{u+1}.
\]
For the second range \(u\ge1, r\le1/2\), the threshold at \(r=1/2\) is equivalent to \(3^u+1\ge2^{u+1}\), by convexity at \(1,3\). Smaller \(r\) retain the bound. The all-one word gives one cell mass at least \(\theta^n\), while \(\|\mu\|_\infty\le\|\mu\|_q\) and (2) for unbounded \(q\) give the matching exponential upper bound.

## Large deviations of the cheapest legal word

For all \(b\ge1\), at most \(\binom{\lfloor bn\rfloor}{n}\le e^{nH(b)}\) cells admit a word of cost at most \(bn\). If \(\beta\ge\theta_*\), the [Rényi limit at order one](ROBUST_BRANCH_FIBRES.md) gives for every \(\varepsilon>0\) a fixed \(q>1\) with
\[
    \liminf_n H_q(\mu_{\beta,n})/n\ge H(1/\beta)-\varepsilon.
\]
For \(b<1/\beta\), Hölder bounds the probability that \(K_n\le bn\) by \(\exp[(1-1/q)(nH(b)-H_q(\mu_{\beta,n}))]\). Choose \(\varepsilon<H(1/\beta)-H(b)\). The upper tail above \(1/\beta\) is exponentially small because \(K_n\le S_n\). Borel–Cantelli proves the asserted almost-sure convergence. The endpoint \(\beta=1\), when used for a change of measure, is the deterministic all-one word.

For \(\theta\ge\alpha\), \(1<b<1/\theta\), choose \(q>1\) by \(r^q=1-1/b\). Formula (2) and the same counting bound give
\[
 \limsup_n n^{-1}\log\Pr_\theta(K_n\le bn)
        \le (1-1/q)H(b)+q^{-1}\log M(0)=-I_\theta(b).                 \tag{9}
\]
Indeed \(p_{1/b}(e)=p_\theta(e)^q/M(0)\), and taking its expected logarithm gives that last identity. At \(b=1\) use the maximum-cell estimate. The reverse inequality follows from the true code event \(S_n\le bn\) (or the all-one word at \(b=1\)). On the expensive side \(b>1/\theta\) the elementary upper bound
\(\Pr_\theta(K_n\ge bn)\le\Pr_\theta(S_n\ge bn)\) gives rate at most \(-I_\theta(b)\), for any \(\theta\).

For the local lower bound fix \(1<b\le a_*\) and draw the actual word at tilt \(\beta=1/b\). Then both \(K_n/n\) and \(S_n/n\) converge to \(b\). The log likelihood of the same word under \(\theta\) relative to \(\beta\), divided by \(n\), converges to \(-I_\theta(b)\), since it is affine in \(S_n/n\). Restrict the word space to the event where both approximations and the likelihood error are within the desired tolerance. Its \(\beta\)-probability tends to one, so its \(\theta\)-probability has lower exponential rate at least \(-I_\theta(b)\) after sending the tolerance to zero. At \(b=1\) use the deterministic word. Taking neighborhoods in (9) or in the expensive-side bound and using continuity proves (3), including the two endpoints. The same argument gives the expensive-side local rate when \(\theta>1/b\ge\theta_*\) even if \(\theta<\alpha\).

For (4), data processing from the independent words gives the upper bound. Under the first source \(\beta\), the event \(K_n/n\in(1/\beta-\varepsilon,1/\beta+\varepsilon)\) has probability tending to one. Under the second source its upper exponential rate is at most \(-I_\theta(1/\beta)+o_\varepsilon(1)\) by the appropriate side above. Applying data processing to this single event in the *lower* bound for the projected relative entropy and shrinking \(\varepsilon\) proves (4).

For equal-prior testing of \(\theta_1<\theta_2\) in \([\alpha,1)\), there is a unique \(b\) strictly between the two means where their affine log likelihoods per word coincide. Equivalently \(I_{\theta_1}(b)=I_{\theta_2}(b)\). The rule selecting the higher tilt when \(K_n\le bn\) has error probabilities bounded by (9) under the lower tilt and the iid upper-tail bound under the higher tilt. For a matching converse, even a full-word test has average error at least half the sum of the smaller of the two word masses over all compositions of total nearest \(bn\). Stirling's formula gives that grade probability under either hypothesis as \(\exp(-nI_{\theta_1}(b)+o(n))\). This also shows directly how the common error exponent is attained by the minimum-cost threshold.

## Posterior list converse at criticality

Use \(p=p_{\theta_*}\), \(\mu=\mu_{\theta_*}\). For the full infinite code \(X\), let \(X^{(j)}\) denote its tail after \(j\) gaps, \(W_k(x)=3^k\mu_k(x\bmod3^k)\), and \(T_j=\sum_{i\le j}\log(3p(e_i))\), with \(T_0=0\), \(W_0=1\). The identity for a single prescribed prefix implies
\(W_n(X)\ge e^{T_j}W_{n-j}(X^{(j)})\) simultaneously for all \(j\le n\). At any random tail with its original marginal, \(\Pr(W_k<e^{-v})\le e^{-v}\), by summing the corresponding cell masses. Hence, except for probability \(ne^{-v}\),
\[
       \log W_n(X)\ge \max_{0\le j\le n-m}T_j-v .
\]
This is the pathwise all-cut argument of Weaver 135, Lemma 4. For \(\ell=n-m\), the actual prefix posterior has the exact value
\[
 \pi=\Pr(e_1,\ldots,e_\ell\mid X\bmod3^n)\big|_{\text{realized word}}
     = e^{T_\ell} W_m(X^{(\ell)})/W_n(X).
\]
Choose \(v=3\log(n+1)\). If \(D_m=m\log3-H(\mu_m)\), then \(\mathbb E\log^+W_m\le D_m+1\), using the lower-tail inequality just proved. Full critical entropy dimension gives \(D_m=o(m)\). Thus along any \(m=O(\sqrt n)\), \(\log^+W_m(X^{(\ell)})/\sqrt n\to0\) in probability, including bounded \(m\). We obtain
\[
           -\log\pi\ \ge\ \max_{j\le\ell}(T_j-T_\ell)-o_{\Pr}(\sqrt n).
\]
Under the iid code the maximum on the right has the law of the maximum through \(\ell\) of a centered random walk with increments \(-\log(3p(e))\). Its variance is \(\sigma_*^2>0\), and \(\ell/n\to1\). The invariance principle and Brownian reflection give convergence after division by \(\sqrt n\) to \(\sigma_*|N(0,1)|\). No independence between this maximum and the tail density correction is required.

At any observation the conditional probability of a listed prefix with posterior below \(e^{-b}\) is at most the list size times \(e^{-b}\). The same bound holds after averaging over any external list randomization independent of the true code given its observation. Take \(b=(t+\varepsilon)\sqrt n\), bound the remaining probability via the drawdown, then send \(\varepsilon\downarrow0\). The half-normal distribution is continuous, including at zero. This proves (10). More generally the same argument works whenever \(m=o(n)\) and \(D_m=o(\sqrt n)\), a condition that also holds for some deterministic \(m/\sqrt n\to\infty\) sufficiently slowly by \(D_m=o(m)\). This is a lower bound on the needed list or terminal allowance; no matching achievability at criticality is proved. [Weaver, Paper 135 v1, Lemma 4 and §6](https://rstation.ai/problems/collatz/papers/135/v1)

## At an actual fixed positive root

There is an unconditional fixed-root statement distinct from the statistical limits. Let \(a\) be any positive odd integer, \(\theta>1/2\), \(p=-\log_2(1-\theta)>1\), and \(b_\theta=\theta(1-\theta)^{g-1}\). Then
\[
             \sum_{n\ge0} b_\theta^{-n}\mu_{\theta,n}(a\bmod3^n)<\infty.       \tag{11}
\]
In particular every fixed positive odd root is exponentially thinner than a typical \(\mu_\theta\)-cell when \(\theta>\alpha\): the typical log probability per depth is \(\log\theta+(1/\theta-1)\log(1-\theta)\), strictly larger than \(\log b_\theta\). The typical statement follows here from bounded word uncertainty and (2), or from Leen’s entropy dimension and the near-order-one AEP. When \(\theta=3/4\), \(b_\theta=1/3\), and (11) is exactly Weaver 9, Proposition 11.

Indeed, write \(U(x)=(3x+1)/2^{v_2(3x+1)}\) and \(\omega_n(x)=3^n2^{-S_n(x)}\) along the actual forward path. At every positive odd \(a\), words coding its \(n\)-trit residue are bijective with ordinary positive odd predecessors \(U^n(x)=a\), including a possible multiple of three at the remote starting site. Each word has probability \(b_\theta^n\omega_n(x)^p\). The positive real affine correction gives \(x\omega_n(x)\le a\). For a nonperiodic \(a\) a given \(x\) contributes at most once over all depths. Hence the sum in (11) is at most \(a^p\sum_{x\text{ odd}>0}x^{-p}\). For a periodic \(a\), subsequent visits from a given \(x\) multiply its weight by \(\omega_{\rm lap}^p\), where \(\omega_{\rm lap}=\prod_{y\text{ on lap}}3y/(3y+1)\le3a/(3a+1)<1\). Multiply the same bound by \(1/(1-\omega_{\rm lap}^p)\). This is Weaver's trace proof at its natural positive power. Thus (11) retains the original integer at every depth but holds for both cycle and noncycle roots; it does not exclude an escaping orbit. In particular the critical finite-list experiment cannot be applied after conditioning on one ordinary target. [Weaver, Paper 9 v2, Proposition 11](https://rstation.ai/problems/collatz/papers/9/v2)

## Scope and prior results

Weaver’s Paper 9 proves the sharp fair-law positive moment spectrum, a bounded expected word-entropy loss and exponential total-clock estimation at the special tilted law \(p(e)=3/4^e\). Its fixed-total spacing and reversed real numerator are the arithmetic inputs generalized here. PR215 obtains the stronger *bounded*, rather than subexponential, normalized collision energy when \(q=2,\ \theta>1/2\). Its affine-overlap classification implies almost-sure decoding of the first letter from the infinite source at and above \(\theta_*\). PR212 also proves full entropy-rate retention and infinite-source rigidity for arbitrary stationary ergodic gap laws of mean at most \(\log_2 3\). Its separate cost paper identifies the Hausdorff and packing spectrum of source sets with specified minima, by constructing separated block measures. The present statistical statements concern the actual geometric laws, their pairwise testing rates, and a parameter-independent finite-observation decoder over an entire interval. [Weaver, Paper 9 v2, Theorem 5, Corollary 6 and §7](https://rstation.ai/problems/collatz/papers/9/v2) · [PR215 collision renewal](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase11/SUBCRITICAL_COLLISION_RENEWAL.md) · [PR215 affine overlaps](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md) · [PR212 dependent gap dimension](https://github.com/GettysburgResearch/collatz/blob/36c64bdf5d3e7f13a0bd949a01c3a9d6371681ed/research/astra-global-20261128/broad/DEPENDENT_GAP_DIMENSION.md) · [PR212 inverse cost spectrum](https://github.com/GettysburgResearch/collatz/blob/36c64bdf5d3e7f13a0bd949a01c3a9d6371681ed/research/astra-global-20261128/broad/INVERSE_COST_SPECTRUM.md) · [Leen, original tilted entropy dimension](https://doi.org/10.5281/zenodo.23268832)

The finite decoder and Fisher-information estimate require \(1/\theta<\log_2 3\); the elementary real-moment bound (6) is missing on the other side. At the entropy-critical tilt, its own typical source has limiting minimum \(a_*\) by the argument above. Identification of the Haar-typical limiting minimum would additionally require control of the critical cost under the opposite source law. The information identity (4) compares geometric source laws and supplies no such change to Haar, and the finite ordinary representatives in (5) do not select one fixed representative for infinitely many depths.

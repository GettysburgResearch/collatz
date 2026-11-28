# Prescribing a different critical collision law while retaining the true Brownian descent

Fix \(b\ge2\), any prescribed distinct odd \(q_0,\ldots,q_{b-1}\ge3\), and any prescribed countable family \(f_i:\mathbb N\to[-1,1]\). The modified map in [Shadowing to the minimum](SHADOWING_TO_THE_MINIMUM.md) can be chosen so that each initial synchronous phase \(a\in\mathbb Z/(2b)\) satisfies
\[
 \lim_{X\to\infty}\frac1X\sum_{n\le X} f_i(n)
              \left(\mathbf1_{F(n)=a}-\frac1{2b}\right)=0                \tag{1}
\]
for every \(i\). One may prescribe the tests from the complete **true** orbits before constructing \(U\). In particular the \(U\)-phase can be asymptotically independent of the entire genuine limiting Brownian descent and the genuine minimum law.

Let \(H_U(n)\) be the first time the modified path enters its designated two-cycle, \(L=\log n\), and \(Z,\tau,\sigma,\mu\) as in the companion. For uniform \(n\le X\),
\[
 Z-1\le H_U\le Z+3\quad\hbox{pointwise},\qquad
                       (H_U-\tau)/\sqrt L\longrightarrow0
                       \quad\hbox{in probability}.                       \tag{2}
\]
The modified log-height process through its own actual cycle entrance has the same limiting Brownian motion as the genuine process through its minimum, jointly with \(m_T\). The initial phase can be chosen independent of this joint limit. Thus for independent uniform starts \(n_1,\ldots,n_k\le X,\ k\ge2\), at the same date
\(h=\lfloor\mu\log X+\sigma u\sqrt{\log X}\rfloor\),
\[
           \lim_{X\to\infty}
             \Pr(U^h n_1=\cdots=U^h n_k)=(2b)^{1-k}\Phi(u)^k.           \tag{3}
\]
At \(k=2,u=0\) the limit is \(1/(8b)\). The [genuine criterion](../ordinary/SYNCHRONOUS_PHASE_DISPERSION.md) concerns collision under the unmodified shortcut. The map here has an actual different branch no later than the true minimum on every single trajectory. Neither genuine orbit behavior after that minimum nor true basin masses are prescribed.

## Selecting frequencies simultaneously for all relevant source cutoffs

The companion's proof uses a divisible tower with \(Q_j\equiv1\bmod 2b\), successive quotient \(1\bmod2b\), \(\operatorname{dist}(Q_j\gamma,2\mathbb Z)\le Q_j^{-1/6}\), and \(B_j=Q_{j-1}^{1/1000}\), where \(\gamma=\log_2 3\). Here choose the slower growth
\[
                Q_{j-1}^{\sqrt j}\le Q_j\le Q_{j-1}^{2\sqrt j}          \tag{4}
\]
for all sufficiently large \(j\). The companion's estimates (3)–(5) hold verbatim: the \(\log\log B\) spacings still tend to infinity, and the upper bound for the logarithm two frequency steps ahead is smaller than the one used there. No other use of its tower-growth bounds is made.

Put \(Q=Q_{j-1}\), \(N=\lceil Q^{\sqrt j}\rceil\), \(P=2bQN\). There are \(\gg_b N^{4/5}\) distinct candidate frequencies \(q=Q(1+2bk)\in[P,3P]\) with \(N\le k<2N\) and \(\operatorname{dist}(q\gamma,2\mathbb Z)\le q^{-1/6}\). To verify this use \(\|t\gamma\|\gg t^{-3}\) from the [audited rational-log bound](CHUDNOVSKY_LOGARITHM_IMPORT.md). For \(\alpha=bQ\gamma\) the first convergent denominator \(v\ge N^{1/4}\) is \(\ll_b (QN^{1/4})^3\le N^{9/10}\) at large stages. In each block of \(v\) consecutive \(k\)'s the angles \(k\alpha\) differ by at most \(1/v\) from a shifted full grid of mesh \(1/v\), using a reduced convergent of denominator \(v\). An arc of length \(cN^{-1/5}\) centered at \(-Q\gamma/2\bmod1\) contains \(\gg_c vN^{-1/5}\) entries. The full blocks cover \(N-o(N)\) dates. Since \(P=N^{1+o(1)}\), their frequencies meet the required resonance and (4) at large \(j\).

For all our candidate frequencies the subsequent frequency, whichever choice is made then, is at most \((3P)^{2\sqrt{j+1}}\). Fix the integer cutoff \(D=\lceil(3P)^{5\sqrt{j+1}}\rceil\). Our choice will control all source shells \(2^J\le n<2^{J+1}\) for integers \(0\le J\le (3P)^{1/1000}+1\), which include the whole stage of use \(B_j\le J\le B_{j+1}\). On the circle of length two, with coordinate \(v\in[0,2)\), use weights supported on \(0\le v<1\),
\[
   W_{J,i,c}(v)=(\log2)2^v f_i(\lfloor 2^{J+v}\rfloor)\mathbf1_{v<c},
 \qquad 1\le i\le j,\qquad c=0,1/j,\ldots,1 .
\]
They have uniformly bounded \(L^2\)-norm. Their unnormalized integrals over whole integer cells are exactly \(2^{-J} f_i(n)\); the possible last truncated cell has error \(O(2^{-J})\). Include the constant test among the countable family.

For each weight let its finite energy at \(q\) be
\[
                    E_W(q)=\sum_{\substack{0<|t|\le D\\q\mid t}}
                                 |\widehat W(t)|^2 .
\]
Parseval gives \(\sum_q E_W(q)\ll \max_{d\le D}\operatorname{div}(d)=P^{o(1)}\) over all candidate \(q\). Here \(\operatorname{div}\) counts positive divisors. For an elementary bound, the factors from primes up to \(\sqrt{\log D}\) contribute logarithm \(O(\sqrt{\log D}\log\log D)\), and the remaining prime factors counted with multiplicity are at most \(2\log D/\log\log D\). Thus the log of the divisor bound is \(O(\log D/\log\log D)\). By (4), \(\log\log P\gg j\log j\), while \(\log D=O(\sqrt j\log P)\), giving the stated \(P^{o(1)}\). Applying this bound to \(O(j^2 P^{1/1000})\) weights leaves at most \(P^{1/1000+o(1)}\) candidates with \(E_W(q)>j^{-2}\) for any one of them. This is smaller than the number of resonant candidates; choose any remaining \(Q_j=q\). This induction treats every cutoff in the indicated range, including cutoffs near transition stages.

For any interpolating pattern \(G_{j,s}\) of the companion, its label indicator evaluated at \(J+v\), minus \(1/(2b)\), is a function \(g\) on the circle of length two with mean zero, period \(2/Q_j\), absolute value at most one and total variation \(O_b(Q_{j+1})\). Its Fejér mean through degree \(D\) has Fourier support only at nonzero multiples of \(Q_j\) and \(L^2\)-norm at most one with normalized circle measure. Its \(L^1\) distance from \(g\) is \(O_b(Q_{j+1}\log(2D)/D)=o(1)\): averaging the translation estimate \(\|g(\cdot+t)-g\|_1\le\mathrm{Var}(g)|t|\) against the Fejér kernel uses its bound \(O(\min(D+1,[(D+1)t^2]^{-1}))\) for \(|t|\le1\). Hence
\[
                \left|\int W_{J,i,c}(v)g(v)\,dv\right|\ll_b j^{-1}+o(1)
\]
by Cauchy–Schwarz and the uniform bound on \(W\). This holds uniformly for all \(s\) and all possible next choices. Passing from the integral to exact labels at integer starts adds \(O_b((Q_{j+1}+1)2^{-J})=o(1)\) on late shells of the stage, by splitting the cells at the pattern's \(O_b(Q_{j+1})\) boundaries. The grid of \(c\)'s approximates every partial shell with normalized cost \(O(1/j)+O(2^{-J})\). Replacing \(G_J\) by the true odd-part scale and imposing the specified dyadic rays cost \(o(1)\) as in the companion, even with the bounded weights. Summing the dyadic shells proves (1); no limit of the unweighted average of \(f_i\) is required.

## The native collision and height observables

For (2), if \(U\) enters a designated cycle before the first discrepancy, it is at \(q_i\) or \(2q_i\), and a discrepancy is forced by the next odd source. The first changed edge itself lands at a cycle vertex or four times one, or is the designated odd edge, so at most two more steps reach the cycle. The companion's (1) proves the second assertion.

For clarity, the two centered height processes at \(0\le s\le1\) are obtained from
\[
 \frac{\log U^{k}n-\log n+k/\mu}{c_*\sqrt{\log n}},\
                  k=\lfloor sH_U(n)\rfloor,\qquad
 \frac{\log T^{j}n-\log n+j/\mu}{c_*\sqrt{\log n}},\
                  j=\lfloor s\tau(n)\rfloor,\qquad c_*=\sigma/\mu .
\]
Both finite paths may be linearly interpolated. Their supremum distance tends to zero in probability. Indeed their two indices differ by \(o_P(\sqrt L)\) uniformly. Through the common part this follows from the true process modulus in the companion's (6). On \([Z,\tau]\), every genuine log height is \(o_P(\sqrt L)\) uniformly since \(\log m_T=O_P(1)\), \(\tau-Z=o_P(\sqrt L)\), and the same modulus controls fluctuations from the endpoint. All modified heights after the first discrepancy are bounded by \(8\max_i q_i\). These estimates also cover an index straddling \(Z\) by \(o_P(\sqrt L)\) dates. The [original height-process proposition](https://doi.org/10.5281/zenodo.23269488) supplies the Brownian limit. One may prescribe a countable convergence-determining family of bounded Lipschitz tests of the genuine interpolated height path and minimum in the separable space \(C[0,1]\times\mathbb N\). Using (1) gives joint phase independence. For (3) it already suffices to prescribe indicators of the true standardized minimum-clock half-lines at rational endpoints.

At the deterministic \(h\) above, \(\log n-\log X=O_P(1)\). By (1), (2), the genuine minimum-clock CLT and continuity of its limit, the probability of entering by \(h\) with any fixed initial phase tends to \(\Phi(u)/(2b)\). For equal initial phases, every path already in its designated cycle at the same date is at the identical vertex. Different phases remain distinct. Contributions with all paths entered give exactly the claimed limit by independence.

If a collision occurs outside the designated cycles, all the samples are still outside. The event that any such path has already taken a changed edge costs \(o(1)\): it forces \(h-3\le Z\le h\), and \(Z\) has the continuous limiting standardized law. Except for \(o(1)\) we can also discard \(\tau=h\). On the remaining event with no change before the comparison, every source has genuine \(\tau>h\): indeed \(h\le Z\le\tau\). If the genuine states agree at \(h\), all their true future minimum values and first times to them agree, hence all their integer \(\tau\)'s coincide. Independent samples have such a tie with probability at most the largest atom of the one-sample \(\tau\) distribution, tending to zero by the Gaussian scaling and continuity (partition a large central compact range into fixed narrow bins, then shrink them). This proves (3) at every fixed \(u\).

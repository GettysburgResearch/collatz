# Two nonnegative losses for a finite critical coding policy

At \(W\ge2\), let \(m_s=\mu_{*,W}(s)\) for a unit state \(s\), let \(N=2\cdot3^{W-1}\), and write \(p(e)=\theta q^{e-1}\), \(t_*=-\log q\), \(a_*=1/\theta\). For every legal inverse gap let \(u=I_e(s)\bmod3^{W-1}\) and let \(v_u\) be the conditional distribution of the three lifts of \(u\) under \(\mu_{*,W}\). In the planted source model the posterior probability of the first gap is
\[
                       Q_s(e)=p(e)\mu_{*,W-1}(u)/m_s.
\]
The actual finite control kernel \(K_e\) selects a **uniform** lift of \(u\). With \(V(s)=-\log(Nm_s)/t_*\), there is an exact pointwise identity for every legal edge,
\[
 t_*\{e+K_eV(s)-V(s)-a_*\}
       =-\log Q_s(e)+D(\operatorname{Unif}_3\Vert v_u).                 \tag{1}
\]
Indeed \(t_*a_*=\log(3\theta/q)\) follows from critical entropy. Expanding the three logarithms of \(v_u\), the right side becomes \(t_*(e-a_*)+\log m_s-\tfrac13\sum_{t\equiv u}\log m_t\). This also verifies the sign and direction of the last divergence.

Consequently \(t_*(c_W-a_*)\) is exactly the least stationary mean of the right side of (1), using actual finite policies and their actual stationary marginals. For a randomized stationary action law \(\pi_s\), the first loss averages to \(H(\pi_s)+D(\pi_s\Vert Q_s)\). Both terms on the right of (1) must become small on average for gains tending to \(a_*\). This identity is complementary to the projected true-source inequality for the optimal Bellman bias. The displayed log density itself is a feasible lower bias at gain \(a_*\); its gain is explicit and can be below \(c_W\). [Finite control and critical entropy identity](../phase5/CRITICAL_BELLMAN_LIFTS.md) · [Weaver 150, finite stationary entropy](https://rstation.ai/problems/collatz/papers/150)

There is an explicit uniform lower bound on every entry of every \(v_u\). Conditional on a \((W-1)\)-trit source, disclose its first \(W-2\) planted gaps. Their affine map fixes all but the first trit of the remaining endpoint: the endpoint law is \(\mu_*\) conditioned on this one unit trit. The next source trit is a permutation of the next endpoint trit because the residual affine slope is a ternary unit in the normalized coordinates. Removing the gap information gives a convex mixture of these permuted root triples. For \(W=2\) this has no gaps to disclose. Geometric memorylessness \(m_s=\theta 1_{2s\equiv1\ (3)}\mu_{*,1}((2s-1)/3)+qm_{2s}\) on the six units modulo nine (interpreting the first-trit law as zero at zero) gives both root triples up to permutation as
\[
         \left(\frac qD,\frac{q^3}D,1-\frac{q+q^3}{D}\right),
                   \qquad D=1+q^2+q^4.
\]
The smallest entry is \(\delta=q^3/D\): for the last coordinate the numerator difference from \(q^3\) is \((1-q)(1+q^2-q^3)>0\). Thus every child probability is at least \(\delta\). In particular \(V\) has last-trit oscillation at most \(t_*^{-1}\log((1-2\delta)/\delta)\), and the two divergence directions on any conditional triple are comparable by constants depending only on \(\delta\) (Taylor's theorem on this compact simplex). [Leen, §5, conditional root-cylinder laws](https://doi.org/10.5281/zenodo.23268832)

Under the projected true source–gap law, the average of \(-\log Q_s(e)\) equals \(d_W=H(E\mid Z_W)\), and the child lower marginal is exactly \(\mu_{*,W-1}\). The reverse conditional divergence in (1) therefore has mean \(O_\delta(d_W)\) under this same law. Full entropy dimension gives \(d_W\to0\). The projected source–gap law generally fails the actual finite stationary equations, so its small loss cannot be substituted into the stationary minimum. This is the precise loss to control in a proposed actual streaming encoder.

For provenance, the published supplied-state positive-policy theorem used in the preceding pressure theorem retains its original separation precision. A November 16 comment proposed changing \(L=3n\) to \(4n\) in Weaver 127 §6. The same author withdrew it at 17:35 UTC after observing that the offsets compared modulo \(3^{3n}\) had already been divided by \(3^n\). This gives \(3^{4n}\) divisibility of the undivided numerator difference, as required. [Public proposal and subsequent withdrawal](https://rstation.ai/r/collatz/posts/76) · [Weaver 127, §6](https://rstation.ai/problems/collatz/papers/127)

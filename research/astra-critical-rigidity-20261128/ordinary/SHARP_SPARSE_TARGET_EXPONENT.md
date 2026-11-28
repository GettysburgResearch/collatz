# A sharp square-root law for sparse high targets before the ordinary minimum

**Proposed, source-qualified written result.** For uniform positive \(U_X\) and the genuine shortcut minimum date \(\tau\), consider the estimate
\[
 \Pr(\exists t\le\tau(U_X):T^t U_X\in E)
                 \le C_\kappa(|E|/Y)^\kappa+o(1)                       \tag{1}
\]
uniformly for deterministic \(E\subset [Y,2Y]\cap\mathbb N\), as \(X,Y\to\infty\) independently. All times are nonnegative. Then **(1) holds at \(\kappa=1/2\)**. The square-root order is sharp even among general moduli: writing
\[
 \mathcal H(\delta)=\limsup_{X,Y\to\infty}\
       \max_{\substack{E\subset[Y,2Y]\cap\mathbb N\\ |E|\le\delta Y}}
                 \Pr(\exists\,0\le t\le\tau(U_X):T^tU_X\in E),
\]
there are absolute \(c,C>0\) with \(c\sqrt{\delta}\le\mathcal H(\delta)\le C\sqrt{\delta}\) for all sufficiently small \(\delta>0\). The joint limsup is the upper envelope over cutoff pairs. For some other cutoff pairs the entire shell lies far above the initial descent.

The transfer from physical integers to stationary concentration is proved below, in both directions. The stationary endpoint itself is an **earlier result**: Weaver's Theorem in §1 of Paper 146/v1 proves \(t^2\lambda\{\rho>t\}\to c_*\in(0,\infty)\) for the original geometric Syracuse law on full additive Haar probability. We use this as a written preprint input. Valbuena's original theorem supplies the preceding strong-\(L^p\) range \(p<2\) and failure at two, which alone suffices to exclude every exponent above one half. The earlier [sparse high target proof](SPARSE_HIGH_TARGETS.md) treats all exponents strictly below one half. [Weaver, November 14, original Theorem and normalization](https://rstation.ai/problems/collatz/papers/146/v1) · [Valbuena, original stationary theorem, parts 2 and 3](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/quadratic-cylinder-energy.tex)

## Positive tests on true integer targets

Write \(\gamma=\log_2 3,\ v=2-\gamma>0\). Let \(\lambda\) be additive Haar probability on \(\mathbb Z_3\), and \(\nu\) the law of \(R=\sum_{i\ge1}3^{i-1}2^{-s_i}\) for independent gaps \(a_i\) with \(\Pr(a_i=j)=2^{-j}\) and \(s_i=\sum_{h\le i}a_h\). Fix a union \(A\) of residues modulo \(3^d\), of mass \(z=\nu(A)>0\). Use the actual odd targets
\[
                 E_Y=\{y\in[Y,2Y]\cap(2\mathbb Z+1):y\bmod 3^d\in A\}.
\]
Here \(|E_Y|/Y\to\lambda(A)/2\). There is an absolute \(c>0\) such that
\[
 \liminf_{J\to\infty}\ \liminf_{Y\to\infty}
 \Pr\big(\exists t\le\tau(U_X):T^tU_X\in E_Y\big)
          \ \ge\ c\,z,\qquad X=\lfloor2^{J+1}Y\rfloor , \tag{2}
\]
where \(J\) is a positive integer. All constants on the right are independent of \(A,d\). The convergence onsets may depend on them.

First restrict the sampled integer to be odd and in \([2^JY,\,2^{J+1/4}Y]\). Its relative frequency in \([1,X]\) tends to a positive absolute constant. For fixed \(J\) and any fixed finite number of odd returns, the valuation gaps of this conditional sample converge in law to independent \(a_i\): any given chronological list of total \(s\) selects one odd residue class modulo \(2^{s+1}\), by the native parity-word dictionary. Finite-dimensional pointwise convergence is convergence in total variation on the countable lists, as the limiting probabilities have total mass one. The real multiplier after these returns is \(3^k2^{-s_k}(1+o_P(1))\), uniformly over the fixed finite list of times. Indeed truncate the total gap at a finite bound; then the true states are all at least a constant times \(Y\), so the product of the additive corrections tends to one. The global minimum of the conditional sample stays bounded in probability by the proper minimum law and the positive relative length of the selected source interval. Consequently all these fixed finitely many odd states are seen before the true minimum with probability tending to one: the intervening native states also tend to infinity in probability. [Leen, proper minimum law and Terras exactness](https://doi.org/10.5281/zenodo.23269488)

At an odd return \(k\ge d\), its actual target residue modulo \(3^d\) is determined entirely by its last \(d\) valuations in reversed order, by the affine composition formula. With the iid gaps write \(A_k\) for the event that this reversed residue lies in \(A\); its probability is \(z\). If
\[
                  s_k-\gamma k\in [J-1/2,J-1/4]=I_J,                  \tag{3}
\]
then the homogeneous odd state is in \([2^{1/4}Y,2^{3/4}Y]\) for every real starting value in the selected interval. There are fixed margins to the target octave boundaries. Thus for each fixed \(J\), the physical limiting lower bound for the marked hitting probability is at least a positive absolute constant times the probability that (3) and \(A_k\) occur for some \(k\) with \(|k-J/v|\le\sqrt J,\ k\ge d\).

We bound the expected number \(Z_J\) of these marked dates below. Truncate the total of the last \(d\) gaps by a fixed integer \(B=B(A,d)\) chosen to retain at least \(z/2\) of their probability on \(A_k\). Among \(|k-J/v|\le\sqrt J\), a positive absolute fraction admit an integer \(m_k\) satisfying \(m_k-\gamma k\in I_J\). Indeed \(\gamma\) is irrational and the fractions \(\{k\gamma\}\) are equidistributed on any consecutive interval of length tending to infinity, uniformly in its starting point by the finite geometric-sum test. The interval in (3) has length \(1/4\), and \(J\) is integral. For all these \(k\) and each retained final total \(b\le B\),
\[
           \Pr(s_{k-d}=m_k-b)\ \ge\ c_0/\sqrt J                       \tag{4}
\]
for all sufficiently large \(J\), with absolute \(c_0>0\). In fact \(m_k=J+\gamma k+O(1)\), so \(m_k-b-2(k-d)=J-vk+2d-b+O(1)\) is within \(2\sqrt J\) of zero eventually. The negative-binomial probability \(\binom{m_k-b-1}{k-d-1}2^{-(m_k-b)}\) has the claimed uniform lower bound there by Stirling, since \(k/J\to1/v\). Independence of the first \(k-d\) gaps and the final list gives \(\mathbb E Z_J\ge c_1 z\) with \(c_1\) absolute.

The first marked date is a stopping time for the **chronological** gaps: its residue test reverses only the last \(d\) already observed gaps, and the window of permitted dates is deterministic. After this date, unobserved gaps are independent. A later marked date at lag \(h\) requires the fresh increment \(s_h-\gamma h\le1\), because both drift values must lie in \(I_J\). Its probability is at most \(C e^{-ch}\) by the exponential Markov inequality. Therefore \(\mathbb E Z_J\le(1+\sum_{h\ge1}C e^{-ch})\Pr(Z_J>0)\), with absolute constants. Combining with the positive fixed source fraction gives (2).

## Why an exponent above one half is impossible

If (1) held with some \(\kappa>1/2\), first taking \(Y\to\infty\) for fixed \(J\), then \(J\to\infty\), would give
\[
                \nu(A)
                              \le C\,\lambda(A)^\kappa                 \tag{5}
\]
for every finite union of ternary cylinders, with a uniform constant. Choose \(q>1/2\) strictly below \(\min(\kappa,1)\). Equation (5) gives \(\nu(A)\le C\lambda(A)^q\), since \(\lambda(A)\le1\).

For a direct finite-level contradiction, let \(\rho_d\) be the Haar conditional density on the ternary residue partition. The set \(A=\{\rho_d>t\}\) is a union of those cylinders, and \(t\lambda(A)\le\nu(A)\). The last bound gives \(\lambda(\rho_d>t)\le (C_q/t)^{1/(1-q)}\), uniformly in \(d\). The exponent exceeds two; integrating the tails for \(t\ge1\) gives \(\sup_d\|\rho_d\|_2<\infty\). The \(\rho_d\) are the martingale of conditional expectations of Valbuena's \(L^1\) density \(\rho\), and converge to it almost everywhere. Fatou would give \(\rho\in L^2\), contrary to his theorem. This excludes all \(\kappa>1/2\) in the actual integer estimate. The same argument at \(\kappa=1/2\) shows that an actual endpoint estimate would require a weak-\(L^2\) stationary density: \(\sup_{t>0}t^2\lambda(\rho>t)<\infty\). Strong \(L^2\) failure alone leaves that possibility open. No rate of divergence of the finite-level quadratic energies and no assumption about ordinary cycles is needed.

## Exact equivalence at the critical exponent

More generally, for every fixed \(0<\kappa<1\), (1) holds **if and only if**
\[
         \nu(B)\le C\,\lambda(B)^\kappa\quad\text{for all measurable }B,
 \qquad\text{equivalently}\qquad
                   \rho\in L^{1/(1-\kappa),\infty}(\lambda).           \tag{6}
\]
In particular the physical estimate at \(\kappa=1/2\) follows from the weak-\(L^2\) case proved by Weaver. His notation is \(A_i=3^i2^{-s_i},\ B_n=(1/3)\sum_{i=1}^nA_i\), so his \(\lim B_n\) is precisely our \(R\) under the same probability.

Necessity on finite unions of cylinders is (2). The finite-level tail argument for \(\rho_d\) gives the weak-space bound on \(\rho\): for \(t>0\), use almost-everywhere convergence and the bound at each \(t'<t\), then \(t'\uparrow t\). Conversely a density with \(\lambda(\rho>t)\ll t^{-p}\), \(p>1\), satisfies \(\int_B\rho\,d\lambda\ll_p\lambda(B)^{1-1/p}\) by integrating \(\min(\lambda(B),Ct^{-p})\) over \(t>0\).

For sufficiency in the physical estimate, revisit the word-counting step immediately **before** (5) of [Sparse high targets](SPARSE_HIGH_TARGETS.md). In its notation the available upper bound on (4) is
\[
       C\,\mathbb E\sum_{k=0}^{K} f_k(R)\mathbf1_{\{s_k-\gamma k\in I\}}.
\]
Here \(R\) is built from one iid string of **reversed** gaps and \(f_k(R)\) only depends on its first \(k\) gaps, by the ternary congruence. For \(t>0\), stop this string at the first \(k\le K\) for which both \(f_k(R)>t\) and \(s_k-\gamma k\in I\). Its future increments are independent. Given any such first mark, the expected number of later visits of the drift walk to \(I\) is bounded by an absolute constant as in the proof of (2), enlarging the constant for the fixed width of this \(I\). Therefore
\[
 \mathbb E\sum_{k=0}^{K}\mathbf1_{\{f_k(R)>t,\ s_k-\gamma k\in I\}}
        \le C\,\Pr\!\left(\max_{0\le k\le K} f_k(R)>t\right).
\]
This uses a stopping time in the reversed representation. The earlier lower bound uses a stopping time in the forward chronology. Both are adapted to their respective iid strings.

Put \(\delta=|F|/B\), so \(\int f\,d\lambda=\delta\) and \(f\le4\). Haar's elementary nonnegative martingale maximal inequality gives
\(\lambda\{\max_k f_k>t\}\le\min(1,\delta/t)\). For completeness, partition this event by first exceedance of \(t\) on the finite residue filtration. On each piece the integrals of \(f_k\) and \(f\) coincide, hence \(t\) times its measure is at most the integral of \(f\) there. By (6), the last probability with \(R\) sampled under \(\nu\) is at most \(C\min(1,(\delta/t)^\kappa)\). Integrating \(0\le t\le4\) gives \(O_\kappa(\delta^\kappa)\) since \(\kappa<1\). The original proof's even-entrance summation, large-source transport, stopped-height bound, and initial dyadic stripping now give (1) with this exact exponent. No loss in the exponent or assumption of independence between the residue and the real clock occurs.

## Matching order of the worst physical mask

Weaver's exact positive stationary tail also gives the matching lower order, beyond failure of higher powers. For small \(\delta\), take \(t=2\sqrt{c_*/\delta}\). The Haar measure of \(D=\{\rho>t\}\) is between \(\delta/8\) and \(\delta/2\) for small \(\delta\), and \(\nu(D)\ge t\lambda(D)\gg\sqrt{\delta}\). Approximate \(D\) by a finite union \(A\) of ternary cylinders in the finite measure \(\lambda+\nu\), with symmetric-difference mass less than \(\min(\delta/4,\nu(D)/2)\). This is possible because cylinders generate the Borel sigma-field. Thus \(\lambda(A)<\delta\) and \(\nu(A)\gg\sqrt{\delta}\). The actual odd targets of (2) have \(|E_Y|/Y\to\lambda(A)/2<\delta\). Equation (2), choosing a sufficiently large fixed \(J\) before taking \(Y\to\infty\), gives \(\mathcal H(\delta)\gg\sqrt{\delta}\). The upper bound follows from (1) with \(\kappa=1/2\). This uses neither a stationary pointwise evaluation at an ordinary integer nor any assumed divergence of an ordinary trajectory.

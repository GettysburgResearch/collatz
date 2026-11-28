# The finite-window optimum is a directed transport problem on one doubling cycle

At window \(W\ge2\) put \(N=2\cdot3^{W-1}\). Index unit residues \(s\bmod3^W\) by \(k\bmod N\) through \(s=2^k\). Doubling traverses one cycle since 2 is primitive modulo powers of 3. A finite inverse policy always appends a uniform top trit after its odd division. Its stationary source law therefore equals a freely chosen lower marginal \(\nu\) on units \(u\bmod3^{W-1}\), extended by one Haar trit. Set
\[
 \alpha_k=\nu(2^k\bmod3^{W-1})/3,\qquad
 \beta_{\log_2(1+3u)}=\nu(u),
\]
with \(\beta\) zero off the displayed addresses. Here \(\log_2\) means the finite discrete logarithm modulo \(3^W\). The map \(u\mapsto1+3u\bmod3^W\) is injective. A source at \(k\) can select child class \(u\) at a positive cost \(e\) precisely when \(k+e=\log_2(1+3u)\bmod N\). The target class receives a fresh uniform top trit. Arbitrary transport couplings of \(\alpha\) and \(\beta\) consequently produce exactly the finite stationary policies with this lower marginal, allowing randomization and zero probabilities. One uses the smallest positive representative of each required cost. A zero modular difference then costs \(N\).

For \(0\le k<N\) let \(D_k=\sum_{j=0}^k(\alpha_j-\beta_j)\), so \(D_{N-1}=0\). The minimum expected gap among these policies is exactly
\[
 \boxed{\ C_W(\nu)=\sum_{k=0}^{N-1}D_k+N\max_k(\alpha_k-D_k),\qquad c_W=\min_\nu C_W(\nu).\ }    \tag{1}
\]
To prove it, let \(J_k\) be total mass traversing the directed edge \(k\to k+1\), counting steps with multiplicity. Flow balance gives \(J_k-J_{k-1}=\alpha_k-\beta_k\); mandatory positive gaps give \(J_k\ge\alpha_k\). The minimum solution to these inequalities is \(J_k=D_k+\max_l(\alpha_l-D_l)\). Its sum is the displayed objective. Conversely route every particle by the mandatory first step and subtract \(\alpha_k\) from the current on edge \(k\to k+1\). The remaining current is nonnegative, has balance for sources \(\alpha\) shifted forward by one and sinks \(\beta\), and vanishes on at least one edge. Cutting there produces a directed line. Pass its incoming mass and its local source mass forward after serving its local sink; conservation makes every service feasible. This decomposes its current into paths, including paths of zero residual length. Prefixing the mandatory first step routes all mass at the stated cost. The all-policy minimum equals the Bellman value by finite occupation-measure duality or by using a minimizing stationary Bellman selector. [Finite decision input](CRITICAL_BELLMAN_LIFTS.md)

A second expression clarifies the dual. Write \(r^N_k(j)=[j-k-1]_N\in\{0,\dots,N-1\}\) and let \(l=\log_2 u\bmod N/3\), \(\psi(l)=\log_2(1+3\cdot2^l)\bmod N\). A cut forces a net forward transport of at least the difference between the mean target and source ranks on its directed line. The cut of zero residual current attains equality. Hence
\[
 C_W(\nu)=1+\max_k\mathbb E_\nu\left[
 r^N_k(\psi(l)) - N/3 - r^{N/3}_{k\bmod N/3}(l+1)\right].         \tag{2}
\]
Indeed the mean rank of the three shifted source lifts \(l+1+iN/3\) is \(N/3+r^{N/3}_{k\bmod N/3}(l+1)\). This expresses the whole finite optimization as a minimax game with one variable per lower residue and one constraint per cut.

For the critical projected source \(m_k=\mu_{*,W}(2^k)\) and \(\nu=\mu_{*,W-1}\), the geometric-gap recurrence is \(m_k=\theta_*\beta_{k+1}+(1-\theta_*)m_{k+1}\). If the starting law were \(m\), its planted edge current would be \(m_k/\theta_*\). The source of an actual stationary finite policy must instead be \(\alpha\). Accordingly the current in (1) equals \(m_k/\theta_*+\sum_{j\le k}(\alpha_j-m_j)\) plus the constant needed for the mandatory first step and the minimizing cut. One cannot impose the planted lower marginal for free merely because its newest-digit conditional entropy approaches \(\log3\). The obstruction is a cumulative discrepancy in the *cyclic discrete-log ordering*. This is a different constraint from ordinary real ordering or total variation of the last trit. Optimizing the marginal in (1) remains essential.

For every bounded-cost stationary marginal, (1) also gives a simple character estimate. For integer \(b\),
\[
 |\widehat\alpha(b)-\widehat\beta(b)|\le 2\pi |b|\,C_W(\nu)/N,
\]
by coupling through paths of length \(e\) and using \(|1-e^{2\pi i b e/N}|\le2\pi|b|e/N\). For \(3\nmid b\), the uniform top lifts make \(\widehat\alpha(b)=0\). Thus the Fourier coefficient of \(\log_2(1+3u)/N\) under the stationary lower source is at most \(2\pi |b|C_W(\nu)/N\). This particular observable uses a multiplicative character of the shifted variable. Additive-character flattening of the iid ternary offset concerns another transform.

## Exact primitive multiplicative-character transform

Write \(M=3^{W-1}\) and \(m=|U_M|=N/3\), with \(W\ge3\). Let \(\chi\) be a unit character modulo \(3^W\) that is primitive at that conductor, and let \(\lambda\) be a multiplicative character of \(U_M\). Then
\[
 \left|\frac1m\sum_{u\in U_M}\chi(1+3u)\overline{\lambda(u)}\right|^2
 =\begin{cases}3/(2m),&\lambda\text{ is primitive at }M,\\0,&\text{otherwise}.\end{cases}       \tag{3}
\]
Indeed its square is the Fourier coefficient of the multiplicative autocorrelation
\[
 K(a)=\frac1m\sum_{u\in U_M}\chi\left(\frac{1+3au}{1+3u}\right).
\]
The substitution \(v=u/(1+3u)\) permutes \(U_M\), with inverse \(u=v/(1-3v)\); the argument becomes \(1+3(a-1)v\). At \(a=1\) this gives 1. If \(j=v_3(a-1)<W-2\), the new arguments uniformly cover the difference of the principal-unit subgroups at depths \(j+1,j+2\). The primitive character sums to zero on both. For \(j=W-2\) the arguments instead cover the two nonidentity elements in the order-three kernel at depth \(W-1\); their mean is \(-1/2\). Thus on the lower group \(K\) is supported on the last order-three subgroup, with values \(1,-1/2,-1/2\). Its Fourier coefficient is zero for a character trivial on that subgroup, and \(3/(2m)\) for the other characters, proving (3).

There is a concrete transport consequence. Take \(\chi(2)=\exp(2\pi i/N)\) and any primitive \(\lambda\) on \(U_M\). For \(0<\varepsilon\le1\) there exists a phase \(|a|=1\) such that the probability with density \(1+\varepsilon\Re(a\lambda)\) against uniform on \(U_M\) requires
\[
 C_W(\nu)\ \ge\ \frac{\varepsilon\sqrt{3/(2m)}}{2\sin(\pi/N)}
 \ \ge\ \frac{3\varepsilon}{2\pi\sqrt2}\sqrt N.                    \tag{4}
\]
Its primitive source-angle coefficient vanishes because of the uniform lifts. In its sink coefficient the constant term vanishes by (3); the two terms from \(\lambda,\overline\lambda\) have equal absolute value by the same identity. Choose \(a\) to align their phases. Telescoping a unit-circle character along each directed edge bounds the coefficient difference by \(2\sin(\pi/N)C_W(\nu)\). This proves (4). It excludes a particular family of prescribed stationary marginals, each with bounded density and bounded reciprocal density when \(\varepsilon<1\). It leaves the optimally chosen marginal in (1) free. Combining the exact transform with a bound on the nonlinear Bellman potential remains open.

The [finite control](check_cyclic_transport.py) compares the cumulative-current formula and cut ranks against a full independent particle assignment in 144 physical fixtures. It also checks (3) on actual primitive characters by exact cyclotomic polynomial reduction. No floating Fourier transform enters that comparison.

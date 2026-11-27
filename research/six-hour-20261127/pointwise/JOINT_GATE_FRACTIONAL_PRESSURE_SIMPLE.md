# Exact fractional moment rates with the genuine prefix gate

Use the original geometric word law, the principal payoff \(Z_n(z)=2^{A_n}/(m+zG)\) with fixed \(z\ge0\), and the all-prefix gate \(W_n=\{A_j\le aj,\ 1\le j\le n\}\), where \(a=7/4\). Put
\[
 d=H_2(1/a),\qquad L=\log_2\frac a{a-1},\qquad
 p_*=\frac{d(L-1)}{L-d}=0.9238628424\ldots,
 \qquad \gamma=(7/8)(7/6)^{3/4}.
\]
For **every real \(p\le p_*\)** the original joint moment satisfies
\[
 \lim_{n\to\infty}n^{-1}\log\mathbb E[\mathbf1_{W_n}Z_n(z)^p]=\log\gamma<0. \tag{1}
\]
Furthermore the ratio of this expectation to \(\gamma^n\) is bounded above and below by powers of \(n+1\) depending only on \(p,z\). These are genuine joint estimates, retaining the true gate on each source term. The first moment whose vanishing detects surviving ordinary atoms is at \(p=1\). Equation (1) leaves it open.

Write \(D\) for the union over all depths of the least positive odd sources of accepted words. PR 201 gives \(\#(D\cap[1,M])\ll M^d\). In brief, a witnessing word for a source in \([2^j,2^{j+1})\) has division clock at least \(j\); its first exponent completion beyond or at \(j\) has odd index at least \(j/a\). Thus its first \(j\) shortcut letters include at least \(j/a\) odd departures. Each such binary parity word specifies a single dyadic residue, hence at most one site of the octave. The binomial entropy bound and a dyadic sum prove the estimate. [Global prefix trace, equation (5)](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)

For each total \(k\in[n,an]\), let \(N_k\) be the accepted word count. Its least sources are distinct by determinism. Ordering them and applying the preceding count shows \(m_j\gg j^{1/d}\). Thus, for \(0\le p\le p_*<d\),
\[
 \sum_{A_n=k,\ W_n}m^{-p}\ll_p N_k^{1-p/d},\qquad
 N_k\le\binom{k-1}{n-1}\le2^{kH_2(n/k)} .
\]
Their joint moment is at most \(2^{(p-1)k}\sum m^{-p}\). Writing \(\theta=k/n\), the exponent in bits per odd date is therefore bounded by
\[
 F_p(\theta)=(p-1)\theta+(1-p/d)\theta H_2(1/\theta).
\]
On \(1<\theta\le a\) this is concave, with derivative \(p-1+(1-p/d)\log_2(\theta/(\theta-1))\). Its derivative at \(a\) is nonnegative exactly when \(p\le p_*\). Consequently the maximum is \(F_p(a)=a(d-1)=\log_2\gamma\). Summing the \(O(n)\) possible totals proves the upper estimate. For \(p\ge0\), the uniform pointwise floor \(Z_n(z)\ge[2\max(1,z)]^{-1}\) and \(\Pr(W_n)\gg\gamma^n(n+1)^{-3/2}\) give its lower counterpart.

For \(p<0\) that same payoff floor proves the upper bound by \(O_{p,z}(\Pr(W_n))\), with \(\Pr(W_n)\le\gamma^n\). For a lower bound take exactly \(k=\lfloor an\rfloor\). The cyclic rotation argument gives at least \(\binom{k-1}{n-1}/n\gg 2^{adn}(n+1)^{-3/2}\) accepted words. This also proves the gate-probability lower bound just used, by multiplying by \(2^{-k}\); Stirling errors and rounding have bounded factors. Discard all words with \(m<2^k(n+1)^{-3/d}\). The principal source count bounds the number removed by \(O(2^{adn}(n+1)^{-3})\). The others have \(Z_n(z)\le Z_n(0)\le(n+1)^{3/d}\) and still form a positive proportion of the guaranteed count. Their original word mass and this polynomial lower bound for the negative power give (1).

The independent all-height reviewer found the same threshold separately. The sharp physical-floor pressure result instead concerns the ungated source norm used in a separated product. The estimates here do not substitute a product of marginals for the gated source expectation. No irrationality, Subspace Theorem or density-one trajectory estimate is needed.

Prepared by the binary-energy reviewer, 27 November 2026 UTC.

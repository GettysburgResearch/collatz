# The first-power boundary layer and the cycle-slope measure

Let \(a=7/4\) and retain the original accepted prefix words \(W_n\), principal starting integer \(m\), terminal clock \(A\), algebraic offset \(G_n\), and payoff \(Z_n(z)=2^A/(m+zG_n)\). Write
\[
 M_n(p,z)=\mathbb E[\mathbf1_{W_n}Z_n(z)^p],\qquad J_n(z)=M_n(1,z).
\]
The preceding fractional pressure results give exponential smallness at every fixed power below one. The transition for powers moving toward one takes place at distance \(1/n\).

Suppose \(p_n\le1\) and \(p_n\to1\). If \(n(1-p_n)\to\infty\), then \(M_n(p_n,z_n)\to0\) for **every** sequence \(z_n\ge0\), even if there are actual persistent ordinary atoms. Indeed take \(d=H_2(4/7)<p_0<1\). For all large \(n\) the sum of the original word contributions is at most
\[
 2^{-n(1-p_n)}\sum_{m\in D}m^{-p_0},
\]
where \(D\) is the sparse union of all eligible principal sources. The sum is finite by the PR 201 bound \(\#(D\cap[1,X])\ll X^d\). For each fixed \(z\ge0\) there is instead the pointwise comparison
\[
 2^{-an(1-p_n)}J_n(z)\le M_n(p_n,z)
     \le [2\max(1,z)]^{1-p_n}J_n(z).
\]
It follows from \([2\max(1,z)]^{-1}\le Z_n(z)\le2^{an}\) on the gate. As \(J_n(z)\) has a limit, if \(\liminf n(1-p_n)<\infty\) then \(M_n(p_n,z)\to0\) precisely when \(J_n(z)\to0\). If \(n(1-p_n)\to0\) their difference goes to zero. The bounded positive-width scaled layer can retain information about the cycle clocks.

Fix any \(\tau\ge0\) and put \(p_n=1-\tau/n\) for \(n>\tau\). For a permanently accepted ordinary source \(m\) eventually visiting a nontrivial odd cycle \(C(m)\), let \(\alpha_C=A_C/P_C\) be its mean division clock per odd step. Then
\[
 \lim_{n\to\infty}\bigl(M_n(p_n,0)-M_n(p_n,1/n)\bigr)
    =\sum_{m\in\mathcal P_{\rm cyc}}\frac1m\,2^{-\tau\alpha_{C(m)}}.   \tag{1}
\]
In particular the limiting critical layer determines the entire finite positive measure \(\sum_{m\in\mathcal P_{\rm cyc}}m^{-1}\delta_{\alpha_{C(m)}}\). Its positive atoms occur at exactly the division-clock slopes of nontrivial positive ordinary cycles, combining coincident slopes if necessary.

To prove (1), on each accepted word its difference contribution is
\[
 2^{-\tau A/n}\bigl[m^{-p_n}-(m+G_n/n)^{-p_n}\bigr].
\]
Regard this as zero on absent members of \(D\). The summable majorant \(m^{-p_0}\) applies eventually. A fixed source failing the prefix gate eventually contributes nothing. A permanently safe source is eventually its own least representative. On an escaping source, \(G_n\) stays bounded by the product identity and the simple-trajectory reciprocal sum, so the bracket goes to zero irrespective of whether \(A/n\) converges. For a source entering a cycle, the normalized correction \(m+G_n=m\prod_{j<n}(1+1/(3U^j m))\) grows geometrically across laps and \(A/n\to\alpha_C\). Its contribution thus has precisely the stated limit. Dominated convergence finishes the argument. The trivial cycle has eventual exponent two, so no source entering it is permanently safe when \(a=7/4\). For every other cycle take its smallest odd phase \(v\ge3\). All \(U^i v\ge v\), so \(2^{A_j}\le(3+1/v)^j\le(10/3)^j<2^{7j/4}\); hence that cycle actually supplies a positive atom. The slopes lie in the compact interval \([\log_2 3,7/4]\). The transform for nonnegative integer \(\tau\) gives all moments after the injective change of variable \(x=2^{-\alpha}\); polynomial approximation on its compact range proves uniqueness of the finite measure.

The case \(\tau=0\), the simple-ray correction and the sparse principal envelope are from PR 201. Its positive-tilt argument already separates cycles from escape without a speed assumption. Formula (1) resolves the cycle slope distribution across the genuine moving-power layer, without establishing whether the measure is zero. [PR 201, Global prefix trace, equations (5) and (6a)](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)

Prepared by the binary-energy reviewer, 27 November 2026 UTC.

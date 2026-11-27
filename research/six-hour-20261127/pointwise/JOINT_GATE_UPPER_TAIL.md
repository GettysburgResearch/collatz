# The remaining subunit powers of the genuine gate

With the notation of JOINT_GATE_FRACTIONAL_PRESSURE.md (SHA-256 bd3390746f772cc3529cee5c388871d0921a049088013686795c892522a3c868), every fixed real \(p<1\) gives exponential decay of \(\mathbb E[\mathbf1_{W_n} Z_n(z)^p]\) for fixed \(z\ge0\). For \(0<p<1\), ordinary Hölder already gives the coarse estimate \(\Pr(W_n)^{1-p}(\mathbb E[\mathbf1_{W_n}Z_n(z)])^p\le\gamma^{(1-p)n}(n+1)^p\). The negative powers and zero satisfy the exact gate exponent in the cited note.

There is a stronger upper bound near one. For \(d<p<1\), the principal-source count \(\#(D\cap[1,M])\ll M^d\) implies \(\sum_{m\in D}m^{-p}<\infty\). The exact contribution from an accepted word is at most \(2^{-(1-p)A_n}m^{-p}\); its clock is at least \(n\), and its principal source is distinct among same-depth words. Hence the whole joint expectation is at most
\[
 2^{-(1-p)n}\sum_{m\in D}m^{-p}.
\]
At \(p=d\), all the participating sources are below \(2^{an+1}\), so truncating the same sum at that upper bound costs \(O(n+1)\) by dyadic summation. For \(p_*<p<d\) the first note's concave total-clock exponent \(\max_{1\le\theta\le a}F_p(\theta)\) also remains an upper bound, even when its maximizing clock is interior. None of these subunit estimates gives uniform integrability at the first moment. For example, the first bound loses its exponential saving as \(p\uparrow1\).

The all-height reviewer has separately refined the exact-rate interval by using the total number of even calendar letters within the source-count cutoff. The upper bounds here are independent of that strengthened count. The near-one Dirichlet-sum observation is due to the root reviewer.

Prepared by the binary-energy reviewer, 27 November 2026 UTC.

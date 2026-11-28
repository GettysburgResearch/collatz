# A three-eighths sufficient criterion for the full two-grade range

Let \(C=1/(6(\ln2)^2)\), \(\gamma=\log_2 3\), and let \(h_2^{-1}\) denote the inverse of binary entropy on \([0,1/2]\). Every infinite sequence of distinct genuine positive integer cycles with greatest and least odd states \(X<4m\) would satisfy
\[
        \liminf_{K=2m} K(\eta_K-\gamma)
        \ \ge C+\frac{h_2^{-1}(\gamma/3)}{6\ln2}
        =0.3756618\ldots >\frac38.                                   \tag{1}
\]
In particular a proof of \(\limsup_{K\to\infty}K(\eta_K-\gamma)\le3/8\) would leave only finitely many ordinary cycles in the *whole* strict two-grade range \(X<4m\), including arbitrarily close approaches to four. This sufficient upper bound on the autonomous grid remains open. It is weaker than the conjectural sharp coefficient \(C=0.3468948\ldots\). The finiteness conclusion would be ineffective through the stated irrationality input.

To prove (1), use folded integer labels \(z=cx\in[K,2K)\), \(K=2m\), \(c\in\{1,2\}\). The labels are distinct; let \(d\) be the fraction of tags equal to two, and let \(p\) be the least odd period. The [grid dictionary](../phase8/DIGITAL_ROTATION.md) gives the measured clock \(\eta_K=A/p\). The native order on the lifted folded orbit is a rank rotation, so its winding letters \(b_t\) form a rational mechanical sequence and have at most \(L+1\) distinct length-\(L\) windows. For \(L=\lceil\log_3(2K)\rceil\), the true integer edges \(2^{b_t}z_{t+1}=3z_t+c_t\) distinguish all \(p\) starts by their joint length-\(L\) windows \((b,c)\): two equal windows give \(2^{\sum b}\mid z-z'\), and \(2^{\sum b}>3^L/2\ge K\).

Sample a start uniformly around the cycle. Its window has entropy \(\log_2p\) by injectivity. Subadditivity and cyclic stationarity give
\[
                         \log_2p\le\log_2(L+1)+L h_2(d).
\]
The product formula gives \(0<A/p-\gamma=O(1/K)\). Chudnovsky's stated irrationality exponent at most three implies \(K\le p^{3+o(1)}\) along any infinite sequence, whence \(\liminf (\log_2p)/L\ge\gamma/3\). Thus \(\liminf d\ge h_2^{-1}(\gamma/3)=0.11963849\ldots\). [Chudnovsky, arXiv:2610.28079, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)

The angles \(\theta=\log_2(z/K)\) are asymptotically Haar since the full orbit advances by \(\gamma+O(1/K)\) and the rotation is irrational. Uniform Taylor expansion of the exact product yields
\[
 K(\eta_K-\gamma)=\frac{1}{3\ln2}\,\mathbb E[c2^{-\theta}]+o(1)
            \ \ge \frac{1}{3\ln2}\left(\mathbb E[2^{-\theta}]+\frac d2\right)+o(1).
\]
The Haar integral of \(2^{-\theta}\) is \(1/(2\ln2)\). This proves (1). For a rational check of the strict threshold it suffices to use \(h_2(59/500)<\gamma/3\) and \(C+(59/500)/(6\ln2)>3/8\). The argument needs the named irrationality theorem and the actual-cycle entropy lower bound. An arbitrary short segment and the profinite extremal models do not meet these hypotheses.

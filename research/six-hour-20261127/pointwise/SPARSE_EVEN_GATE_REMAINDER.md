# Sparse even departures improve the upper bound above the certified endpoint

Keep the all-height joint-gate notation \(1<a<2\), \(d=H_2(1/a)\), \(p_c=1-a(1-d)\). Put \(\lambda=\log_2 3\). For each fixed \(p_c<p<1\), the true source dynamics give the polynomial improvement
\[
 \mathbb E[\mathbf1_W Z(z)^p]
 \ \le\ 2^{-(1-p)n}\, n^{-\xi+o(1)},\qquad
 \xi=\frac{\min((p-p_c)/(a-1),1-p)}{\log_2\lambda}>0.                 \tag{1}
\]
This remains an upper bound at powers strictly below one.

Let \(D=A-n\) be the number of even shortcut departures and \(k=\lfloor\log_2m\rfloor\). A run of consecutive odd shortcut steps starting at \(x\) has length at most \(\log_2(x+1)\): in a run of length \(r\), the numerator \(x+1\) is divisible by \(2^r\). At total shortcut time \(s\), the current state satisfies \(x_s+1\le(3/2)^s(m+1)\). Dividing the itinerary into at most \(D+1\) odd runs shows that the time after the next run and an even departure is at most \(\lambda s+k+2\); it is harmless to count a final fictitious even departure. Iteration yields
\[
 n\le A\le (k+2)(\lambda^{D+1}-1)/(\lambda-1).                    \tag{2}
\]
In particular \(k+2\ge c n\lambda^{-D}\) with an absolute \(c>0\).

For \(p_c<p\le d\), use the shell bounds from the all-height manuscript frozen at SHA-256 85b05a2755d155feb09ba1924127284cae595e220053cc602e032c613bbeb80f. Put \(k_0=aD/(a-1)\), \(u=p-\log_2 a>0\), \(v=(p-p_c)/(a-1)>0\). After removing the factor \(2^{-(1-p)n}\), a shell at this fixed \(D\) costs at most
\[
 2^{-vD}\begin{cases}2^{-(d-p)(k_0-k)}&k\le k_0,\\
                       2^{-u(k-k_0)}&k>k_0.\end{cases}
\]
The left expression is the first shell's exact exponential upper bound, and the right follows from the derivative bound of the second shell. Thus total cost at fixed \(D\) is \(O((1+D)2^{-vD})\), including \(p=d\). For any fixed \(0<\epsilon<1\), if \(D<(1-\epsilon)\log_{\lambda} n\), equation (2) instead forces \(k\gg n^\epsilon\), while \(k_0=O(\log n)\). Summing the decaying right tail shows all these small \(D\) cost less than any fixed negative power of \(n\). The other \(D\)'s cost \(n^{-v(1-\epsilon)/\log_2\lambda+o(1)}\) in total. Let \(\epsilon\downarrow0\).

For \(d<p<1\), (2) directly gives \(2^{-(1-p)D}\ll_p((k+2)/n)^{(1-p)/\log_2\lambda}\). The sum of \(m^{-p}(2+\log_2m)^{(1-p)/\log_2\lambda}\) over all eligible principal sources converges by the global \(O(M^d)\) count. Applying this to the original summands \(2^{-(1-p)(n+D)}m^{-p}\) proves the other branch of (1). The exponents agree at \(p=d\). No step establishes decay at \(p=1\).

Prepared by the binary-energy reviewer on 27 November 2026 UTC.

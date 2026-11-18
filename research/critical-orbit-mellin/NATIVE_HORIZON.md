# What the native parity horizon can resolve

**PROPOSED.** Keep the shortcut map and the constants \(p,h\) of the [critical window bound](CRITICAL_MOMENT.md). Let \(G_L\) consist of length-\(L\) binary words for which \(q_t\ge pt\) at every prefix. The window proof counts uncaptured words without an orbit membership test. The order of magnitude of that particular counting error is sharp:
\[
 |G_L|\asymp 2^{hL} L^{-3/2}.
\]

The upper bound follows from (3) there with the constant barrier zero: for terminal \(d=q_L-pL\ge0\), multiply its probability bound by \(2^{hL}e^{-\lambda d}\) and sum over unit-spaced \(d\). For the lower bound take every word of weight \(q=\lceil pL\rceil\) and rotate it at a minimum of its centered partial sums, considering times \(0,\ldots,L-1\). Its total surplus is positive. Prefixes of the rotated word ending before the old endpoint are nonnegative by minimality, and wrapping prefixes add the positive total surplus to a difference from that same minimum. At most \(L\) words can supply the same rotation. There are at least \(\binom Lq/L\gg2^{hL}L^{-3/2}\) surviving words by Stirling at \(q=pL+O(1)\). The repository's previous entropy-exponent lower bound already used this rotation.

Every such word has exactly one ordinary source in *each* complete interval of \(2^L\) consecutive integers, by the parity bijection. In particular these are actual finite ordinary sources failing every multiplicative capture test \(2\cdot3^{q_t-pt}\le1/c_{u(t)}\) used to prove the upper bound. This says nothing about how many of them lie on one injective orbit.

## A post-horizon experiment with both conditionings explicit

A test of additional ordinary cancellation can restrict first-block words to \(G_L\) with \(q_L=\lceil pL\rceil\). For their source \(x\) in \([2^L,2^{L+1})\), one needs the second block from the actual endpoint \(y=T^L(x)\). The affine identity gives
\[
 y= (3^{q_L}/2^L)x+E_L,\qquad
 0\le E_L=\frac12\sum_{j=1}^L v_{j-1}3^{D_L-D_j}\le\frac32 L .
\]
This locates the second source within an additive \(O(L)\) of a known dilation of the first one. The second word is determined by that ordinary endpoint. An estimate for its splicing probabilities cannot use independent fair bits as a theorem.

As a precise open target, let \(B_L\) count the ordinary sources in this interval whose first and second blocks *both* belong to \(G_L\) with the displayed terminal weight, imposing the two prefix constraints relative to their respective starts. Does \(B_L\le C2^{(h-\epsilon)L}\) hold for some fixed \(\epsilon>0\)? The statement is weaker than controlling arbitrary terminal weights and omits source windows at unbounded translations. Even a proof would not alone exclude a positive divergent orbit.

Prior symbolic rotation argument: [fixed-height attack, Proposition 3](../external/mazur-2026/fixed-height-power-saving-attack.md).

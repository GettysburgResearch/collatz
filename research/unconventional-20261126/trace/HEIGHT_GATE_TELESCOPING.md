# Exact telescoping across consecutive physical gate heights

**Status.** Written. The one-height identity is elementary. The summability refinement uses the source-qualified distinct-path reciprocal estimate cited in [the damping sum rule](DIRICHLET_CHARGE.md). The identification of the limiting charge uses [the critical gate theorem](CRITICAL_EXIT_GATES.md). No vanishing subsequence follows.

For the physical shortcut map and its odd-departure factor \(c(v)=3v/(3v+1)\), let \(A_N=H_{N-1}\|J_N\|_1\) and \(G_N=H_{N-1}J_N(N)\), the unnormalized total mass and the part exiting exactly at \(N\). Set \(A_1=G_1=H_0=0\). Let \(r_N\) be the surviving weight from \(N\) to its first state strictly larger than \(N\), or zero if that state is never reached. This can be decided by following the path until exit or repetition below the new threshold.

On raising the threshold to \(N+1\), old exits above \(N\) retain their weights. Exactly the old mass \(G_N\) continues from \(N\), and the new source \(N\) enters with weight \(1/N\). Consequently
\[
 A_{N+1}=A_N+r_N/N-(1-r_N)G_N,\qquad
 H_{X-1}-A_X=\sum_{N<X} d_N,\quad
 d_N=(1-r_N)(1/N+G_N).
\]
The nonnegative partial sums are at most \(H_{X-1}\). Gate vanishing along a subsequence requires the reverse lower bound \(\limsup_X H_{X-1}^{-1}\sum_{N<X}d_N=1\).

**Which heights can supply logarithmic loss?** An arrival from below at exactly \(N\) must come from the odd predecessor \((2N-1)/3\), so \(G_N=0\) unless \(N\equiv2\pmod3\). At every odd height, \(r_N=3N/(3N+1)\). We claim that \(\sum_{N\ {\rm odd}}d_N<\infty\). The own-source sum is bounded by \(\sum_N 1/(N(3N+1))\). Interchange nonnegative sums for the remaining term. A source \(x<N\) contributing to \(G_N\) visits \(N\) as a strict record. For fixed \(x\) all these odd records are distinct visits at heights above \(x\). The cited distinct-path bound gives reciprocal sum \(O(x^{-1/40})\), uniformly in the source; qualifying records occur before any repetition. Gate products are at most one, so the total is \(O(\sum_x x^{-1-1/40})\).

Also, for \(N\equiv6\pmod8\) the first upcrossing is
\[
 N\longmapsto N/2\longmapsto (3N+2)/4\longmapsto(9N+10)/8>N.
\]
Its two odd departures give \(r_N=9N/(9N+10)\). For each contributing \(x<N\), the distinct odd states \(N/2>x/2\) lie on its ordinary path before a repeat, since the displayed continuation immediately makes a new record. The same bound proves \(\sum_{N\equiv6\ (8)}d_N<\infty\).

Thus on any vanishing subsequence the exact residual sum must satisfy
\[
 \sum_{\substack{N<X\\2\mid N,\;N\not\equiv6\ (8)}}\frac{1-r_N}{N}
 +\sum_{\substack{N<X\\N\bmod24\in\{2,8,20\}}}(1-r_N)G_N
 =(1-o(1))H_{X-1}.
\]
The first term is at most \((3/8)\log X+O(1)\) by harmonic summation on residue classes. The second must supply at least \((5/8-o(1))\log X\). No lower bound of this size is established.

**Why scale choice alone fails.** On a hypothetical escaping ordinary orbit let \(n_j\) be its successive strict record heights, including its start. The disjoint segments between records exhaust the future, hence \(\prod_j r_{n_j}=W(n_0)>0\) under the stated escape survival estimate. In particular \(\sum_j(1-r_{n_j})<\infty\). Since \(G_N\le H_{N-1}\), dominated convergence gives \(H_X^{-1}\sum_{n_j\le X}(1-r_{n_j})G_{n_j}\to0\), even for any finite union of such record sets. Finite-core approximation leaves this complete future in place.

For a concrete control take the [binary graph](ENTRANCE_AND_INDEX.md), using the same odd killing factors and unit even weights on its different edges. Every source escapes, with at most two visited vertices per dyadic level. Every finite path product is therefore at least \(\exp[-\tfrac13\sum_{k\ge0}2\cdot2^{-k}]=e^{-4/3}\), using \(\log(1+u)\le u\). Its normalized harmonic gate total is at least this constant at every height despite its tight finite-core landing laws. This control tests positivity, scale nesting and finite-core tightness. The residual congruence formula above uses the actual Collatz branches.

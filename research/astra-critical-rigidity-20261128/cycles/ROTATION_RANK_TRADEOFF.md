# Every ordinary rotation pays in multiplicative rank or mismatches

Let \(p\) be the least odd period of a positive integer cycle with odd states \(x_i\), and \(s_\ell\) the number of unequal odd valuations at a proper lag \(\ell\). If \(r_*\) is the multiplicative rank of all the odd states, then
\[
                     \min_{0<\ell<p}\frac{s_\ell(r_*+1)^2}{p}
                                  \longrightarrow\infty.                 \tag{1}
\]
This relation uses no unmeasured maximum or mean height. Near-periodicity of the valuations requires high multiplicative rank of the actual integer orbit.

More generally, select any proper lag along growing periods. Choose a multiplicative subgroup \(G\subset\mathbb Q_{>0}^{\times}\) after observing the cycle and choose integer divisors \(u_i\mid x_i\) from \(G\). Suppose its rank \(r\) satisfies \(r^2s_\ell=O(p)\), allowing \(r\) to grow. Then
\[
                  \frac{\sum_{i=0}^{p-1}\log u_i}
                       {\sum_{i=0}^{p-1}\log x_i}\longrightarrow0.       \tag{2}
\]
For each fixed \(0<\eta\le1\), put \(D_\eta=\{i:\log u_i\ge\eta\log x_i\}\). The locations also satisfy
\[
          \frac{\#\{i:i,i+\ell\in D_\eta\}}p\longrightarrow0.            \tag{3}
\]
If the order \(p/\gcd(p,\ell)\to\infty\), then \(|D_\eta|/p\to0\). Thus on this last class, almost all dates retain at least a \(1-\eta\) share of their logarithmic height outside the chosen divisors. A selected pool of \(r\) primes is a special case. Statement (2) addresses logarithmic mass on the full orbit; (3) gives a count of dates and need not follow from a mass estimate alone.

**Proof.** Write \(s=s_\ell,\ H_i=\log x_i,\ A_p=\sum H_i\), with natural logarithms, and let \(V\le p\log6\) be the actual circular odd-edge return cost. The [all-origin rotation theorem](UNIFORM_ROTATION_HEIGHT.md) gives \(s A_p/p^2\to\infty\), since the difference between the true logarithm of \(x\) and that of \(x+1\) is uniformly bounded. By the [finite rank and height estimate](MISMATCH_EVENT_FACTORS.md), \(A_p\le r_*(r_*+2)V\), which proves (1). For the whole-state conclusion alone one can equally use Weaver's earlier height estimate \(\log(\max_i x_i)=O((r_*+1)^2)\) and the new all-origin mean theorem. [Weaver, Paper 137, Theorem 2](https://rstation.ai/problems/collatz/papers/137)

The single-list version of the [divisor layer inequality](MISMATCH_EVENT_FACTORS.md) has \(K=r(r+2)V\). Rank zero is immediate; at positive rank \(K/A_p=O(p^2/(s A_p))\to0\), proving (2).

For each fixed \(T>0\), the same finite estimate gives
\[
   \frac1p\#\{i\in D_\eta:H_i\ge T p/s\}
          \le \frac{r(r+2)V s}{\eta T p^2}
          \ll\frac{1}{\eta T}.
\]
The implicit constant is uniform along any sequence with a fixed upper bound for \(r^2s/p\). By the paired-height conclusion outside \(o(p)\) dates at least one of \(H_i,H_{i+\ell}\) exceeds \(Tp/s\). If both dates lie in \(D_\eta\), such an origin can be charged to a high member of \(D_\eta\), with multiplicity at most two. Take a limit superior and then \(T\to\infty\), proving (3). At orders tending to infinity the single-state consequence of the all-origin theorem leaves only \(o(p)\) low dates; the same argument gives the final density conclusion. All changes between logarithm bases or between \(x_i\) and \(x_i+1\) in these bit thresholds are absorbed by a fixed enlargement of \(T\).

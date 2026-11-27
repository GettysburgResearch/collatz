# Sharp uniform source cutoff for every exact first-arrival row

Let \(y\) be any specified positive odd target. A positive source \(x\) first visits \(y\) after \(s\) shortcut steps and \(j\) odd departures, with initial halvings counted. Include the empty first visit. Put \(p=y2^s/3^j\). On the written input below there is an absolute \(C\) such that for every \(y,j,s\) with a nonempty row,
\[
        \frac1p\#\{x:\operatorname{first}(x,y)=(j,s)\}
              \ \le\ \frac{C}{\sqrt{1+\log p}} .                       \tag{1}
\]
Consequently the exact uniform source-tail quantity introduced by [PR 212, FAIR_CLOCK_DIFFUSION](https://github.com/GettysburgResearch/collatz/blob/e082b95a503d622bbbd121801f6bcadcab50df05/research/astra-infinite-descent-20261127/escape/FAIR_CLOCK_DIFFUSION.md) satisfies
\[
 \sup_{y,j,s}\frac1p\#\{x>R:\operatorname{first}(x,y)=(j,s)\}
                  \asymp (1+\log R)^{-1/2}\qquad(R\ge2).                \tag{2}
\]
This is uniform in a moving target, arbitrary cycles and clock/grade, and uses the literal original integer. The lower already occurs at a fixed terminating target. The normalization is \(p^{-1}=3^j2^{-s}/y\). All logs without a base are natural.

The main analytic input is the signed starting-residue cancellation at a short physical clock, [PR 195, MARKED_FIBRES, (3)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md). Its underlying precise one-extra-digit exact-total mixing input is [Weaver and Wren, Paper 48 v1, §8, Theorem 6 (66)](https://rstation.ai/problems/collatz/papers/48/v1). The geometric smoothing and tail split below are from [PR 195, LOCAL_HEIGHT_LAW, (4)–(6)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/LOCAL_HEIGHT_LAW.md), which already gives this order for full corrected-height classes in escaping components. [PR 193, CRITICAL_POISSON_PROFILE](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/CRITICAL_POISSON_PROFILE.md) gives the stronger marked local limit at the fixed first hit of 1, and its [support-neighborhood companion](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/CRITICAL_SUPPORT_NEIGHBORHOODS.md) already gives the lower neighborhood order at 1 and in any escaping component. The new uniform step here is the target-independent control of *early* first visits at moving \(y\), before transporting the original joint clock. This leads to (1) without classifying the target's component or identifying any limiting corrected-height measure. The proof is a written deduction, with no formalization of these analytic inputs.

### Uniform cancellation at a moving first visit

First restrict \(x\) to odd positives, use \(U\) for the odd map and \(A_t(x)\) for the sum of the first \(t\) physical valuations. Put \(f_t(x)=\prod_{i<t}3U^i x/(3U^ix+1)\in(0,1]\). On a first-arrival row,
\[
       p^{-1}=f_j(x)/x,\qquad c_0p\le x\le p,
\]
with an absolute \(c_0>0\) from the uniform reciprocal packing of simple segments in [Weaver 176 v1, §5.1, after (26)](https://rstation.ai/problems/collatz/papers/176/v1). A repeated state before a first visit would prevent the subsequent first visit, so the relevant segments are simple. Initial powers of two contribute no product loss.

For every mean-zero function \(\psi\) on \(\mathbb Z/3\) of supremum norm at most one, every \(A>0\), and each one specified \(y\), with constants independent of \(y\),
\[
 \sum_{j,s}\left|p^{-1}
       \sum_{\substack{x\ {\rm odd},\ x\ge R\\\operatorname{first}(x,y)=(j,s)}}
              \psi(x\bmod3)\right|
       \ \ll_A\ (1+\log R)^{-A}.                                      \tag{3}
\]
There is no sum over targets outside the absolute values in this assertion.

To prove (3), take an octave or a subinterval \(I\subset[X,2X]\), at a large \(X\), and \(t=\lfloor(\log_2X)/32\rfloor\). The input (3) of PR 195 gives
\[
 \sum_{h,z}
 \left|\sum_{\substack{x\in I\ {\rm odd}\\ U^t x=z,\ A_t(x)=h}}
       \frac{\psi(x)f_t(x)}x\right|\ll_B t^{-B}                        \tag{4}
\]
for any fixed \(B\). For a pair \((h,z)\), if \(z\) first hits \(y\) at its own odd clock \(u\) and native clock \(v\), send the coefficient to \((t+u,h+v)\), multiplying by \(f_u(z)\le1\). Otherwise discard it. This deterministic operator contracts the sum norm; whenever \(x\) had no hit of \(y\) before \(t\), the result is exactly its true first-hit coefficient. A hit at time \(t\) is handled by \(u=v=0\).

The set \(A_t(x)>4t\) has initial reciprocal mass \(O(e^{-c t}+2^{4t}/X)\) in \(I\), by the parity-cylinder estimate in [PR 195, PHYSICAL_SOURCE](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/PHYSICAL_SOURCE.md). The event forces at most \(t\) odd departures in the first \(4t\) shortcuts. On the remainder, any earlier hit of \(y\) takes at most \(4t\) shortcut steps. Each possible binary word of length at most \(4t\), together with this specified \(y\), determines at most one ordinary starting integer by its affine rule. So there are at most \(2^{4t+1}\) exceptional starts independently of the value, periodicity or height of \(y\). Removing their possible incorrect contributions and restoring the true ones costs at most twice their initial reciprocal mass, since both kinds of coefficients have absolute value at most \(1/x\). This is also valid when \(y\) is visited more than once after a first visit. Equations (4) and the errors give \(O_B((\log X)^{-B})\). Sum over the original dyadic intervals above \(R\), with \(B>A+1\). Bounded initial intervals cost an absolute constant because each source has at most one first arrival at a given target. This proves (3), also for any truncated input range \([R,R')\) with constants independent of \(R'\).

### The exact geometric recurrence

Write \(m_{j,s}=p^{-1}\#\{x\text{ odd}:\operatorname{first}(x,y)=(j,s)\}\), zero for empty or negative-index cells. Split \(m_{j,s}\) into its three initial residue weights \(m_{j,s,a}\); let \(b^a_{j,s}=m_{j,s,a}-m_{j,s}/3\). By (3), \(\sum_{j,s,a}|b^a_{j,s}|\le C\) uniformly in \(y\). More precisely the sum restricted to \(p\ge L\) is \(O_A((1+\log L)^{-A})\) for each fixed \(A\): in a cell of this height every physical member has \(x\ge c_0L\), so (3) with that source cutoff applies before taking the sum.

Put \(G(e)=2^{-e}{\bf1}_{e\ge1}\). The unique inverse step from a previous source \(u\) with exponent \(e\) exists precisely when \(u\equiv a_e=2^{-e}\bmod3\); its positive odd parent is \((2^e u-1)/3\). It changes row weight by \(3\,2^{-e}\). If \(y\) is periodic in the odd map, write its primitive cycle length as \(\ell\), native lap total as \(b\), and \(\omega=3^\ell2^{-b}<1\). The sole rejected extension produces \(x=y\) after one primitive reverse lap: the proper remaining path from \(Uy\) to \(y\) has a unique first arrival. Any other new source has no earlier visit to \(y\) because its own proper suffix was already a first-hit word. Thus for \(j\ge0\)
\[
 m_{j+1,s}=(G*m_j)(s)+3\sum_{e\ge1}2^{-e} b^{a_e}_{j,s-e}
                 -{\bf1}_{y\ {\rm periodic}}\,\frac{\omega}{y}
                      {\bf1}_{(j+1,s)=(\ell,b)} .                     \tag{5}
\]
The empty first-hit row is \(m_{0,0}=1/y\). This covers a fixed point such as 1 and all nonunit targets as well.

Regard the residue term, the possible negative lap impulse and the initial root as a single signed array \(c_{i,t}\), with the entries at the new or root coordinates in (5). Then
\[
         \sum_{i,t}|c_{i,t}|\le C,\qquad
         \sum_{\substack{i,t\\p_0=y2^t/3^i\ge L}}|c_{i,t}|
                \ll_A(1+\log L)^{-A}                                  \tag{6}
\]
uniformly in \(y\). Indeed the old height of a residue term moving to \(p_0\) is \(3p_0\,2^{-e}\). For \(p_0\ge L\), a previous height \(\ge\sqrt L\) is covered by the signed tail just proved; otherwise \(2^e>3\sqrt L\), and the geometric \(2^{-e}\) tail multiplies the uniform full sum norm of \(b^a\). The root impulse has mass \(1/p_0\) at \(p_0=y\); the lone lap impulse has exactly that same absolute mass at \(p_0=y/\omega\). Each is \(O(1/L)\) above \(L\). The signed source has height at least \(2/3\) wherever nonzero, including newly empty cells reached by imbalance terms.

For \(g_k=G^{*k}\), let \(g_0=\delta_0,\ g_k(l)=\binom{l-1}{k-1}2^{-l}\) for \(k\ge1,l\ge k\), and zero otherwise. Iteration of (5) gives
\[
          m_{j,s}=\sum_{i=0}^j\sum_t c_{i,t}\,g_{j-i}(s-t).             \tag{7}
\]
For \(p/p_0=2^{s-t}/3^{j-i}\ge Y\ge2\), the kernel is \(O((1+\log Y)^{-1/2})\). Indeed if \(k=j-i\ge(\log_2Y)/10\), use the central point bound \(\|g_k\|_\infty\ll (1+k)^{-1/2}\). For smaller \(k\), when \(l=s-t\) is nonnegative, \(l\ge\log_2Y+\lambda k\); the geometric Markov bound \(g_k(l)\le3^k(2/3)^l\) is exponentially small in \(\log Y\). The empty kernel cannot contribute at a height ratio \(>1\). Use this bound for \(p_0<\sqrt p\) and (6) for \(p_0\ge\sqrt p\), bounding \(g_k\le1\) there. This proves (1) for odd sources.

For all positive starts decompose \(x=2^a u,\ u\) odd. The first hit to an odd \(y\) occurs only after those \(a\) native halvings, and the remaining physical row is \((j,s-a)\) at odd-source height \(p'=p/2^a\), with mass multiplied by \(2^{-a}\). For \(2^a\le\sqrt p\) use (1) at \(p'\); for \(2^a>\sqrt p\) use the uniform bound \(m_{j,s-a}\le1\) because every source in a nonempty row is a distinct integer \(\le p'\). Summing the geometric weights proves (1) on the full domain. Its use at a row containing \(x>R\) gives the upper in (2), since \(p\ge x\). The exact-central-row lower at \(a=5\) is proved in [the maximizing class controls](MAXIMIZING_CLASS_CONTROLS.md). It can instead be read off the stronger real-marked local limit at root 1 from PR 193, after retaining a positive subinterval of its simple correction support.

### A specified root and its largest row

For any fixed nonperiodic odd \(y\), the number of potential starting integers in a maximizing first-arrival row is finite and now its physical height itself has a bound \(p\le\exp(C' y^2)\), since the empty row has mass \(1/y\) and any row of greater or equal mass obeys (1). Thus all candidate sources for a maximizer lie below the same height. In an escaping component a fixed base origin of corrected height \(P_0\) likewise gives a maximizing full synchronized class supported below \(\exp(C'P_0^2)\), either by the prior full-class bound or by applying (1) to its common future and taking the corresponding simple correction to one along the escaping ray. The input constants here are those of a written asymptotic estimate, not a machine-verified numerical search bound. Neither conclusion excludes the finite origin that supplies the maximum.

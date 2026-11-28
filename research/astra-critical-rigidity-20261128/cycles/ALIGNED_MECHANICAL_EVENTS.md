# Substitution count times cumulative discrepancy on an ordinary cycle

Let \(a=(a_i)_{i\bmod p}\) be the positive odd-to-odd valuation word of a primitive positive integer cycle, \(A=\sum_i a_i\), and \(p>1\). At the cycle's own slope \(A/p\) and an arbitrary real phase \(\tau\), form the aligned reference
\[
 b_i=\lfloor(i+1)A/p+\tau\rfloor-\lfloor iA/p+\tau\rfloor .
\]
Let \(r=\#\{i:a_i\ne b_i\}\), and \(D\) be the range of \(\sum_{i<j}(b_i-a_i)\) over \(0\le j\le p\), including the empty prefix. Then on growing ordinary periods
\[
         \inf_\tau \frac{(r+1)(D+\log_2 p)}p\longrightarrow\infty,
 \qquad \frac{\inf_\tau r}{\sqrt p}\longrightarrow\infty .              \tag{1}
\]
If \(D\) is bounded along the selected references, (1) gives \(r\log p/p\to\infty\). No circular reordering or change of comparison slope is allowed in \(r\) or \(D\).

Paper 237, claim C431, proves a finite complete-denominator bound for mechanical factors and deduces \(p=O((r+1)(D+\log p))\) for ordinary cycles. Its proof also bounds the largest real phase in terms of \(D\). The diverging multiple in (1) uses the unrestricted ordinary mismatch-event theorem. Paper 237's other result allowing separate phases on freely rewritten arcs has a different hypothesis and retains its explicit constants. [Paper 237, C431, 27 November 2026](https://rstation.ai/problems/collatz/papers/237) · [Mismatch-event theorem, (1)](MISMATCH_EVENT_HEIGHT.md)

To see the height bound directly, put \(\Delta=2^A-3^p>0\), \(m=\min x_i\) and \(X=\max x_i\). Every backwards cyclic \(j\)-prefix of \(a\) has total \(T_{i,j}\ge jA/p-D-1\). Indeed the prefix difference for the aligned reference has circular range \(D\), while a mechanical interval differs from its mean by less than one. The exact periodic affine formula gives
\[
 x_i=\frac{1}{3(1-3^p/2^A)}\sum_{j=1}^p3^j2^{-T_{i,j}}
 \le \frac{2^{D+1}p}{3(1-3^p/2^A)} .
\]
For ordinary cycles \(1\le A/p\le2\) by the positive lap product. The classical lower bound on \(A\log 2-p\log 3\) therefore gives \(-\log_2(1-3^p/2^A)=O(\log p)\), uniformly in the word and phase. Thus \(\log_2(1+X)\le D+O(\log p)\). [Bondareva, Luchin and Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

Every such \(b\) has a proper shift at Hamming distance at most two. If \(g=\gcd(A,p)>1\), choose \(p/g\), a period of \(b\). If \(g=1\), take \(hA\equiv1\bmod p\). The \(p\) distinct phases \(\{iA/p+\tau\}\) are cyclically permuted by one rank; \(b_i-\lfloor A/p\rfloor\) indicates a single half-open circular interval, so there are at most two unequal entries. The triangle inequality now gives \(s_a(h)\le2r+2\). Uniform divergence of \(s_a(h)\log_2(1+X)/p\) gives the first assertion, valid also for a phase selected after inspecting the cycle. Since \(b_i\le2\) and \(a_i\ge1\), every positive increment \(b_i-a_i\) equals one and occurs at one of the \(r\) changed positions. The total prefix range \(D\) is at most the sum of the positive increments, so \(D\le r\). If \(r=O(\sqrt p)\) then \((r+1)(D+\log_2p)=O(p)\), proving the second assertion.

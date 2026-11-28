# Typical first landing in every exponentially long numerator interval

Fix \(0<\theta\le1\). At denominator \(3^n\) choose **any** contiguous interval \(I\subset[1,3^n]\) of \(M\ge3^{\theta n}\) integers, and choose \(m\) uniformly from its elements prime to three. Let \(T\) be the first integer landing time from the positive rational \(m/3^n\) under the shortcut map. All estimates below are uniform in the position and length of \(I\).

**Proposed local law.** For each fixed \(A>0\),
\[
  \Pr_I\{|T-2n|>C_{A,\theta}\sqrt{n\log(2+n)}\}\ll_{A,\theta} n^{-A}. \tag{1}
\]
For each fixed \(\epsilon>0\), the lower tail \(T<(2-\epsilon)n\) has probability \(O_{\epsilon,\theta}(e^{-c_{\epsilon,\theta} n})\). The upper tail \(T>(2+\epsilon)n\) has probability \(e^{-\omega_{\epsilon,\theta}(\sqrt n)}\). In particular the same typical time holds on the short real interval \([3^{-n},3^{-(1-\theta)n}]\), after rounding its upper endpoint, as it does near an arbitrary positive real point of the full grid. Integer intervals around specified sequences of centers may change arbitrarily with \(n\).

The [complete-grid law](TYPICAL_INTEGER_LANDING.md) obtains these estimates from elementary congruence counting on the entire ternary grid. Here a three-place Diophantine estimate handles the stages at which the remaining ternary modulus is larger than the whole source interval. Its onset can be ineffective. A single fixed numerator, a subexponential interval specified in advance, or the longest possible time \(J(n)\) is outside (1).

## Uniform counting for arbitrary translates of a dyadic residue

At native date \(t\), before landing, the reduced state \(d/3^h\) with \(h\ge1\) satisfies \(2^td\equiv m\bmod Q\), \(Q=3^h\). Given the integer part \(j=\lfloor d/Q\rfloor\), the candidate \(d\) lies in \([jQ,(j+1)Q)\). A fixed future binary word of length \(l\) specifies one residue \(d\equiv r\bmod 2^l\). The word remains defined on its rational input even if its final segment falls after landing.

**Counting lemma.** Fix \(C_0\). For all sufficiently large \(n\) depending on \(\theta,C_0\), if \(t\le C_0n\), \(1\le l\le h\le n\), and \(2^l\le\sqrt M\), then at most \(8M/2^l\) integers \(m\in I\) satisfy the two candidate congruences at the stated floor. This includes all actual sources realizing that triple and word. For \(Q\le M\), each residue modulo \(Q\) is represented at most \(1+M/Q\) times and there are at most \(1+Q/2^l\) candidates \(d\), whose product is at most \(4M/2^l\).

Suppose \(Q>M\) and write \(d=r+2^l e\). The candidate pairs \((e,m)\) lie in a translate of the lattice
\[
      \Lambda=\{(x,y)\in\mathbb Z^2:2^{t+l}x-y\equiv0\pmod Q\}
\]
of covolume \(Q\), inside a rectangle of side lengths \(D=Q/2^l,M\). Its dual consists of \((a/Q,b/Q)\) with \(a+2^{t+l}b\equiv0\bmod Q\). We claim its only point with \(|a|\le2^{l-1},\ |b|\le Q/(2M)\) is zero. Both bounds are strictly below \(Q\), which handles a zero coordinate using coprimality of two and \(Q\). Otherwise put \(a+2^{t+l}b=Qk\). When \(k=0\), \(|a|\ge2^{t+l}\) contradicts its bound, including at date zero. For \(k\ne0\), the [primitive three-place product estimate, (5)](COPRIME_ENDPOINT_PRODUCTS.md) gives
\[
          Q\ll_\delta |ab|\,|abk|^\delta.
\]
Here \(|ab|\le Q/(4\sqrt M)\) and \(|abk|\le2^{C_1 n}\) for a fixed \(C_1\) depending only on \(C_0\), because \(h,l\le n,\ t\le C_0 n\) and \(|k|\le 1+2^{t+l}\). Take \(\delta C_1<\theta\log_2(3)/4\), then \(n\) large enough, to obtain a contradiction. No incomplete residue period has been replaced by a uniform sample.

To count arbitrary translates, let \(f(x)=(\sin(\pi x/2)/(\pi x/2))^2\), \(f(0)=1\). Its Fourier transform with kernel \(e^{-2\pi i x\xi}\) is a triangle supported on \([-1/2,1/2]\), with integral of \(f\) equal to two. On \(|x|,|y|\le1/2\) we have \(2f(x)f(y)\ge1\). Center this product on the given rectangle and scale its arguments by \(D^{-1},M^{-1}\). Its Fourier support meets the dual only at zero by the preceding bound. Lattice periodization therefore gives the sum of this majorant over **every** affine translate as \(2\cdot2^2 DM/Q=8M/2^l\). For a direct justification, periodize the decaying product over \(\Lambda\); the sum converges locally uniformly by its product quadratic decay and \(\Lambda\subset\mathbb Z^2\). The Fourier coefficient at a dual vector is its Euclidean Fourier transform divided by \(Q\). Only the constant coefficient survives. This proves the lemma, including rectangles at arbitrary floors for which there may be no real trajectory.

Each interval has at least \(M/2\) ternary units for large \(n\). Hence for any collection of length-\(l\) words of fair-bit probability \(p\), the probability that the actual triple \((t,h,j)\) occurs **and** its following word belongs to the collection is at most \(16p\), under the lemma's hypotheses. This is an unconditional bound at a triple fixed in advance. The law conditioned on that triple need not be fair.

## The native blocks and the deadline

Take \(L_0=\lfloor\theta n/4\rfloor\). Use only starts \(t\le3n\), and let \(B\ge B_0\) and \(H_0=\lceil32D_0^2B\rceil\), where \(D_0\ge2\) is an absolute fixed constant. We take \(B\le c_\theta n\) sufficiently small that \(H_0\le L_0\). In particular \(2^{L_0}\le\sqrt M\).

By the [high-excursion estimate](TYPICAL_INTEGER_LANDING.md), a segment departing at \(x\le2\) with its next \(B\) values all above two has odd count at least \(\rho B\) for some fixed \(\rho>1/2\), for all large \(B\). The reason is that from \(x>2\) the odd multiplier is at most \((7/2)/2\), while the even multiplier is one half. Apply the counting lemma with \(l=B\) to each fixed \(t\le3n, h\ge B, j=0,1,2\). The binomial Chernoff bound and union over all such triples cost \(O(n^2 e^{-cB})\). Outside this event, every actual visit at clock \(t\le3n\) and height \(h\ge B\) has \(x\le2^{B+2}\): trace to the last state at most two, of which the initial state is one possible choice. Its height is at least the current height.

For \(h\ge H_0\) prescribe \(l_h=\min(h,L_0)\). Apply the candidate-word bound to each fixed triple with \(t\le3n\), \(j\le2^{B+2}\), \(h\ge H_0\). Hoeffding's bound at threshold \(D_0\sqrt{l_h B}\) and the union over at most \(O(n^2 2^B)\) triples cost \(O(n^2 e^{-cB})\). Off both exceptional events every such actual block has odd count
\[
                 |g-l_h/2|\le D_0\sqrt{l_h B},\qquad l_h/4\le g\le3l_h/4 .
\]
Following the block before seeing its bits is legitimate because the common good event covers all starts. It cannot contain landing, as \(g<h\). Along any partial list of blocks the sum of \(\sqrt{l_h}\) is \(O_\theta(\sqrt n)\). There are at most \(4n/L_0+1\) capped blocks before the height falls to \(L_0\), and subsequent full-height blocks shrink the height by a factor at most \(3/4\). Thus at the end of every such partial list the elapsed time differs from twice the consumed grade by at most \(C_\theta\sqrt{nB}\). With \(c_\theta\) smaller if necessary, this ending date is always below \(3n\). Induction therefore never needs the local counting lemma at a later start.

The first height \(h_*<H_0\) still satisfies \(h_*\ge H_0/4\), so its real state is at most \(2^{B+2}\). As in the full-grid proof, within \(O(B+h_*)\) extra dates it either lands or reaches \((0,1]\): until that visit an odd factor is at most two, an even factor one half, and a crossing from above one ends above one half. Bound the remaining time by \(J_*(H_0)=\max_{h\le H_0}J(h)\). We have proved outside probability \(O(n^2e^{-cB})\) that
\[
  2n-C_\theta(\sqrt{nB}+B)\le T
      \le 2n+C_\theta(\sqrt{nB}+B)+J_*(H_0).                             \tag{2}
\]
For (1) let \(B=C_{A,\theta}\log(2+n)\), rounded up, and use the elementary \(J_*(H)=O(H^2)\). For the lower tail take a sufficiently small fixed multiple of \(n\). For the upper tail take \(B=\lceil K\sqrt n\rceil\) for each fixed \(K\), and use the [uniform worst-case theorem](../literature/EFFECTIVE_WORST_LANDING.md), which in particular gives \(J_*(H)=o(H^2)\). This proves the claimed probability bounds.

For each fixed \(\theta\), (1) compares a number of ordinary rational **source numerators** exponentially smaller than the full grid. It gives no rate uniform as \(\theta\) decreases to zero. The three-place estimate also explains the separate [one-source numerator-product constraint](COPRIME_ENDPOINT_PRODUCTS.md).

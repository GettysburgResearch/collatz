# First integer landing at \(2n+O_A(\sqrt{n\log n})\) for almost every numerator of denominator \(3^n\)

Let \(M\) be uniform on the \(2\cdot3^{n-1}\) integers \(1\le m\le3^n\) prime to three. Start the actual shortcut map at \(M/3^n\), and let \(\tau\) be the first date with an integral state. Until landing, write the positive reduced state as \(d/3^h\). The denominator exponent decreases by one at each odd departure, so landing takes exactly \(n\) odd letters. Denote the largest first landing time at height \(h\) for starting real value in \((0,1]\) by \(J(h)\), and put \(J_*(H)=\max_{1\le h\le H} J(h)\).

**Proposed source-grid law.** For each fixed \(A>0\), outside \(O_A(3^n n^{-A})\) initial numerators,
\[
                    |\tau-2n|\ \ll_A\ \sqrt{n\log(2+n)}.                 \tag{1}
\]
The same estimate eventually holds at every height \(n\) for the least positive residues modulo \(3^n\) of Haar-almost every single ternary unit. For each fixed \(\epsilon>0\), the lower large-deviation probability \(\Pr(\tau<(2-\epsilon)n)\) is \(O_\epsilon(e^{-c_\epsilon n})\). The upper probability \(\Pr(\tau>(2+\epsilon)n)\) is \(e^{-\omega_\epsilon(\sqrt n)}\), using the previously established \(J(h)=o(h^2)\). Neither (1) nor the exponential lower-tail bound uses the Subspace Theorem. Individual fixed ordinary numerators and the maximizing sequence in \(J(n)\) are outside the quantifiers of (1). [The landing map, its ordinary-pair realization and the worst-case bound](POSITIVE_DESCENDING_INTERVALS.md)

## Counting on complete residue intervals

The update for the reduced numerator is \(d'=d/2\) on an even letter, or \(d'=(d+3^{h-1})/2\) on an odd one. Before landing \(d\le3^n\), since every odd update is an average with \(3^{h-1}\). Each of the \(n\) odd departures follows at most \(n\log_2 3\) consecutive even dates. Therefore
\[
          \tau\le T_n=n(1+\lceil n\log_2 3\rceil),\qquad
                         2^t d\equiv M\pmod{3^h}                         \tag{2}
\]
at every prelanding date \(t\), with the congruence following by induction on native steps.

Fix in advance a date \(t\le T_n\), a height \(h\ge1\), a nonnegative integer \(k\), and \(L\ge1\). If the actual state at that date has height \(h\) and integer part \(k\), then its numerator is uniquely
\[
                 k3^h + r,\qquad r=2^{-t}M\bmod 3^h,\quad 0<r<3^h.
\]
Without conditioning on the actual height or integer part, \(r\) is uniform on the units modulo \(3^h\). Each length-\(L\) shortcut word is a single residue class of the numerator modulo \(2^L\), since the odd denominator is a binary unit and each prescribed affine prefix sends its two next dyadic lifts to opposite parities. Thus for any collection of words with fair-bit probability \(p\), the probability that the specified actual triple occurs **and** its following word belongs to the collection is at most
\[
            \frac32 \left(1+\frac{2^L}{3^h}\right)p.                    \tag{3}
\]
Indeed each residue class contributes at most \(\lceil3^h/2^L\rceil\) candidate numerators even before omitting multiples of three. The native word of the candidate rational remains defined past an integer landing if needed. Estimate (3) requires no conditional independence at a stopping time. Its loss is at most three whenever \(L\le h\).

## Bounding the integer part before looking at blocks

There are absolute constants \(C,c>0\) in the estimates below. Let \(B\) be a positive integer above an absolute fixed threshold. Suppose the state at \(t\) is at most two and all the next \(B\) states exceed two. The first one is at most \(7/2\). At a subsequent odd departure from \(x>2\) the multiplier is \((3+1/x)/2\le(7/2)/2\), and an even multiplier is \(1/2\). If \(g\) is the full \(B\)-letter odd count, then
\[
                      2 < (7/2) (7/2)^g\,2^{-(B-1)} .
\]
Choose \(1/2<\rho<1/\log_2(7/2)\). Hence \(g\ge\rho B\) at large \(B\). For independent fair bits this word event has probability at most \(e^{-cB}\) by the binomial Chernoff bound. Apply (3) with \(L=B,\ h\ge B,\ k=0,1,2\) and sum over all dates and heights. Outside probability \(Cn^3e^{-cB}\), every actual visit with height at least \(B\) has real magnitude
\[
                                 x\le 2^{B+2}.                         \tag{4}
\]
For a visit above two, trace backwards to its last departure at most two, which exists because the initial state is at most one. That departure has height at least the current height. The high excursion has length less than \(B\), and \(x'+1\le(3/2)(x+1)\) gives (4). This explicit bound on the integer part permits the next union to include every possible lift.

For each triple \(t,h,k\), \(h\ge B,\ 0\le k\le2^{B+2}\), consider its next \(h\) native letters. For an absolute \(D\ge2\) the probability of
\[
                  |g-h/2|>D\sqrt{hB}
\]
and the occurrence of that triple is at most \(6e^{-2D^2B}\) by (3) and Hoeffding's binomial bound. Summing over the \(O(n^3 2^B)\) triples and excluding the exceptional set of (4), we have a common event of probability at least \(1-Cn^3e^{-cB}\) on which every prelanding start of height \(h\ge B\) obeys this odd-count bound. The constants are independent of \(n,B\).

## Following the true blocks

Choose a fixed integer \(H_0=\lceil 32D^2 B\rceil\), and suppose \(n\ge H_0\). While the current height \(h\ge H_0\), follow exactly \(h\) native dates. Its odd count \(g\) belongs to \([h/4,3h/4]\), so landing cannot occur in this block and the next height \(h-g\) belongs to the same interval. The first height \(h_*\) below \(H_0\) still exceeds or equals \(H_0/4\), so (4) holds there. Write \(t_*\) for the elapsed time. Summing the deviations along these geometrically decreasing heights yields
\[
              |t_*-2(n-h_*)|\le 2D\sqrt B\sum_{\rm blocks}\sqrt h
                                       \le C\sqrt{nB}.                   \tag{5}
\]
At the remaining start, \(x\le2^{B+2}\). While \(x>1\), an odd multiplier is at most \(4/2\), an even multiplier \(1/2\), and the first subsequent value at most one, if reached from above one, exceeds \(1/2\). Thus within \(O(B+h_*)\) dates the trajectory lands or visits \((0,1]\). Any remaining time is at most \(J_*(H_0)\). Consequently, outside the exceptional probability \(Cn^3 e^{-cB}\),
\[
      2n-C(\sqrt{nB}+B)\ \le\ \tau\
             \le 2n+C(\sqrt{nB}+B)+J_*(\lceil32D^2B\rceil).            \tag{6}
\]
This is a finite-scale concentration inequality with the remaining worst-case input explicit. For (1) take \(B=\lceil C_A\log(2+n)\rceil\) and use the elementary \(J_*(H)=O(H^2)\) from (2). For the assertion about one ternary unit, take \(A>1\) and apply the first Borel–Cantelli lemma to its uniformly distributed residue at each height.

For a fixed lower deviation \(\epsilon n\), take \(B=\lfloor c_\epsilon n\rfloor\) sufficiently small in (6). For the upper deviation fix any \(K>0\) and take \(B=\lceil K\sqrt n\rceil\). The uniform consequence \(J_*(H)=o(H^2)\) of the worst-case theorem gives \(J_*(\lceil32D^2 B\rceil)=o_K(n)\); the other error terms are also \(o_K(n)\). The bound \(Cn^3e^{-cK\sqrt n}\) for every fixed \(K\) is the stated \(e^{-\omega_\epsilon(\sqrt n)}\) estimate. With just (2), taking a sufficiently small fixed \(K\) yields \(O_\epsilon(e^{-c_\epsilon\sqrt n})\). If a uniform \(J(h)=O(h\log(2+h))\) is established, the same proof would give an upper large-deviation bound \(O_\epsilon(e^{-c_\epsilon n/\log n})\). A uniform linear bound would give an exponential upper tail.

The proof concerns exact positive rational inputs on the full ternary grid. Their physical realizations as intervals in unmatched ordinary pairs use different source cylinders. A small exceptional fraction on this grid does not exclude an unusually long worst-case interval, or force a merger for a particular positive integer pair.

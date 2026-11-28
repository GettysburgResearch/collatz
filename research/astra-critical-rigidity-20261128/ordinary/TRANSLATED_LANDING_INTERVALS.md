# A uniform landing estimate up to the critical real translation, and an obstruction beyond it

Fix \(0<\theta\le1\). For each denominator \(3^n\) choose any interval of \(3^{\theta n}\le M\le3^n\) consecutive positive integers \(m\), and choose uniformly among its ternary units. Its real sources \(m/3^n\) lie in \((X,X+1]\) for some \(X\ge0\); for example take \(X=(\min m-1)/3^n\). Write \(T\) and \(N\) for the first integer landing date and landing integer, and \(\gamma=\log_2 3\).

**Proposed uniform estimate.** For each fixed \(A>0\), outside probability \(O_{A,\theta}(n^{-A})\),
\[
  2n-C_{A,\theta}\sqrt{n\log(2+n)}\ \,\le T\le\,
  2n+C_{A,\theta}\sqrt{n\log(2+n)}
       +[\log_2(X+1)-(2-\gamma)n]_+ .                                  \tag{1}
\]
On the same event the two observables obey the sharper joint law
\[
           T+\log_2 N=\max\{2n,\log_2 m\}
                      +O_{A,\theta}(\sqrt{n\log(2+n)}).                 \tag{1a}
\]
Both quantities on the left refer to the same actual first landing. Above the critical real height, the starting binary height may be shared between a later landing and a larger landing integer. There is no upper bound on \(X\). In particular the concentration around \(2n\) persists uniformly up to \(X+1\le2^{(2-\gamma)n}\), and still holds with the same order when the logarithm exceeds that threshold by \(O(\sqrt{n\log n})\). If \(\log_2(X+1)\le(2-\gamma-\eta)n\) for fixed \(\eta>0\), then \(N\le n^{C_{A,\theta}}\) outside the same probability for sufficiently large \(n\). For unrestricted \(X\), the time to erase all but \(O_{A,\theta}(\log n)\) ternary factors still differs from \(2n\) by \(O_{A,\theta}(\sqrt{n\log n})\). The residual height in this last assertion may depend on the sampled source.

The height correction in (1) is necessary on arbitrarily high translates. There are absolute \(c,C>0\) such that for every sufficiently large \(n\) and every integer \(D\ge1\), some integer translate \(X>0\) of the complete real grid \((0,1]\), with \(X<2^{D+3n+2}\), has
\[
                         \Pr_X(T>D)\ge c n^{-C}.                         \tag{2}
\]
One can choose \(\log_2 X=D+O(n)\) and require the same sources to take at least \(D\) consecutive even steps at remaining height one. When \(D/n\to\infty\), this rules out replacing the coefficient one on the unbounded positive-part term in (1) by any fixed smaller coefficient while retaining arbitrary polynomial confidence. The sources in (2) are actual positive rationals on one common translated grid.

## Tracking the contribution from the common real translate

At a native date \(t\) before landing let \(g=n-h\) be the consumed odd grade and decompose the actual positive state as
\[
              x_t=3^g 2^{-t}X+y_t .
\]
Initially \(0<y_0\le1\). Using the actual departure bit \(b\) of \(x_t\), the residual obeys \(y_{t+1}=(3^b y_t+b)/2\). It stays positive. Its letters need not be the bits of \(y_t\); they are always read on the true \(x_t\).

Use the [local source counting lemma](LOCAL_INTEGER_LANDING.md) at fixed dates \(t\le3n\), heights \(h\), and specified integer floors of the **actual** state. Its proof depends on the length of the source interval and the remaining ternary modulus, and applies unchanged to arbitrary translates of either interval. In fact its lattice periodization counts all translates at once. The phase \(3^{n-h}2^{-t}X\) is known at each fixed \((t,h)\), so \(y_t\le2\) puts \(x_t\) in at most four possible unit floors, regardless of \(X\). A run of \(B\) visits of \(y\) above two after this upcrossing needs at least \(\rho B\) true odd bits for the same \(\rho>1/2\) as in the local proof. Its multiplicative estimate uses only the displayed affine recurrence for \(y\). Consequently outside probability \(O(n^2 e^{-cB})\), all visits with \(h\ge B,\ t\le3n\) have \(y_t\le2^{B+2}\). At that point there are only \(2^{B+2}+2\) possible unit floors for \(x_t\) at each fixed \((t,h)\), even if the predictable translate is very large.

The capped word blocks of the local theorem now apply on this common good event with their unchanged union bounds. Use \(B=\lceil C_{A,\theta}\log(2+n)\rceil\). At the first block endpoint with \(h_*=O(B)\) below the cutoff, still \(h_*\ge B\), one has \(y_*\le2^{B+2}\) and
\[
                       t_*=2(n-h_*)+O_\theta(\sqrt{nB}).
\]
In particular this time is uniform over **all** positive real translates. If one prefers a deterministic remaining height, the first visit to the cutoff level itself occurs within the last block. That entire block has length \(O(B)\): an uncapped block ending below the cutoff began below four times the cutoff, and for large \(n\) a capped block cannot end this low. So the same time estimate holds for that deterministic level.

At this endpoint,
\[
 \log_2(1+x_*)\le O_\theta(B+\sqrt{nB})
                     +[\log_2(X+1)-(2-\gamma)n]_+ .
\]
While the actual state exceeds one its odd multiplier is at most two and its even multiplier is one half. The first later visit at most one from above has state above one half; a landing from above has positive integer state at least one. Thus within \(2h_*+\log_2(1+x_*)+1\) extra dates the orbit lands or visits \((0,1]\). After the latter visit the remaining time is bounded by \(J_*(h_*)=O(B^2)\). This proves (1). In the subcritical range with fixed margin \(\eta n\), the deterministic term \(3^{n-h_*}2^{-t_*}X\) tends to zero, so \(x_*\le2^{B+2}+1\). The quantity \(x+1\) is multiplied by \(3/2\) on each odd step and never grows on an even step. There are only \(h_*\) remaining odds, proving the polynomial bound on the final integer.

For the upper bound on the **sum** in (1a), take the first portion of the tail on which the input stays above one. If its length is \(r\) and endpoint is \(v\), then
\[
               r+\log_2 v\le\log_2 x_*+2h_*
\]
by the same multiplier inequality. If that endpoint is the landing, this already includes \(\log_2 N\). If it is the first crossing into \((0,1]\), then \(v>1/2\), the additional duration is at most \(J_*(h_*)\), and the eventual \(\log_2 N\) is \(O(1+h_*)\) by the \(x+1\) inequality. When \(x_*\le1\) only this latter argument is needed. Thus uniformly
\[
            T-t_*+\log_2 N\le \log_2(1+x_*)+O(h_*+J_*(h_*)).
\]
Insert the displayed bound on \(x_*\). If \(X\ge1\), \(\log_2(X+1)\le\log_2(m/3^n)+1\); if \(X<1\), the positive-part term vanishes for large \(n\). This gives the upper bound in (1a). Conversely the exact nonnegative carry equation \(2^T N=m+C_w\) gives \(T+\log_2 N\ge\log_2 m\); also \(N\ge1\) and \(T\ge 2n-O_{A,\theta}(\sqrt{n\log n})\). This proves its lower bound.

## A many-source obstruction using a single high translate

First use the complete grid of \(m/3^n\in(0,1]\). The preceding argument with \(X=0\), say at confidence \(1-O(n^{-2})\), gives a set of probability at least one half on which \(T\le3n\), and a previous controlling height \(h_*=O(\log n)\) at real state at most \(n^{O(1)}\). All subsequent positive-level reduced numerators are at most \(n^{O(1)}\): at the controlling date the numerator is bounded by \(3^{h_*} n^{O(1)}\), and an odd update averages this with the next smaller ternary power. Each source in this set therefore has a height-one visit at one of at most \(O(n)\) native dates \(t\), with one of at most \(n^{O(1)}\) numerators \(d\). Fix a pair \((t,d)\) shared by at least \(c n^{-C}\) of the entire grid, choosing a single such visit for each source.

Choose an integer \(2^D\le z<2^{D+1}\) with \(d+3^n z\equiv0\bmod 2^D\), and put \(X=2^t z\). Every previously selected source acquires the very same first \(t\) departure bits after adding \(X\) to its real starting value. Indeed its initial difference is divisible by \(2^t\) in \(\mathbb Z_2\), and each common native step divides the difference by two and possibly multiplies it by three. Exactly \(n-1\) odd grades have been consumed by this common height-one date, hence the new rational state there is \((d+3^n z)/3\). Its numerator is positive, prime to three and divisible by \(2^D\). The next \(D\) departures are even, with level still one. The translated initial grid consists of ordinary positive ternary-unit numerators \(m+3^n X\) of the same denominator. This proves (2) and its height claim. No single ordinary Collatz orbit or fixed unbounded translate is extracted from this construction.

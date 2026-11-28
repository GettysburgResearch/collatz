# A sharp block-size threshold for synchronized powers of three

Fix integers `M>0` and `c`. Write
\[
 X_n^+=c+M3^n,\qquad X_n^-=c+M3^{-n}\quad(n\ge0).
\]
Use the shortcut Collatz map on rationals of odd denominator. A block synchronizes by date \(t\) if all its trajectories have the same value at the same native date at most \(t\), equivalently at date \(t\). Ignore the finitely many nonpositive ascending terms when positive sources are desired. For the positive descending and integer-landing conclusions take \(c\ge0\) and \(3\nmid M\).

**Written theorem, using Leen's fixed-state absorption law.** Put \(t=\lfloor\log_2 N\rfloor\). Uniformly in every starting index \(a\ge0\), the fraction of \(a\le n<a+N\) for which the pair \(X_n^\pm,X_{n+1}^\pm\) fails to synchronize by \(t\) is
\[
                    \frac{\kappa(c,M)+o_{c,M}(1)}{\sqrt t}.                 \tag{1}
\]
The same positive finite constant works in both directions. For blocks \(X_n^\pm,\ldots,X_{n+k}^\pm\), with \(k=k(N)\ge1\), the fraction synchronizing by \(t\) tends to one if \(k=o(\sqrt t)\), and tends to zero if \(k/\sqrt t\to\infty\). In the latter direction, uniformly for every \(k\ge1\), the synchronizing fraction is at most
\[
                 C_M\exp[-k^2/(2t)]+O_{c,M}((t+1)/N).                      \tag{2}
\]
For the positive descending tower, a block synchronizing this early has identical first integral landing dates and identical first landing integers throughout whenever \(n>t\). Thus a density-one proportion of starts has that common landing data on any \(o(\sqrt{\log N})\)-length block. Equation (2) limits *early* synchronization. It gives no bound on later mergers or later eventual equality of landing data.

## Two conditional cylinder laws

Let \(v=v_2(M)\), \(d=v+3\). The positive and negative powers of \(3\) modulo \(2^u\), for \(u\ge3\), each generate exactly the unit classes \(1,3\pmod8\), of order \(2^{u-2}\). This follows by induction from \(v_2(3^{2^b}-1)=b+2\) for \(b\ge1\). Therefore in each complete period of \(P_j=2^{j-v-2}\) exponents, either tower runs once through all of a fixed pair of cylinders modulo \(2^j\), for \(j\ge d\). The two cylinders at depth \(d\) have residues \(c+M,c+3M\); denote their union in \(\mathbb Z_2\) by \(U\), of Haar mass \(2^{1-d}\). Shifting or reversing the exponent order preserves this conclusion.

Use the canonical initial state \(z=(1,-2c)\) for the two bases \(x,3x-2c\), where \(x=X_n^+\) on the ascending tower and \(x=X_{n+1}^-\) on the descending tower. Canonical absorption means equality of the two affine functions of the original base on its parity cylinder. Each labelled history of length \(j\) is exactly a cylinder modulo \(2^j\); the residual oriented base is conditionally Haar. Conditional on each of the two depth-\(d\) classes of \(U\), let \(z_1,z_2\) be its canonical end state, with the absorbed state kept fixed. If \(A\) denotes canonical absorption, set \(S_j=\mathbb P(A>j\mid U)\). Leen's fixed-state capacity theorem gives
\[
  \sqrt j S_j\longrightarrow\kappa(c,M)
       =\frac{h(z_1)+h(z_2)}{\sqrt\pi}.                                  \tag{3}
\]
Here \(h\) is finite, harmonic, positive at every live state, and zero at absorption. At least one of \(z_1,z_2\) is live. Otherwise every consecutive pair of ascending powers would have absorbed by \(d\). If \(g_i\in[0,d]\) is the odd-input count of the \(i\)-th tower member through date \(d\), equality of adjacent slopes forces \(g_i=1+g_{i+1}\) for *every* \(i\), impossible. For instance, at \(c=0,M=1\) the two states at depth three in the convention \((x,3^s x+D)\) are \((1,-2)\) and \((1,-1)\). These formulas do not give a numerical evaluation of the external harmonic capacity. [Leen, fresh labels and exact cylinders](https://doi.org/10.5281/zenodo.23268755) · [Leen, Theorem 7.2, harmonic capacity and conditioned histories](https://doi.org/10.5281/zenodo.23268751)

We need accuracy at the full deadline \(t\), where a partial period cannot simply be discarded. Take \(j=t-\lceil2\log_2(t+2)\rceil\), eventually exceeding \(d\). For any length-\(N\) exponent interval, the survivor fraction at date \(j\) differs from \(S_j\) by at most \(P_j/N=O(t^{-2})\). The number of additional absorptions between dates \(j\) and \(t\) in that interval is at most
\[
       (\lfloor N/P_t\rfloor+1)P_t(S_j-S_t)
                 \le (N+P_t)(S_j-S_t).
\]
The containment of both events is literal on the finer cylinders. Since \(P_t\le N\) and \(j/t\to1\), equation (3) gives \(S_j-S_t=o(t^{-1/2})\). This proves (1) first for canonical absorption, uniformly over interval location.

## Physical equality at arbitrary exponent gap

For any length-\(t\) parity word of odd grade \(g\), the endpoint from \(x\) has numerator \(3^g x+C\) over \(2^t\), with \(0\le C\le 3^t-2^t\) by induction. Orient the two endpoint inputs as \(c+y,c+3^k y\), with \(y=M3^n\) ascending and \(y=M3^{-(n+k)}\) descending. If their physical values agree at date \(t\), then their word grades \(g_1,g_2\) satisfy
\[
 (3^{g_1}-3^{g_2+k})y
      =(3^{g_2}-3^{g_1})c+C_2-C_1.                                       \tag{4}
\]
Equal slopes in (4) give equality on the cylinder. In particular \(g_1-g_2=k\). With unequal slopes the right side has absolute value at most \((|c|+1)3^t\). Ascending, this requires \(M3^n\le(|c|+1)3^t\). Descending, the coefficient on the left has 3-adic valuation \(\min(g_1,g_2+k)\le t\), so \(n+k\le t+v_3(M)\). Hence there are at most \(O_{c,M}(t+1)\) unbalanced equality indices in any interval, uniformly in \(k\). For \(k=1\) this proves (1) for actual equality. Equation (4) concerns the ordinary numerical values, including exceptional rational inputs where different affine functions agree just once. Determinism lets us test every earlier merger by equality at the single terminal date.

## The block transition

Failure of a whole block requires at least one of its \(k\) adjacent pairs to disagree at the common deadline. Apply (1) to each shifted interval, using its uniform error. This proves the short-block conclusion.

For the opposite direction, any synchronized block must have synchronized endpoints. Except for the \(O_{c,M}(t+1)\) indices in (4), their grades differ by \(k\). Thus one grade is at least \(t/2+k/2\) or the other is at most \(t/2-k/2\). For a Haar base, the first \(t\) parity symbols are uniform on the binary cube: each word of length \(t\) is one cylinder modulo \(2^t\), by iterating the bijective affine transition on each fixed parity. Hence each grade individually has the binomial \((t,1/2)\) law. Conditional probability on \(U\) is at most \(2^{d-1}\) times the corresponding full Haar probability. Empirical probability on any length-\(N\) exponent interval is at most \((1+P_t/N)\) times that conditional probability, by complete periods including the last partial period. This holds for each of the two tower indices separately, even when \(k\) grows arbitrarily. Hoeffding's one-sided bound and a union bound give (2), for instance with \(C_M=2^{d+1}\). The two marginal counts need no independence assumption.

On the descending tower with \(3\nmid M\), the fully reduced initial denominator of \(X_i^-\) is \(3^i\). Each odd shortcut step removes exactly one factor of three until the integral landing. A positive noninteger source cannot take only even steps indefinitely because its positive integer numerator would be divided by two each time. Thus a first integral landing exists and takes at least \(i\) native dates. For \(i\ge n>t\) it follows the common state at \(t\), which proves the stated block conclusion.

Write \(\tau_n\) for the actual first integral landing date on this fixed descending tower. Formula (1) implies a pointwise large-jump consequence
\[
       \limsup_{n\to\infty}\frac{\tau_{n+1}-\tau_n}{\sqrt{\log_2 n}}
                                      \ \ge\ \frac1{\kappa(c,M)}.          \tag{5}
\]
Indeed among the first \(N\) boundaries at most \((\kappa+o(1))N/\sqrt{\log_2 N}\) have different landing data: a synchronized boundary at \(n>t\) has identical data, and the first \(t+1\) boundaries do not affect the estimate. Since \(\tau_N\ge N\), summing the signed increments forces (5); an eventual upper bound strictly smaller than \(1/\kappa\) in (5) would give \(\tau_N\le(1-\varepsilon)N+O(1)\) for some \(\varepsilon>0\). In every length-\(N\) interval there is also a consecutive run with the same first date and integer of length at least \((1/\kappa-o(1))\sqrt{\log_2N}\), by dividing by one plus the number of changed boundaries. Neither assertion requires any positive ordinary orbit to reach one.

Leen's original exact rates already include asymptotics on consecutive *integer* populations. The powers-of-three residue permutation was also used in the [translated ternary obstruction](../ordinary/TRANSLATED_TERNARY_POWERS.md) to exhibit exceptional exponent progressions with long separation. Here the count is on exponent intervals, including arbitrary interval origins, and both sides of the typical early block-size transition concern actual members of the two arithmetic towers. The asymptotics allow infinitely many exceptional exponents. They do not prove convergence for one specified positive integer or give a pointwise worst landing bound.

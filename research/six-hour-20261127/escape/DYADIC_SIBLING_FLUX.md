# Signed changes between actual dyadic siblings

Let \(T(2n)=n\), \(T(2n+1)=3n+2\). Let \(b\colon\mathbb N_{>0}\to\{0,1\}\) be unchanged along every shortcut edge outside finitely many initial integers. Suppose both colors have positive lower natural density. These hypotheses hold for either color of any nonconstant exactly invariant binary labeling, on the fixed-target predecessor theorem. They also hold for the actual plus-map indicator of ever visiting 5. Its only exceptional edge leaves 5. The predecessors of 5 have color one, and the predecessors of 85 have color zero because the orbit from 85 reaches 1 without visiting 5. [Paper 212, dyadic siblings and visit-to-five application](https://rstation.ai/problems/collatz/papers/212)

Give \(x\in[1,2)\) Lebesgue probability. Put \(n_j=\lfloor2^jx\rfloor\), \(F_j=b(n_j)\) and \(B_j=n_{j+1}-2n_j\). The next bit \(B_j\) is fair given the prefix through \(n_j\). Fix \(J\ge1\) above all exceptional edges in the sense that \(2^J\) exceeds their initial vertices. At \(j\ge J\) define
\[
 E_j=b(2n_j+1)-b(n_j),\qquad K_N=\sum_{J\le j<N}E_j^2.
\]
Call \(j\) an opportunity when the two children differ, equivalently \(E_j\ne0\). The count \(K_N\) is the number of opportunities actually seen on the dyadic ray, including those on which its child keeps the parent color.

**Written conclusions.** Along every predetermined infinite subsequence of levels, both colors appear infinitely often for almost every \(x\). The null set may depend on the selected subsequence. Almost every ray consequently has infinitely many opportunities. The signed values \(E_j\) read only at those opportunities, after their first value, are independent fair signs. In particular
\[
 \limsup_{N\to\infty}{\sum_{J\le j<N}E_j\over
         \sqrt{2K_N\log\log K_N}}=1,\qquad
 \liminf_{N\to\infty}{\sum_{J\le j<N}E_j\over
         \sqrt{2K_N\log\log K_N}}=-1
 \quad\text{almost surely}.                                           \tag{1}
\]
The ratios concern the tail where the logarithms are defined. Nevertheless, for every deterministic nonincreasing \(w_j\ge0\) tending to zero with \(\sum_{j\ge J}w_j^2/\sqrt j<\infty\), the signed series \(\sum_j w_jE_j\) converges almost surely and in \(L^2\). This includes \(w_j=j^{-s}\) for \(s>1/4\), whereas direct absolute summation of the available shell bound requires \(s>1/2\). The weighted estimate gives genuine cancellation. Formula (1) excludes a bounded unweighted charge of this particular signed sum.

## Weak limits of physical shell labels

Write \(f_j(u)=b(\lfloor2^j u\rfloor)\) on the positive real axis, assigning any value if its index is zero. In every compact annulus the fraction of adjacent integer sites with different colors is \(O(j^{-1/2})\) at scale \(2^j\). To see this, apply the fixed-offset counted-fusion estimate through \(t=\lfloor j/2\rfloor\). Its failure event depends on the first \(t\) binary digits, so the transfer from complete periods incurs \(O(2^{t-j})\). Sites on either path through that deadline stay above the finite exceptions on a fixed compact annulus for large \(j\), since a step loses at most a factor two. Restricting the starting site to one fixed residue class modulo 2 or 3 costs at most a fixed factor in this upper bound. [Weaver, Paper 124, fixed-block fusion estimate](https://rstation.ai/problems/collatz/papers/124) · [Paper 212, shell transfer](https://rstation.ai/problems/collatz/papers/212)

Consequently \(d_j=\mathbb E E_j^2\ll j^{-1/2}\): different siblings must be adjacent sites with unequal labels. Also
\[
           f_j(2\,\cdot)-f_j\longrightarrow0,\qquad
           f_j(3\,\cdot)-f_j\longrightarrow0
                   \quad\text{in local }L^1.                           \tag{2}
\]
For the first identity on the cell of \(n=\lfloor2^ju\rfloor\), the even child has the parent color while the odd child can differ only at a sibling mismatch. For the second, \(b(3n+2)=b(2n+1)\) above the exceptions, and \(\lfloor3\cdot2^ju\rfloor\) is one of \(3n,3n+1,3n+2\). The resulting finite shifts use the adjacent-site bound.

Every sequence \(j_i\to\infty\) has a locally weak-* convergent subsequence of \(f_{j_i}\), by weak-* compactness on each bounded annulus, separability of its \(L^1\), and diagonal extraction. Equation (2) gives \(f(2u)=f(3u)=f(u)\) almost everywhere for each such limit. In log coordinates translation by \(\log 2\) and \(\log3\) preserves it. The subgroup they generate is dense, and translations are continuous in local \(L^1\), so \(f\) is spatially constant almost everywhere. Both colors have positive lower fraction in each sufficiently large full dyadic octave. Indeed if a color occupies at least \(eY\) integers below \(Y\), its points in \([eY/2,Y]\) still number at least \(eY/2-O(1)\); double them into \([Y,2Y)\) with multiplicity at most \(1+\lceil\log_2(4/e)\rceil\). The starting points are above all exceptions for large \(Y\). Hence every weak-* limiting constant belongs to a common compact subinterval of \((0,1)\). No common value of that constant is required.

On a measurable subset of \([1,2)\) where a predetermined \(f_{j_i}\) eventually has color zero, dominated convergence would give zero integral on that set. Testing a weak-* cluster limit on the same set forces its measure to be zero. The proof for eventual color one uses \(1-f_{j_i}\). This establishes the first assertion. Paper 212 already derives constancy from summable sibling variation by strong convergence. Here the vanishing one-shell variation gives constancy of every weak-* cluster; in particular there is no strongly convergent subsequence on any subset of positive measure. For labels with a known natural density, the same weak-* conclusion also follows directly by partial summation. [Paper 212, §Density from dyadic siblings](https://rstation.ai/problems/collatz/papers/212)

## The signs and their quadratic variation

At every level \(j\ge J\) the realized increment is \(F_{j+1}-F_j=B_j E_j\). If the opportunities stopped, the color would be eventually constant, an event of probability zero. Enumerate opportunities as \(\tau_1<\tau_2<\cdots\). Each \(\tau_i\) is known before its next bit is revealed. At any finite such stopping time, the next bit is fair conditionally on the stopped prefix, by summing the fair-bit identity over its possible values. Since all these stopping times are finite almost surely, the bits \(B_{\tau_i}\) are independent fair bits, also independent of all information known through \(\tau_1\).

On an opportunity \(S_i:=E_{\tau_i}=1-2F_{\tau_i}\). The label is constant from its chosen child up to the next opportunity, giving the exact recurrence
\[
                       S_{i+1}=S_i(1-2B_{\tau_i}).
\]
For either initial sign, the map from the first \(h\) fair bits to \(S_2,\ldots,S_{h+1}\) is bijective. This proves the independent-sign assertion and (1) by the usual iterated-logarithm law. The physically realized signed changes have sum \(F_N-F_J\) in \([-1,1]\). The predictor in (1) sums the available changes before choosing a child. [Hartman and Wintner, American Journal of Mathematics 63 (1941), 169–176](https://doi.org/10.2307/2371287)

Set \(M_N=\sum_{J\le j<N}(2B_j-1)E_j\) and \(P_N=\sum_{J\le j<N}E_j\). Orthogonality of the centered fair-bit increments gives
\[
 \mathbb E M_N^2=\mathbb E K_N=\sum_{J\le j<N}d_j,\qquad
                P_N+M_N=2(F_N-F_J).
\]
In particular \(|\mathbb E P_N^2-\mathbb E K_N|\le4\sqrt{\mathbb E K_N}+4\). The means of the signed realized increments telescope even if the one-shell absolute rates are nonsummable. The bound on \(d_j\) gives \(\mathbb E K_N\ll\sqrt N\). Markov's inequality at \(N=2^r\), Borel–Cantelli and monotonicity imply \(K_N=O_x(\sqrt N(\log N)^{1+\epsilon})\) almost surely for each \(\epsilon>0\). There is no asserted matching ordinary-level growth rate.

With weights \(w_j\), the centered martingale has total expected quadratic variation \(\sum w_j^2d_j<\infty\), giving almost sure and \(L^2\) convergence. The realized sum \(\sum w_j(F_{j+1}-F_j)\) converges in both senses by summation by parts, boundedness of \(F_j\) and finite total variation of \(w_j\); its tails are uniformly \(O(w_j)\). Twice this realized sum minus the centered martingale equals the weighted predictive series. This proves the stated signed cancellation without treating the changing integer prefixes as independent samples.

The visit-to-five example obeys the entire flux theorem even though it has its single exceptional low edge. An argument based only on this asymptotic cancellation would therefore have to distinguish the orbit crossing that edge in order to force a constant true component label. A measurable full-measure assertion along changing integer prefixes is compatible with an exceptional trajectory of one fixed positive integer. Neither the finite binary harmonic mass nor the existence of a surviving ordinary source is decided here.

The [Lean interfaces](DyadicSiblingFlux.lean) verify the finite binary identities for predictor signs, realized changes, fair children and their squares. Weak-* convergence, predictable sampling, weighted martingale convergence and (1) are written arguments. The [finite control](check_dyadic_sibling_flux.py) computes the visit-to-five labels of every required positive integer by tracing to 1 or 5, checks every ray ending at level 12 or 16 from level 3, and checks fair next outcomes separately at every observed opportunity count and sign. No finite-depth conditioning is used to infer independence of later signs. [Retained exact counts](DYADIC_FLUX_CONTROLS.json)

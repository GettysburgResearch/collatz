# Quantiles and the complete denominator at every odd rotation

**PROPOSED, elementary.** A positive primitive rational odd cycle has least odd period \(p\), cyclic exponents \(e_i\ge1\), and a common reduced denominator \(q\). Write \(x_i=y_i/q\), so the different \(y_i\) are positive odd integers and \(2^{e_i}y_{i+1}=3y_i+q\). This is the physical odd map on odd-denominator rationals with their ordinary two-adic parities. Closing the lap shows \(q\mid 2^{\sum e_i}-3^p\), so \(q\) is prime to six and is preserved at every step. We use the full reduced denominator.

For any proper odd shift \(\ell\), let \(s=\#\{i:e_i\ne e_{i+\ell}\}\) and \(M=p/\gcd(p,\ell)\). For \(Y>0\) write \(D_Y=\#\{i:x_i\le Y\}\). An unrestricted orbit maximum can be exponentially larger than \(Y\). Write \(T=\max(0,\lfloor\log_2(qY)\rfloor)\). For every integer \(2\le J\le M\),
\[
       \boxed{\quad D_Y\le \frac pJ+\frac{J^2-1}{6}\,sT .\quad}          \tag{1}
\]
At bounded order there is a separate finite estimate. Put \(d=p/M\), and let \(K\) be the number of residues modulo \(d\) on which the \(M\) physical exponents are nonconstant. Then \(1\le K\le s/2\), and
\[
                     D_Y\le d+(M-1)KT.                                    \tag{2}
\]
For example, if a proportion at least \(\delta>1/J\) is below \(Y\), with \(J\le M\), then
\[
   \log_2 q\ \ge\ \frac{6(\delta-1/J)p}{(J^2-1)s}-\log_2Y.                \tag{3}
\]
Hence a bounded mismatch count, a positive margin in that quantile, and \(\log Y=o(p)\) force exponential growth of the full denominator. For integer cycles with a positive proportion in \([1,p^C]\), each such shift has \(s\gg_{C,\delta,J}p/\log p\). In the bounded-order frontier, at most \(1/M+o(1)\) of the phases of a bounded-mismatch candidate can have subexponential height, uniformly for each specified subexponential cutoff. The remaining possible case still includes cycles with almost all phases very large. These assertions allow arbitrarily many unequal exponents and unrestricted values of the exponents.

## Two-sided spacing at every date

Compare two tracks, either at lag \(\ell\) around the whole lap or among all \(M\) phases in a column modulo \(d\). Partition their chronological base into blocks ending with an unequal departure. On one block let \(L\) be its odd length, including this last departure. Use the common exponents for the first \(L-1\) steps and the smallest participating exponent at the last. Write \(S_k\) for their first \(k\) division sums, \(0\le k\le L\), and \(A=S_L\).

For two different tracks with numerator difference \(g_k\) at the state after \(k<L\) steps, one has
\[
             3^k 2^{A-S_k}\mid g_k,\qquad
             |g_k|\ge 3^k 2^{A-S_k}\ge 3^k2^{L-k}\ge2^L.                 \tag{4}
\]
Indeed the common past gives \(2^{S_k}g_k=3^k g_0\), so \(3^k\mid g_k\). The complete common remaining division sum, including the minimum at the final departure, divides the incoming difference in the dyadic sense: subtract the two future affine laws before the final excess divisions to get \(2^{A-S_k}B=3^{L-k}g_k\) for an integer \(B\). The same carry appears because the carry on an odd block is independent of the last exponent. The difference \(g_k\) is nonzero by primitivity, and the two powers forced to divide it are coprime. On the whole block the relative correction of the higher of any pair along its first \(L\) departures also obeys
\[
      \sum_{k=0}^{L-1}\log(1+q/(3y_k^{\rm high}))
       \ \le\ \frac{q}{3}\sum_{k=0}^{L-1}\frac{1}{3^k 2^{L-k}}
       =q2^{-L}\left(1-(2/3)^L\right).                                  \tag{5}
\]
The same track is higher before each departure, since identical positive-slope maps propagate its strict order through the first \(L-1\) steps. Switching order on the last, unequal departure causes no exception.

For a pair of tracks at lag \(h\ne0\bmod p\), let \(s_h\) count its inequalities and \(E_h\) count dates at which both heights are at most \(Y\). If \(qY<1\) there are no such points. Otherwise (4) shows that only blocks of length at most \(T\) can contain such a date: two positive numerators at most \(qY\) have difference strictly smaller than \(qY\). The \(s_h\) disjoint blocks partition the whole lap. Thus
\[
                              E_h\le s_h T .                              \tag{6}
\]
The particle comparison at a single interior date uses both the entire shared past *and* the entire shared future of its actual block.

## Arbitrary translate order and exact occupation

For each \(i\bmod p\), take the first \(J\) distinct indices \(i,i+\ell,\ldots,i+(J-1)\ell\) and denote the number of low phases there by \(b_i\). Since \(b_i\le1+\binom{b_i}{2}\), summing over all translates gives
\[
    J D_Y\le p+\sum_{h=1}^{J-1}(J-h)E_{h\ell}
            \le p+sT\sum_{h=1}^{J-1}(J-h)h.
\]
For the last inequality, a difference at shift \(h\ell\) requires at least one of the \(h\) intervening comparisons to differ, so \(s_{h\ell}\le hs\). The last sum is \(J(J^2-1)/6\). This proves (1) and (3).

For (2), order the \(M\) exponents on a residue modulo \(d\) by the rotation \(+\ell\). Every nonconstant circle has at least two unequal neighboring exponents. If \(K=0\), the exponent list repeats after \(d<p\) odd steps. The affine map of that shorter block has positive slope \(3^d/2^E\ne1\); its \(M\)-th iterate and the map itself have the same unique fixed point. The physical cycle would therefore return after \(d\) steps, contradicting primitivity. Cut the base circle of length \(d\) immediately after each variable column, so its \(K\) blocks have lengths \(L_1,\ldots,L_K\). At a base date in a block of length greater than \(T\), (4) applies to every pair in the column. At most one of its \(M\) numerator points can be low. All short blocks together use at most \(KT\) columns, where there can be up to \(M\) low points. This proves (2). Even when the seam crosses the end of an actual cell the list of tracks is only cyclically permuted, preserving every pairwise statement.

## Geometric mean and all ordered quantiles

In a block with \(M\) tracks, the \(j\)-th smallest positive numerator in a column after \(k\) steps is at least \(1+(j-1)3^k2^{A-S_k}\). Thus each individual column has a full spacing bound. Averaging over the physical cycle gives, with \(\gamma=\log_2 3\),
\[
 \frac1p\sum_i\log_2 y_i\ \ge \frac{\log_2((M-1)!)}M+
 \frac{M-1}{M}
 \left[\frac{1+\gamma}{2}\frac{d}{K}-\frac{\gamma-1}{2}\right].     \tag{7}
\]
Indeed the product of the column is at least \((M-1)!(3^k2^{L-k})^{M-1}\). The sum of the exponents \(\log_2(3^k2^{L-k})\) over \(0\le k<L\) is \((1+\gamma)L^2/2-(\gamma-1)L/2\). Now use \(\sum L_j^2\ge d^2/K\). Without the factor \(M\), compare just one shift around the full lap. At each date \(\max(y_i,y_{i+\ell})\ge 3^k2^{L-k}\) and \(\log_2\max(y_i,y_{i+\ell})\le\log_2 y_i+\log_2 y_{i+\ell}\). This yields
\[
 \log_2 q+\frac1p\sum_i\log_2 x_i
       \ge \frac{1+\gamma}{4}\frac p s-\frac{\gamma-1}{4}.             \tag{8}
\]
Equations (5), (7) and (8) have no external analytic input. They do not provide an unrestricted upper bound on a cycle's geometric mean.

**Predecessors and boundary.** PR191 at `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, `research/two-sided-cycle-packing-20261124/README.md`, §2 already proves the two-sided dyadic/ternary spacing for coincident future/past at specified starts. PR212 at `505d3fe782922904e86477990cc5d41e9110edda`, `research/astra-infinite-descent-20261127/cycles/ODD_ROTATION_COMPLEXITY.md`, obtains qualitative mismatch growth at unbounded rotation order using Weaver's finite-descent theorem. At the same pin, `ROTATION_DENOMINATORS.md` proves the unconditional full denominator exponent through six mismatches, and `MISMATCH_CHAINS.md` gives Diophantine estimates at selected cuts. Here the spacing applies at *every* date of every aligned block, yielding period-wide low-quantile, geometric-mean and high-track correction constraints for every number of mismatches. The largest-period bounded-order case with at most its one-per-fiber low population remains open.

[Exact rational-cycle controls](check_rotation_occupation.py) · [Recorded counts](rotation_occupation_controls.json) · [Lean source for the partial final edge, subtraction and interior prime-power product](RotationOccupation.lean). The written argument supplies the block partition, occupation counting and averaging.

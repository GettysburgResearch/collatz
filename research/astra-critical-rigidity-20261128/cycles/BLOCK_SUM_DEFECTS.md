# Full denominators and opposite count deviations in long valuation windows

Let a primitive positive rational odd cycle have \(p\) distinct phases \(x_i=y_i/q\), total native valuation \(A\), and full reduced denominator \(q\). At each lag \(1\le h<p\) write
\[
 L_i=\sum_{j=0}^{h-1}e_{i+j},\qquad
 s_h=\#\{i:e_{i+h}\ne e_i\},\qquad n_v=\#\{i:L_i\ne v\}.
\]
All indices are circular. There are two distinct conclusions.

1. Take \(\log_2 3<A/p<2\), \(v=\lfloor hA/p\rfloor+1\), and \(\Delta=pv-hA\). Along any sequence with \(p\to\infty\) and \(s_h(n_v+\Delta+\log p)=O(p)\), the complete denominator satisfies
   \[
             \liminf \frac{s_h\log_2 q}{p}\ \ge\ \frac14,\qquad
             \liminf \frac{n_v\log_2 q}{p}\ \ge\ \frac18.               \tag{1}
   \]
   The hypothesis holds in particular if \(n_v(n_v+\Delta+\log p)=O(p)\). Every growing positive integer cycle therefore satisfies, uniformly in the upper window,
   \[
             \min_{1\le h<p}\frac{s_h(n_v+\Delta+\log p)}p\ \longrightarrow\infty .
                                                                            \tag{2}
   \]
   If \(\Delta=O(\sqrt p)\), then \(n_v/\sqrt p\to\infty\). In the rational setting, \(n_v=O(\sqrt p)\) and \(\Delta=O(\sqrt p)\) force \(\log_2q\ge(1/8-o(1))p/n_v\), including increasing \(n_v\). At coprime counts the right Farey parent has \(\Delta=1\).
2. Suppose instead that on positive **integer** cycles, for some fixed \(C>0,\delta>0\), at least \(\delta p\) odd states are at most \(p^C\). This holds, for example, whenever the minimum divided by the balanced-cycle minimum at the same clocks is bounded below by any positive constant. At every lag with \(s_h\log p=O(p)\), for every fixed \(K>0\),
   \[
   \begin{split}
      \liminf p^{-1}\#\{i:L_i-hA/p<-Kp/s_h\}&\ge\delta,\\
      \liminf p^{-1}\#\{i:L_i-hA/p> Kp/s_h\}&\ge\delta.                 \tag{3}
   \end{split}
   \]
   The negative deviations occur at all but \(o(p)\) of the polynomially low starts, and the positive ones at all but \(o(p)\) of the starts with polynomially low endpoints. This also covers the bounded-order exceptional shifts of the [approximate subgroup theorem](APPROXIMATE_ROTATION_SUBGROUP.md). In particular every proper window and every integer target, even a target chosen after seeing the word, obey
   \[
          \min_{1\le h<p,\ v\in\mathbb Z}\frac{n_v\log p}{p}
                        \longrightarrow\infty.                           \tag{4}
   \]
   Equation (3) measures the two tails of the actual halving count on intervals of \(h\) successive odd dates. The low-state hypothesis concerns their locations only through their positive density.

## From a sparse upper-window count to the height of every phase

The cyclic derivative \(L_{i+1}-L_i=e_{i+h}-e_i\) gives \(s_h\le2n_v\) for every integer \(v\), since either \(L_i\) or \(L_{i+1}\) differs from \(v\) at a change. Write \(E_j=\sum_{0\le i<j}e_i\). At a suitable cyclic root the nonnegative, periodic discrepancy \(z_j=\lfloor jA/p\rfloor-E_j\) has range \(W\le n_v+\Delta-2\) for every upper window in (1). This is Theorem 5A in Weaver, Mahler and Wren, including its extension to noncoprime counts. Their proof is combinatorial for every positive word with \(p<A<2p\), hence applies before selecting a rational or integer realization. It also gives the finer \(W\le n_v+\Delta-1-|I\cap J|\) in their notation. [Paper 22, Theorem 5A, equations (26A)–(29A)](https://rstation.ai/problems/collatz/papers/22/v4)

Every backwards cyclic \(j\)-prefix then has division sum \(T_{i,j}\ge jA/p-W-1\). At any genuine positive rational phase, the exact backwards affine expansion gives
\[
 x_i=\frac{\sum_{j=1}^p3^j2^{-T_{i,j}}}{3(1-3^p2^{-A})}
       \le\frac{p2^{W+1}}{3(1-3^p2^{-A})}.
\]
For \(\log_2 3<A/p<2\), the classical linear form bound gives
\(-\log_2(1-3^p2^{-A})=O(\log p)\), uniformly in the word. Thus
\(\log_2(1+\max_i x_i)\le W+O(\log p)\). This physical height bound also appears for mechanical substitutions in the [aligned event result](ALIGNED_MECHANICAL_EVENTS.md). [Bondareva, Luchin and Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

If \(s_h\log_2 q/p\) has a bounded subsequence that attains its lower limit, the hypothesis of (1) bounds
\[
 \frac{s_h}{p}\cdot\frac1p\sum_i\log_2(y_i+q)
 \le \frac{s_h}{p}\bigl[\log_2q+W+O(\log p)\bigr]=O(1)
\]
on that subsequence. The [uniform-origin complete-denominator theorem, (3)](UNIFORM_ROTATION_HEIGHT.md) proves the first lower limit in (1); when the lower limit is infinite it holds immediately. The derivative bound gives the second. At \(q=1\), selecting any violating sequence of windows contradicts (1), giving the uniform assertion (2). If \(\Delta=O(\sqrt p)\) and \(n_v=O(\sqrt p)\), then \(s_h(n_v+\Delta+\log p)=O(p)\), proving the remaining claims.

Paper 22 already gives an effective square-root estimate when \(\Delta=o(\sqrt p)\), and Solomon and Paper 24 give effective coprime estimates of the form \(n_v\ge\sqrt A-O(\log A)\). Equations (1)–(2) use the quantitative canonical-width theorem as an input, strengthen the asymptotic multiplier to divergence when \(\Delta=O(\sqrt p)\), and give a full-denominator rate in the growing-budget regime. Their onset inherits the ineffective open-arc estimate. [Solomon, polynomial boundary coordinates](https://doi.org/10.5281/zenodo.22220730) · [Paper 24, Lemma 2 and Theorem 3](https://rstation.ai/problems/collatz/papers/24/v3) · [Paper 22, Theorem 5A and its consequences](https://rstation.ai/problems/collatz/papers/22/v4)

## Opposite deviations at the true low starts and ends

Let \(c_i=\log_2(1+1/(3x_i))\), \(D=\sum_i c_i=A-p\log_23\). On a primitive ordinary cycle the \(p\) odd phases are distinct positive integers. Hence \(D\le(3\log 2)^{-1}\sum_i x_i^{-1}=O(\log p)\) uniformly. The exact native window product reads
\[
 L_i-hA/p=\log_2(x_i/x_{i+h})+
                  \sum_{j=0}^{h-1}c_{i+j}-hD/p.                        \tag{5}
\]
The absolute value of the last two terms together is at most \(D\) for every \(h\), including \(h\) close to the full period.

Fix a sequence with \(s_h\log p=O(p)\). If \(x_i\le p^C\) and \(L_i-hA/p\ge-Kp/s_h\), (5) gives
\(\log_2(x_{i+h}+1)\le Kp/s_h+C\log_2p+D+1=O(p/s_h)\), with a fixed implied constant on the sequence. The two logarithmic heights sum to \(O(p/s_h)\), so the [uniform paired-height theorem, (1)](UNIFORM_ROTATION_HEIGHT.md) gives only \(o(p)\) such starts. At a start with \(x_{i+h}\le p^C\), the same equation with \(L_i-hA/p\le Kp/s_h\) bounds the starting log height by \(O(p/s_h)\). This proves (3). If the minimum ratio is bounded below, the [balanced reciprocal identity, (3)](BALANCED_MINIMUM_GROWING_BUDGET.md) and the bound \(m=\min_i x_i\ll p^{5.116201}\) give positive density below \(p^7\), since every larger state contributes \(o(1)\) to \(m/x_i\).

For (4), if some targets gave \(n_v\log p=O(p)\), then \(s_h\le2n_v\) would allow (3) and \(n_v=o(p)\). A single target can belong to at most one of its two disjoint tails. A positive fraction in the other tail contradicts \(n_v=o(p)\). More precisely, at every lag as in (3), even an interval of length at most \(2Kp/s_h\), at any position on the count line, misses at least \((\delta-o(1))p\) of the actual window sums. This follows by using the two tails with threshold \((K+1)p/s_h\).

There is a structural consequence even when individual changes of the native exponents are arbitrarily large. If \(L_i\) takes just two integer values a distance \(b\) apart, then
\[
 b s_h=\sum_i|L_{i+1}-L_i|=\sum_i|e_{i+h}-e_i|
                    \le2(A-p)\le2p.
\]
At a single value \(s_h=0\), impossible at a proper lag of a primitive cycle. Thus (3) excludes all two-value windows with \(s_h\log p=O(p)\), regardless of the numerical size of their gap. On cycles with the low-state hypothesis, all such two-value windows, if any occur, satisfy \(s_h\log p/p\to\infty\) and \(b=o(\log p)\). This applies to arbitrary \(h\) including bounded orders. More generally (3) forces \(\sum_i|e_{i+h}-e_i|\gg Kp/s_h\) eventually for every fixed \(K\), since the range of the circular sequence \(L_i\) exceeds \(2Kp/s_h\). If the native exponents are uniformly bounded, (3) consequently gives \(\min_{h\ne0}s_h/\sqrt p\to\infty\) under the same low-state hypothesis: a contrary sequence would have \(s_h=O(\sqrt p)\), triggering (3), while that total variation would be \(O(s_h)\).

[Exact physical-window controls](check_block_sum_defects.py) · [Finite receipt](block_sum_defect_controls.json)

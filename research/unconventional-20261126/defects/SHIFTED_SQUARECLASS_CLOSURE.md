# Finite squareclass rank at shifted reset entrances characterizes eventual periodicity

**Status.** Proposed cross-packet consequence. This is a condition on a single positive ordinary trajectory, with no bound on the lengths of its ascents or on its reset depths. The proof uses the elementary square-product-of-translates bound A1 at the newly published PR192 head, together with the fixed-number-of-blocks duration bound in Theorem D. No effective rank-independent cycle or height bound is obtained.

At complete Syracuse block boundaries write \(Y_j=x_j+1\), where block \(j\) starts at the odd source \(x_j\), takes \(t_j=v_2(Y_j)\) odd steps and lands at \(x_{j+1}\). Its total shortcut duration is \(t_j+b_j\). Rank means the dimension of the span of the classes of the indicated positive rational numbers in \(\mathbb Q_{>0}^*/(\mathbb Q_{>0}^*)^2\) over \(\mathbb F_2\).

**Theorem F.** A fixed positive ordinary trajectory is eventually periodic if and only if the squareclasses of its **shifted block entrances** \(Y_j\) have finite rank. For every fixed rank bound \(d\), there are only finitely many positive ordinary cycles whose shifted entrances have rank at most \(d\), irrespective of their prime generators.

More locally put \(m=d+3\), \(K=12(m+3)\). There is a possibly ineffective threshold \(Y_*(d)\) with the following property. If the first \(Km\) complete blocks remain at boundary values at least their entrance \(Y>Y_*(d)\), then some group of \(m\) consecutive blocks among them has \(m+1\) shifted boundary values spanning rank at least \(d+1\). Only the boundary floor is required.

**Finding a short physical window.** Fix \(d,m,K\) before allowing \(Y\) to vary. For the \(Km\) blocks put \(T=\sum t_j\), \(B=\sum b_j\). Drop the divisor and terminal duration from D(1), taking \(\epsilon=1\), to get \(T\le 2\log_2Y+O_{m,K}(1)\). Its elementary block product, using the final boundary \(Y_{Km}\ge Y\), gives
\[
        B\le (\log_2 3-1)T+Km.
\]
Thus the total shortcut length is at most \(2\alpha\log_2Y+O_{m,K}(1)\), \(\alpha=\log_2 3\). Partition into \(K\) disjoint groups of \(m\) blocks, so one such group has shortcut length \(H\le(2\alpha/K)\log_2 Y+O_{m,K}(1)\). Its own entrance \(Y'\) is at least \(Y\).

**Translates for shifted rows.** Within this chosen group index the individual odd steps by \(i\); let \(a_i\) be the actual valuation and \(A_i\) the cumulative division count before that step. At the odd state \(n_i\) put
\[
  Z_i=2^{A_i}(n_i+1)/3^i=Y'+u_i.
\]
The shifted affine equation gives
\[
 u_{i+1}-u_i=2^{A_i}(2^{a_i}-2)/3^{i+1}.
\]
Consequently the \(m+1\) offsets at the selected boundaries are pairwise distinct: each of the \(m\) intervening blocks contains exactly one strictly positive correction. Also \(0\le u_i<2^H\), since \(A_{j+1}\le H\) and the reciprocal powers of three have sum less than one. With \(D_1=3^H\), each \(a'_i=D_1u_i\) is an integer in \([0,6^H]\), as \(i\le H\).

Suppose these \(m+1=d+4\) shifted boundary values had physical rank at most \(d\). Adjoin the three binary coordinates \(A_i\bmod2,i\bmod2,1\) to their squareclass vectors. The ambient rank is at most \(d+3\), so a nonempty relation exists. It selects an even number \(l\ge2\) of distinct boundaries, with \(l\le m+1\), whose normalized product \(\prod Z_i\) is a rational square. Therefore \(\prod(D_1Y'+a'_i)\) is an ordinary square: scaling by the even power \(D_1^l\) retains a rational square, and a rational square root of an integer is an integer.

A1 of the pinned PR192 packet excludes that square whenever \(D_1Y'>(64(6^H+1))^{l+2}\). The sufficient condition \(\log_2Y>(3H+7)(m+3)\) holds for all sufficiently large \(Y\). Indeed the coefficient of \(\log_2Y\) on this right side is at most \(6\alpha(m+3)/K=\alpha/2<1\). This is why one first chooses many disjoint physical windows and keeps the number of factors fixed. Applying the earlier growing-window estimate without this step would lose the relevant scale.

An escaping orbit is an injective sequence of ordinary positive integers tending to infinity, after discarding possible initial even steps. There are infinitely many complete blocks since the next reset occurs after exactly \(v_2(x+1)\) odd transitions at every odd source. The boundary sequence tends to infinity, and each of its tails attains an ordinary minimum. Applying the local theorem at arbitrarily large such minima forces unbounded squareclass rank. On an eventually periodic trajectory the boundary values lie in a finite set. For a cycle of rank at most \(d\), cut at its smallest block entrance and wrap around if necessary. Its minimum is at most \(Y_*(d)\), and each integer lies on at most one deterministic cycle. This proves both conclusions.

**Sources and boundary.** The elementary polynomial A1 already bounds squares of products of distinct positive translates, and A2 already uses three binary lifting coordinates. A3 concerns the **raw** odd-state squareclasses and gives an explicit bound for the cycle maximum in terms of that raw rank. Here translation by one and restriction to reset boundaries change the observable: normalized shifted offsets repeat on every ascent. The fixed-window duration comparison selects sufficiently short groups with arbitrarily many distinct reset offsets. Equivalently their total duration follows directly from Paper 147, Proposition 1 with constant-bit fragments and positive entrances, so this argument does not need the new divisor part of Theorem D. In either route it gives a bounded minimum for each fixed shifted rank. It does not force the shifted rank of every positive source to be finite or bound the rank across all possible cycles. [PR192, A1–A3, frozen head](https://github.com/GettysburgResearch/collatz/blob/1cb3e8496a6bd6092d3d0dc1dd043c3bcd662aca/research/astra-unconventional-20261126/adelic/README.md) · [Theorem D](PERSISTENT_RESET_DIVISOR.md) · [Paper 147 v1, Proposition 1](https://rstation.ai/problems/collatz/papers/147/v1)

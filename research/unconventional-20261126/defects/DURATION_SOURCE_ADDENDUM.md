# Independent reconstruction of the fixed-fragment duration input for actual reset windows

**Verification scope.** This proves just the constant-bit special case of Paper 147, Proposition 1, used for the large-order uniformity in E1. The special case and its coefficient one are prior results. The arithmetic input is Evertse (1984), Theorem 2, printed p. 228. No general signed-subsum nondegeneracy assertion is taken for granted.

In the notation of [Theorem D](PERSISTENT_RESET_DIVISOR.md), retain the exact unrolling but divide only by the entrance power \(2^{t_0}\). Write its odd root term as \(W_*=3^Tw_0\), and replace the correction at \(j\) by the two signed terms
\[
   W_j^+=3^{T-T_{j+1}}2^{D_{j+1}-t_0},\qquad
   W_j^-=-3^{T-T_{j+1}}2^{D_j+t_j-t_0}.
\]
The positive sum of the root and these pairs is \(2^{T+B-t_0}Y_r\). In chronological order the dyadic valuations of the correction terms are strictly increasing, from low \(D_j+t_j-t_0\) to high \(D_{j+1}-t_0\), and then up another \(t_{j+1}\) before the next low term. Thus any nonempty sum of correction terms alone is nonzero.

Suppose first that each of the \(r\) input boundaries satisfies \(Y_j>2^{r+1}r\). Let \(U_j\) be the root plus the true correction pairs before \(j\), on the *same terminal scale* as these terms. From the exact prefix identity,
\[
       U_j=3^{T-T_j}2^{D_j-t_0}Y_j,\qquad
       |W_j^-|/U_j=(3^{t_j}w_j)^{-1}\le 1/Y_j .
\]
The true relative correction \((W_j^++W_j^-)/U_j=(2^{b_j}-1)/(3^{t_j}w_j)\) lies strictly between zero and one. Consequently \(U_j\le2^r W_*\). The sum of *all* negative absolute values is then less than \(W_*\), so no subset including the root can vanish either.

Apply Evertse (13)–(14) to the \(2r+1\) integral signed coordinates at the three places \(S=\{\infty,2,3\}\) and with dyadic subset. All correction coordinates are \(S\)-units; the root's three-place product is at most \(w_0\). The maximum dyadic absolute value is one, and the dyadic norm of the total is exactly \(2^{-(T+B-t_0+t_r)}\). Therefore
\[
                2^{T+B+t_r}\le C_{r,\delta}Y_0\max_i|W_i|^\delta .
\]
Each \(|W_i|\) is bounded by \(Y_0^{O_r(1)}\), since \(2^{T+B}\), \(3^T\) and \(Y_r\) have such bounds by the elementary height estimate in D. Take \(\delta\) sufficiently small to achieve exponent \(1+\epsilon\).

For a general path cut at the first input boundary below or equal to the fixed threshold. The initial segment satisfies the argument above, with a constant maximized over lengths at most \(r\); if empty its duration is zero. The suffix starts at a bounded ordinary value and lasts at most \(r\) complete blocks, giving bounded total clocks and terminal valuation. This proves \(T+B+t_r\le(1+\epsilon)\log_2Y_0+C'_{r,\epsilon}\) without an unverified zero subsum. [Paper 147 v1, Proposition 1 and Appendix A](https://rstation.ai/problems/collatz/papers/147/v1) · [Evertse, Theorem 2](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

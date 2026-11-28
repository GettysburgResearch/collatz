# Conditional coding entropy at the critical integer trace

Use the actual tilted law, least odd representative and variable \(X_j\) from the [representative theorem](TILTED_ORDINARY_REPRESENTATIVE.md). Weaver's Theorem 5 bounds the entropy of the full iid gap word conditioned on its ternary residue, uniformly in depth. This conditional entropy also stays bounded **after weighting by the actual ordinary observable**, regardless of whether its size-biased entropy \(K_j\) grows linearly. [Weaver, Paper 9/v2, Theorem 5 and Corollary 6](https://rstation.ai/problems/collatz/papers/9)

Let \(w\) have total \(s\). Its original probability is \(p_w=3^j4^{-s}\). Its residue has one least positive odd representative \(y\). Peeling its inverse word at this actual \(y\) gives one positive odd source \(x\) with \(U^j x=y\). Conversely the set of \(x\) with \(U^j x\) in the representative range parametrizes the words bijectively: a word determines its residue, the representative, and then \(x\). Under multiplication by \(X_j\) the joint subfinite weights on these words and their residues are exactly
\[
   q_x=X_jp_w=f_j(x)^2/x^2,\qquad
   Q_y=\sum_{U^j x=y}q_x=\sigma_j(y)X_j(y).
\]
Here \(f_j\) is the genuine reciprocal correction. Conditional on a given \(y\) both before and after reweighting, the word probability is \(q_x/Q_y\). Thus the weighted conditional entropy is
\[
     \sum_y Q_y H(w\mid y)=\sum_x q_x\log(Q_y/q_x)
       \le \sum_x q_x\log(C/q_x)=O(1) ,
\]
using \(Q_y\le C=\sum_{x\ {\rm odd}}x^{-2}\) and \(0<q_x\le x^{-2}\). Enlarge \(C\) to at least \(e\) for monotonicity in \(q_x\), and use \(\sum_x x^{-2}\log(2x)<\infty\). Indeed even \(-\sum_xq_x\log q_x\) is bounded. The gap-word entropy budget stays bounded when the nonnormalized L1 mass survives. By contrast the signed size-biased marginal entropy is
\[
 \mathbb E[X_j\log X_j]
      =\sum_x q_x\log(q_x/p_w)
      =\sum_x q_x(2s\log2-j\log3)+O(1).
\]
Normalizing the joint measure by \(Z_j=\mathbb E X_j>0\), its relative entropy to the iid law is \(\mathbb E[X_j\log X_j]/Z_j-\log Z_j\), exactly the relative entropy of the two residue marginals. This calculation identifies where linear relative entropy would occur. Conditional word recovery does not bound the changed marginal.

## An actual signed cycle with the same ternary law

There is a concrete test of any proposed inference based only on ternary decoding, affine-translate singularity, subcritical moment decay and a bounded first moment. Retain **the same stationary law \(\sigma\)**. Let \(-b_j\) be its least-in-magnitude negative odd representative, \(-1,-3,\ldots,-(2\cdot3^j-1)\), and put
\[
                  N_j=(4/3)^j/b_j^2.
\]
The normalization divides the negative squared-Jacobian trace by \((9/4)^j\), exactly its known \(-1\) fixed-point growth. It changes both the real representative and the normalization from the positive problem.

An integral inverse step at a negative odd integer is again negative odd. For \(t>0\) odd write \(u_i=|U^i(-t)|\), so \(u_{i+1}\) is the odd part of \(3u_i-1\). The same finite word identity gives
\[
 \mathbb E N_j=\sum_{\substack{t>0\ {\rm odd}\\u_j\le2\cdot3^j-1}}
       \frac1{t^2}\prod_{i<j}\left(\frac{2u_i}{3u_i-1}\right)^2 .
\]
Each fixed \(t\) eventually meets the representative restriction, since \(u_j\le(3/2)^j t\). Factors before squaring equal one at \(u_i=1\) and are at most \(3/4\) at \(u_i\ge3\). Dominated convergence identifies the limit \(L_-\) as the corresponding sum over the basin of the true negative fixed point \(-1\). Its own source gives \(L_-\ge1\), and \(L_-\le\pi^2/8\). All its surviving sources have \(u_j=1\) eventually. A second dominated convergence then gives
\[
        \lim_j j^{-1}\mathbb E[N_j\log^+N_j]=L_-\log(4/3)>0 .
\]

Nevertheless all fractional moments of \(N_j\) decay exponentially. At any residue \(z\) the first inverse congruence allows at most one parity of the gap. Under \(3/4^e\) the heavier parity has total \(4/5\), so by recursion \(\sup_z\sigma(z+3^j\mathbb Z_3)\le(4/5)^j\). Fix \(\tfrac12\log(4/3)<b<\log(5/4)\). The event \(b_j\le e^{bj}\) has probability at most \(O(e^{bj}(4/5)^j)\). Outside it \(N_j\le\exp((\log(4/3)-2b)j)\). For any \(0<u<1\) use Hölder on the event with the uniform first-moment bound, and the displayed pointwise upper outside. The same word parametrization as above has joint weights bounded by \(t^{-2}\), so the genuine \(N_j\)-weighted conditional coding entropy stays bounded as well. All properties of \(\sigma\) and its fixed translates are identical in this test. The positive proof must use the positive real dynamics beyond these stationary and entropy conclusions.

# Recovering an ordinary source across finitely many missing intervals

**Written theorem using the integral fixed-place Subspace Theorem.** Fix \(g\ge1\), \(\eta,\epsilon>0\), and \(C\ge1\). Consider two length-\(K\) chronological shortcut words from ordinary integer sources \(x,\widetilde x\). Suppose that for every interval of length \(t\) in either word with \(a\) odd inputs, \(C^{-1}2^t\le3^a\le C2^t\). The words agree outside at most \(g\) disjoint intervals \([u_i,u_i+t_i)\), and each paired missing interval contains the same number of odd inputs in the two words. Between any successive missing intervals there are at least \(\eta K\) known bits. Put
\[
 A=K-\sum_i t_i,\qquad D=|x-\widetilde x|.
\]
For all sufficiently large \(K\), there is no such pair satisfying
\[
 D>0,\qquad \log_2D\le A-\epsilon K,\qquad D\ge 2^{\eta K}. \tag{1}
\]
The lower bound on \(D\) is automatic if the words share an initial string of at least \(\eta K\) bits. More generally it suffices that \(D/K\) tends to infinity along a proposed infinite family. No final matching string is required. The threshold is ineffective and the number of missing intervals is fixed.

This applies to the true bounded-cycle windows of length \(K\asymp\log s\). Their rank mask gives an absolute bounded clock discrepancy at all subintervals, since \(K(\lambda-\log_2 3)=o(1)\). Distinct actual odd phases have spacing \(\gg s/p\). Indeed \(\log(x/s)\) differs by \(O(p/s)\) from \((k+r/p)\log2\), with integer band \(k\) and distinct ranks \(r\), while the proposed branch has \(p^2/s=o(1)\). Thus in the bounded branch the weaker growth condition \(D/K\to\infty\) holds even when the first missing block starts at zero. The hypothesis about the number of matched bits still applies to each pair.

## Integral comparison

Let \(a\) denote the common total odd count. For each missing interval let \(a_i^+\) be the common cumulative count through its end. Write \(B_i\) for the signed difference of its two literal affine carries, using the same orientation as \(x-\widetilde x\). A shortcut word with odd positions \(j_1<\cdots<j_b\) has raw carry \(\sum_\ell 3^{b-\ell}2^{j_\ell}\). At fixed odd count and native duration this determines the complete word. Its least nonzero dyadic valuation gives \(j_1\). Subtract the first term and repeat. The empty support is unique. Delete the holes for which \(B_i=0\). This only increases known separation and the original value of \(A\) remains a valid lower bound on the agreement.

If no holes remain, the common word gives \(2^K\mid x-\widetilde x\), contradicting (1). Otherwise set
\[
 Z_0=3^a(x-\widetilde x),\qquad Z_i=2^{u_i}3^{a-a_i^+}B_i .
\]
Unrolling both words to their actual final states \(y,\widetilde y\) gives
\[
 Z_0+\sum_i Z_i=2^K(y-\widetilde y).
\]
The clock bound gives \(|B_i|\ll_C K 2^{t_i}\), hence \(|Z_i|\ll_C K2^K\), whereas \(|Z_0|\gg_C 2^KD\). For \(i>0\) the possible valuations are
\[
 u_i\le v_2(Z_i)\le u_i+t_i+O_C(\log K). \tag{2}
\]
The Lean module proves fixed-grade carry injectivity and unrolls any signed block sequence while retaining all the block multipliers and errors. [PuncturedWindows.lean](PuncturedWindows.lean)

Use the integral fixed-place Subspace Theorem with places \(\infty,2,3\). At infinity and at three use the coordinate forms. At two replace \(Z_0\) by the sum of all the coordinates. Each matrix of forms is nonsingular. Since the two final phases are integers, the product of the local absolute values is at most
\[
 \bigl|3^a(x-\widetilde x)\bigr|\prod_{i>0}
 2^{u_i}3^{a-a_i^+}|B_i|\;\cdot\;
 2^{-K-\sum_{i>0}u_i}\;3^{-a-\sum_{i>0}(a-a_i^+)}
 \ \le\ O_{C,g}(K^g)\,D\,2^{-A}.
\]
This is exponentially small by (1); the coordinate height is at most \(2^{O_{C,g}(K)}\). For each of the finitely many possible dimensions, the integer tuples lie in finitely many proper rational subspaces. The usual primitive-vector statement gives the stated integral consequence by dividing by the coordinate gcd: its product of absolute values at these places is at least one. [Schlickewei, *On linear forms with algebraic coefficients and diophantine equations*](https://www.sciencedirect.com/science/article/pii/0022314X77900737) · [Earlier two-coordinate separation, Lemma 4](https://rstation.ai/problems/collatz/papers/145/v1)

An infinite sequence consequently has a fixed nonzero integral relation among the \(Z_i\). Its \(Z_0\) coefficient is zero, since \(D/K\to\infty\) makes that term dominate at infinity. Among the remaining nonzero coefficients choose the earliest hole. By (2) its contribution has strictly lower dyadic valuation than every later contribution, even after multiplying by the fixed coefficients. Their sum cannot vanish. This proves the theorem.

For a family of balanced integer windows this gives recovery from a prescribed collection of retained blocks together with the clock counts in the gaps, when the hypotheses hold for every pair of distinct sources. Counting these patterns alone still costs the ordinary entropy of the retained symbols. The result does not require a periodic input and does not exclude a nontrivial cycle.

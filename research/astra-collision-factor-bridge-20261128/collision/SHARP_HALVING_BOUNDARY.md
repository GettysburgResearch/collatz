# Why the dyadic summability threshold cannot be weakened using halving alone

**PROPOSED, elementary construction.** There is an explicit computable binary function \(f\) on the positive integers such that
\[
 f(2n)=f(n)\quad\hbox{for every }n,\qquad
 d\{n:f(n)=1\}=\frac12,
\]
and
\[
 \#\{n\le X:f(n+1)\ne f(n)\}=O(X/\log X),\qquad
 \sum_{f(n+1)\ne f(n)}\frac1n=\infty.                                  \tag{1}
\]
Thus the summable-boundary implication in [the zero-one note](DYADIC_BOUNDARY_ZERO_ONE.md) has a genuine threshold: replacing its summability condition by the bound \(O(X/\log X)\), or merely by a zero boundary density, is false even with exact halving and an existing natural density.

This is **not** a Collatz-invariant label, a change to the Collatz map, or an ordinary counterexample. It isolates the part of the proposed full-proof route that cannot be obtained from halving and density alone. The actual odd equation must do additional work.

## The binary rule

For \(k\ge1\), set
\[
 a_k=\lceil\log_2(k+1)\rceil,\qquad
 b_k=\lceil\log_2(a_k+1)\rceil,\qquad
 \ell_k=a_k+b_k,\qquad J_k=\sum_{i=1}^k\ell_i.
\]
Partition the binary digits of a positive integer, **from its most significant digit**, into the successive blocks of lengths \(\ell_1,\ell_2,\ldots\). Ignore an incomplete final block. Let \(f(n)\) be the parity of the number of completed blocks consisting entirely of ones.

Multiplication by two appends a zero. No earlier completed block changes, and any newly completed block ends in zero and is not all ones. Hence \(f(2n)=f(n)\) exactly.

The probability that a late complete block is all ones, when its digits are fair, is
\[
 p_k=2^{-\ell_k}\asymp\frac1{k\log(k+1)}.                              \tag{2}
\]
In particular \(\sum_k p_k=\infty\), while \(p_k\to0\). The bounds follow directly from
\(k+1\le2^{a_k}<2(k+1)\) and
\(a_k+1\le2^{b_k}<2(a_k+1)\).

## Natural density on every cutoff

Fix any finite initial binary prefix, beginning with one. Uniform integers of a sufficiently large prescribed binary length having this prefix have independent fair digits beyond the prefix. All complete blocks beyond the finitely many that touch the prefix are therefore independent. If \(Z_k\) indicates an all-one block, then
\[
 \mathbb E\,(-1)^{\sum_{k=r}^K Z_k}
                =\prod_{k=r}^K(1-2p_k)\longrightarrow0.               \tag{3}
\]
The incomplete final block contributes nothing. Thus the conditional proportion with \(f=1\), on every fixed prefix cylinder, tends to one-half as the binary length tends to infinity. The first block, which includes the fixed leading one, is among the finitely many discarded blocks.

Finite unions of prefix cylinders approximate any interval of binary mantissas in \([1,2)\), with arbitrarily small uniform length error. It follows that the normalized count in every partial dyadic shell tends uniformly to one-half its relative length. Summing complete earlier shells geometrically gives natural density one-half at every integer cutoff, not just at powers of two.

## An exact boundary recurrence

For an arbitrary binary function satisfying exact halving, put
\[
 V_j=\sum_{n=2^j}^{2^{j+1}-1}|f(n+1)-f(n)|,\qquad
 E_j=\sum_{\substack{2^j\le n<2^{j+1}\\2\mid n}}|f(n+1)-f(n)|.
\]
For each \(m\), exact halving and the triangle inequality give
\[
 |f(2m+1)-f(2m)|+|f(2m+2)-f(2m+1)|
 \le |f(m+1)-f(m)|+2|f(2m+1)-f(2m)|.
\]
Summing over the complete paired shell yields
\[
                         V_j\le V_{j-1}+2E_j.                         \tag{4}
\]
There is also the exact three-color-free identity
\[
 |f(2m+1)-f(2m)|+|f(2m+2)-f(2m+1)|
 = |f(m+1)-f(m)|
       +2\mathbf1_{\{f(m)=f(m+1)\ne f(2m+1)\}}.                      \tag{5}
\]
It distinguishes inherited boundaries from a pair of new boundaries created inside a monochromatic parent interval.

For the constructed function, an even \(n\) and \(n+1\) differ only in their last binary digit. They have different labels exactly when this last digit completes a block and all preceding digits in that block are ones. Apart from the fixed first block,
\[
 E_j=\begin{cases}
        2^j p_k,& j+1=J_k,\quad k\ge2,\\
        0,& j+1\notin\{J_k:k\ge1\}.
       \end{cases}                                                     \tag{6}
\]
The initial first-block case is finite and harmless.

The lengths \(\ell_k\) are nondecreasing. Since \(b_k\le a_k\),
\[
 J_k p_k\le k\ell_k 2^{-\ell_k}
       \le\frac{2ka_k}{(k+1)(a_k+1)}\le2.
\]
Thus \(E_j/2^j\le2/(j+1)\) beyond the finite initial exception. Dividing (4) by \(2^j\), or convolving it with its geometric factor, gives
\(V_j/2^j=O(1/(j+1))\). Summing preceding dyadic shells proves the upper bound in (1).

Conversely \(V_j\ge E_j\). On a shell with \(j+1=J_k\), every summand has reciprocal weight at least \(2^{-j-1}\), so the total weighted boundary over that shell is at least \(p_k/2\). Summing these disjoint shells and using (2) proves the divergence in (1).

## What this does and does not reject

The construction rejects an attempted inference from exact halving, a proper natural density, and an \(O(X/\log X)\) boundary count to a zero-one law. It does not reject the genuine summability theorem, nor any argument that quantitatively uses \(f(2n+1)=f(3n+2)\) at every input.

For the actual Collatz basin label, the known generic pair-survival estimate is only \(O(X/\sqrt{\log X})\). Improving its constant, or improving that power up to and including one, would still not justify the dyadic proof. A successful argument must obtain an accumulated summable bound, or prove a stronger form of cancellation or compactness from the exact odd equation. The construction here makes that distinction mathematical rather than a matter of requested numerical precision.

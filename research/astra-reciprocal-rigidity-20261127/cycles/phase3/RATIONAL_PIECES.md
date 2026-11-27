# Rational paths and periodic pieces with small fixed points

This extends the integer-source argument in [SMALL_ANCHOR_WORDS.md](../../rigidity/phase4/SMALL_ANCHOR_WORDS.md) to the reduced denominator of a positive rational orbit. A finite positive shortcut path with common reduced denominator \(d\) prime to 6 uses the parity of its numerator at each step. Let its source and target be \(x,y>0\). Split its \(L\) steps into \(J\le K\) nonempty pieces, where \(K\) is fixed. The affine map of a piece of length \(l\) and weight \(q\) is \((3^q x+C)/2^l\). Write \(c=C/(2^l-3^q)\) for its rational fixed point, and use logarithmic height in lowest terms.

**Rational path bound.** Consider any sequence of these paths for which \(L\to\infty\), all piece fixed points have height \(o(L)\), and the orbit at each piece start differs from that piece's fixed point. Then
\[
 \liminf \frac{\log_2\max(1,x)+K\log_2 d}{L}\ \ge\ 1.             \tag{1}
\]
The source can exceed the target or vice versa. An equivalent uniform form has, for every fixed violation margin, a positive allowed coefficient in the height bound and a sufficiently large length threshold.

**Primitive cycle consequence.** For a sequence of positive primitive rational cycles of least length \(n\to\infty\), each decomposed into at most \(K\) nonempty **proper** pieces with rational fixed points of height \(o(n)\),
\[
 \liminf\frac{\log_2 d}{n}\ \ge\ \frac1K .                          \tag{2}
\]
In particular the pieces can be powers \(v_j^{m_j}\) of varying words with \(\max_j|v_j|=o(n)\). For \(K=2\) the bound is sharp even if \(u=\lfloor n\log_3 2\rfloor\) and \(2^n/3^u\to1\). The family and its exact integer divisor are in [ADJACENT_SWAPS.md](ADJACENT_SWAPS.md).

The rational path argument uses Schlickewei's rational \(S\)-adic Subspace Theorem with \(S=\{\infty,2,3\}\) and fixed rational forms. The cycle specialization additionally uses Rhin's two-logarithm lower bound. The conclusions are ineffective. See [Varjú, Theorem 5](https://arxiv.org/abs/2104.04367), [Schlickewei's paper](https://doi.org/10.1016/0022-314X(77)90073-7) and [Rozier–Terracol v5, Proposition 6.3, p. 19](https://arxiv.org/pdf/2502.00948v5#page=19).

Weaver 15, Theorem 9, already gives an effective height bound on the odd clock for positive rational paths covered by a changing periodic dictionary, with an absolute charge for the total dictionary division budget. Its Corollary 7 and adaptive inequality (C6) give a positive denominator exponent at fixed dictionary cost and sublinear budget. Proposition 8 (S1) records an exact two-piece boundary reset. The present statements use full binary clock length, give the sharp integer-source coefficient 1 and denominator coefficient \(1/K\), and apply to pieces specified by the heights of their rational fixed points. The example at \(K=2\) attains the denominator coefficient under primitivity. Weaver's quantitative estimates also apply with growing cost and have effective constants. [Weaver 15, Theorem 9, Corollary 7 and Proposition 8](https://rstation.ai/problems/collatz/papers/15)

## Reducing to interior boundaries

Write \(p_i\) for the step count at boundary \(i=0,\ldots,J\), \(r_i\) for its preceding odd count, and \(U_i=2^{p_i}3^{-r_i}\). Thus \(p_0=0,\ p_J=L\). Let \(X_i\) be the actual state at boundary \(i\), and \(c_i\) the fixed point of piece \(i\), from boundary \(i\) to \(i+1\). The exact affine equation gives
\[
 U_{i+1}X_{i+1}-U_iX_i=c_i(U_{i+1}-U_i).
\]
Merge adjacent endpoint terms to obtain
\[
 W=Z+\sum_{i=1}^{J-1} b_i,\qquad
 Z=x-c_0,\qquad W=U_J(y-c_{J-1}),\qquad b_i=(c_{i-1}-c_i)U_i.       \tag{3}
\]
The absence of fixed-point hits gives \(Z,W\ne0\), since a last piece returning to its own fixed point must also have started there by injectivity of its affine map. Each nonzero \(c_{i-1}-c_i\) has height \(o(L)\). Passing to a subsequence, keep a fixed \(J\) and omit the identically zero \(b_i\). For each remaining \(b_i\), the product of its absolute values over \(S\) is \(e^{o(L)}\), and the coefficient of \(U_i\) changes its logarithm at every individual place by \(o(L)\).

Suppose (1) fails by a fixed margin. At every selected \(L\), a common denominator \(B\) for \(Z\) and all \(b_i\) can be taken to be \(d\,3^L\prod_j\operatorname{den}(c_j)\). Its size is \(e^{O(L)}\), and \(\prod_{v\in S}|B|_v\le d\,e^{o(L)}\). Each coordinate times \(B\) has size \(e^{O(L)}\). The rational states \(x,y\) are integral at 2 and 3. Thus
\[
 |Z|_\infty\le\max(1,x)e^{o(L)},\quad |Z|_3\le e^{o(L)},\quad
 |W|_2\le 2^{-L}e^{o(L)}.                                           \tag{4}
\]

Choose a minimal rational linear subspace containing infinitely many tuples \((Z,b_1,\ldots,b_s)\), where \(s\le J-1\). Restrict to those tuples. A basis of the span of the \(b_i\) can be taken among the endpoint coordinates. If \(Z\) is independent of that basis, choose the basis together with \(Z\) as coordinates. Their number \(q\) is at most \(J\le K\). At infinity and 3 take coordinate forms. At 2 replace the \(Z\)-form by \(W=Z+\sum b_i\) expressed in the basis. The full product of sizes at the three places on the integer vector scaled by \(B\) is at most
\[
 \max(1,x)\,2^{-L}\,d^q e^{o(L)}\le e^{-\gamma L}
\]
for a fixed \(\gamma>0\) on the violating subsequence. The integer-vector norm is at most \(e^{O(L)}\). If \(q\ge2\), the Subspace Theorem confines this vector to finitely many proper rational subspaces, contradicting minimality. For \(q=1\), there are no nonzero \(b_i\), the integer \(BZ=BW\ne0\) has product of its sizes over \(S\) at least 1, and the same displayed exponential upper bound contradicts the product formula. Thus \(Z\), and also \(W\), belong to the fixed rational span of the \(b_i\).

## Recovering the exact physical return

For a fixed nonzero linear combination \(A\) of independent endpoint basis elements \(b_j\), the proof of §3 of the integer-source result gives, at each \(v\in S\),
\[
 \log |A|_v \ \ge\ \max_{j\ {\rm occurring}}\log|b_j|_v-o(L).
 \tag{5}
\]
For completeness, a failure by a fixed exponential factor lets us replace a maximizing coordinate form by \(A\) at that one place. The product of all coordinates over \(S\) is \(e^{o(L)}\). At this stage only endpoint coordinates are being cleared, so use \(3^L\prod\operatorname{den}(c_i)\), whose \(S\)-product is \(e^{o(L)}\), with no \(d\) cost. The Subspace Theorem again contradicts minimality; dimension one follows by proportionality. Applied to a dependent endpoint in its basis expansion, (5) and the product over \(S\) show comparability up to \(e^{o(L)}\) at all three places with every occurring basis coordinate. In particular, their \(p_i/L\) limits agree by their 2-adic valuations.

Extract convergent boundary-position fractions. Their distinct limits therefore define a direct-sum decomposition of the basis span. For a basis coordinate occurring in \(Z\), (4) and (5) at 3 give \(r_i=o(L)\). Applying (5) at infinity gives \(p_i\le\log_2\max(1,x)+o(L)\). The violated inequality implies that these position limits are at most \(1-\delta\) for a fixed \(\delta>0\). Every coordinate occurring in \(W\) has position limit 1, by (4) and (5) at 2.

Choose \(1-\delta<\alpha<1\) different from every boundary limit. Let piece \(j\) eventually be the unique one spanning \(\alpha L\). Project (3) to the summands below \(\alpha\). It gives the exact rational identity
\[
 0=Z+\sum_{1\le i\le j}(c_{i-1}-c_i)U_i
   =U_j(X_j-c_j).
\]
The second equality follows by telescoping the actual prefix. This is the excluded fixed-point hit. It proves (1).

## A small boundary state in every cycle of this class

A proper piece starting at its fixed point would return to that same rational state in fewer than \(n\) true steps. Primitivity excludes every such hit. To apply (1), cut at a boundary at which \(x\) is subexponential. Let \(X_*=\min_i X_i\), \(M=\max(1,|c_0|,\ldots,|c_{J-1}|)=e^{o(n)}\). If \(X_*\le2M\), the conclusion is immediate. Otherwise all \(X_i-c_j\) are positive, and the affine equations give
\[
 \prod_i\frac{X_{i+1}-c_i}{X_i-c_i}=\frac{3^u}{2^n}.
\]
Cancel the \(X_{i+1}/X_i\) factors around the cycle. Since \(|\log(1-z)|\le2|z|\) on \(|z|\le1/2\), the positive defect \(\Lambda=n\log2-u\log3\) satisfies \(\Lambda\le4JM/X_*\). Rhin's \(\Lambda\ge n^{-13.3}\) gives \(X_*\le4JMn^{13.3}=e^{o(n)}\). Cut at this boundary and (1) yields (2). A word power has the same fixed point as its underlying word; its numerator and denominator before reduction are bounded by \(3^{|v|}+2^{|v|}\). This proves the asserted power-block specialization.

For arbitrary fixed \(K\) presented periods can repeat a shorter rational orbit exactly. The proper-piece and primitive hypotheses in (2) preclude the exact returns which make such examples possible. Both (1) and (2) leave open trajectories and cycles whose piece fixed points have height proportional to the observation length.

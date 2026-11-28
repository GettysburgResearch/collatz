# Independent stopping dates after a long shared native block

Consider two positive odd Collatz paths over the same positive denominator \(q\) prime to six. Their integer numerators obey \(2^{a_i}y_{i+1}=3y_i+q\). Assume the starts are distinct and the first \(L\) native valuations agree. The two paths may come from different orbits. Stop track \(j\) after \(K_j\ge L\) steps, with positive terminal numerator \(X_j\) **prime to three**. Let \(S_{j,i}\) be its halving count up to date \(i\), let \(B_{j,i}=2^{S_{j,i}}/3^i\), and put
\[
 J=\max\bigl(\{0\}\cup\{\log_2(B_{j,i}/B_{j,L}): j=1,2,\ L\le i<K_j\}\bigr),\qquad \gamma=\log_2 3.
\]
Take a scale \(P\to\infty\). If both halving totals are \(O(P)\), the two initial numerators and \(q\) have logarithms \(O(P)\), and \(L\ge\delta P\) for fixed \(\delta>0\), then
\[
            J+\log_2 q+\log_2 X_1+\log_2 X_2\ \ge\ \gamma L-o(P).       \tag{1}
\]
The bound is uniform with the stated constants fixed. The two cores can use overlapping dates in one orbit, and their stopping lengths can be equal. In particular, no restriction is imposed on the division exponents at the final transitions. This is an independently stopped extension of [the common-cut block theorem](REPEATED_BLOCK_DRAWDOWN.md).

Write \(A_c=S_{1,L}=S_{2,L}\). The distinct source difference \(U\) is \(2^{A_c}G\) for a nonzero integer \(G\). Define \(V=B_{1,K_1}X_1\), \(W=B_{2,K_2}X_2\). The exact per-track identity \(B_{j,i}y_{j,i}=y_{j,0}+(q/3)\sum_{a<i}B_{j,a}\) gives
\[
 U-V+W=(q/3)\left(\sum_{a=L}^{K_2-1}B_{2,a}-\sum_{a=L}^{K_1-1}B_{1,a}\right).
\]
The finite-place product calculation of the common-cut theorem now gives an upper bound \((K_1+K_2)qX_1X_2\,2^J3^{-L}\) for the same three fixed-place forms. This uses \(B_{1,L}=B_{2,L}=2^{A_c}3^{-L}\). If (1) fails by a fixed linear margin, the product is exponentially small while the projective logarithmic height is \(O(P)\). The Subspace Theorem gives a fixed nonzero rational relation \(aU+bV+cW=0\) along a subsequence. One has \(v_3(U)\ge0\), \(v_3(V)=-K_1\), \(v_3(W)=-K_2\).

If \(a\ne0\) and \(|K_1-K_2|\to\infty\), the participating negative valuations cannot cancel: both \(K_j\ge L\) grow, and once both \(V,W\) participate their valuation difference grows too. If the length difference is bounded, extract \(k=K_1-K_2\) fixed. The cases \(bc=0\) are already impossible by the gap from zero. Otherwise put \(Z=2^{S_{2,K_2}-S_{1,K_1}} X_2\). Multiplying the relation by \(3^{K_1}2^{-S_{1,K_1}}\) yields
\[
                  v_3(bX_1+c3^kZ)\ge K_1-O(1).                         \tag{2}
\]
The linear form is nonzero because \(aU\ne0\). Apply the two-dimensional Subspace Theorem to \((X_1,Z)\), with the two forms \(bX_1+c3^kZ,X_1\) at three and the coordinate forms at two and infinity. Both coordinates are three-adic units. The product is \(O(X_1X_2\,3^{-K_1})\), exponentially small under the **same** failed (1), since \(J,\log_2 q\ge0\) and \(K_1\ge L\). The coordinates are \(S\)-integers of height \(\exp(O(P))\). A fixed rational line forces \(Z/X_1\) fixed. The left side of (2) is then a nonzero constant times the unit \(X_1\) and has fixed valuation, a contradiction. This argument permits either sign of \(S_{2,K_2}-S_{1,K_1}\) and does not require the endpoint heights individually to be subexponential.

If \(a=0\), then \(w=W/V\) is fixed and nonzero. Apply the theorem to \((U,V)\), with \(U-(1-w)V,V\) at infinity and the coordinate forms at two and three. The product bound only loses the factor \(X_2\) from the preceding estimate; its removal can only decrease the bound. This also works at \(w=1\). A fixed line contradicts \(v_3(U/V)\ge K_1\). These alternatives exhaust all exceptions and prove (1). [Classical fixed-place Subspace Theorem, Bilu, Theorem 2.3 and ensuing extension](https://www.numdam.org/item/AST_2008__317__1_0.pdf)

## Several independent ascents in an original integer cycle

Suppose a family of primitive positive **ordinary** cycles of odd period \(p\to\infty\) can each be cut at a fixed bounded number of odd dates. Assume the logarithm of every cut height is \(o(p)\), and within every piece the largest logarithmic drawdown between any two preterminal positions is \(o(p)\). The final halving into the next cut is excluded from that maximum separately on each piece. Then the longest repeated native valuation block between distinct cyclic starts is \(o(p)\). In particular every proper rotation has an unbounded number of valuation mismatches, uniformly in the choice of rotation.

To see this, align an alleged common interval of length at least \(\delta p\), taking at most one lap of each track. The finitely many cut positions in either copy split the alignment into boundedly many shorter intervals. One macroscopic common subblock lies in a single piece on each track. Trim a step if needed to keep its endpoint strictly preterminal. Follow each copy from its subblock start to its **own** next cut, independently. Both terminal numerators have logarithm \(o(p)\), both total halvings are at most \(A\le2p\), and all starting logs are \(O(p)\) by forward growth from a low cut. On ordinary cycles the harmonic bound from the common-cut theorem translates the physical drawdowns into \(J=o(p)\). Equation (1) contradicts the macroscopic common length. Fixed mismatch counts produce a macroscopic repeated block by counting the matched runs between discrepancies.

These ascending pieces are defined only at the exponential height scale. They can contain an unbounded number of ordinary local maxima, local minima, and nontrivial valuations. No fixed number of Steiner circuits or constant valuation stretches is assumed. As an example of a sufficient scheduling condition, let there be a bounded number of distinguished departures of any sizes, ending at cuts of subexponential height, while the total excess relative to valuation one over all other sites is \(o(p)\). Between distinguished departures, every internal forward drawdown is \(o(p)\), even if the number of nondistinguished exponents greater than one tends to infinity. The conclusion then excludes any macroscopic recurrent block. Applying only a global one-cut estimate would charge the other distinguished endings inside its tails.

For illustration on arbitrary finite distinct starts, take \(L\) shared transitions and let the two terminal steps immediately afterward be arbitrary, so \(K_1=K_2=L+1\). Then \(J=0\) and the two tails cancel exactly. Under the theorem's linear height bounds the **product of the two post-transition numerators** must be at least \(3^{L-o(P)}/q\), despite the arbitrary terminal division counts. Independent stops include much longer overlapping or disjoint continuations.

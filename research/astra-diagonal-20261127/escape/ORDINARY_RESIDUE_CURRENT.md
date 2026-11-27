# The ordinary residue-two current, including a boundary edge

Write \(T(2n)=n\), \(T(2n+1)=3n+2\) for the positive shortcut map, and take any bounded real sequence \(b\) on positive integers with \(b(2n)=b(n)\). Set \(H_b(X)=\sum_{n\le X}b(n)/n\) and
\[
 J_2(b;X)=\sum_{n\le X}\frac{b(n)}n(\mathbf1_{n\equiv2\ (3)}-1/3).
\]
At every integer \(N\ge1\) the exact physical-cutoff relation is
\[
 J_2(b;3N)+\frac23\sum_{n\le2N,\ n\ {\rm odd}}
 \frac{b(n)}{n(3n+1)}+\sum_{n\le2N,\ n\ {\rm odd}}
 \frac{2[b(n)-b(Tn)]}{3n+1}
 =\frac{2H_b(2N)-H_b(N)-H_b(3N)}3.                    \tag{1}
\]
For each \(m=3k+2\le 3N\) put \(n=2k+1\). The three corresponding uncentered summands on the left add to \(2b(n)/(3n)\). Removing even terms from \(H_b(2N)\) gives (1). The [Lean proof](OrdinaryCurrent.lean) checks the three exact rational summands, the even filtration, and the full identity. The [build receipt](../../../reports/astra-diagonal-20261127/escape/ordinary_current_lean.txt) records four declarations.

If \(b\) has ordinary mean \(d\), partial summation on each fixed-ratio annulus gives \(H_b(cX)-H_b(X)\to d\log c\). Consequently the right side of (1) tends to \(d\log(4/3)/3\), without a claim about convergence of \(H_b(X)-d\log X\). Taking \(b=\mathbf1_B\) for any complete union of basins of density \(d\), the current converges and
\[
 J_2(B)=\frac23\left[\frac{\log(4/3)}2d-
 \sum_{n\in B,\ n\ {\rm odd}}\frac1{n(3n+1)}\right].    \tag{2}
\]
The two remaining endpoints between multiples of three affect the limit by \(O(1/N)\). If the smallest odd source is \(m\), the [ordinary counting comparison](DENSITY_AND_SQUARE_MASS.md) makes the displayed sum \(O(d/m)\) with an absolute constant. The sign at a specified finite \(m\) requires the constant. The equality on \(B\) is a direct critical first-moment test in one residue.

## Tests involving finer ternary residue classes

For invariant \(b\) let \(A_{q,r}(M)=\sum_{m\le M,\ m\equiv r\ (q)} b(m)/m\). At \(q=3^k\), \(k\ge1\), take \(r\equiv2\bmod3\), \(p=(2r-1)/3\bmod q/3\) and \(X=(2M-1)/3\). The same exact change of variables gives
\[
 A_{q,r}(M)+\sum_{\substack{m\le M\\m\equiv r\ (q)}}\frac{b(m)}{m(2m-1)}
 =\frac23 A_{q/3,p}(X)-\frac13 A_{q/3,p/2}(X/2).         \tag{3}
\]
Here \(p/2\) is computed modulo \(q/3\), including the single class at \(q=3\). Indeed \(n=(2m-1)/3\) runs through exactly the odd positive \(n\equiv p\bmod q/3\) up to \(X\). The rational kernel on the left combines to \(2b(m)/(2m-1)\). The right side removes even \(n\) exactly. This identity prescribes a combination of currents at linked physical cutoffs. It supplies no limit for every isolated centered harmonic class of an arbitrary invariant label.

One can also count all contrasts of the form \((I-\mathcal A)u\) arising from finite ternary potentials, with
\[
 (\mathcal A u)(y)=\tfrac12u(2y)+\tfrac32\mathbf1_{y\equiv2\ (3)}u((2y-1)/3).
\]
Haar integration is preserved. If a nonconstant \(u\) has exact ternary period \(3^m\), then \((I-\mathcal A)u\) has exact period \(3^{m+1}\): replacing \(y\equiv2\bmod3\) by \(y+3^m\) shifts only the last argument by \(2\cdot3^{m-1}\). Invariance under this shift for all such \(y\) would contradict the exact period. A nonzero constant has nonzero image of exact period three. Thus the contrasts at depth at most \(k\) in this finite-potential image have dimension exactly \(3^{k-1}\) among the \(3^k-1\) Haar-centered contrasts. This dimension counts the specified coboundaries. It does not bound other available relations from a different operator or from nonperiodic potentials.

## Testing a proposed sign bound on genuine one-edge defects

Take a positive nonperiodic odd unit \(a\) in the tree of 1, and \(B_a\) its full ordinary predecessor set. The only edge with different labels is the odd outgoing edge at \(a\). Formula (1) therefore gives
\[
 J_2(B_a)=\tfrac23\left[\frac{\log(4/3)}2 d_a-
 \sum_{n\in B_a,\ n\ {\rm odd}}\frac1{n(3n+1)}-\frac3{3a+1}\right]. \tag{4}
\]
For each prescribed \(D>0\) there are arbitrarily large such \(a\) with \(a d_a\asymp_D (\log a)^D\), by Weaver 202, Corollary 2 with target 1. The least odd ancestor \(m(a)\) tends to infinity along this sequence. Any bounded source which enters one of these \(a\) then visits 1 and has only finitely many distinct future states. The uniform finite-union comparison of Weaver 12, Theorem 17, applies directly to the single predecessor basin \(B_a\), so its odd count below \(R\) is \(O(d_aR)\). Layer cake starting at \(m(a)\) makes the sum in (4) \(O(d_a/m(a))\). Consequently
\[
             J_2(B_a)/d_a\longrightarrow\log(4/3)/3.
\]
In particular no upper inequality for all even-invariant labels vanishing at 1 can bound this current by a sum of nonnegative local edge costs, if on an isolated odd defective edge at \(a\) its charge is at most \(O((\log a)^K/a)\) for any fixed \(K\). Take \(D>K\) and apply (4). The construction uses the original \(+1\) dynamics and actual natural predecessor densities. Exactly invariant labels have zero defect. The result identifies what an extension to nearly invariant labels would have to distinguish. [Weaver, *How little a Collatz predecessor set can gain at its first odd doubling*, Corollary 2](https://rstation.ai/problems/collatz/papers/202) · [Weaver, *First-landing bounds and canonical inverse laws for Collatz*, Theorem 17](https://rstation.ai/problems/collatz/papers/12).

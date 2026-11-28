# Diophantine spacing and source-window discrepancy for native affine intercepts

**Proposed written results.** Write \(Q=2^t\), \(A=3^s/Q\), \(0\le s\le t\). Let \(I\) be an interval of \(N\le Q\) consecutive ordinary integers, \(J\) a circle arc of length \(w\), and \(z\) any real translate. For every \(\epsilon>0\), uniformly in these data,
\[
 \left|\#\{n\in I:An+z\bmod1\in J\}-Nw\right|
       \ll_\epsilon e^{\epsilon t}+\mathbf1_{A<1/2}\,w/A .             \tag{1}
\]
The constant is ineffective. In particular the permutation \(n\mapsto3^s n\bmod 2^t\) has absolute rectangle discrepancy \(e^{o(t)}\) for grades with \(A\ge e^{-o(t)}\). At a shrinking slope the explicit width factor multiplying \(1/A\) matters.

The arithmetic engine is the classical restricted-approximation argument for rational powers. Corvaja and Zannier explicitly give Pourchet's antecedent for \((a/b)^n\) and its subexponential partial-quotient bound on p. 738. PR215's phase-two matched-intercept note states the two-dimensional two-cofactor inequality, which also directly implies the estimate below when the approximating numerator is nonzero. The applications here use independently varying shortcut odd and total clocks, the exact shrinking-slope remainder, and the actual intercept of the word that the ordinary spatial source selects. [Corvaja–Zannier, JTNB 17 (2005), pp. 738, 740](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.517.pdf) · [PR215, equation (3)](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase2/MATCHED_INTERCEPT_AND_SMOOTH_PARTS.md)

## The varying-clock lower bound

For each \(\eta>0\) and all sufficiently large \(t\), if \(1\le h<Q\) and the nearest integer \(k\) to \(hA\) is nonzero, then
\[
                              h\|hA\|>e^{-\eta t}.                     \tag{2}
\]
Either choice at a tie suffices. To prove this suppose the reverse inequality holds and put \(U=h3^s, V=k2^t\). At the infinite place take the forms \(U-V,U\), and at two and three take the coordinate forms. Their product is at most \(h\|hA\|\): the factors \(2^t\) and \(3^s\) from the two real forms cancel against the indicated finite valuations. The vector height is at most \(C6^t\). The integral-vector formulation of the Subspace Theorem therefore puts all sufficiently late exceptions on finitely many proper rational lines. On each possible line \(U/V=c\ne1\) the distance \(|hA-k|=|c-1||k|\) is bounded away from zero. The line \(U=V\) cannot occur because \(2^t\nmid h3^s\). This proves (2). At a zero nearest integer the exact product is \(h^2A\). In particular (2), with an arbitrarily small loss in its exponent, holds uniformly for *all* \(h<Q\) on any family with \(A\ge e^{-o(t)}\). [Schlickewei's Subspace Theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Integral-vector version on p. 740](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.517.pdf)

For a word with these counts, \(F_w(n)=An+C_w/Q\). Two exponentially accurate integral endpoints at distinct ordinary sources less than \(Q\) apart require
\[
               |n-n'|\,2e^{-\sigma t}\ge e^{-o(t)}
\]
if \(A\ge e^{-o(t)}\). This is a single-word source gap of size \(e^{(\sigma-o(1))t}\). The restriction modulo the full true-source period \(Q\) is needed.

## Rectangle count, including the first continued-fraction digit

Let \(\beta=\{A\}\in(0,1)\), and let \(p_j/q_j\) be its standard continued-fraction convergents, beginning with \(0/1\) and ending with denominator \(Q\). Use the finite expansion with last partial quotient at least two. For \(1\le j\) before the final denominator, \(p_j\ge1\) and \(q_j A\ge1/2\), with a nonzero nearest integer available. Indeed if \(A<1/2\), then \(q_j\ge q_1=\lfloor1/A\rfloor\). Equation (2) and the standard convergent bound give
\[
                   e^{-o(t)}\le q_j\|q_j A\|
                       \le q_j|q_j\beta-p_j|\le q_j/q_{j+1}.
\]
Thus every ratio after the first denominator is \(e^{o(t)}\), uniformly. When \(A\ge1/2\), also \(q_1\le e^{o(t)}\), since a small fractional part at \(h=1\) must then have a nonzero nearest integer. There are \(O(t)\) convergents by the elementary Fibonacci growth of alternate denominators.

A block of \(q_j\) consecutive points of the rotation, starting anywhere, differs pointwise by at most \(1/q_j\) from a translated regular \(q_j\)-grid, by comparison with \(p_j/q_j\). Its unnormalized arc-count error is at most an absolute constant, including arcs that cross zero. Full denominator blocks are regular grids exactly. Greedily decompose \(N\le Q\) from the largest denominator down through \(q_1\). Above the remainder there are \(e^{o(t)}\) blocks in total since each multiplicity is bounded by the next denominator ratio rounded up. If \(A\ge1/2\), the remaining fewer than \(q_1\) individual points incur only \(e^{o(t)}\) more error.

If \(A<1/2\), the remainder has length \(r<q_1\le1/A\). These successive points traverse less than one turn with mesh \(A\). Their count in any translated arc is at most \(w/A+2\) (the arc can have two pieces in the traversed interval). The expected count \(rw\) is between zero and \(w/A\). This gives the remaining error in (1), including when \(s=0\) and the fraction has just one nonzero continued-fraction digit.

For \(0<\sigma<\log2\) and \(A\ge e^{-o(t)}\), (1) implies matching source coverage on the exponential scale: every interval of \(\lceil e^{(\sigma+\delta)t}\rceil\) ordinary starts contains some input whose affine endpoint is within \(e^{-\sigma t}\) of an integer, for each \(0<\delta<\log2-\sigma\) and all sufficiently large \(t\). This chooses a potentially different start for every supplied word and horizon.

## A genuine ordinary-source conclusion with no sum over words

Sample the true shortcut map at **its own** source \(n\in[X,2X)\). For its first \(t\) letters write \(s(n)\) for the odd count, \(K(n)\) for the integral affine intercept, and \(A_s=3^s/2^t\). Thus \(2^tT^t n=3^{s(n)}n+K(n)\). Fix arbitrary arcs \(J_s\) of lengths \(w_s\), free to depend on the clock and source octave, and a floor \(c>0\). At any post-binary clock \(\log_2(2X)\le t\le C\log X\), the proportion of native sources satisfying both
\[
               n A_{s(n)}\ge c,\qquad K(n)/2^t\bmod1\in J_{s(n)}
\]
is at most
\[
        \sum_{s=0}^t w_s+ O_c(\max_s w_s)+ X^{-1+o_C(1)}.             \tag{3}
\]
All errors are uniform in the arcs. The same conclusion holds if the arcs and floor are tested only on a further selected subset of the original octave, with the proportion measured against the whole octave. Finite unions of arcs follow by summing the corresponding individual errors.

Indeed \(K(n)/2^t\equiv -A_{s(n)}n\pmod1\) by physical integrality. For each grade drop the requirement that \(n\) chose the grade and apply (1) on the original source interval to its own arc. Only grades with \(A_s\ge c/(2X)\) are eligible. Since \(A_s\) grows geometrically in \(s\), the sum of \(w_s/A_s\) on these grades is \(O(X\max_s w_s/c)\). There are at most \(t+1\) discrepancy errors, giving \(X^{o_C(1)}\) before normalization. This uses no independence between actual source and actual word and costs no factor \(2^t\) or \(\binom ts\).

A fixed absolute \(c>0\) works for every *simple* positive segment (distinct starting states of its steps). The ratio \(T^tn/(nA_{s(n)})\) is a product of \(1+1/(3y)\) at its odd sources. Uniform reciprocal packing bounds this ratio by an absolute constant. For a short proof, in any finite simple segment let \(V(H)\) count its states through \(H\). Discard its final \(k=\lfloor\log_2H\rfloor\) indices. Each remaining state \(y\le H\) with at most \(3k/5\) ones on the next \(k\) steps maps below \(H/2\) for all large \(H\), since its image is at most \(H(3^{3/5}/2)^k+(3/2)^k\). These images are distinct within the segment. The other words number at most \(2^{k H_2(3/5)}\), with \(H_2\) binary entropy, and each word selects at most two starts through \(H\) by the parity-cylinder bijection. Thus \(V(H)\le V(H/2)+O(H^{H_2(3/5)}+\log H)\); dyadic summation gives a uniform bound on the sum of reciprocals. If the very last endpoint repeats, omit that endpoint from this counting argument and discard one additional index. Finally \(T^t n\ge1\) gives the homogeneous floor. This is the established simple-orbit packing mechanism. [Weaver, paper 180, finite sparsity bound and proof](https://rstation.ai/problems/collatz/papers/180/v1)

For example, at any fixed multiple beyond the binary horizon, the true intercept modulo one on simple segments lies within \(X^{-\delta}\) of a prescribed per-grade phase at only \(X^{1-\delta+o(1)}+X^{o(1)}\) sources. One may also sum over all clocks in the displayed logarithmic range at no exponential cost. At a *supplied terminal integer* \(y\), simplicity and the same bounded product give \(y/C_0\le n A_s\le y\) for an absolute \(C_0\). Only \(O(1)\) grades are now possible on the octave. For a specified interval of width \(w\) at each such grade, the proportion is \(O(w(1+1/y))+X^{-1+o_C(1)}\), uniform in the moving target. This bounds the joint event before conditioning on landing at \(y\).

These estimates constrain the **fractional affine intercept**, which discards its integer part. The terminal residue modulo \(3^s\), the mass of a fixed canonical predecessor tree and the demand that an orbit hit a smaller integer are additional arithmetic data. In particular no assertion that escaping mass must concentrate in the small arcs of (3) follows from canonical fixed-root nonatomicity, nor from the compact-null support for full correction products after multiplication by an unbounded terminal height. The number of grade-dependent arcs and their widths must be charged.

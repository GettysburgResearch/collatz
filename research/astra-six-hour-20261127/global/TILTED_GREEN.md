# A summable ternary Green function with actual ordinary-point tests

**PROPOSED.** Use the original odd map \(U(x)=(3x+1)/2^{e(x)}\) on positive odd integers. This test uses a deliberately changed word weight. It does not identify that weight with the original-law Dirichlet trace. Both nontrivial positive cycles and positive escape would produce specified failures of one ordinary restriction of the function.

For \(s=3/2\), \(t=25/24\), write \(F_e(z)=(3z+1)/2^e\) on \(\mathbb Z_3\). For a chronological gap word \(w=(e_1,\ldots,e_k)\) let \(A=\sum e_i\), \(F_w=F_{e_k}\circ\cdots\circ F_{e_1}\) and \(B_w=F_w(0)+3^k\mathbb Z_3\). Define
\[
 G(y)=\sum_{k\ge0}\sum_{|w|=k} t^k (3^k/2^A)^s\boldsymbol1_{B_w}(y).
                                                                    \tag{1}
\]
The depth-zero summand is one. The function is lower semicontinuous, taking values in \([1,\infty]\). Haar integration gives exactly
\[
 \int_{\mathbb Z_3}G(y)\,dy
    =\frac1{1-t\lambda_s},\qquad
 \lambda_s=\frac{3^{s-1}}{2^s-1},\qquad t\lambda_s<1 .                \tag{2}
\]
Indeed each ball has Haar mass \(3^{-k}\). Here \(t\sqrt3< 2\sqrt2-1\), for example by squaring and using \(\sqrt2<99/70\). This concerns an integrated geometric series; it gives no pointwise upper bound at an ordinary integer. The total-gain tilts and the exponent-two ordinary reciprocal identity are present in [Weaver, Paper 176](https://rstation.ai/problems/collatz/papers/176). The extra time multiplier in (1) changes the ordinary thresholds.

On a positive odd integer \(y\), every legal inverse word ends at the actual positive odd integer \(x=F_w^{-1}(y)\), and its successive transitions are its genuine forward gaps. Indeed at each inverse edge the integer \((2^e y-1)/3\), when integral, is odd and positive. Integrality of the full inverse is equivalent to \(y\in B_w\), since the intermediate ternary divisions follow by reduction. With \(f_k(x)=\prod_{i<k}3U^ix/(3U^ix+1)\),
\[
 \frac{G(y)}{y^s}=
   \sum_{k\ge0}\sum_{U^k x=y}t^k\left(\frac{f_k(x)}{x}\right)^s.     \tag{3}
\]
All sums here are positive, including returns on periodic laps.

* For any positive integer cycle whose minimum odd phase is at least 13, the product of the per-edge lower factors \(t[3x/(3x+1)]^s\) grows geometrically over laps. In fact \(t^2(39/40)^3>1\). Repeating the genuine cycle word in (3) gives \(G(y)=\infty\) at **every phase**. Direct calculation for the odd starts \(1,3,5,7,9,11\) shows that they reach 1, so this covers every candidate additional cycle. The cycle of 1 has per-edge factor \(t(3/4)^s<1\).
* If a positive odd \(x\) escapes, its forward states \(y_j=U^jx\) are distinct and tend to infinity. The simple-path reciprocal bound gives \(f_\infty(x)>0\). Keeping just its original word in (3) gives \(G(y_j)\ge c_x t^j y_j^s\), where \(c_x=(f_\infty(x)/x)^s>0\). Since \(y_j+1\le(3/2)^j(x+1)\), put \(\eta=\log(25/24)/\log(3/2)>0\). Then \(G(y_j)\ge c'_x y_j^{s+\eta}\) at **every depth**. [Uniform simple-path packing](../../astra-multiple-attacks-20261125/synthesis/README.md)

Consequently finiteness at ordinary positive odd integers together with \(G(y)=o(y^{s+\eta})\) along them would settle both obligations. This is a sufficient estimate. Slow terminating inverse histories can affect a time-exponentially tilted Green function even if all orbits terminate. No equivalence with termination is assumed.

## Dense infinite values at positive real, nonintegral dyadic centers

The test has explicit singularities. At \(-1\in\mathbb Z_3\), each all-one word is legal and its summand is \([t(3/2)^s]^k\). Hence \(G(-1)=\infty\). Appending any final letter gives
\[
     G(F_e z)\ge t(3/2^e)^s G(z).
\]
The infinite-value set therefore contains all forward images of \(-1\) under the displayed affine branches with arbitrary exponents. The first letter \(e\ge2\) sends \(-1\) to \(-2^{1-e}\). In lowest terms this has an even denominator; every subsequent numerator is odd and the denominator is multiplied by the next \(2^e\). Thus the only ordinary integer in this explicitly generated set is \(-1\). These arbitrary branches describe singularities of (1) on \(\mathbb Z_3\), not the actual signed odd map of a negative integer after its gap is changed.

Even **one fixed exit from \(-1\)** gives a dense set of infinite values in the product \(\mathbb R_{>0}\times\mathbb Z_3^\times\), by diagonally embedding the dyadic rational centers. Indeed take the exit \(e=2\) to \(-1/2\), then \(h\) exponents one, then an exponent \(d\). The final dyadic rational is
\[
       r_{h,d}=2^{-d}\bigl[(3/2)^{h+1}-2\bigr].
\]
For \(h+1\ge m\), its ternary residue modulo \(3^m\) is \(-2^{1-d}\). Prescribe \(d\) in one class modulo \(2\cdot3^{m-1}\) to obtain any desired ternary unit. Along \(h\to\infty\) the irrational rotation by \(\log_2(3/2)\) modulo this integer period lets one choose such positive \(d\to\infty\) with \((h+1)\log_2(3/2)-d\) arbitrarily close to any prescribed real logarithm. The error \(2^{1-d}\) tends to zero. In particular \(G=\infty\) on a dense subset of ternary units; lower semicontinuity makes the full infinite-value set dense \(G_\delta\) there, while (2) gives it Haar measure zero. A local real/ternary upper envelope is therefore impossible. The required estimates concern the diagonal of actual positive odd integers, on which none of these displaced centers lands.

## Arithmetic cost of shadowing a specified negative center

There is a compensating physical cost when an actual positive source shares an **initial** block with a specified negative odd rational \(r=-a/b\), \(a,b>0\) odd. If their first \(m\) true gaps coincide and have total clock \(L\), then \(2^{L+1}\mid bx+a\). This is the odd-cylinder bijection for a complete gap word, valid over odd denominators. Hence \(x\ge (2^{L+1}-a)/b\). For \(2^L\ge a\), this gives \(x\ge2^L/b\) in ordinary size. For \(-1\) it gives the exact familiar requirement \(2^m\mid x+1\) for \(m\) initial one gaps; the complete odd-gap endpoint additionally fixes the next odd bit and gives \(2^{m+1}\mid x+1\) when the reference is \(-1\).

In particular, at any one target and any terminal word with such a matched initial block, the source's summand on the right of (3) is at most \(b^s t^k 2^{-sL}\) when \(2^L\ge a\). A long fixed negative shadow followed by a short displacement cannot by itself supply the floor of a fixed positive escaping source. The bound does not sum arbitrary displacement words or enforce a long negative shadow on an aperiodic positive trajectory. The ordinary majorant in (3) remains open.

### Summing all later displacements on the ordinary grid

The source payment above controls the entire suffix without counting its words. Let a fixed negative odd rational \(-a/b\) have a specified initial true gap block of total clock \(L\), with \(a\le2^L\). Every positive source sharing it satisfies \(bx+a=2^{L+1}m\) with \(m\ge1\). Since \(2^{L+1}m-a\ge2^L m\), the positive sources in this cylinder obey
\[
        \sum_x x^{-s}\le b^s 2^{-sL}\zeta(s).
\]
For any total odd depth \(k\) containing that initial block, the source maps to just one actual terminal integer. Consequently the sum **over all positive odd targets** of the matched contribution to \(G_k(y)/y^s\), including every possible subsequent displacement, is at most \(\zeta(s)b^st^k2^{-sL}\). The normalized contributions over all depths are summable when \(L\ge ck\) and \(c>\log t/(s\log2)\). For a depth-dependent collection of references the same estimate uses the sum of \(b^s2^{-sL}\) over the collection. In particular all negative odd references with numerator and denominator at most \(H_k\le2^{ck}\) cost at most \(\zeta(s)t^k H_k^{s+2}2^{-sck}\) if each matching event first reaches a complete gap clock at least \(ck\). A fixed reference with an undefined later gap supplies only its actually defined block.

There is also a source-height payment for an interior shadow. If a reference of denominator \(b\) and numerator at most \(2^L\) matches at \(z=U^i x\), then
\[
        x+1\ge (2/3)^i (z+1) \ge (2/3)^i2^L/b .
\]
If the right side exceeds \(2\), summing \(x^{-s}\) over the resulting ordinary tail bounds the total normalized contribution at depth \(k\) by
\[
         O_s\bigl(t^k[b(3/2)^i2^{-L}]^{s-1}\bigr).
\]
This bound is uniform over any number of interior alternatives sharing the same height lower bound. It uses no independence between the preceding physical orbit and the selected block. A collection with no sufficiently long early match can evade both payments.

[Formal finite rational inequalities, displaced centers and shadow cost](TiltedGreen.lean)

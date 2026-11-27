# Transposing two complete blocks cannot give an ordinary merger before a threefold drop

**Theorem E.** Start at any positive odd ordinary integer \(x\), follow two complete ascent-and-reset blocks, and let \(z\) be the final odd landing. If
\[
                         3(z+1)\ge x+1,
\]
no distinct positive integer can reach that same terminal by executing the same two complete blocks in the opposite order. In fact, if the two blocks have different parameter pairs, the rational entrance of their transposed affine maps is nonintegral. This remains true even if one would allow a nonphysical second path with integral entrance and fractional intermediate value.

Let \(Y=x+1\). A complete block with \(t\ge1\) odd shortcut inputs and \(b\ge1\) subsequent even shortcut inputs has shifted affine map
\[
      F_{t,b}(Y)=\frac{3^tY}{2^{t+b}}+1-2^{-b}.
\]
The true valuation at the reset odd input is \(b+1\). For original blocks \((t,b),(u,c)\), the unique other shifted entrance \(Y'\) with identical terminal satisfies
\[
 \Delta=Y'-Y=(2^b-1)(2/3)^t-(2^c-1)(2/3)^u
                       +(2^c-2^b)(2/3)^{t+u}.                          \tag{1}
\]
This follows by comparing the two compositions, which have the same positive slope. If the blocks are identical then \(\Delta=0\). We prove it cannot be an integer in the other cases under the stated floor.

Write \(m=\min(t,u)\), \(T=\max(t,u)\), and \(B=\max(b,c)\). The proof uses two consequences of the ternary denominator; the integrality of (1) and the resulting cuts are symmetric under interchanging the two parameter pairs. Orient them so that \(t=m,\ u=T\), which replaces \(\Delta\) by its negative if needed.

* Reducing \(3^{t+u}\Delta\) modulo \(3^m\) shows that \(3^m\mid2^c-2^b\). If \(b\ne c\), then \(2\cdot3^{m-1}\le|b-c|\le b+c\). The elementary order identity used here is \(\operatorname{ord}_{3^m}(2)=2\cdot3^{m-1}\). Indeed an exponent with \(2^d=1\pmod3\) is even, \(d=2h\); \(v_3(4^h-1)=1+v_3(h)\) follows from \(4^h\equiv1+3h\pmod9\) when \(3\nmid h\), and the factorization \((v^3-1)/(v-1)=v^2+v+1\equiv3\pmod9\) for \(v\equiv1\pmod3\). If \(b=c\) but \(t\ne u\), (1) reduces to \((2^b-1)((2/3)^t-(2/3)^u)\). The difference in parentheses has exact reduced ternary denominator \(3^T\). The same order identity gives \(2\cdot3^{m-1}\le 2\cdot3^{T-1}\le b\). Thus \(2\cdot3^{m-1}\le b+c\) in all nonidentical cases.
* Reducing \(3^{t+u}\Delta\) modulo \(3^u\), and cancelling its unit factor \(2^u\), gives
\[
   3^T\mid K,\qquad K=(2^c-2^b)2^m-(2^c-1)3^m .
\]
One has \(K<0\), since \(2^c-2^b<2^c-1\) and \(2^m<3^m\). Moreover \(|K|<2^{B+1}3^m\), so \(3^{T-m}<2^{B+1}\le 2^{b+c}\). In particular there is no vanishing congruence marker to exempt.

For one physical block the shifted endpoint is its homogeneous gain times the shifted entrance times a factor strictly less than 2. Indeed at entrance \(Y=2^t w\) this last factor is \(1+(2^b-1)/(3^t w)\), and \(3^t w=2^b x_{\mathrm{next}}+1\) with \(x_{\mathrm{next}}\ge1\). Thus the *original* path and its supplied terminal floor imply
\[
                   2^{t+u+b+c}<12\cdot3^{t+u}.                         \tag{2}
\]
Only the original two-block path has been used physically. The inequalities \(3/2<\log_2 3\), \(\log_2(3/2)<3/5\) follow from \(8<9\) and \(3^5<2^8\). Taking logarithms gives
\[
 \tfrac32(T-m)\le\log_2(3)(T-m)<b+c<4+\tfrac35(T+m).
\]
Hence \(T<(40+21m)/9<5+3m\), and \(b+c<7+3m\). Since \(2\cdot3^{m-1}\ge7+3m\) for \(m\ge3\), the first ternary cut forces \(m\le2\). We have proved \(T\le10\), \(b+c\le12\).

There are now only \(2\cdot10\cdot12^2=2880\) binary-parameter tests even before imposing the sum and ordering bounds. For \(1\le t\le2\), \(1\le u\le10\), \(1\le b,c\le12\), the following exact conditions have **zero** joint solutions:
\[
\begin{gathered}
 (t,b)\ne(u,c),\qquad b+c\le12,\qquad 2^{t+u+b+c}\le12\cdot3^{t+u},\\
 (2^b-1)2^t3^u+2^{c+t+u}
 \equiv (2^c-1)2^u3^t+2^{b+t+u}\pmod{3^{t+u}} .
\end{gathered}
\]
The last condition is exactly (1) being integral. The theorem \(\mathtt{bounded\_swap\_exclusion}\) in the accompanying Lean file checks every tuple by kernel reduction. Its other theorem checks the full signed difference from the four block equations. The finite reduction using the two ternary cuts and the real height bound is the written proof above.

**Minimum consequence.** For a putative least tripling disagreement \(s\), its nonconvergent leg starts at \(x=3s\) and every positive integer at most \(s\) converges. Thus its second landing has \(z>s\). The theorem rules out a distinct ordinary source obtained by transposing those first two complete blocks. More generally, any such swap in any supplied trajectory already entails \(3(z+1)<x+1\) over that local two-block segment. If that happens at the initial bad triple, its own path has already crossed its known good floor. For later sites a drop relative to that site's own height need not reach the original floor. Other merger words are outside the theorem.

Swaps without the protected endpoint occur on ordinary integers. For example the blocks \((1,3),(2,5)\) send \(1893\to355\to25\). In the other order they send \(1891\to133\to25\). Both paths have the displayed full maximal runs, and the source difference is \(-2\). Here the endpoint is well below the asserted floor. The shifted affine map and permutation calculations have precedents in work on Collatz valley blocks and affine permutation shells. The constraint here is the exact common ordinary terminal at a protected height. [Affine block permutations, Paper 201](https://rstation.ai/problems/collatz/papers/201)

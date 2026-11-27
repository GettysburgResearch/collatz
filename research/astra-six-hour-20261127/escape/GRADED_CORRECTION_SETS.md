# Scattered correction sets and large equal-clock classes on an escaping component

Suppose that an actual positive odd component escapes. Write \(g(x)\) for its integer odd-step grade, increasing by one under \(U\), and put \(F(x)=\prod_{j\ge0}3U^jx/(3U^jx+1)\) and \(P(x)=x/F(x)\). With \(e=v_2(3x+1)\), the relation \(P(Ux)=3\,2^{-e}P(x)\) is exact. All vertices have \(F>0\), with a uniform lower bound from reciprocal packing. The absolute values of the grades depend on the chosen reference ray.

## The topology at a fixed odd grade

Take only the odd positive ternary units of the component and set
\[
 K_v=\overline{\{F(x):g(x)=v,\ 3\nmid x\}} .
\]
Let \(K'\) mean the set of accumulation points of a compact real set \(K\). Then
\[
 \begin{split}
 K_v'&=K_{v+1},\qquad \bigcap_{j\ge0}K_{v+j}=\{1\},\\
 K_v&=\{1\}\ \cup\
       \{F(x):g(x)\ge v,\ 3\nmid x\}.                                \tag{1}
 \end{split}
\]
Every displayed ordinary value occurs at exactly one unit vertex in the whole component. Consequently each \(K_v\) is countable and compact. An ordinary point of grade \(v+j\) disappears at derivative \(j+1\). Its membership at derivative \(j\) is exact. The \(\omega\)-th Cantor–Bendixson derivative is the singleton \(\{1\}\), and its next derivative is empty. The [full component correction closure](CLOSED_CORRECTION_SUPPORT.md) can nevertheless carry a non-atomic measure of Hausdorff dimension one, through unboundedly negative grades.

Indeed, distinct grade-\(v\) unit states with a convergent sequence of values have a subsequence with heights tending to infinity. Since \(F(Ux)-F(x)=F(x)/(3x)\), its limit belongs to \(K_{v+1}\). Conversely each unit \(y\) of grade \(v+1\) has infinitely many unit inverse parents \(x=(2^e y-1)/3\) of growing exponent: the parity restriction makes \(2^ey\equiv1\pmod3\), and two of the three resulting classes modulo six exclude divisibility of \(x\) by three. Their distinct values \(F(x)=F(y)(1-2^{-e}/y)\) approach \(F(y)\), giving the first identity by closedness. The slightly more general inclusion \(K_v\subseteq K_{v+1}\cup\{F(x):g(x)=v,3\nmid x\}\) follows by taking a constant or a diverging subsequence.

As \(v\to+\infty\), \(F(x)\to1\) uniformly over grades \(g(x)\ge v\). For any fixed height \(L\), there are finitely many component vertices of height at most \(L\), hence a finite upper bound on their grades. From any vertex of higher grade all future states exceed \(L\). The uniform simple-orbit reciprocal tail above \(L\) tends to zero as \(L\to\infty\), proving the claim. Every positive grade is populated by the forward ray, and the reverse-parent argument transfers its limiting value 1 to each \(K_v\). This proves the intersection claim and, by iteration of the preceding inclusion, the last formula in (1).

For uniqueness, at any two vertices \(x,y\) in the component,
\(P(x)/P(y)=3^{g(x)-g(y)}2^b\) for an integer \(b\), by transport to an ordinary common successor. If \(F(x)=F(y)\), their ratio \(x/y=P(x)/P(y)\) is an \(S\)-unit for \(S=\{2,3\}\). Positive odd units have ratio an \(S\)-unit only if they coincide. No ordinary vertex has \(F=1\), since its first factor is strictly smaller than one. This gives the derivative ranks stated above. [Uniform reciprocal packing as used for the component flux](../../astra-unconventional-20261126/boundary/COLLISION_SOURCE.md)

## Many ordinary integers in each sufficiently high dyadic level

Fix any unit vertex \(a\) of grade \(v\), take its actual forward ray \(a_k=U^k a\), and let \(S_k\) be the total forward exponents from \(a\) to \(a_k\). For every sufficiently large integer \(b\), the level
\[
                   L_b=\{x:g(x)=v,\ P(x)=2^bP(a),\ x\text{ odd}\}
\]
contains at least
\[
                    c_a\frac{(4/3)^b}{\sqrt b}                         \tag{2}
\]
distinct ordinary integers. In particular every such level is finite with an unbounded cardinality as \(b\to\infty\). The lower bound includes possible nonunit leaves.

Put \(\beta=2-\log_2 3>0\). The integer walk \(V_k=2k-S_k\) starts at zero and has upward jumps of at most one. The transport identity gives
\[
 V_k=\beta k+\log_2(P(a_k)/P(a))\ge\beta k-\log_2 P(a),\qquad V_k\le k .
\]
It hits each positive integer \(b\) at some \(k\) with \(b\le k\le (b+\log_2 P(a))/\beta\). Put \(y=a_k\). Use the bridge of Weaver’s Paper 12, Theorem 14, with \(M=y\). Its exponent \(e\) is bounded by an absolute constant, its parent \(r=(2^e y-1)/3\) lies in the selected cylinder, and \(r\) exceeds the bounds needed to reconstruct all positive words of Lemma 13. Apply that lemma to length \(k-1\) and exact total \(d=2k-e\). The total is within a fixed constant of \(2(k-1)\). The negative-binomial mass at this total is \(\gg1/\sqrt k\). As each selected word has probability \(2^{-d}\), the number of its words is
\[
        \gg (2^d/3^{k-1})/\sqrt k\gg (4/3)^k/\sqrt k .
\]
Appending the selected bridge at the root gives actual length-\(k\) words based at \(y\) of total exactly \(2k\), all with real offset bounded by an absolute constant. The source determines its word because forward dynamics is deterministic. All these sources lie in the interval
\[
        (4/3)^k(y-C)\le x\le (4/3)^ky
                    =2^bP(a)F(a_k).
\]
Their grade is \(v\) and their corrected height is \((4/3)^k P(a_k)=2^bP(a)\), as asserted. The inequality \(x\le2^bP(a)\) bounds the entire level. The selected window has length \(O((4/3)^k)\) and the selected set has relative density \(\gg1/\sqrt{k}\) in a window of that order. All its corrected marks converge uniformly to 1 as \(b\to\infty\). [Weaver, Paper 12, Lemma 13 and proof of Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1)

A pair of positive odd vertices in this component has the same \(P\) precisely when its shortcut trajectories coalesce at equal shortcut times with equal accumulated odd counts. For the forward implication choose their actual common successor at an odd state. Equality of \(P\) forces the two elapsed counts and the two total exponents to agree by multiplicative independence of 2 and 3. For the converse, use exact homogeneous transport at every shortcut step (extend \(P\) to even integers by \(P(2^r x)=2^rP(x)\)). Thus (2) supplies large finite synchronization classes at prescribed absolute levels. Summing the underlying entry lower bounds over distinct ray vertices recovers weights of order \(1/a_k\) with a convergent total. The multiplicities in (2) have not yielded an exclusion of such a ray.

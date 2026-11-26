# Short additive relations balanced at both residue places

Let \(x_1,\ldots,x_p\) be the distinct positive odd phases on a bounded least-disagreement cycle, and let \(k_i\in\{0,1,2\}\) be their dyadic band marks. Put \(q,r\) equal to the first powers of 2 and 3, respectively, at least \(p^{31/15}\). For all sufficiently large \(p\), there are at least
\[
                         p-O(p^{199/200})
\]
linearly independent integer vectors \(c=(c_i)_{1\le i\le p}\) with the following simultaneous properties.

* Each vector has \(\sum_i|c_i|\le1000\) and \(|c_i|\le2\).
* Within every individual class \((k_i,x_i\bmod q)\) its coefficients sum to zero. They also sum to zero in each class \((k_i,x_i\bmod r)\).
* The ordinary integer equality \(\sum_i c_i x_i=0\) holds exactly.

The vectors can, moreover, each be chosen in a single band, so \(\sum_i c_i Z_i=0\) for the folded integer mantissas \(Z_i=2^{2-k_i}x_i\) as well. All equalities involve phases from one realized positive orbit.

## Proof

Write \(\delta=479/1000\). The [pinned 4096-step strip count](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md) bounds the number of admissible words of \(l\) odd steps by \(O(3^{\delta l})\). The affine endpoint of each incoming word fixes \(x_i\bmod3^l\). For a forward word of length \(l\) and total exponent \(A\), the same identity fixes its starting residue modulo \(2^A\). Throughout the strip \(2^A\ge c3^l\) with an absolute \(c>0\), by the ratio of the initial and terminal odd phases and positivity of the affine corrections. Taking \(l=\lceil\log_3(q/c)\rceil\) therefore bounds the number of dyadic residue vertices by \(O(q^\delta)\). The ternary vertex count is \(O(r^\delta)\). Adding the band labels multiplies either bound by at most three.

Build the bipartite multigraph whose edges are the ordinary phases and whose two ends have the indicated two marked residue labels. Its number of nonisolated vertices is \(O(p^{14849/15000})\). As long as at least \(p^{199/200}\) edges remain, find a cycle with at most 500 edges. Two parallel edges supply a cycle of length two. Otherwise the graph contains a nonempty subgraph of minimum degree at least the edge count divided by the vertex count: repeatedly remove any vertex of smaller degree, keeping the initial ratio as threshold. For large \(p\) this minimum degree minus one is at least \(p^{1/200}\), since \(199/200-14849/15000>1/200\). If a breadth-first search to depth 201 had no short cycle, it would have more than \(p\) vertices at its last level. The total vertex bound is \(o(p)\). This supplies the claimed cycle bound.

Give the edges on this cycle alternating signs and delete one of them. Continue until fewer than \(p^{199/200}\) edges remain. The resulting at least \(p-O(p^{199/200})\) signed cycle vectors are linearly independent, since each successive pivot edge is absent from all later vectors. Each vector \(v\) is balanced at every vertex of both types, so
\[
                 m(v)=(qr)^{-1}\sum_i v_i x_i\ \in\mathbb Z .
\]
Its signed sum contains at most 500 terms of size \(O(s)\), where \(s=\min_i x_i\). The [pointwise two-logarithm height ceiling](https://github.com/GettysburgResearch/collatz/blob/f192322f70073ba44bc9f98785a51c27a4da9ee5/research/astra-global-closure-20261124/round10/arithmetic/README.md) gives \(s\ll p^{5.12}\), hence
\[
                        |m(v)|\ll p^{5.12-62/15}=p^{74/75}.
\]
Each cycle has just one band by construction. Group the independent vectors by the pair consisting of their band and the signed integer \(m(v)\). Subtract a fixed representative within each nonempty group from all its other vectors. The differences remain linearly independent, because in the original independent family each nonrepresentative has coefficient one in exactly one difference. This loses only \(O(p^{74/75})\) dimensions. Every remaining vector has the asserted support, balances and exact integer equality. This proof allows \(s>qr\); it does not replace divisibility by equality termwise at that size.

## The geometric inference still needed

In sorted rank \(j\) the mantissa is \(4s2^{j/p}+O(p)\). Consequently the same independent short vectors, permuted into rank order, all satisfy
\[
                \left|\sum_{j=0}^{p-1}c_j\,2^{j/p}\right|\ll p/s.
\]
The numbers \(2^{j/p}\) are linearly independent over \(\mathbb Q\), since \(X^p-2\) is Eisenstein. That fact only excludes an exact zero on these ideal real samples. It does not bound these polynomially small values along a family of short signed forms. Conversely, bounded-length additive relations can occur frequently in sparse sets of integers, so their mere existence at the physical heights cannot exclude a cycle. To close through this route one must use the residue balancing and precise curve approximation together. The argument above establishes the simultaneous high-rank system of exact arithmetic relations.

A direct control shows why near-full rank and small real values alone cannot close the branch. The \(p-5\) independent polynomials \(X^j(X-1)^5\), \(0\le j<p-5\), have coefficient \(\ell^1\)-norm 32 and value \(O(p^{-5})\) at \(2^{1/p}\), already smaller than \(p/s\) throughout the height ceiling. Even the coefficient-by-coefficient restriction \(|c_i|\le2\) can be met: replace \((X-1)^5\) by \(\prod_{k=0}^4(X^{2^k}-1)\). Its 32 coefficients are all \(1\) or \(-1\), its degree is 31, and its value is again \(O(p^{-5})\). Its \(p-31\) allowable shifts are independent. These examples carry neither the exact physical equalities nor the two residue balances of the theorem.

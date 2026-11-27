# Prime-to-six mass in comparisons of every pair of ranks

On the bounded least-disagreement branch, all differences between two lifted phases of one ordinary cycle obey the following arithmetic constraint. The time positions of the discrepancies can be partitioned into any fixed number of sets. The bound uses the exact binary depth at the ending gap and the exact ternary depth at the initial gap, simultaneously.

## The uniform statement

Use the ordered integer mantissas \(Z_r\) from the [window theorem](README.md), with increasing rank \(0\le r<p\), odd minimum \(s\), shortcut period \(h\), and marks \(c_r\in\{1,2,4\}\). Lift to nonnegative indices by \(Z_{r+p}=2Z_r,\ c_{r+p}=2c_r\). The physical identity becomes \(Z_{r+h}=3Z_r+c_r\). For any \(1\le t\le p\), set \(G_r=Z_{r+t}-Z_r>0,\ J_r=c_{r+t}-c_r\) at each base rank \(0\le r<p\). The input cut \(r+t\ge p\) uses the doubled upper mark. For a fixed starting rank \(v\), put
\[
 r_i=(v+ih)\bmod p,\quad b_i=\lfloor(r_i+h)/p\rfloor,\quad
 B_i=\sum_{j<i}b_j,\quad G_i^*=G_{r_i},\quad J_i^*=J_{r_i}.
\]
Then \(2^{b_i}G_{i+1}^*=3G_i^*+J_i^*\), including at either cut.

Fix \(K\ge1\), \(0\le n\le p\), and any partition of \(\{0,\ldots,n-1\}\) into at most \(K\) sets \(I\). For a rational number with denominator supported on \(S=\{2,3\}\), let \(H_S\) denote the positive prime-to-six part of its reduced numerator, and put \(H_S(0)=1\). Define
\[
 Y_I=\sum_{i\in I}\frac{2^{B_i}J_i^*}{3^{i+1}}.
\]
For every \(\epsilon>0\), all sufficiently long such ordinary cycles satisfy, uniformly in \(t,v,n\) and in the partition,
\[
 2^{B_n+v_2(G_n^*)}3^{v_3(G_0^*)}
 \ \le\ \exp\!\big(\epsilon(n+\log p)\big)\ G_0^* \prod_I H_S(Y_I).       \tag{1}
\]
For \(K=1\), the three-form inequality in [the moving-center argument](MOVING_CENTERS.md) supplies this result directly if \(Y\ne0\), since
\(2^{B_n}G_n^*-3^nG_0^*=3^nY\).
When \(Y=0\), \(2^{B_n+v_2(G_n^*)}\) divides \(G_0^*\), with its ternary part coprime to that power. The higher-dimensional assertion permits arbitrary, noncontiguous groups without presuming that the individual sums are nonzero.

## Proof

The rank envelope \(Z_r=4s2^{r/p}+O(p)\) and its doubled extension give
\[
 G_r=4s2^{r/p}(2^{t/p}-1)+O(p)\asymp st/p.
\]
This is uniform including the lifted seam, since \(s/p^2\to\infty\). In particular \(\min_r G_r\gg s/p\gg p\) and \(\max_r G_r\ll s\ll p^{O(1)}\). Also \(|J_r|\le7\) on the base period. The wrap identity \(B_i=\lfloor(v+ih)/p\rfloor\) and \(h/p=\log_2 3+O(1/s)\) give \(2^{B_i}/3^i=O(1)\) for \(i\le p\). Thus \(|Y_I|\ll n\) simultaneously for every partition. The strict separation \(G_0^*/(n+1)\to\infty\) is an ordinary rank-spacing input for this argument.

Suppose (1) fails for fixed \(K,\epsilon\) along a sequence \(p\to\infty\). Pass to a subsequence with a fixed number of nonzero \(Y_I\) and keep \(G_0^*\) as the first coordinate. Iterating the integer gap recurrence gives
\[
 G_0^*+\sum_I Y_I=2^{B_n}G_n^*/3^n.                                     \tag{2}
\]
Use the coordinate forms at infinity and at 3. At 2 replace the first coordinate form by (2). The local systems are independent. The product of all their absolute values is
\[
 2^{-B_n-v_2(G_n^*)}\,3^{-v_3(G_0^*)}\,G_0^*\prod_I H_S(Y_I)
 <\exp\!\big(-\epsilon(n+\log p)\big).
\]
Clearing denominators by \(3^n\) preserves this product by the product formula over the selected places. Dividing common integral content to obtain a primitive vector cannot increase it. The resulting maximum coordinate height is \(\exp(O(n+\log p))\), since each denominator divides \(3^n\), the real discrepancies are \(O(n)\), and the starting gap is polynomial in \(p\). Thus the fixed-place Subspace Theorem gives a repeated proper rational subspace. If a bounded-height primitive point were to repeat, it too is on a proper line in any dimension at least two.

Take a fixed nonzero rational relation along that subsequence. Its coefficient at \(G_0^*\) must vanish, since every remaining coordinate is \(O(n)=o(G_0^*)\). Express one discrepancy through the others and eliminate it. The new dyadic form still has leading coefficient one at the starting gap and still equals the right side in (2) exactly. The local coordinate forms elsewhere stay independent, the archimedean domination persists, and the preceding product loses only a factor \(H_S(Y_I)\ge1\). Repeat until only the starting gap remains. Its dyadic absolute value now equals \(2^{-B_n-v_2(G_n^*)}\). Hence the entire product equals the positive integer \(H_S(G_0^*)\), contradicting its strict bound below one. This also covers an initially empty list of nonzero discrepancies. The onset is ineffective.

The partition argument on an escaping ordinary ray in PR193 supplies the elimination method. Here strict rank spacing provides the needed domination uniformly for two arbitrary phases of the same bounded cycle. Neither an escape nor a choice of one distinguished comparison source is involved. [Schlickewei's finite-place theorem](https://doi.org/10.1007/BF01220404) · [PR193 all-word escape comparison](https://github.com/GettysburgResearch/collatz/blob/4cc06e7d8fdec923eed73a26b1e9d680c9f701d1/research/astra-multiple-attacks-20261125/arithmetic/README.md) · [PR195 integer ranks, lifted gap equations and both cuts](https://github.com/GettysburgResearch/collatz/blob/f192322f70073ba44bc9f98785a51c27a4da9ee5/research/astra-global-closure-20261124/round10/arithmetic/README.md)

## Consequence for replacements on positive fractions of a window

Suppose every nonzero \(J_i^*\) lies in at most \(K\) intervals of total length \(L\). For an interval starting at \(j\) of length \(l\), its \(Y\) is \(2^{B_j}3^{-j-l}\) times the integer
\[
 \sum_{i=j}^{j+l-1} 3^{j+l-1-i}2^{B_i-B_j}J_i^* .
\]
The interval wrap estimate \(2^{B_i-B_j}\ll3^{i-j}\) bounds this integer by \(O(l3^l)\). The complement gives zero. Applying (1) to these groups, allowing one extra group for the complement, gives
\[
 (n-L)\log3 + v_2(G_n^*)\log2+v_3(G_0^*)\log3
 \ \le\ \log G_0^*+o(n+\log p)+O_K(\log(n+2)).                        \tag{3}
\]
We used \(B_n\log2=n\log3+O(1)\). In particular for \(n/\log p\to\infty\) every fixed number of changed intervals must cover \(n-o(n)\) positions. At the logarithmic threshold the initial height is that of the actual lifted difference, \(\asymp st/p\), even for neighboring ranks. Within each changed interval the marks can differ on arbitrarily many positions.

These estimates exclude concentrated discrepancies on all ranks, while allowing frequent changes spread across many separated intervals. Equation (1) gives no uniform upper bound on the outside-prime parts of arbitrary groups of errors. The independent-bit admissible masks in PR195 illustrate why nearby ranks need not have sparse differences merely from legal gap transitions. No contradiction for every high-complexity mask follows here.

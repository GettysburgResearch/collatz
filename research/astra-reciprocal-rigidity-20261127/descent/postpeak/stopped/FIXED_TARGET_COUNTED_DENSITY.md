# Counted fusion with one fixed ordinary target has density zero

Let \(T\) be the shortcut Collatz map and \(F_t(n)\) the number of odd departures in its first \(t\) steps. Fix any positive integer \(a\). The set
\[
 \{n\ge1:\exists t\ge0,\quad T^t(n)=T^t(a),\quad F_t(n)=F_t(a)\}
\]
has ordinary natural density zero. Both equalities use the same physical clock. The claim covers every possible future of \(a\).

We use the external theorem that \(n,n+1\) counted-fuse for a natural-density-one set of \(n\). The finite-clock tests are unions of binary residue classes, since equal odd counts give equal affine slopes. Their densities approach one by the adjacent-pair theorem of Said Duran and the quantitative estimate of Leen, as restated by Weaver. [Source and finite-clock transfer](SYNCHRONIZATION.md) · [Weaver 124/v1, Theorem 1 and §2](https://rstation.ai/problems/collatz/papers/124/v1)

Weaver 13 discusses stable labels and residue-class comparisons for synchronization. This explicit fixed-target consequence also fits the packet's earlier joint clock-phase transport. The proof below applies an integer label and disjoint rescaled levels directly, without choosing cycle cuts. No general priority claim is made. [Weaver 13/v1](https://rstation.ai/problems/collatz/papers/13/v1) · [Joint clock phases](../../../rigidity/phase3/CLOCK_PHASES.md)

## An integer label on the target's component

Let \(C(a)\) consist of sources whose forward paths intersect the forward path of \(a\), allowing unrelated clocks. If that path is eventually periodic, take \(P\) to be its least cycle period and \(U\ge1\) the cycle's odd count. Otherwise put \(P=2,U=1\). Write \(I_r(n)=PF_r(n)-Ur\). For \(n\in C(a)\) set
\[
 J(n)=I_r(n)-I_s(a)\quad\text{whenever }T^r(n)=T^s(a).
\]
Two witnesses may be advanced to the same clock on the \(n\)-path. This preserves each difference by additivity. The resulting two clocks on the \(a\)-path either agree or visit the same periodic point a whole number of cycles apart. In the latter case the intervening integral vanishes by the choice of \(P,U\). Hence the label is well defined. Give sources outside \(C(a)\) the label \(\infty\), with the arithmetic convention \(\infty+k=\infty\) for each integer \(k\). Counted fusion with \(a\) forces \(J(n)=0\).

The edge formula is \(J(n)=P\mathbf1_{n\text{ odd}}-U+J(Tn)\). Any counted-fused pair has equal labels, by adding its equal integrals to the label of its common endpoint. Consequently \(J(n)=J(n+1)\) outside a set of density zero. In particular the edge formula gives
\[
 J(2n)=J(n)-U\quad\text{everywhere},\qquad J(3n)=J(n)-P\quad\text{almost everywhere}.
\]
For the second identity replace \(J(2n+1)\) by \(J(2n)\) and \(J(3n+2)\) by \(J(3n)\). Each replacement uses at most two adjacent comparisons on fixed arithmetic progressions, which preserve zero upper density of exceptional inputs.

## Rescaling disjoint level sets

For finite integer \(j\), let \(d_j(X)=X^{-1}\#\{n\le X:J(n)=j\}\). Within each fixed-length block, all labels agree unless an adjacent comparison fails. Thus the indicator of level \(j\) has the same average up to \(o(1)\) on each residue class modulo any fixed modulus. Applying this to the two dilation identities gives
\[
 d_j(2X)=d_{j+U}(X)+o(1),\qquad d_j(3X)=d_{j+P}(X)+o(1).
\]
Iteration, also replacing \(X\) by a fixed fraction of itself, gives \(d_{j+rU+sP}(X)=d_j(2^r3^sX)+o(1)\) for each fixed pair of integers \(r,s\).

Given \(K\) and \(0<\varepsilon<1/2\), take \(K\) such pairs with \(|2^r3^s-1|<\varepsilon\) and distinct shifts \(rU+sP\). Indeed irrationality supplies arbitrarily large \(s\) with \(r+s\log_2 3\to0\), while \(P-U\log_2 3\ne0\) makes the shifts unbounded. Changing the counting endpoint by this factor costs \(O(\varepsilon)+O(1/X)\) uniformly over all level sets. Their disjointness gives \(K\limsup_X d_j(X)\le1+O(K\varepsilon)\). Letting \(\varepsilon\downarrow0\) and then \(K\to\infty\) proves the claim for every finite level, including zero.

Thus even for target one, whose ordinary arrivals have positive lower natural density, requiring a common clock and equal odd counts leaves a density-zero population. This yields no conclusion about convergence of an individual source. [Ordinary arrival theorem and scope](SOURCE_VARIANCE.md)

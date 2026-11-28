# Every two nearby denominator levels pay a joint numerator cost

For a finite set of primes \(S\) write \(b(u)\) for the positive factor of \(|u|\) supported outside \(S\), with multiplicity. Include two and three in \(S\). Take any positive odd \(S\)-smooth \(q\) prime to three. On a reduced signed shortcut descent from \(m/(q3^n)\), let \(u_h\) be the reduced odd numerator just before the odd departure from level \(h\). The positive integer level drops by one at this departure. Changing to any other date at the same positive level changes its numerator by a power of two, preserving \(b(u_h)\).

**Proposed pointwise theorem.** For any fixed integer \(K\ge1\) and \(\epsilon>0\),
\[
       q3^{h-k}\ \ll_{S,K,\epsilon}\ [b(u_h)b(u_{h-k})]^{1+\epsilon}
              \qquad(1\le k\le K,\quad h-k\ge1).                       \tag{1}
\]
There is no bound on the source magnitude or on the complete denominator \(q\). Even two low-cofactor levels separated by an arbitrarily long native wait must jointly pay (1) if their denominator levels are close. This bounds each individual pair, complementing the [uniform sparse exceptional set theorem](../literature/DESCENDING_NUMERATOR_COFACTORS.md).

For an unrestricted number of intervening levels there is also a native-time version. If two dates \(i<j\) have reduced nonzero numerators \(d_i,d_j\), the interval contains an odd departure, its ending height is \(h\ge1\), and \(d=j-i\), then
\[
 q3^h\ \ll_{S,\epsilon}\ [b(d_i)b(d_j)]^{1+\epsilon} 2^{C\epsilon d} .   \tag{2}
\]
Here \(C\) is absolute. Thus whenever \(m,q\le2^{O(n)}\), uniformly on intervals of at most \(C_0 n\) native dates, \(\log_2[b(d_i)b(d_j)]\ge\log_2(q3^h)-o(n)\). In particular after the first odd departure, a source with \(\log b(m)=o(n)\) has \(b(d_j)\ge q3^h 2^{-o(n)}\) at **every** subsequent date \(j\le C_0 n\) of positive level. This includes moving exponentially large \(S\)-smooth numerators. For positive inputs the corresponding real state is at least \(2^{-o(n)}\) on those dates. The error is on the original scale \(n\); its relative interpretation at a denominator with bounded logarithmic height can be vacuous.

## A three-term estimate for the factors outside a finite prime set

For nonzero integers \(x+y=z\), \(\gcd(x,y,z)=1\), set \(H=\max(|x|,|y|,|z|)\). For each \(\varepsilon>0\),
\[
                         H\ll_{S,\varepsilon} b(xyz)^{1+\varepsilon}.    \tag{3}
\]
This is the rational two-dimensional case of the \(p\)-adic Subspace Theorem: use the three forms \(X,Y,X+Y\) at infinity and every prime in \(S\). Their complete product is \(b(xyz)\). Primitive pairs with product at most \(H^{1-\delta}\) lie on finitely many rational lines, each containing only two opposite primitive pairs. Adjust the constant and take \(1-\delta=1/(1+\varepsilon)\). The comparability of \(H\) with the norm of \((x,y)\) costs an absolute factor. This classical inequality is ineffective. [Schlickewei, original paper](https://doi.org/10.1016/0022-314X(77)90073-7) · [Evertse, Theorem 1.1 and the three-form application](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

Write \(Q=q3^h\) and unroll the native interval. If it contains \(l\ge1\) odd departures at dates \(0\le t_1<\cdots<t_l<d\) measured from its start, the exact original and final numerators satisfy
\[
         2^d d_j-d_i=Q V,\qquad V=\sum_{r=1}^l3^{l-r}2^{t_r}>0 .        \tag{4}
\]
Let \(g=\gcd(2^d d_j,d_i)\). The reduced starting numerator is prime to \(Q\), so \(g\mid V\). Split \(g=g_S g_o\), with \(g_o=b(g)\), and similarly \(V=V_S b(V)\). The primitive triple obtained from (4) has outside-\(S\) product \(W=b(d_i)b(d_j)b(V)/g_o^3\). Its height is at least \(Q V/g\). Since \(g_S\mid V_S\),
\[
       W\frac{g}{V}=
         b(d_i)b(d_j)\frac{g_S}{g_o^2 V_S}\le b(d_i)b(d_j).
\]
Putting these facts into (3), and using \(W\le b(d_i)b(d_j)V\), gives (2), because \(V\le2^{O(d)}\). For the logarithmic consequence note that all numerator magnitudes are \(2^{O(n)}\): an odd update averages the old numerator with \(q3^{h'-1}\), and an even update halves it. Apply (2) for each fixed \(\epsilon\), then let \(\epsilon\downarrow0\).

For (1) use odd marks at both ends and \(k\le K\). The [chronological two-endpoint estimate](SPARSE_DISCREPANCY_BLOCKS.md), as applied in [the scalar numerator paper, (3)](../literature/DESCENDING_NUMERATOR_COFACTORS.md), gives \(d\le2\log_2[b(u_h)b(u_{h-k})]+C_{K,S}\). Its hypotheses follow from nonzero intermediate reduced numerators, the strictly positive descending impulses, and odd endpoint numerators. Substitute this upper bound for \(d\) in (2) and choose its error parameter sufficiently small for the prescribed \(\epsilon\) in (1).

## The congruence product used for local source counts

For \(Q=3^h\), \(a,b,k\) nonzero integers and \(s\ge0\), suppose \(a+2^s b=Qk\). Then
\[
                  Q\ll_\epsilon |ab|\,|abk|^\epsilon .                 \tag{5}
\]
Here \(a\) need not be a ternary unit. Use \(S=\{2,3\}\) in (3), divide the triple by \(g=\gcd(a,2^s b)\), and write \(g=g_2g_3g_o\) for its binary, ternary and prime-to-six parts. We have \(g_2\mid k\) and \(g_3\mid a\). The normalized outside product is \(W=b(a)b(b)b(k)/g_o^3\), and
\[
         \frac{gW}{|k|}
            \le g_3 b(a)b(b)\le |ab| .
\]
Since \(Q|k|/g\le H\), (3) gives (5). This excludes exponentially small products in nonzero congruence relations at linearly growing exponent heights. The exact relation \(a=-2^s b\) has \(k=0\) and must be treated separately. For comparison, Pourchet's three-place argument for continued fractions of rational powers, and general power-sum extensions, are described in [Corvaja and Zannier, introduction](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.517.pdf).

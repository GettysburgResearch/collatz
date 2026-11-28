# A Farey tiling of all phases at a best upper clock

Let a primitive positive cycle have odd phases \(C\), odd period \(p\) and total halving clock \(A\). Each actual odd step is \(2^{e_x}U(x)=3x+1\). Write \([v]\) for the positive dyadic ray of \(v\), viewed as an oriented circle in \(\log_2 v\bmod1\). Suppose \(p\ge2\), \(\gcd(A,p)=1\) and \(A/p\) is a best upper through denominator \(p\): there is no rational strictly between \(\log_2 3\) and \(A/p\) of smaller positive denominator. Take the unique \(1\le b<p\) with \(Ab\equiv1\pmod p\), and put \(a=(Ab-1)/p\). Then \(a/b<\log_2 3\), since it is strictly below \(A/p\), and the reduced approximation is an upper record.

The following \(p(b+1)\) points all differ:
\[
                       [3^{-j}x],\qquad x\in C,\quad 0\le j\le b.           \tag{1}
\]
Their **immediate angular successors** in this whole set are exactly
\[
 (x,j)\longmapsto
 \begin{cases}
      (U(x),j+1),&0\le j<b,\\
      (x,0),&j=b.
 \end{cases}                                                              \tag{2}
\]
At each of the first \(b\) levels the logarithmic gap is \(\log_2(1+1/(3x))\). The remaining level has the constant gap \(\log_2(3^b/2^a)>0\). These assertions require no bound on the cycle's width or its native exponents. They also hold as geometric identities for a genuine positive rational cycle with odd numerators and a common denominator prime to six.

## A pointwise counting identity

Define the integer counting function of the dyadic lifts by
\[
 H(t)=\sum_{x\in C}\lfloor\log_2(t/x)\rfloor.
\]
It satisfies \(H(2t)=H(t)+p\) and \(H(v)-H(u)\) counts true lifted points in \((u,v]\) for \(v\ge u\). Put
\[
 D(t)=\sum_{x\in C}\#\{k\in\mathbb Z:x\le2^k t<x+1/3\}.
\]
A direct floor count for each interval gives the exact identity
\[
                    H(3t)=H(t)+A-D(t).                                    \tag{3}
\]
Indeed the contribution of \(x\) to \(D(t)\) equals \(\lfloor\log_2(t/x)\rfloor-\lfloor\log_2(3t/(3x+1))\rfloor\). The sum of the second floors is \(H(3t)-A\) by the true cyclic successor equation. This argument for (3) uses no upper-clock assumption.

Iterating and using \(Ab-ap=1\) gives for every real \(t>0\)
\[
 \bigl(H(3^b t)-H(2^a t)\bigr)+\sum_{j=0}^{b-1}D(3^j t)=1.              \tag{4}
\]
All terms are nonnegative since \(3^b>2^a\). Thus the indicated lifted intervals cover the dyadic circle exactly once with their half-open conventions. On level \(j<b\) the interval at \(3^{-j}x\) ends at \(3^{-j}(x+1/3)\), the ray of \(3^{-j-1}U(x)\). A point counted by the first difference has \(2^a t<2^k x\le3^b t\), so its tile runs from the ray of \(3^{-b}x\) to the ray of \(2^{-a}x=x\) on the circle. Both endpoint descriptions include the left edge and exclude the right edge. Distinct starts follow directly from their unit valuations at both two and three: \(3^{-j}x=2^k3^{-h}y\) first implies \(j=h\), then \(k=0\), then \(x=y\). Removing a common odd rational denominator gives the same reasoning on rational cycles. This proves (1)–(2).

For any integer \(0\le j<b\), the half-open strip
\[
      x\le2^k3^j y<x+1/3,\qquad x,y\in C,\ k\in\mathbb Z,
\]
has only the occurrences \(j=k=0,\ x=y\): the ray of \(y\) is already a level-zero tile start. More generally, for every positive real probe \(v\), at most one triple \((x,j,k)\) with \(0\le j<b\) satisfies this strip with \(y\) replaced by \(v\). If none does, exactly one terminal gap contains \([v]\). Formula (4) also gives an exact multiple-cover identity for an arbitrary positive lower fraction \(a/b<\log_2 3\), now with integer right side \(Ab-ap\). A determinant of one is what makes these angular neighbors immediate.

## What the order says about a native word

Starting at an odd \(x=x_0\), write \(x_j=U^j(x)\), \(E_j=\sum_{i<j}e_{x_i}\). The \(b\) increasing drift-tile edges issuing from this level-zero ray have lifted endpoints
\[
 t_j=2^{E_j}x_j/3^j=x+\sum_{i<j}\frac{2^{E_i}}{3^{i+1}},\qquad 0\le j\le b.
\]
The terminal tile ends at \(2^{E_b-a}x_b\), the next true odd ray in rank order. In particular \(U^b\) advances one rank in the original set \(C\), and \(U\) advances \(A\bmod p\) ranks. The \(e_x\) in this formula are still the actual varying exponents. The statement does not require them to be the cyclic mechanical valuation word.

The mechanical subcase is already excluded for ordinary nontrivial cycles, as in Knight's high-cycle theorem. One can see the complete denominator directly. If a cyclic word has prefix clock \(E_i=\lfloor (r+iA)/p\rfloor\) for some rank \(r\), consider its two rotated prefix lists with initial ranks zero and one. At exactly one index \(1\le i<p\) their exponents differ by one, and the others agree. Hence the two full carries \(\sum_{i<p}3^{p-1-i}2^{E_i}\) differ by a power of two times a power of three. The positive determinant \(D_0=2^A-3^p\) is prime to six. The gcd of \(D_0\) with a native carry is the same at every rotation by the exact affine step. It therefore equals one. The reduced denominator is all of \(D_0\); ordinary integrality requires \(D_0=1\), which modulo eight is impossible for \(A\ge3\). The remaining positive word gives \(p=1,A=2\). This is prior structural context. [Knight, Discrete Mathematics 349 (2026), 114812](https://doi.org/10.1016/j.disc.2025.114812) · [Complete mechanical determinant in the PR192 tree](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-literature-closure-20261125/cycle/README.md)

The same exact tiling can hold on a nonmechanical positive rational cycle at a primitive best upper clock. Consequently the tiling itself gives no implication from mechanical angular order to a mechanical native valuation word. Distinguishing the complete denominator one among the remaining native profiles is the unresolved arithmetic inference.

[Exact sorted tilings and nonmechanical reduced rational controls](check_farey_tile.py) · [Recorded output](farey_tile_controls.json)

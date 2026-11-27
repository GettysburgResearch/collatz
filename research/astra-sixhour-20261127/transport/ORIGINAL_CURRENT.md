# The signed current at the original bounded minimum

Let \(f\) indicate failure to reach one on actual positive integers, let \(S\) denote the odd map, and use the odd children \(v_e(p)\) from [the smaller-parent row theorem](PARENT_ROWS.md). Write \(D(v)\) for the unique parent of an odd \(v\), including \(D(1)=1\), and \(e(v)=v_2(3v+1)\). At every positive odd \(p\) define
\[
 d(p)=f(p)-\sum_{e\ge1}2^{-e}f(v_e(p))
     =f(p)-\tfrac23 f(3p+2)-\tfrac13 f(3p-2).                       \tag{1}
\]
The two signs have actual representatives \(2p+1\) and \(4p-3\), by applying their first odd steps. For positive odd \(p\), the children at exponents \(e+2\) and \(e\) have the same label since \(v_{e+2}(p)=4v_e(p)+1\) and \(S(4v+1)=S(v)\). Thus the minimal representatives alone have the exact two probabilities in (1). In the odd index \(u=(p-1)/2\) these representatives append the binary words \(1\) and \(00\), while appending \(10\) preserves the label.

Assume the bounded alternative, let \(s\) be the global least bad positive integer, and let \(z\) be the original least \(17\bmod48\) bad canonical source with \(3z\) good. Use the established inputs that \(s\equiv1\bmod9\) is the minimum of a bad odd cycle with exponent set contained in \(\{1,2\}\), every phase is less than \(8(2s+1)/3\), the verified floor is \(s>2^{71}\), and \(243(z-1)\le1024(s-1)\). The least-multiple and interval orientation results imply that \(z\) is the least bad canonical integer outright and \(k=v_2(z-1)\) is odd and at least five. [Original canonical floor](../descent/ORIGINAL_CANONICAL_FLOOR.md) · [Global minimum and neighbors](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md)

## First loss and the actual original parent

All odd \(p<s\) have \(d(p)\le0\). For all odd \(p<(s+2)/3\), both neighbors in (1) are below \(s\), so \(d(p)=0\). The earliest nonzero charge is **exactly**
\[
             p_*=(s+2)/3,\qquad d(p_*)=-1/3.                         \tag{2}
\]
Indeed \(3p_*-2=s\), and \(3p_*+2\) has the smaller good predecessor \(2p_*+1<s\). The same calculation gives \(d(p)=-f(3p-2)/3\) for every odd \(p\) with \(2p+1<s\). The minimum must have \(s\equiv3\bmod4\) since an odd successor of \(s\equiv1\bmod4\) would be below \(s\). At \(p=(s-1)/2\), the odd-sign representative is \(s\) and \(4p-3=2s-5\) is a multiple of three below the first bad triple \(2s+1\). Hence \(d((s-1)/2)=-2/3\).

At the **original supplied** input take
\[
 p=(z+3)/4,\qquad p\equiv1\bmod8,\qquad
 p\le1+(256/243)(s-1),\qquad d(p)=-1/3.                             \tag{3}
\]
Here \(S(p)\le(3p+1)/4<s\). For \(p=8u+1\), direct shortcuts give \(T^3p=T^3(3p+2)=9u+2\), while \(3p-2=S(z)\) is bad. Thus **all** the even-indexed ordinary children of \(p\) are bad, starting at \(v_2(p)=z\), and **all** the odd-indexed ones are good.

For every odd \(x\) with \(e(x)=2\) put \(R(x)=f(x)-f(3x)\). Then
\[
                  d(4x+1)=\{R(x)+2R(Sx)\}/3.                        \tag{4}
\]
Indeed \(S(4x+1)=S(x)\); the lower neighbor \(12x+1\) has the label of \(3x\) by the same lift. The upper neighbor \(12x+5=16Sx+1\) has the label of \(3Sx\): two pairs of shortcuts from it reach \(9Sx+1\), and one more halving agrees with \(T(3Sx)\). In (4), therefore, \(d(4z+1)\ge1/3\). When \(k\ge7\), \(Sz=1+3(z-1)/4\equiv1\bmod16\) is bad, and the interval orientation at \(Sz<z\) gives \(3Sz\) good. In this case \(d(4z+1)=1\). Notice that \(4z+1\) is itself a multiple of three, so being bad here gives no branching into genuine odd predecessors. None of these outward charge changes includes a smaller bad canonical source.

## Exact reciprocal-weight boundary flux

For \(X\ge1\) define the nonnegative outgoing term
\[
 B_X=\sum_{\substack{p\le X<v_e(p)\\p\ {\rm odd},\ e\ge1}}
                      {2^{-e}\over p} f(v_e(p)).
\]
All children satisfy \(v_e(p)\ge p\). Regrouping the absolutely summable child rows at the finitely many \(p\le X\) gives the exact identity
\[
 \sum_{\substack{p\le X\\p\ {\rm odd}}}{d(p)\over p}
  =\sum_{\substack{v\le X\\v\ {\rm odd}}}
        f(v)\left({1\over v}-{2^{-e(v)}\over D(v)}\right)- B_X.    \tag{5}
\]
Let \(a_e=(2(-1)^{e+1}-2^{-e})/3\), so \(v_e(p)=2^e(p+a_e)\). Its coefficient in the first sum equals \(-2^{-e}a_e/[p(p+a_e)]\). Whenever \(f(v_e(p))=1\), the ordinary terminal \(3p\pm2\) is bad, so \(p\ge(s-2)/3\). Thus the interior correction has absolutely summable total variation \(O(1/s)\), uniformly for all such floors, all cutoffs \(X\), and every subset of the bad components. In particular, the positive single-site charge at \(4z+1\) cannot be identified with the full compensation of (3).

If the odd label \(f\) possesses a natural mean \(b\), then
\[
                               B_X\longrightarrow b\log 2.           \tag{6}
\]
The known fixed-additive-shift fusion estimate implies \(f(v+2h)=f(v)\) except on a density-zero set for every fixed integer \(h\) on positive odds. Therefore every fixed dyadic subprogression of odd inputs has relative mean \(b\): bounded translation compares any two classes at the same modulus. The labels \(f(3p+2)=f(2p+1)\) and \(f(3p-2)=f(4p-3)\), over odd \(p\), consequently have mean \(b\). For fixed \(e\), partial summation on \(X/2^e-a_e<p\le X\) gives the contribution \(2^{-e}b e\log2/2+o_e(1)\). The absolute contribution is \(O(2^{-e}(1+e))\) uniformly in \(X\), using the harmonic sum on that window (and \(\log X=O(e+1)\) when the lower endpoint is small). Summing proves (6). The factor \(1/2\) in the window count is essential since \(p\) ranges over odd integers. This argument assumes a mean for the specified label, it does not deduce a mean for a union of components. [Fixed-shift fusion input](https://rstation.ai/problems/collatz/papers/13)

## A period-sized deficit at the original absolute floor

Let \(P\) be the odd period of the distinguished bounded cycle and let
\[
                  L_s=-\sum_{\substack{p<s\\p\ {\rm odd}}}d(p)/p .
\]
One has \(L_s\ge 1/(s+2)+4/[3(s-1)]\) by (2) and its second explicit charge. In addition there are absolute constants \(c>0,C<\infty\) with
\[
                              L_s\ \ge\ (cP-C)/s.                      \tag{7}
\]
For the sharper asymptotic constant at candidates in the pinned grid estimate, use \(y<8(2s+1)/3\) on the cycle. A phase \(y\ge3s-2\) has \(\log_2(y/s)\bmod1\) in the projection of a single real interval of length
\(\log_2(8(2s+1)/(3(3s-2)))<9/10\) at the verified floor. The pinned rank estimate gives the \(P\) residues \(\log_2(y/s)\bmod1\) within circular distance \(1/(2P)\) of the distinct points \(j/P\). A circular interval of length \(9/10\) can then cover at most \(9P/10+3\) phases. Each remaining \(y<3s-2\) is a unit and has the form \(3p\pm2\) for one odd \(p<s\). It contributes at least \(1/(3p)>1/(3s)\) to \(L_s\). If two phases use the same parent their distinct signs both appear in (1), with their individual positive weights. Thus one may take \(c=1/30,C=1\). [Pinned normalized rank estimate and its constants](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md)

There is an independent bound \(L_s\ge P/(36s)\) at **every** candidate above the stated verified floor. Write \(\xi_j=\log_2(y_j/s)\bmod1\) on the actual periodic sequence. Each step advances by \(\log_2 3+\log_2(1+1/(3y_j))\) modulo one, independently of its native exponent. The integer inequalities \(2^{19}<3^{12}\) and \(3^{17}<2^{27}\) bracket \(\log_2 3\) between \(19/12\) and \(27/17\), whose difference is \(1/204\). The positive correction is less than \(1/10000\). Thus in twelve consecutive phases the points equal a rotated twelve-grid, in permuted order, with individual shifts in \([0,11(1/204+1/10000)]\). Every circle gap in the resulting set is at most \(1/12+11(1/204+1/10000)<3/20\): each grid point moves only forward by the stated one-sided bound. The arc occupied by all \(y\ge3s-2\) has length less than \(17/20\), since the height ratio above is less than \(179/100\) and \(179^{20}<2^{17}100^{20}\). Its complementary gap is too long to avoid throughout a block of twelve. Counting all \(P\) cyclic starts, each low phase occurs in exactly twelve windows with multiplicity, giving at least \(P/12\) low phases. The same charge argument gives \(P/(36s)\) without the high-period normalized-grid input.

Equations (5) and (7), with no assumption on a mean, force
\[
              B_X+\sum_{\substack{s\le p\le X\\p\ {\rm odd}}}d(p)/p
                        \ \ge\ (P/30-O(1))/s \qquad(X\ge s).         \tag{8}
\]
The independent bound gives \(P/36\) in place of \(P/30\) above the verified floor. This charges the very first bad floor, including an entire subset of its actual cycle, against the later ordinary current and its boundary. Either term on the left can contribute. A contradiction would require an upper bound *jointly* on those two terms with the original floor retained. When (6) applies its nonzero boundary contribution is explicit.

[OriginalCurrent.lean](OriginalCurrent.lean) verifies the lifted shortcut and three-clock component identities, the first-charge sign and all preceding zeros, (4), and the exact rational reciprocal coefficient. [Strict axiom receipt](../../../reports/astra-sixhour-20261127/transport/original-current-lean.txt). Equations (5)–(8) are written proofs.

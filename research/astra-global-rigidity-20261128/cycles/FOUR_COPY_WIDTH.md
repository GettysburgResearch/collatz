# Every cycle pays the four-copy cost of the two-grade matching

**PROPOSED written theorem, using the fixed-place Subspace Theorem.** Let \(p,s,X,q\) be the primitive odd period, real minimum, real maximum and complete reduced denominator of a positive rational Syracuse cycle. Native exponents are arbitrary positive integers. Fix \(2\le R\le4\), and let
\[
  a=\log_2(3/2),\qquad \eta=\log_2(R/2),\qquad f=(\eta-a)_+,\qquad
  \chi(R)=\frac{(\eta-2f)\log6+f\log15}{3\log3}.
\]
For any \(\epsilon>0\), uniformly over \(q\), the number of distinct odd states in \([Y,2Y]\) on **all** positive rational cycles of this one reduced denominator and width \(X/s\le R\) is
\[
                         O_{R,\epsilon}(qY^{\chi(R)+\epsilon})
                  \qquad (Y\ge2).                                    \tag{1}
\]
Consequently every such cycle satisfies \(p\ll_{R,\epsilon}q(1+s)^{\chi(R)+\epsilon}\). In particular every sequence of *ordinary* cycles of growing period and width \(X/s\le R+o(1)\) obeys
\[
   \limsup\frac{\log p}{\log s}\le\chi(R),\qquad
   0<H/p-\log_2 3\le p^{-1/\chi(R)+o(1)}\quad(\chi(R)>0),             \tag{2}
\]
where \(H\) is the sum of the native exponents. The second conclusion bounds the particular rational clock of each candidate. At \(R=3\) the required approximation exponent is greater than \(3.14\); at \(R=4\) it is greater than \(2.30\). An estimate for the number of allowed words at fixed total length alone would not imply (2).

Weaver 145/v1 already proves the full two-grade product, the exact ordered energy on singleton and matching components, the backwards ternary decoder, and the four-segment source separation. At physical width four the exponent here is exactly its previously established height-one exponent. The additions are the physical-width-dependent thinning of available sites below four, the complete-denominator outer arcs, the limiting endpoint for widths tending to four, and the higher-moment comparison below. [Weaver 145/v1, §§2–6, especially Lemmas 3–4 and §5](https://rstation.ai/problems/collatz/papers/145/v1)

## The matching determines its additive energy exactly

Fix an intercept for the homogeneous calendar in [the exact width formula](EXACT_WIDTH_ENTROPY.md). If \(F_i=\lfloor t_0+i\log_2 3\rfloor\) and \(g_i\) is the grade, the cumulative valuation of a word with fixed initial grade is \(E_i=F_i+g_0-g_i\), taking \(0\le t_0<1\). In a local segment of length \(l\) beginning at \(j\) set \(r_i=E_{j+i}-E_j\) and
\[
                       C=\sum_{i<l}3^{l-1-i}2^{r_i}.
\]
Once the segment's initial grade is fixed, \(r_i=v_i-g_{j+i}\) with \(v_i=F_{j+i}-F_j+g_j\ge0\). Multiplying by two gives \(2^{r_i+1}=2^{v_i}(2-g_{j+i})\) at grades zero and one.

In any equality \(C_1+C_2=C_3+C_4\), the signed bit difference at the final nonfixed position is in \([-2,2]\). Reduction modulo three forces it to be zero because \(2^{v_i}\) is a ternary unit. Iterate back through all positions. Thus equality holds **exactly when the two summed grade arrays agree at every position**. A singleton with two possibilities has ordered pair energy six. A matched pair permits \(00,10,11\). The sum of two such two-bit vectors determines their unordered multiset: the three doubletons have one ordering, and the three unequal pairs have two. The energy is \(3+3\cdot4=15\). For the full product on \(A-2F\) singletons and \(F\) matched pairs the energy therefore equals
\[
                              6^{A-2F}15^F.                            \tag{3}
\]
Forced grades and fixed endpoint constraints can only reduce the count. One matching edge crossing a segment boundary can be dropped at a constant factor. The exact singleton/pair energy and decoder, including valuation three, are Weaver's. PR200 uses the same decoder for an additional restriction to binary native valuations. Below four, the moving physical cut determines which of these previously identified sites and edges survive.

## Four actual source segments and their common clock

For an odd rational phase \(y_0\in[Y,2Y]\) of a cycle of width at most \(R\), every actual odd state is at least \(Y/R\). The exact physical equations give, on a window of \(b=O(\log Y)\) odd edges,
\[
  j\log_2 3-E_j=\log_2(y_j/y_0)
      -\sum_{i<j}\log_2(1+1/(3y_i)).
\]
Hence the range of the left side across the window is strictly below \(\log_2R+d_Y\), with \(d_Y=O_R((\log Y)/Y)\) taken positive and slightly enlarged. Translate its minimum to zero as in the width proof. There are \(O(b+1)\) possible phase cells for all floor, availability, and endpoint tests at the two widths. Relative to width \(R\), only \(o(b)\) dates have any extra allowed grade, uniformly in the initial phase, by irrational rotation equidistribution applied first to a fixed small neighborhood of the limiting cut. This permits grade two near the bottom phase when \(R=4\). Condition on all grades there, using at most \(3^{o(b)}\) choices for sufficiently large \(Y\). Their contributions in a four-sum cancel identically, even when a grade equals two: one may multiply all numerators by four to treat the other dates with integral coefficients. Drop the at most \(2o(b)\) matching edges incident to these dates, at cost \(\exp(o(b))\) in a counting bound. On every segment of length comparable to \(b\), (3) and uniform equidistribution give the upper bound
\[
             \exp\!\left(l[(\eta-2f)\log6+f\log15]+o(l)\right)        \tag{4}
\]
on its ordinary four-sum collision count. The same argument applies to a sequence of widths \(R+o(1)\) at \(Y\to\infty\); its exceptional phase arc still shrinks to zero. The fixed-width statement (1) has uniform constants at the specified \(R\).

Here are the source variables and the separation step. Fix \(\sigma>0\) small, \(l=\lceil(\log_3(2Y))/3\rceil\), \(g=\lceil\sigma l\rceil\), \(b=4l+2g\), and \(h=\lfloor(1+\sigma/2)(\log_2 3)l\rfloor\). Take four adjacent \(l\)-edge segments starting at \(j=g,g+l,g+2l,g+3l\). Fix the whole phase cell, the five segment endpoints and the two window endpoints, the guard grades and the exceptional grades just described. These choices cost \(\exp(O_R(\sigma l)+o(l))\). For the total \(K=E_b\), each segment's start \(u=E_j\), local length \(T=E_{j+l}-u\), remaining binary clock \(m=K-u\) and terminal odd count \(v=j+l\), the fixed-width strip yields
\[
 K-h\ge\log_2(2Y),\quad m\ge h,\quad v\log_2 3\ge h,\quad
 T\le h-c_\sigma l .
\]
These hold uniformly for large \(Y\), since every \(E_i=i\log_2 3+O_R(1)\). The local numerator \(C\) is \(O_R(l\,2^T)\) by the same bounded differences on each suffix. Conditional values of \(u,K,T,v\) are fixed.

The normalized canonical source of the whole word modulo one is
\[
  S=\frac{[-\sum_{i<b}2^{E_i}3^{-i-1}]_{2^K}}{2^K}.
\]
Its contribution from this segment is \([ -3^{-v}C]_{2^m}/2^m\) modulo one. Quantize this last number by the floor of \(2^h\) times it, modulo \(2^h\). A four-sum collision of its quantized values gives an integer \(Z\), congruent to the signed sum of the four residues modulo \(2^m\), with \(|Z|\le4\,2^{m-h}\). Writing \(D\) for the corresponding signed sum of the four ordinary local numerators, we have
\[
     D=2^m A-3^v Z,\qquad |D|\ll_R l\,2^{h-c_\sigma l},\qquad
     |A|=O_R(3^v).
\]
The fixed-place integral Subspace Theorem forces \(D=0\) for sufficiently large \(l\), with ineffective onset. Explicitly apply it to \(U=2^m A,V=3^vZ\), with forms \(U-V,V\) at infinity and the coordinate forms at 2 and 3. The product is at most \(|D|\,|V|\,2^{-m}3^{-v}\ll_R l2^{-c_\sigma l}\), and the maximum coordinate is \(\exp(O_R(l))\). Zero coordinates already give \(D=0\) at large \(l\) since both divisors exceed \(2^h\). On the finitely many exceptional rational lines with both coordinates nonzero, \(|D/V|\to0\) since \(3^v\ge2^h\); only the diagonal can persist. This is the same source separation used at the two frozen four-segment papers. [PR201 physical placement and separation](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FOUR_COPY_TAILS.md) · [PR200 binary equality decoder and four bridges](https://github.com/GettysburgResearch/collatz/blob/2346db2d49030ef385b73e1ee3e27dcbff86d2d9/research/six-hour-20261127/cycles/FOUR_BRIDGE_BINARY_CYCLE_BOUND.md) · [Bilu, Theorem 2.3](https://www.numdam.org/item/AST_2008__317__1_0.pdf)

Thus the four-energy of each segment's quantized counting measure is at most (4). For four different segments, Fourier inversion and Hölder on \(\mathbb Z/2^h\) bound any convolution atom by the geometric mean of those four energies. Cartesian products of the allowed interiors enlarge the physical set and require no independence of actual cycle states. An arc of length \(2^{-h}\) for their *unquantized* sum costs at most six such atoms, including the four floor errors. Guards give a fixed translation.

For an actual numerator \(N=qy_0\) one has \(N\equiv q2^K S\pmod {2^K}\). Hence \(y_0/2^K=S+j/q\) for some integer \(j\) among \(O(q)\) possibilities, using \(0\le S<1\) and \(Y\le y_0\le2Y\le2^K\). For each \(j\) this forces \(S\) into a specified arc of width \(Y/2^K\le 2^{-h}\); each fixed full word and \(j\) gives at most one numerator. **The denominator affects only these outer arcs.** The separation estimates for the four local measures do not depend on \(q\).

Multiply (4) by the outer choices and the \(O(q)\) arcs. Since \(l=(\log Y)/(3\log3)+O(1)\), taking \(\sigma\) sufficiently small for a prescribed \(\epsilon>0\) proves (1). Sum dyadic shells up to \(Rs\); the positive \(\epsilon\) handles even \(\chi=0\), and the odd states below height two number \(O(q)\). This proves the pathwise bound. For \(q=1\) a growing primitive period forces \(s\to\infty\); the exact angle clock \(0<H/p-\gamma\le(3s\log2)^{-1}\) gives (2).

## Denominator and continued-fraction consequences

Using the published Bondareva–Luchin–Salikhov inequality gives \(s\ll p^{5.116201}\) on the real-minimum branch \(s\ge1\), since \(H\ll p\) there. For \(s<1\) the bound \(p=O_R(q)\) is immediate by distinct numerators. Thus every cycle in (1) satisfies
\[
             q\gg_{R,\epsilon} p^{\,1-5.116201\,\chi(R)-\epsilon}.
\]
This can force denominator growth only where the exponent is positive. [BLS, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

Since \(\chi(4)<1/2\), (2) gives a power improvement on ordinary Dirichlet approximation throughout the band up to four. On reduced clocks \(H/p\) such candidates must be upper continued-fraction convergents, by the elementary \(1/(2p^2)\) criterion; moreover the following partial quotient is at least \(p^{1/\chi(R)-2-o(1)}\) by the convergent error bounds. Even without assuming that the clock is reduced, (2) applies to its displayed \(p\).

**Source-qualified width consequence.** If \(\mu(\log_2 3)\le3\), then for each fixed
\[
 R<R_3=2\cdot 2^{(\log3-a\log(12/5))/\log(5/2)}
\]
there are only finitely many ordinary cycles of width at most \(R\). This follows because \(\chi(R)<1/3\) throughout \(2\le R<R_3\); smaller widths are included at \(R=2\). The reduced denominator of \(H/p\) is at most \(p\) and must tend to infinity when \(H/p\to\gamma\), so reduction preserves the contradiction. Chudnovsky, arXiv:2610.28079v1 Theorem 11.1, states the exponent bound for positive multiplicatively independent rationals; its appendix A.5 records the author's compiler and axiom evidence. The present packet has not independently rebuilt that external formalization. The unconditional clock restriction (2), the exact energy, and the denominator census use no exponent-three input. [Chudnovsky, Theorem 11.1 and appendix A.5](https://arxiv.org/html/2610.28079v1#S11)

## What higher collision moments can see

For \(2k\) signed copies, write \(\Delta_i=\sum_{u\le k}g_i^u-\sum_{u>k}g_i^u\). Fixed calendar, endpoint grades and all exceptional digits as above reduce exact equality to
\[
               \sum_{i=0}^{l-1}3^{l-1-i}2^{F_i}\Delta_i=0 ,
 \qquad F_0=0,\quad b_i=F_{i+1}-F_i.
\]
The exact recognizer takes integral values \(z_0=z_l=0\) and obeys
\[
                    2^{b_i}z_{i+1}=3z_i+\Delta_i .
\]
Indeed, the partial sum through \(j-1\), using powers \(3^{j-1-i}\), is divisible by \(2^{F_j}\): multiply by the odd factor \(3^{l-j}\) and subtract the remaining terms of the total zero. Divide by \(2^{F_j}\) to obtain \(z_j\); the converse follows by telescoping. Since \(|F_j-F_i-(j-i)\gamma|\le1\), this also gives \(|z_j|\le 2kj\). This recognizer is valid at all orders irrespective of whether nonzero carries occur.

Coordinatewise equal signed sums always contribute. On a singleton the two possible grades are affinely independent; on a matching edge the three grades \(00,10,11\) are affinely independent. Thus the local site-diagonal count for \(k\) versus \(k\) copies on a cell with \(d\) configurations is
\[
 M_k(d)=\sum_{n_1+\cdots+n_d=k}\binom{k}{n_1,\ldots,n_d}^{\!2}.
\]
This gives a lower bound \(M_k(2)^{A-2F}M_k(3)^F\) for the entire collision energy, even when there are additional carry collisions. Here \(A\) is the number of active bits and \(F\) the number of matched pairs. The equality \(M_k(d)=\int_{\mathbb T^d}|\sum_{j=1}^d e^{2\pi ix_j}|^{2k}\,dx\) proves log-convexity in \(k\). Now \(M_2(2)=6,M_3(2)=20\) and \(M_2(3)=15,M_3(3)=93\); in both cases \(M_3(d)^3>M_2(d)^5\). Hence log-convexity gives \(M_k(d)^{1/(2k-1)}\ge M_2(d)^{1/3}\) for all \(k\ge2\) (use the slope of the secant from 2 to 3). The \(k=1\) inequality follows from \(d^3\ge M_2(d)\).

In the equal-length, single-resolution generalization of the four-segment proof, the local alphabet needs \(h\ge\gamma l-o(l)\) bits of resolution, while the outer source arc requires \(K-h\ge\log_2Y\). At zero guard density this gives \(l\ge(\log Y)/((2k-1)\log3)-o(\log Y)\). Consequently the local Hölder collision cost alone is at least \(Y^{\chi(R)-o(1)}\), at every fixed even moment. This is a limitation of that full-product equal-length energy argument. It leaves open estimates that exploit correlations between actual segments, signed Fourier cancellation at a specific target, unequal placements, or several arithmetic places simultaneously.

Extra collisions really can enter at six copies. For \(R>27/8\), choose a rotation intercept sufficiently close to zero from above. The four consecutive dates have increments \(b=(1,2,1,2)\), and all four active bits are available since their largest phase tends to \(3a-1<\eta\). The allowed configurations on positions \((0,1)\) and \((2,3)\) are \(00,10,11\). Use the three rows \(1110,1010,0000\) on one side and \(0011,0011,0011\) on the other. The difference of their coordinate sums is \((2,1,-1,-3)\); its scalar product with the true clock weights \((27,18,24,16)\) vanishes. Zero grades before and after this block are compatible with every row because the incoming and outgoing edges wrap. Thus the carry is genuine at common surrounding endpoints. For \(R\le3\), successive active sites have binary dates separated by at least two: if they are consecutive odd dates they must be separated by a wrapping increment of two. At the earliest differing active site modulo four then forces \(\Delta_i=0\) even for three against three. The site-diagonal moment cost already increases there.

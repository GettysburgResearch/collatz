# A shrinking interval below four

**Source-qualified written theorem.** Fix any positive constant \(C\). Only finitely many primitive positive ordinary cycles of least odd period \(p\), minimum odd state \(m\) and maximum odd state \(X\) can satisfy
\[
                     X/m\le 4-Cp^{-1/25}.                              \tag{1}
\]
More generally one may replace \(1/25\) by any fixed \(0<\sigma<1-3d_*/\gamma=0.0408865\ldots\), where \(d_*\) is specified below. In particular any sequence of distinct cycles satisfying \(X<4m\) has \(p^{1/25}(4-X/m)\to0\). This remains an asymptotic restriction and gives no effective largest exceptional period. The argument combines the physical Sidon register and the stated irrationality theorem used in [the fixed-margin proof](../phase6/FOURFOLD_ODD_SPREAD.md) with moving angular intervals and an entropy estimate for its unequal alphabets. For comparison PR213 gave a height-dependent approach to the lower threshold three through a different finite-difference mechanism. [PR213, 5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128, WIDTH_THREE_RATE.md](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE_RATE.md)

### Counting atoms in a moving angular interval

Suppose (1) holds on an infinite sequence, with exponent \(\sigma\) in the stated range. Then \(m,p\to\infty\), and \(m\gg p\) since the distinct odd states lie in \([m,4m]\). Their angles advance by \(\gamma+e_j\bmod1\) with \(0<e_j\le(3m\ln2)^{-1}\), where \(\gamma=\log_2 3\). Any angular interval of length \(l\asymp p^{-\sigma}\) contains \(\gg lp\) true phases uniformly in its location.

Indeed take the first convergent denominator \(q\ge16/l\) for \(\gamma\). The preceding denominator is less than \(16/l\); the usual convergent error estimate together with the stated irrationality exponent \(\mu(\gamma)\le3\) implies \(q\ll_\varepsilon l^{-2-\varepsilon}\). The \(q\) consecutive ideal rotation points starting at any initial angle are within \(1/q\) of the corresponding translated rational \(q\)-grid, since a convergent numerator \(h\) obeys \(|q\gamma-h|<1/q\). The genuine \(q\)-block incurs the additional pointwise angular error \(O(q/m)=o(l)\), since \(m\gg p\) and \((3+\varepsilon)\sigma<1\). Every such block contains at least \(lq/2\) phases of the interval for sufficiently large \(p\), by using only interior points of the rational grid. Splitting one chronological lap into disjoint complete blocks proves the count, since \(q=o(p)\). [Chudnovsky, arXiv:2610.28079v1, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)

In the folded octave take \(R_p=4-Cp^{-\sigma}\), \(v=(1-\log_2(R_p/2))/2\asymp p^{-\sigma}\) and \(L=2^{1-v}m\). Each angular end interval of length \(v/2\) contains \(\gg vp\) ranks. The left interval has only tag one because its labels are below \(2m\). The right interval has only tag two because its labels exceed \(X\). Doubling the left tags after a wrap makes them two. Thus for \(w=\lfloor c p^{1-\sigma}\rfloor\) and a sufficiently small fixed \(c>0\), every unwrapped span of \(w+1\) consecutive ranks starting at a fundamental rank has all its tags in \(\{1,2\}\). The strict sign propagation, weighted shift sum and physical dyadic register in the fixed-margin proof apply verbatim to these spans. The resulting \(B_2\) code of chronological length \(N=\log_3 m+O(1)\) has \(M=w+1\gg p^{1-\sigma}\) members, with \((a+o(1))N\) disjoint ternary pair blocks and \((s+o(1))N\) binary singleton blocks, where \(a=2-\gamma\) and \(s=2\gamma-3\). [PR214, f769b0c79059cc18b0be89e880ed6ea6a279e1c0, TWO_GRADE_SIDON.md](https://github.com/GettysburgResearch/collatz/blob/f769b0c79059cc18b0be89e880ed6ea6a279e1c0/research/astra-critical-rigidity-20261128/cycles/TWO_GRADE_SIDON.md)

### An entropy bound after shortening the paired coordinates

For a block with \(k\in\{2,3\}\) available symbols put
\[
 D_k=h_2(1/k)+(1-1/k)\log_2(k(k-1)).
\]
Use any \(t\) of the ternary blocks as a prefix. If its buckets have sizes \(n_i\), let \(S=\sum_i n_i^2\ge M^2/3^t\) and sample uniformly one of the \(S\) ordered pairs with common prefix, including diagonal pairs. Distinct nonzero ordered differences identify their pair; every diagonal gives zero. Thus the entropy of the entire suffix difference equals
\[
                    \log_2 S-(M/S)\log_2 M.                           \tag{2}
\]
Conditional on a fixed prefix, the two words are independent and uniform in its bucket. At each remaining block with alphabet size \(k\), their probability of agreement is at least \(1/k\), by Cauchy's inequality on its letter frequencies. The same lower bound survives mixing over the buckets with weights \(n_i^2/S\). There are at most \(k(k-1)\) nonzero differences, so the entropy of this block difference is at most \(D_k\). Indeed, conditional entropy off zero is at most \(\log_2(k(k-1))\), and the resulting binary-entropy expression decreases once the zero probability reaches \(1/k\). Subadditivity bounds (2) by the sum of these \(D_k\) over the suffix.

Pass to a subsequence with \((\log_2 M)/N\to r\). The elementary mixed-alphabet bound already gives \(r\le0.5249<a\log_2 3\). For \(r>0\) take \(t=\lfloor(r/\log_2 3-\epsilon)N\rfloor\) for any sufficiently small fixed \(\epsilon>0\). Then \(M/S\le3^t/M\to0\). Using (2), dividing by \(N\), and sending \(\epsilon\downarrow0\) gives
\[
 r\le d_*:=\frac{aD_3+sD_2}{1+D_3/\log_2 3}
 =0.50671960\ldots.                                                    \tag{3}
\]
This covers \(r=0\) as well. Here \(D_2=3/2\) and \(D_3=\gamma+\tfrac23(\gamma-1)+\tfrac23=5\gamma/3\). In particular
\[
 d_* =\tfrac38\left((2-\gamma)\tfrac53\gamma
                            +(2\gamma-3)\tfrac32\right).
\]
The last display involves only \(\gamma\). The interval \(1.58496250<\gamma<1.58496251\) suffices to certify \(1-3d_*/\gamma>0.04088>1/25\). This is a direct counting version of the classical coding-theoretic difference-entropy method, applied to the register's disjoint pair and singleton alphabets. [Della Fiore and Dalai, Discrete Mathematics 345 (2022)](https://doi.org/10.1016/j.disc.2021.112751)

Now \(M\gg p^{1-\sigma}\) implies \(\log m/\log p\ge(1-\sigma)\gamma/d_* -o(1)\). The exact ordinary product bound \(0<A/p-\gamma\le1/(3m\ln2)\) would give rational approximations of exponent strictly larger than three. This contradicts the same stated irrationality theorem and proves the claim.

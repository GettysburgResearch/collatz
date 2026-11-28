# Every real denominator rate occurs within a shrinking physical octave

**Proposed written theorem.** For each real \(0\le\lambda\le1\) there are primitive positive rational odd cycles of the genuine Syracuse map with odd period \(p\to\infty\), total valuation \(A\), minimum \(m\), maximum \(X\) and complete reduced denominator \(q\), such that simultaneously
\[
 \frac{\log_3 q}{p}\longrightarrow\lambda,\qquad
 0<A-p\log_2 3\le p^{-1+o(1)},\qquad
 m\ge p^{2-o(1)},\qquad
              X/m=2+O(p^{-1+o(1)}).                                    \tag{1}
\]
Here the last bound is two-sided about two, allowing physical widths slightly below or above it. More precisely the construction allows bounds \(2^{1-1/P-O(g/P)}\le X/m\le2^{1+O((K+g)/P)}\) at each stage described below. The true chronological degree \(r\) in the same construction satisfies \(r/p\to\lambda\), and one can simultaneously arrange \(\log_3 q/r\to1\) even when \(\lambda=0\). Thus a small fraction in (1) can coexist with an asymptotically maximal complete denominator at the spectral rank actually present.

The [prior independent-clock construction](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md) supplies prime-indicator marker switches, explicit denominators in that family, and a near-octave, nearcritical diagonal of rate zero. The [arbitrary rational denominator rate construction](../literature/EVERY_RATIONAL_DENOMINATOR_RATE.md) realizes every rational rate at common clocks and every real diagonal limit with the total valuation divided by grade tending to infinity. Here the width tends to two and the total valuation divided by odd period tends to \(\log_2 3\) at the rates in (1). The proof uses binary sheet masks that can activate one specified prime-power frequency level independently of the lower levels, and controls all numerical cancellation at the active modes by a short moving-binomial resultant. It does not require a bound for the number of physical order reversals.

## The exact rate for any finite list of binary sheet masks

Fix \(g\ge1\), distinct ranks \(j\) in \(\{1,\ldots,K\}\) and binary functions \(b_j:\mathbb Z/g\to\{0,1\}\). Assume their only common translation period in \(\mathbb Z/g\) is zero. An empty list is allowed at \(g=1\). Let \(\mathcal H\) be the union of the supports of their ordinary discrete Fourier transforms, with the trivial character always added. This union is Galois invariant. Write \(k=|\mathcal H|\). For every sufficiently large upper continued-fraction convergent \(B/P\) of \(\gamma=\log_2 3\), so \(0<B-P\gamma<1/P\), set \(p=gP,A=gB\). For \(0\le i\le p\) define
\[
  R_i=[iB]_P,\quad s_i=\lfloor i/P\rfloor\bmod g,\quad
  \epsilon_i=b_{R_i}(s_i)\ \text{on the marked ranks, zero otherwise},
                \qquad E_i=\lfloor iB/P\rfloor-\epsilon_i.             \tag{2}
\]
At any step entering a marked rank \(R_{i+1}\le K\), the unmarked floor increment is two for large \(P\): \(B/P\to\gamma\in(1,2)\) and \(K<B-P\), so the rotation by \(B-P\) must wrap. Every cumulative difference \(E_{i+1}-E_i\) is positive. The endpoints are \(E_0=0,E_p=A\). If the increments had a proper repetition factor \(h\), then \(h\mid(gP,gB)=g\). Advancing by \(p/h\) would add exactly \(A/h\) to the cumulative exponent, by summing the repeated increments, thus preserving each \(b_j\) after the same nonzero translation \(g/h\). This contradicts the common-period condition. The positive fixed point of the genuine affine word therefore has least odd period \(p\). For completeness, its phase-zero numerator over the determinant \(\Delta=2^A-3^p\) is \(M=\sum_{i=0}^{p-1}3^{p-1-i}2^{E_i}\). It and each rotated numerator are odd, the positive determinant is odd, and \(3x_i+1=2^{E_{i+1}-E_i}x_{i+1}\) with odd rational endpoint. Thus all native valuations are exactly those prescribed.

Let \(\mathcal A\) be the set of orders of the characters in \(\mathcal H\); Galois invariance gives \(k=\sum_{d\in\mathcal A}\varphi(d)\). For these cycles,
\[
          r=kP,\qquad \log q=kP\log3+O_{g,K}(\sqrt P+\log P)            \tag{3}
\]
at large convergents. Here are the details ensuring that a vanishing symbolic component and numerical cancellation at a surviving component are distinguished. Apply the algebra in the [cyclotomic component proof](SPARSE_PHYSICAL_INVERSIONS.md) directly to the explicit \(E_i\) in (2). This part needs only (2); it does not use its geometric inversion hypothesis. For a primitive \(d\)-th root \(\zeta,\ d\mid g\), and \(Pu+Bv=1\), the coefficient at \(R_i=j\) is
\[
     c_j=\sum_{i:R_i=j}2^{-\epsilon_i}\zeta^{v\lfloor iB/P\rfloor+ui}.
\]
At a fixed \(j\), the \(g\) indices are \(i_0+sP\), \(0\le s<g\), so the root-of-unity powers are one common unit times \(\zeta^s\). For \(d>1\), \(c_j\) is precisely a nonzero unit factor times \(-\sum_s b_j(s)\zeta^s/2\) at a marked rank, and zero elsewhere. Thus the corresponding \(L_d(T)=\sum c_j T^j\) is nonzero exactly at the nontrivial orders in \(\mathcal A\); the different ranks never need to be combined before taking that decision. Subtracting the constant nominal coefficient \(g\) for \(d=1\), then multiplying by \(T-1\) and replacing \(T^P\) by \(\zeta^v/2\), gives a short polynomial. At \(d=1\) its value at \(T=1\) is \(-g/2\). After clearing a factor two all these polynomials have bounded coefficients in every embedding and degree at most \(K+1\) (for \(d>1\) one can use \(2(T-1)L_d\)). These size bounds are fixed as \(P\) grows.

Every nonzero such polynomial is nonzero at all \(T\) with \(T^P=\zeta^v/2\) for sufficiently large \(P\). Indeed \(T\) is \(2^{-1/P}\) times a root of unity, and its degree over \(\mathbb Q^{\mathrm{ab}}\) is at least \(P/2\), greater than \(K+1\). The direct Fourier identity in the component proof therefore shows that the active chronological roots are exactly *all* \(P\varphi(d)\) roots of \(z^P=2^B/\zeta\) for each \(d\in\mathcal A\), as \(\zeta\) varies over that order. This proves \(r=kP\). In particular the minimal polynomial value satisfies
\[
        |f(3)|=\prod_{d\in\mathcal A}\Delta_d,\qquad
                     \Delta_d=3^{P\varphi(d)}\Phi_d(2^B/3^P).
\]

For every active component the same resultant proof, with fixed coefficient bound and fixed degree, gives
\(\log\gcd(M,\Delta_d)=O_{g,K}(\sqrt P)\): use \(H=\lfloor\sqrt P\rfloor\), so the Dirichlet exponent \(\ell=|bB-aP|\ll\sqrt P\) and both exponents \(a,b\ll\sqrt P\). The noncommon-root argument applies because reduced \(b\to\infty\) at the irrational slope. The full reduced \(q\) is a multiple of \(\prod_{d\in\mathcal A}\Delta_d/\gcd(M,\Delta_d)\) and divides \(|f(3)|\) by the [minimal recurrence divisor](MINIMAL_RECURRENCE_DENOMINATOR.md). Consequently the logarithm of its cancellation inside \(|f(3)|\) is \(O_{g,K}(\sqrt P)\). At an upper convergent each \(\log\Delta_d=P\varphi(d)\log3+O_g(\log P)\): for \(d=1\) the lower bound uses the classical finite irrationality measure, and for \(d>1\) use \(\Phi_d(1)>0\) and continuity. This proves (3).

The physical clocks also give the claimed height conditions. The total positive correction around one lap is
\(\Lambda=\sum_{i<p}\log(1+1/(3x_i))=(A-p\gamma)\log2=O(g/P)\).
On any prefix its correction is in \([0,\Lambda]\). Substituting \(E_i\) from (2) into the unfolded product thus gives, uniformly through one lap,
\[
               x_i/x_0=2^{R_i/P+\epsilon_i}\exp(O(g/P)).
\]
If marked, \(R_i/P\le K/P\); otherwise the exponent is less than one. Ranks \(0\) and \(P-1\) are both unmarked. This proves the width estimates in the opening statement. Since \(\Lambda\ge p/(3X+1)\), one also has \(m\gg P^2\) as long as \(K+g=o(P)\); the constants can be absolute in that range.

## A dense set of rates from genuine binary rows

Take an odd \(L\ge1,\ g=2^a L,\ a\ge2\), using the product coordinate on \(\mathbb Z/2^a\times\mathbb Z/L\). The row \(h_j\), for \(1\le j\le a\), is the indicator of the first half of the residues modulo \(2^j\). Its Fourier support consists exactly of the trivial character and all characters of exact order \(2^j\) on this two-power factor. This follows from the geometric sum of the first \(2^{j-1}\) powers: it vanishes on every other nontrivial level and has nonzero numerator on each odd frequency of the \(2^j\)-cycle. The row \(v\) which singles out zero modulo \(L\) has all \(L\) frequencies of that factor (constant for \(L=1\)). Its product \(v h_j\) has the Cartesian product of the two supports by the finite product Fourier formula.

Include \(v\) and \(h_a\) at distinct small physical rank positions. Their common translation stabilizer is trivial. At further distinct ranks optionally include \(v h_j\) for any \(1\le j<a\). The resulting \(\mathcal H\) consists of all \(L\) characters at the trivial two-power frequency, the \(2^{a-1}\) primitive two-power frequencies of the row \(h_a\) paired only with the trivial odd-factor frequency, and \(L\,2^{j-1}\) further frequencies for each optional level. Thus all the following fractions are realized at fixed finite sheets by (3):
\[
      \frac{k}{g}=\frac{L+2^{a-1}+L t}{2^aL}
                 =\frac{1}{2L}+\frac{t+1}{2^a},
                  \qquad 0\le t\le 2^{a-1}-1.                         \tag{4}
\]
All integers \(t\) in this range occur by binary expansion. For each odd \(L\) these possibilities are dense in the interval \([1/(2L),1/2+1/(2L)]\) as \(a\to\infty\). The closure of their union over \(L\), including \(L=1\), is \([0,1]\): \(L=1\) covers the upper half in closure, and the left endpoints tend to zero while all right endpoints are above \(1/2\). For a specified real target choose a sequence of finite mask choices approaching it. At each fixed stage then take an arbitrarily large upper convergent, ensuring \(g,K=p^{o(1)}\) in the resulting diagonal and that the fixed-stage error in (3) divided by \(r\) tends to zero. This uses no uniform onset for the finitely many cyclotomic resultants as the mask list varies. Since \(p=gP\), the width, height and total-clock estimates just proved yield (1).

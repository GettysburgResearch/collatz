# Four resonant defects and a continuum of full cycle denominator slopes

**PROPOSED elementary construction.** For every real \(\tau\in[1/2,2/3]\) there exists a sequence of primitive positive rational Collatz cycles with odd periods \(p\to\infty\), full determinants \(D\), and actual reduced phase denominators \(d\), satisfying
\[
 \frac{\log d}{\log D}\longrightarrow \tau .
\]
Each cycle has an exactly resonant proper odd-time window with **four** exceptional starts of both signs and largest spacing exactly \(p/3\). For the signed residual Z of that same window, \(\log\gcd(D,Z)/\log D\to2/3\), independently of \(\tau\). All phase values tend uniformly to infinity and the full real logarithmic drift tends to zero. Thus rational accumulation for the *sparse residual gcd* does not extend to actual phase denominators across exact resonance. All prime powers of the complete determinant are retained in the accounting below.

The independent-switch construction is prior. The frozen toric-window manuscript's two-switch family gives fixed-period fractions and equality examples. Here a growing family of independent base periods is invisible to one specified window; its complete set of active cyclotomic factors determines a continuously adjustable limiting fraction. [Prior near-full cancellation construction](https://github.com/GettysburgResearch/collatz/blob/ebf2682a0cefb8d66ef43c822f19ac4c1c97bbd4/research/unrestricted-cycle-denominator/NEAR_FULL_GCD.md)

## Block clocks and the four rows

Start with a finite nonempty set of distinct primes \(r_1,\ldots,r_s>3\). Set \(R=\prod_i r_i,\ n=6R,\ B=n/3,\ t_0=n/2,\ t_i=n/(3r_i)\) for \(1\le i\le s\), and \(L=s+1\). For now all these parameters are fixed. Choose arbitrarily late upper convergents \(b/a>\log_2 3\), with \(a-L>6,\ b-a-L>6\). For \(j\bmod n\), place L successive shortcut parity pairs in block j. In slot i write \(10\) if \(t_i\nmid j\), and \(01\) if \(t_i\mid j\), in the order \(i=0,\ldots,s\). Append \(a-L\) ones and \(b-a-L\) zeros. Each block contains a odd dates in b native steps. Thus \(p=an\), \(A=bn\), and \(D=2^{bn}-3^{an}>0\).

The transition with six consecutive ones immediately before it and six zeros immediately after it occurs once per block at a common offset. Across the encoded pairs both run lengths are at most two, and the long zero-to-next-pair seam cannot create a qualifying one-to-zero transition. Every period therefore advances a whole number of blocks. The independently recoverable slot labels then force that number to be a multiple of \(\operatorname{lcm}(t_0,t_1,\ldots,t_s)=n\), since \(\gcd(2,3r_1)=1\). The word is primitive in native and odd time.

Compare the window of \(v=aB\) odd dates with \(u=bB\) native steps. Shifting v advances exactly B blocks, so \(pu=Av\). Slot i's odd date has fixed inner offset \(2i+\mathbf1_{t_i\mid j}\); all odd dates after the pairs have fixed offsets. The B-shift preserves every slot except slot zero, since \(t_i\mid B\) for \(i>0\). The zero-slot changes at exactly \(j=0,R,3R,4R\bmod6R\). Their odd-time spacings are \(aR,2aR,aR,2aR\), giving \(m=4\), \(h/p=1/3\), and both signs.

The unique fixed point of the composed affine word is positive, and has odd denominator prime to six. The cyclic affine identities give the specified native and accelerated parities at every rotation: the carry numerator at a native phase has the parity of its current letter, while D is odd. A rational shortcut step preserves the reduced denominator since that denominator is prime to six. Thus the block-boundary denominator computed below agrees with the reduced denominator at each odd phase.

## Detecting the complete cyclotomic factors

Put \(P=3^a,\ Q=2^b,\ k_i=3^{L-1-i}4^i\). The block map is
\[
 Qx_{j+1}=P x_j+c_j,\quad
 c_j=c+3^{a-L}\sum_{i=0}^s k_i\mathbf1_{t_i\mid j}.
\]
Indeed one pair has numerator \(3x+1+\mathbf1_{t_i\mid j}\) over 4. Composition and the trailing ones and zeros give \(c=3^{a-L}(4^L+\sum_i k_i)-4^L2^{a-L}>0\) for sufficiently large a. Let \(F(X)=\sum_{j=0}^{n-1}c_j X^j\). One period gives
\[
 C=P^{n-1} F(Q/P),\qquad x_0=C/D.
\]

For each positive divisor \(\ell\mid n\), put \(M_\ell=P^{\varphi(\ell)}\Phi_\ell(Q/P)\). Every \(M_\ell\) is a positive integer prime to six, and \(\prod_{\ell\mid n}M_\ell=D\). At each primitive \(\ell\)-th root, \(\ell>1\), the common background c sums to zero. The sum over the multiples of \(t_i\bmod n\) has value \(n/t_i\) when \(\ell\mid t_i\), and zero otherwise. Consequently the **polynomial remainder in \(\mathbb Z[X]\)** is
\[
 F(X)\equiv 3^{a-L}K_\ell\pmod{\Phi_\ell(X)},\qquad
 K_\ell=\sum_{\ell\mid t_i}(n/t_i)k_i .
\]
The sum is strictly positive exactly when \(\ell\) divides one of the chosen periods. Denote these orders, including order one, by \(\mathcal A\). No cancellation between simultaneously active switches is possible at this step.

All \(\Phi_\ell\) for \(\ell\notin\mathcal A\) divide F jointly over \(\mathbb Z[X]\), by distinct irreducibility and monicity. Accordingly \(\prod_{\ell\notin\mathcal A}M_\ell\mid C\): evaluation at Q/P and clearing powers of P introduce only a unit modulo this product. For every active \(\ell>1\), one has \(\gcd(C,M_\ell)\mid K_\ell\). Even where factors share a prime, these imply
\[
 \frac{\prod_{\ell\in\mathcal A,\ell>1}M_\ell}
      {\prod_{\ell\in\mathcal A,\ell>1}K_\ell}
 \ \le\ d=\frac{D}{\gcd(C,D)}
 \ \le\ M_1\prod_{\ell\in\mathcal A,\ell>1}M_\ell.             \tag{C1}
\]
For the lower bound use \(\gcd(C,\prod m_j)\le\prod\gcd(C,m_j)\) for positive integers. The upper bound uses the joint polynomial divisibility; separate divisibility by each inactive factor would be insufficient.

Write \(d_{\mathcal A}=\sum_{\ell\in\mathcal A}\varphi(\ell)\). As the upper convergents grow, \(Q/P\to1\). For every fixed \(\ell>1\), \(\log M_\ell=\varphi(\ell)\log P+O_n(1)\), because \(\Phi_\ell(1)>0\). The remaining factor satisfies \(0\le\log M_1=\log(Q-P)\le\log Q=\log P+o(1)\). In particular \(\log D/\log P\) lies between \(n-1+o_n(1)\) and \(n+o_n(1)\). Equation (C1) therefore places \(\log d/\log D\) within \(O(1/n)+o_n(1)\) of \(d_{\mathcal A}/n\). The constants in the term \(o_n(1)\) may depend arbitrarily on the finite prime set. The subsequent diagonal choice is essential. No lower bound for a linear form in logarithms enters this construction.

## The actual interval of limits

Characters of the cyclic group of size n are indexed by \(j\bmod n\). The order of the j-th character divides \(t_i\) exactly when \(n/t_i\mid j\). Thus \(d_{\mathcal A}/n\) is the proportion of j divisible by 2 or by one of \(3r_i\). The Chinese remainder theorem gives
\[
 \frac{d_{\mathcal A}}n
 =\frac12+\frac16\left(1-\prod_{i=1}^s(1-1/r_i)\right).       \tag{C2}
\]
Finite nonempty prime sets with their smallest prime tending to infinity can make this product converge to any prescribed number in \([0,1]\). Indeed the positive numbers \(-\log(1-1/r)\) tend to zero and have divergent sum over primes: a bounded sequence of partial Euler products would bound all harmonic partial sums. In each sufficiently late tail take successive primes until their sum first exceeds the prescribed negative logarithm. The overshoot tends to zero. For target zero product choose sums tending to infinity, and for target one pick a single growing prime.

For fixed \(\tau\), select prime sets in this manner; then \(n\to\infty\). For each set choose a sufficiently late convergent that the finite-n errors above are at most \(1/n\), and \(a>n^2\). Since \(0<b-a\log_2 3<1/a\), the full drift \(n(b-a\log_2 3)\) tends to zero. Every odd phase x satisfies \(1+1/(3x)\le 2^{n(b-a\log_2 3)}\) by the positive cycle product. The intervening positive shortcut phases between odd dates are at least the smaller neighboring odd phase. Thus the minimum across the entire native cycle diverges. Equations (C1)–(C2) give the claimed \(\tau\).

## The residual keeps one rational slope

The comparator multiplies the input carry, up to a unit modulo D, by \((Q/P)^B-1\). The block-boundary and odd-phase carries also differ by a unit modulo D, since digit rotation multiplies by a power of two or three modulo D. Consequently \(\gcd(D,Z)\) is given by evaluation of \((X^B-1)F(X)\) at Q/P up to such a unit. This uses the prior exact cyclic difference, valid even when the multiplier shares factors with D. [Weaver, Mahler and Wren, Paper 22 v4](https://rstation.ai/problems/collatz/papers/22/v4)

All factors \(\Phi_\ell\) except those with \(\ell\mid t_0,\ \ell\nmid B\) divide the product polynomial jointly. At a remaining order its reduction is \(3^{a-L}K_\ell(X^B-1)\); here \(K_\ell>0\). Since \(\Phi_\ell\) and \(X^B-1\) are coprime over the rationals, their integral Bézout resultant is nonzero and depends only on n. After evaluation and clearing powers of P, the gcd with \(M_\ell\) is bounded by \(K_\ell\) times that fixed absolute resultant, including prime powers. The proportion of the remaining character orders, counted with their degrees, is the density of j with \(2\mid j,\ 3\nmid j\), namely \(1/3\). Applying the same full-product bounds and including their finite-n errors in the diagonal choice gives
\[
 \lim\frac{\log\gcd(D,Z)}{\log D}=\frac23 .
\]
Thus the maximum allowed ternary width is attained by the same four-row supports on which the original denominator fraction can approach every point of the stated interval. The changing clock gcd is n, and the window is exactly resonant throughout.

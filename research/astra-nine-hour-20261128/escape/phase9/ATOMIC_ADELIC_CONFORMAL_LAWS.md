# Finite atomic conformal laws with exact local arithmetic and positive real escape

Let \(F_0(t)=t/2,\ F_1(t)=(3t+1)/2\). On \(\mathbb Z_3\) their inverse branches are \(I_0(y)=2y\) everywhere and \(I_1(y)=(2y-1)/3\) on \(y\equiv2\bmod3\). Consider the unnormalized positive operator on finite measures
\[
      A\delta_y=\tfrac14\delta_{I_0(y)}
                   +\tfrac94\,1_{y\equiv2(3)}\delta_{I_1(y)}.       \tag{1}
\]
These are precisely the squared forward affine slopes. Haar probability \(h\) is fixed by (1). On a hypothetical positive ordinary escape basin let \(g(n)=1/P(n)\), with \(P\) the corrected height and \(g=0\) outside the basin. Then \(g(2n)=g(n)/2\), \(g(2n+1)=3g(3n+2)/2\), and \(g(n)\le1/n\). Consequently \(\sum g(n)^2\delta_n\) is a nonzero finite atomic fixed measure for (1). The same holds on the diagonal embedding into the real, binary and ternary coordinates. The reciprocal correction and its positivity on a simple ordinary path are the sole external inputs for this motivation. [Ordinary product and tilted trace](../phase8/TILTED_ORDINARY_REPRESENTATIVE.md)

**Unconditional theorem.** There are uncountably many mutually singular finite atomic fixed probabilities for (1), each supported on countably many nonrational ternary points. They lift to fixed probabilities on \(\mathbb R_{>0}\times\mathbb Z_2\times\mathbb Z_3\), with the ternary test in (1) and each affine inverse acting in all three coordinates. The deterministic forward parity at each atom is its binary parity, and its full forward real trajectory tends to infinity. Given any finite height \(K\ge1\) and precision \(N\ge1\), every real atom can be taken above \(K\). A distinguished atom then has real coordinate an ordinary positive integer \(t\), binary coordinate congruent to \(t\bmod2^N\) and ternary coordinate congruent to \(t\bmod3^N\). Every real coordinate is a positive rational with denominator a product of powers of two and three. The law on the ordinary diagonal is the part that (1) does not classify.

## A fractional bound for the full ternary Green sum

Let \(M_k(z)=(A^k\delta_z)(\mathbb Z_3)\). A length-\(k\) inverse word with \(p\) odd letters is legal on exactly one cylinder modulo \(3^p\). Its coefficient in (1) is \(4^{-k}9^p\). Successive inverse branches give this cylinder by taking the image of \(\mathbb Z_3\) under the forward affine word, whose linear multiplier is \(3^p/2^k\). Concavity gives, for \(0<q<1\),
\[
 \int M_k(z)^q\,dh(z)\le
          [4^{-q}(1+3^{2q-1})]^k.                                   \tag{2}
\]
The bracket is one at \(q=1\) and its logarithmic derivative there is \(\tfrac32\log3-\log4>0\). Fix \(q<1\) close enough that the bracket is less than one and \(9^q>6\). Then \(G(z)=\sum_{k\ge0}M_k(z)\) has finite \(q\)-moment by (2) and concavity. Its Haar expectation is infinite since every \(M_k\) has expectation one. The fractional exponent retains the full untrimmed Green sum almost surely.

## An exact inverse tree from the negative fixed point

Write \(D=\{v\in\mathbb Z_{\le-1}:\exists k,\ T^k v=-1\}\) with the ordinary shortcut parity map \(T\) on signed integers. For \(v\in D\), \(e(v)\) is the number of even ticks up to first hitting \(-1\). Further ticks at \(-1\) are all odd. In a reverse ordinary path from \(-1\), an even preimage doubles the magnitude and an odd preimage of \(-a\) with \(a\ge1\) has magnitude \((2a+1)/3\le a\). Hence \(|v|\le2^{e(v)}\). In particular at most \(2^e\) such \(v\) have \(e(v)=e\). Define
\[
 B(z)=\sum_{v\in D}9^{-e(v)}\delta_{v+3^{e(v)}(z+1)},\qquad
 z_j=-1+(3/2)^j(z+1).
\]
Its mass is constant, positive and at most \(\sum_e(2/9)^e\); the \(v=-1\) term is \(\delta_z\). Define the finite-word measure \(B_j(z)=(4/9)^j A^j\delta_{z_j}\). Since \(z_j\equiv-1\bmod3^j\), its legal length-\(j\) words are exactly those for \(-1\). These are in bijection with the signed integers \(v\) such that \(T^j v=-1\): ordinary reverse branches yield integers of their stipulated parities, and the forward dynamics are single-valued. Such a word has \(p=j-e(v)\) odd letters. Changing its starting target from \(-1\) to \(z_j\) adds \(2^j3^{-p}(z_j+1)=3^{e(v)}(z+1)\) to its final source. The normalizing multiplier leaves weight \(9^{-e(v)}\). Thus \(B_j(z)\uparrow B(z)\). If \(z_1=F_1(z)\), the finite formula gives \(AB_j(z_1)=(9/4)B_{j+1}(z)\), hence
\[
                            AB(z_1)=(9/4)B(z).                      \tag{3}
\]

For Haar \(z\), the distribution of \(v+3^e(z+1)\) has density at most \(3^e\) relative to \(h\). Thus
\[
 \int\!\left(\sum_{k\ge0}\|A^kB(z)\|\right)^q dh(z)
  \le \|G\|_{L^q(h)}^q \sum_e 2^e3^e9^{-qe}<\infty,                 \tag{4}
\]
where the norm is total mass. Define
\[
        V(z)=\sum_{k\ge0}A^k B(z),\qquad
        W(z)=V(z)+\sum_{j\ge1}(4/9)^j B(z_j).                       \tag{5}
\]
For almost every \(z\), these are finite positive atomic measures. We have \(AV=V-B\). By (3), applying \(A\) to the second sum adds exactly \(B\) to that sum. Therefore \(AW=W\), and normalization is available. Every atom is an affine image \(az+b\) with nonzero rational \(a\) and rational \(b\). All atoms are nonrational when \(z\notin\mathbb Q\). Distinct orbits of the countable rational affine group support mutually singular measures; the full-measure set of admissible \(z\)'s meets uncountably many such orbits.

## Positivity of every real inverse branch at every depth

For Haar \(z\), let \(D_k(z)\) be the maximum forward slope of a depth-\(k\) word whose inverse is legal at \(z\). Set \(D_0=1\). For \(1<p<2\) the legal-word count also gives
\[
                 \int D_k(z)^p\,dh(z)
                    \le [2^{-p}(1+3^{p-1})]^k.                     \tag{6}
\]
The bracket is strictly less than one between its values one at \(p=1,2\), by strict log-convexity (it is the sum of two distinct exponentials). For a legal inverse word write its forward affine action as \(x\mapsto a x+b\), \(a>0,\ b\ge0\). In outer-to-inner order its nonzero additive terms are half the slopes of the preceding prefixes. Every such prefix is legal at \(z\). Therefore
\[
       H_K(z):=\sup_{\text{all legal words}}(b+Ka)
          \le (K+\tfrac12)\sum_{k\ge0}D_k(z),\qquad H_K\in L^p(h)
\]
by (6) and Minkowski. In particular any real target \(r>H_K(z)\) has \((r-b)/a>K\) on **every** legal inverse path, including the empty word.

Fix \(1+\log_3 2<p<2\). Again the density of the translated image of Haar is at most \(3^e\). Consequently
\[
 \int\sum_{v\in D}\left[
   \frac{H_K(v+3^{e(v)}(z+1))}{3^{e(v)}}\right]^p dh(z)
     \le \|H_K\|_{L^p}^p\sum_e 2^e3^{(1-p)e}<\infty.                \tag{7}
\]
Fix a nonrational \(z\) satisfying (4) and (7). The supremum of all the ratios inside (7) is finite. Choose a positive integer \(t>K\) above that supremum. Impose \(t\equiv-1\bmod2^N,\ t\equiv z\bmod3^N\) by taking a sufficiently large representative of their coprime CRT class. Since \(|v|\le2^e\le3^e\), every real value \(v+3^e(t+1)\) exceeds \(H_K(v+3^e(z+1))\).

Lift the starting atom to \((t,-1,z)\). Follow all-odd forward branches, obtaining \((t_j,-1,z_j)\) where \(t_j=-1+(3/2)^j(t+1)\). The lifted analogue of \(B(z_j)\) places its mass for \(v\) at
\[
 (v+3^{e(v)}(t_j+1),\ v,\ v+3^{e(v)}(z_j+1)).
\]
Every equation in (3) results from the same affine words coordinatewise. On an \(I_0\) preimage the binary coordinate is even; on an \(I_1\) preimage it is odd. Forward application of the branch determined by that parity inverts the lift. The lifted positive series in (5) has the identical finite mass. All atoms of its Green term stay above \(K\) by the previous paragraph. In its second sum, \(t_j\ge t\), hence those atoms also have real coordinate above \(K\). An atom in \(B(z_j)\) reaches \((t_{j+l},-1,z_{j+l})\) in \(l\) physical ticks for any \(l\) such that \(T^l v=-1\), by the finite-word calculation. Every Green descendant reaches such an atom in finitely many additional ticks. Thereafter the real height tends to infinity along the all-odd ray. The real coordinates are rational with denominators supported on \(2,3\).

This construction uses the genuine squared slopes, ternary integral branches and binary parities. Its binary coordinates are negative rationals with odd denominator whose binary-parity trajectories reach \(-1\). Extra Green descendants need not have signed-integer binary coordinates. None can equal its positive real height as a rational number. In particular the positive-ordinary escape problem still demands control on the simultaneous diagonal, even under positivity above an arbitrary floor and arbitrarily long initial local agreement. No step provides an ordinary escaping source.

# Two positive padded returns at every proper reduced clock

Retain the notation of [the prior physical crossing theorem and its reconstruction](EVERY_SUBLAP.md). Thus \(p=gU\) and \(A=gN\) are the odd and halving counts of a primitive positive integer cycle, and \(g=\gcd(p,A)\). Write \(s=\min x_i\), \(X=\max x_i\). For each \(1\le k<g\), set \(t=kU\), \(n=kN\), \(D=2^n-3^t>0\). At a suitable pair of consecutive dates, both actual \(t\)-odd-step arcs can be padded by positive numbers of even letters to give positive rational cycles of clocks \((n,t)\). Their complete reduced denominators \(q_+,q_-\) satisfy
\[
 \operatorname{lcm}(q_+,q_-)=2^{n-o(n)},\qquad
 \min(q_+,q_-)\ge 2^{t-O(\log(2+n))}.                         \tag{1}
\]
Both statements are uniform in the ordinary cycle and in \(k\). If the physical width \(X/s\) is bounded by a fixed \(R\), both denominator losses \(D/q_\pm\) are bounded by \(R\). If \(X<16s\), both denominators equal \(D\) exactly. Each padded word has least period \(n\) whenever its denominator exceeds \(2^{n/2}\). In particular this holds simultaneously along any family with \(n\to\infty\) and \(t/n\ge 1/2+\eta\) for a fixed \(\eta>0\). For distinct ordinary cycles with minimum tending to infinity the ratio \(U/N\to\log_3 2>1/2\), by the cycle log identity. These two rooted words may belong to the same rational orbit.

## Exact integer losses

By the crossing theorem there is an \(i\) with
\[
 y=x_{i+t}=2^d x_i+r, \qquad 0<3r<2^d-1,\qquad S_{i+t}-S_i=n-d.
\]
Here \(d\le n-t\), since each of the \(t\) native odd transitions costs at least one halving. Put \(a=v_2(3x_i+1)\) and \(b=v_2(3r+1)\). Because \(0<3r+1<2^d\), one has \(b<d\) and \(v_2(3y+1)=b\). Dividing the two native transitions gives
\[
 x_{i+t+1}=2^{d+a-b}x_{i+1}-v,\qquad
 v=(2^d-1-3r)/2^b>0.                                                \tag{2}
\]
Thus \(r,v\) are odd, \(r,v<2^d\), and the next arc has deficit \(d'=d+a-b>0\). Both genuine arcs have a positive number of even letters available for formal padding after their last native transition. For the two unaltered carries \(C_+,C_-\) one gets precisely
\[
 C_+=D x_i+2^{n-d}r,\quad C_-=D x_{i+1}-2^{n-d'}v,
 \quad q_+=D/\gcd(D,r),\quad q_-=D/\gcd(D,v).                       \tag{3}
\]
Positivity of the second root follows also from its positive affine carry. The usual backwards parity test at the odd determinant realizes both padded words on rationals with odd denominator. Their valuation words, rotated into common order when \(t\ge2\), have the same first \(t-2\) entries and final pair \((a_{i+t-1}+d,a_i)\), respectively \((a_{i+t-1},a_i+d)\). For \(t=1\) a crossing would require \(n-d=a_i\) and \(x_{i+1}>8x_i\), which is impossible in one odd transition.

Equation (2) gives \(2^b v+3r=2^d-1\). Therefore
\[
 \frac D{\operatorname{lcm}(q_+,q_-)}=\gcd(D,r,v)\mid\gcd(D,2^d-1).    \tag{4}
\]
For \(1\le d\le n-t\), the positive rational \(S\)-units \(2^n3^{-t},2^d\) are multiplicatively independent since \(td>0\), and have heights \(O(n)\). Corvaja–Zannier, Corollary 1, equation (1.3), bounds the logarithm of the full gcd on the right of (4) by \(o(n)\) uniformly. At primes outside \(S=\{2,3,\infty\}\) the sum of positive local contributions is the full logarithmic gcd since \(D\) is coprime to six. The corollary permits all independent unit pairs once finitely many small inputs are discarded for each tolerance. The classical two-log lower bound gives \(D=2^{n-O(\log(2+n))}\) for \(D>0\), \(1\le t\le n\). Combining (3) and (4) proves (1). A proper repetition of length \(m\mid n\), \(m\le n/2\), forces the reduced denominator to divide the smaller positive determinant \(2^m-3^{tm/n}<2^{n/2}\), proving the assertion about primitivity. For \(X/s\le R\), one has \(2^d<y/x_i\le R\). For \(X<16s\), the crossing has \(d=3,r=1\), hence \(b=2,v=1\). [Corvaja–Zannier, Corollary 1](https://arxiv.org/pdf/math/0311030) · [Two-log source and height estimate](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE.md)

The sparse carry difference in (4) has antecedents in the division of differences of edited words. Here the ordinary orbit supplies the two adjacent dates, the exact signed distortions, and the bound \(d\le n-t\) at **every** proper reduced clock. [PR212, sharp edit discrepancy](https://github.com/GettysburgResearch/collatz/tree/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles)

## All dates at bounded physical width

For each date \(j\) let \(e_j=S_{j+t}-S_j-n\), let \(C_j\) be the genuine arc carry, and define the nonzero integer
\[
 H_j=2^{\max(e_j,0)}x_{j+t}-2^{\max(-e_j,0)}x_j .
\]
The odd denominators in (3) have the following uniform all-date extension at the level of residue divisors:
\[
          \gcd(D,C_j)=\gcd(D,H_j),\qquad
        |H_j|\ll_R U\min(k,g-k)\quad (X\le Rs).                       \tag{5}
\]
Indeed \(C_j=Dx_j+2^n(2^{e_j}x_{j+t}-x_j)\), and \(D\) is odd. Put \(\ell_h=\log(1+1/(3x_h))\), \(L=\sum_h\ell_h\). The natural logarithm \(z=\log(2^{e_j}x_{j+t}/x_j)\) is the arc sum of \(\ell_h\) minus \((t/p)L\). Both terms lie in \([0,t/(3s)]\), and replacing the arc by its complement negates \(z\). Hence \(|z|\le\min(t,p-t)/(3s)\). Distinctness of the positive odd states gives \(p\le X\le Rs\), so \(|z|\le R/3\). If \(e_j\ge0\), then \(|H_j|=x_j|e^z-1|\); otherwise \(|H_j|=x_{j+t}|e^{-z}-1|\). This proves (5). At dates with \(e_j>0\), the quantity \(D/\gcd(D,C_j)\) is an exact residue divisor; the original word has more than \(n\) clocks, so positive even padding alone does not realize that quotient.

For a concrete ordinary trajectory segment, \(47\) reaches \(377=8\cdot47+1\) in 17 odd transitions using 24 halvings. The next starting point \(71\) reaches \(283=4\cdot71-1\) in 17 transitions using 25 halvings. Appending three and two even letters respectively yields denominator \(2^{27}-3^{17}=5,077,565\) at both roots. This finite path shows the local crossing and even-padded returns can both occur in ordinary dynamics. The simultaneous source of all \(g-1\) imposed crossings is closure of the original cycle; the padded words by themselves supply no exclusion of that possibility.

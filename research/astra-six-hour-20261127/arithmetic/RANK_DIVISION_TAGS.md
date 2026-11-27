# A positive rank division can retain both native digit windows

Use the lifted ordered three-band labels \(Z_r\), marks \(c_r\), minimum \(s\) and mechanical clock \(B_j,b_j,r_j\) from [Rank division](RANK_DIVISION.md). Let \(n\ge1\) and \(B=B_n\). Fix an index \(0\le t\le n\). For prescribed \(k,\ell\ge0\) put \(M=2^k3^\ell\), and assume
\[
           t\ge\ell,\qquad B-B_t\ge k,\qquad 2^B\ge8Ms.
\]
There are integers \(e_0,\ldots,e_n\), depending only on these fixed data, whose positive linear image
\[
         V_r=\sum_{j=0}^n e_j Z_{r+r_j}
\]
has the following simultaneous properties at every rank:
\[
 0<V_r\le1+8Mn,\qquad \operatorname{den}(V_r)=d,\qquad
 V_r\equiv Z_{r+r_t}\pmod M .                                      \tag{1}
\]
For \(d>1\) the congruence is in \(\mathbb Z[1/d]\), and \(d\) is coprime to six. This holds for the actual integer coefficients of a common linear form across all translated windows.

On an ordinary cycle choose \(k\ge4\). The fundamental image has the same lowbit as its tagged target, which has lowbit at most eight including the seam. Let \(v_r\) be the odd part of \(V_r\), and let \(x\) be the true odd part of \(Z_{r+r_t}\). Then \(v_r\equiv x\bmod 2^{k-3}3^\ell\). In particular \(v_r\) has the same \(\ell\) incoming binary exponents as \(x\), through actual positive odd integers. It also reproduces any initial outgoing native word of clock at most \(k-4\). Each outgoing step uses the next residue modulo \(2^{a+1}\) to certify its exact exponent \(a\). Therefore the ordinary odd outputs occupy the two-child ternary tree of that depth; three in arithmetic progression must have spacing divisible by \(3^\ell\). This step uses the finite binary-past theorem in PR201. Positive integers with these two local certificates can already be obtained by direct CRT for an individual phase. Formula (1) gives a common linear form for all those phases and retains the complete denominator. [PR201, binary predecessor tree](https://github.com/GettysburgResearch/collatz/blob/860a67dedc860adcd82b964958d91b9e21d610f1/research/six-hour-20261127/arithmetic/TERNARY_PAST_ENTROPY.md)

## Specifying the coefficients

More generally take an integer \(u\) with \(1\le u\le M\) and targeted coefficients \(a_j\in\mathbb Z\) satisfying
\[
          u\equiv\sum_{j=0}^n a_j 3^j2^{B-B_j}\pmod M .
\]
First use the rank division construction with \(v_0=u2^{-B}\) and least residues \(k_j\equiv u3^{-(j+1)}\bmod2^{B-B_j}\). Its initial weights \(u_j=k_j/2^{B-B_j}\) lie in \([0,1)\); denote its integral coefficients by \(f_j\). Increase each \(u_j\), \(j<n\), by some integer \(w_j\in[0,M)\). This changes the coefficients to
\[
 e_0=f_0-3w_0,\quad
 e_j=f_j+2^{b_{j-1}}w_{j-1}-3w_j\ (0<j<n),\quad
 e_n=f_n+2^{b_{n-1}}w_{n-1}.
\]
Modulo \(2^k\) solve \(e_j=a_j\) in forward order up to \(n-1\), since 3 is a unit. The condition at \(n\) follows from the displayed target congruence and the unit \(3^n\). Modulo \(3^\ell\) work in reverse using the dyadic units, leaving \(e_0=a_0\) from the same congruence and the unit \(2^B\). Combine the two choices for each \(w_j\) by CRT. As before,
\[
   V_r=u2^{-B}Z_r+\sum_{j<n}(u_j+w_j)c_{r+r_j},\qquad
   2^B dV_r\equiv u\,dZ_r\pmod d .
\]
For (1) choose \(a_j=\mathbf1_{j=t}\) and \(u=M\). The bounds on \(t,B-B_t\) make the target congruence hold, and \(M\) is a unit modulo \(d\).

## Spatial reversals forced by an ordinary cycle

Take \(M=16,\ \ell=0,\ k=4,\ t=0\), and the least \(n\ge1\) with \(B_n\ge4\) and \(2^{B_n}\ge128s\). Thus the positive integers \(V_r\) have height \(H=1+128n\) and the exact native lowbit \(c_r\) at the **same** rank. This choice uses the multiplier 16, still a unit at every prime dividing \(d\). Extend \(V\) by doubling. The equality \(\operatorname{lowbit}(V_r)=c_r\) then also holds at every lifted rank.

For any proper offset \(0<t'<p\), no chronological run of equalities
\[
              V_{a+ih+t'}=V_{a+ih} \quad (0\le i<L)
\]
can have \(L>\log_2(16s)\), uniformly in the starting rank \(0\le a<p\). Indeed equal images force equal lowbits, so the native lifted gap \(G_b=Z_{b+t'}-Z_b\) obeys \(G_{a+Lh}=3^L G_a\). The strict rank order gives \(0<G_a<16s\), and \(G_{b+p}=2G_b\) makes \(2^{\lfloor(a+Lh)/p\rfloor}\mid G_a\). The exponent is at least \(L\). This proves the asserted limit. In particular, if two chronological output words of this length agree along with their relative octave normalizations, the starting ranks coincide.

Consequently for \(t'=1\) the number of fundamental \(r\) with \(V_{r+1}\ne V_r\) is at least \(p/(1+\lfloor\log_2(16s)\rfloor)\). Here chronological rotation visits every fundamental rank. The sum over \(r\) of those signed differences is \(V_p-V_0=V_0\le H\), and each has absolute value at most \(2H\). Once the preceding lower bound exceeds \(2H\), **each** strict spatial sign occurs at least
\[
                \frac{p}{8H(1+\lfloor\log_2(16s)\rfloor)}
\]
times. This is \(\gg p/\log^2(s+2)\) along growing bounded ordinary candidates. The result holds even when the starting labels have the strict convexity proved in PR200 for its canonical-height-one subclass. Recovering the correct ordinary lowbit from these small positive integers therefore still allows both spatial signs, and their native forcing need not be the ordinary mark. [PR200, strict rank convexity and its two-grade scope](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/cycles/STRICT_CONVEX_RANKS.md)

Below the least bad integer, positive tagged outputs are good. The native ternary past and the dyadic forward word recovered from them have finite length. Even the exact local energy extremizers can occur on one finite ordinary trajectory; the argument gives no ordinary return of a tagged output to the original bad component. [Finite binary-past cubes](BINARY_PAST_CUBES.md)

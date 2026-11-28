# Polylogarithmic residence at inverse log-log distance from a factor of two

**Proposed written theorem.** Put \(\gamma=\log_2 3\), fix a finite irrationality-measure bound \(\mu(\gamma)\le\mu_0\), and write \(\kappa=\mu_0-1\). All unmarked logarithms are natural. Fix \(\alpha>\kappa\) and \(0\le\beta<\alpha/\kappa-1\). For \(M\to\infty\), let \(x=\log\log M\) and
\[
    0\le\eta\ll x^{-\alpha},\qquad R=2^{1+\eta},\qquad
              \log(2Q)\ll(\log M)x^\beta .
\]
Every chronological run of \(T\) **distinct** positive odd rational Collatz states of common complete denominator \(Q\) prime to six, all in \([M,RM]\), satisfies
\[
                             T\le(\log M)^{3+o(1)} .                    \tag{1}
\]
In particular this holds for all ordinary positive orbits and for \(Q\) polynomially bounded in \(M\). With the published classical exponent one may take every \(\alpha>4.116201\) for these inputs. With the separately audited exponent-three theorem every \(\alpha>2\) suffices. The width and the additive order in this result both vary *during* the limit in \(M\).

Equivalently, if \(\eta\ll(\log\log M)^{-\alpha}\), \(\alpha>\kappa\), and \(T\ge(\log M)^{3+\epsilon}\) for a fixed \(\epsilon>0\), then the complete denominator of any such family obeys
\[
          \log(2Q)\ \ge\ (\log M)
                    (\log\log M)^{\alpha/\kappa-1-o(1)} .              \tag{2}
\]
For each exponent strictly below the displayed limiting power, failure on any subsequence would fall under (1). The earlier near-octave estimate gives \(O(\log M)\) on much narrower bands, including width surplus \(O((\log M)^{-2-\epsilon})\) under the exponent-three input. Equation (1) permits inverse powers of \(\log\log M\) and has a larger power in the residence bound. The fixed-width higher-order theorem alone has constants depending on its additive order. Here every comparison is estimated with that order varying. [Earlier moving-width theorem](../literature/NEAR_DOUBLING_RESIDENCE.md) · [Fixed-width high-order argument](HIGH_ORDER_NATIVE_RESIDENCE.md) · [Classical BLS bound](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [Modern log-ratio source and audit](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

## Explicit determinant estimate for a moving number of prime powers

Let \(1\le d\le2h\), and let \(1\le l_1<\cdots<l_d\le m\) be distinct integers. Suppose \(z_1,\ldots,z_d\) are distinct positive reals with \(|\log z_j|\le a/m\), \(0<a\le1\). Suppose \(|z_i-z_j|\ge\Delta\) when \(i\ne j\), with \(0<\Delta\le1\). For the matrix \(A_{ij}=z_j^{l_i}\),
\[
                  |(A^{-1})_{ji}|
                      \le e^{2ad}2^{d-1}\Delta^{-(d-1)}.               \tag{3}
\]

For completeness, factor each generalized Vandermonde determinant as the usual Vandermonde in its variables times its Schur polynomial for ascending degree list \(\boldsymbol l\). The polynomial is homogeneous of degree \(\sum l_i-d(d-1)/2\le dm\), and has nonnegative coefficients by its tableau expansion. At the all-ones vector its value is \(\prod_{r<t}(l_t-l_r)/(t-r)\). These statements apply also to the list with \(l_i\) removed; the empty determinant is one. By positivity, the Schur factor evaluated on the given variables is between \(e^{-ad}\) and \(e^{ad}\) times its all-ones value, and the same bounds hold for every cofactor. The ratio of the cofactor's all-ones value to the full one is
\[
 \frac{(d-1)!}{\prod_{r\ne i}|l_r-l_i|}
       \le\binom{d-1}{i-1}\le 2^{d-1},
\]
since the list increases by at least one at every step. The ratio of the ordinary Vandermonde factors after deleting column \(j\) has absolute value \(\prod_{r\ne j}|z_r-z_j|^{-1}\). The cofactor formula now gives (3). Hence all dependence on \(m\) in this estimate is already included in the allowed interval of the \(z\)'s. [A. Khare, *Matrix Analysis and Entrywise Positivity*, tableau definition (42.2), Proposition 42.6 and proof of the alternant formula in Theorem 46.1](https://math.iisc.ac.in/~khare/teaching/Math341-notes.pdf)

## A chronological interval, with all parameters growing together

Suppose (1) fails. After truncating the original trajectory on a subsequence, fix \(\theta>0\) and take
\[
              T=\lfloor(\log M)^{3+\theta}\rfloor .
\]
Choose \(\kappa'>\kappa\) and a fixed \(u>1+\beta\) sufficiently close to \(1+\beta\) that \(u\kappa'<\alpha\). There is a fixed \(c_0>0\) with \(\|t\gamma\|\ge c_0t^{-\kappa'}\) for all positive integers \(t\), directly from the irrationality measure. Define
\[
 L=\lfloor x^u\rfloor,\qquad
 h=\left\lfloor\frac{\log M}{8(\kappa'+1)\log T}\right\rfloor .
\]
Then \(h\to\infty,\ \log h=x+o(x),\ h<3^L\). Choose \(2h\) distinct odd primes larger than \(h\) whose maximum \(m\) is \(O(h\log(2h))\); for instance, take prime indices \(h+1,\ldots,3h\). Thus \(\log m=x+o(x)\). The classical upper bound \(p_n\ll n\log(2n)\) is more than enough. [Rosser–Schoenfeld, 1962, Theorem 3](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf)

Set \(N=\lfloor T/(100m)\rfloor\). Among \(0\le t<N\), retain the times whose \(\{t\gamma\}\) belong to one most populated bin of a partition into \(\lceil100m\rceil\) equal intervals. Subtract the smallest retained time \(t_*\); let \(\mathcal S\subset[0,N]\) be the resulting offsets. Its size \(K\) satisfies
\[
               \log K\ge \log T-2\log m-O(1)
                           =(1+\theta+o(1))x.                          \tag{4}
\]
For \(s\in\mathcal S\), write \(k_s=\lfloor(t_*+s)\gamma\rfloor-\lfloor t_*\gamma\rfloor\), \(D_s=2^{-k_s}\operatorname{shift}^s\), and \(z_s=3^s2^{-k_s}\). Then \(|\log z_s|\le(\log 2)/(100m)\). The numbers are distinct, and the mean value theorem on this fixed neighborhood of one gives
\[
                         |z_s-z_t|\ge c_1 T^{-\kappa'}\quad (s\ne t),  \tag{5}
\]
since the absolute difference of their base-two logarithms dominates \(\|(s-t)\gamma\|\).

Write the actual odd states as \(y_i\), put \(U_i=2^{E_i}\) for the cumulative genuine division exponent, \(V_i=U_i y_i\), \(J=M\sqrt R\), \(F_i=\lfloor\log_2(V_i/J)\rfloor\). Thus \(V_{i+1}=3V_i+U_i\). Uniformly for \(1\le l\le m\) and all needed central dates,
\[
     2^{-F_i}D_s^l V_i=2^{-F_i}V_i z_s^l(1+O(T/M)),\qquad
               C_{i,l,s}=2^{-F_i}D_s^l U_i\in\{1,2\}.                 \tag{6}
\]
Here \(ls\le mN\le T/100\), and the log of the error factor is between zero and \(ls/(3M)\). The base label lies in \([J,2J)\), with \(J/M\to\sqrt2\); the dilation changes the log height by at most \((\log2)/100+O(T/M)\). This places the result strictly between \(RM/2\) and \(4M\) for large \(M\), giving the binary dyadic tags in (6). Every rescaled label is in \(Q^{-1}\mathbb Z\). At the **undilated** rows \(l=1\), the log error from the base is \(O(1/m+T/M)\), including \(z_s\). Consequently a row on which the tags of the different offsets vary has base angle \(\{\log_2(V_i/J)\}\) in a circle interval of length
\[
                 \eta+O(1/m+T/M).
\]
This is the intersection condition between a tag-one label at most \(RM\) and a tag-two label at least \(2M\). For \(1\le t<L\), the angle shift over \(t\) true dates differs from \(t\gamma\) modulo one by \(O(L/M)\). Since \(\eta+1/m+(T+L)/M=o(L^{-\kappa'})\) and \(\|t\gamma\|\ge c_0 L^{-\kappa'}\), all the variable undilated rows are separated by at least \(L\) actual dates, uniformly over the entire used native interval. This yields the coding bound \(1+n/L\) without requiring any discrepancy estimate for a varying arc.

## Integer separation of all \(h\)-sums

Take \(a=\lfloor T/2\rfloor\) and suppose two different \(h\)-term multisets of the labels \(2^{-F_a}D_sV_a\) have the same sum. Cancel common occurrences, and write \(P=\sum_{s}c_sD_s\) for the remaining signed operator. It has \(d\le2h\) distinct offsets, nonzero integer coefficients of sum zero and total absolute mass at most \(2h\). For \(H_i=2^{-F_i}PV_i,\ e_i=2^{-F_i}PU_i\),
\[
 2^{F_{i+1}-F_i}H_{i+1}=3H_i+e_i,\qquad QH_i\in\mathbb Z,\quad |e_i|\le h .
\]
When \(H_{i+1}=0\) at a variable row \(i\), the preceding \(L-1\) inactive rows show \(3^{L-1}\mid QH_i\); thus \(3^L\mid Qe_i\). Coprimality and \(|e_i|\le h<3^L\) force \(e_i=H_i=0\). At an inactive row the backward implication is immediate. Starting at \(a\) and retaining a guard of \(L-1=o(T)\) supplied dates, this forces \(PU_i=0\) throughout \([\lceil T/4\rceil,a-1]\).

For each of the chosen primes \(l\), every evaluation in \(P^{l-1}(PU)\) shifts time forwards by at most \(mN\le T/100\). Therefore \(P^lU=0\) on the common interval \([\lceil T/3\rceil,\lfloor5T/12\rfloor]\). In the dyadic shift ring modulo \(l\), this operator agrees with \(\sum c_s D_s^l\). Its normalized actual forcing \(\sum c_s C_{i,l,s}\) is an integer with absolute value \(\le h<l\), so it vanishes exactly there. The corresponding signed dilated label has homogeneous native evolution there. Set \(n=\lceil\log_3(64hQM)\rceil+4\), so \(n=O((\log M)x^\beta)=o(T)\). From \(i=\lceil3T/8\rceil\) there are \(n\) edges inside that same interval. The entire integer \(Q2^{-F_i}\sum c_s D_s^lV_i\) is divisible by \(2^{F_{i+n}-F_i}\ge3^n/2\) and has absolute size \(\le 4hQM\) by (6). It is zero. Thus, at a single genuine base date,
\[
                      \left|\sum_s c_s z_s^l\right|
                               \le C h T/M                              \tag{7}
\]
for **every** chosen prime, with an absolute constant uniform in \(h,l,M\). The error follows by dividing through the common positive base label and using \(z_s^l\le 2^{1/100}\). Arbitrarily many formal temporary differences introduce no coefficient-size bound in the exact modular identity.

Apply (3) using the first \(d\) primes to the \(d\) nonzero coefficients. With \(a=(\log2)/100\) in that lemma and \(\Delta=\min(1,c_1 T^{-\kappa'})\), equations (5) and (7) imply
\[
               1\le \max_s|c_s|
                   \le (C hT/M)\,d\,\exp(Cd)(C' T^{\kappa'})^{d-1}.
\]
The logarithm of the right side is at most
\[
       -\log M+2h\kappa'\log T+O(h+\log T+\log h)
                           \le -(1/2+o(1))\log M .
\]
This contradiction proves the true labels at the anchor form a \(B_h\) set, with multiplicities allowed.

Encode each offset by its future binary tag word on \(n\) native edges beginning at \(a\); delete constant rows. There are \(k\le1+n/L\) coordinates. A coordinatewise \(h\)-sum equality gives a homogeneous signed recurrence, so the same complete dyadic divisor at \(a\) implies an equality of the physical \(h\)-sums of the normalized labels. Individual words are also distinct: equality of individual labels forces equality of physical odd states on two dyadic rays, by comparing the powers of two in the odd numerators. Hence this is a \(B_h\) code of size \(K\). The binary cube Fourier bound, valid at every finite \(k,h\), gives
\[
          \log K\le\frac{\log(h!)}h
                  +\frac{k}h\log\left(\frac{4^h}{\binom{2h}h}\right)
             \le\log h+\frac{1+n/L}{h}\log(2h+1).                     \tag{8}
\]
It follows by averaging coordinate flips of a law on the cube in the \(2h\)-th Fourier norm and then bounding the number of permutations of a source multiset. The proof is given in the [fixed-order note](HIGH_ORDER_NATIVE_RESIDENCE.md). [Gu, Proposition 3.8](https://arxiv.org/abs/1809.07364)

Now \(h\asymp(\log M)/x\), \(L\asymp x^u\), and \(n=O((\log M)x^\beta)\). The second term in (8) is \(O(x^{2+\beta-u})+o(1)=o(x)\) by \(u>1+\beta\). We obtain \(\log K\le(1+o(1))x\), contradicting (4). This proves (1) for every fixed \(\theta>0\) and the stated complete denominator consequence.

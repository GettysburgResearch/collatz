# An exact positive real kernel on every ternary source lattice

Define the stopped forward map on a positive real \(x=u/3^j\) with formal remaining degree \(j\ge1\) by taking \(e=v_2(u)\) even steps followed by one odd step. Its output is
\[
 y=\tfrac12+\frac{3x}{2^{e+1}}=\frac{\operatorname{oddpart}(u)+3^{j-1}}{2\,3^{j-1}} .
\]
Thus the new numerator is an ordinary integer at degree \(j-1\). For a nonnegative pointwise-defined function \(f\) on the positive reals set
\[
 (Kf)(y)=\frac{1_{\{y>1/2\}}}{3}\sum_{e\ge0}f\!\left(\frac{2^e(2y-1)}{3}\right).
                                                                    \tag{1}
\]
For \(y=v/3^{j-1}\), \(v\ge1\), the candidate preimages are exactly the numerators \(2^e(2v-3^{j-1})>0\) at degree \(j\). The parenthesis is odd, so the exponent \(e\) is forced by the source. The preimages belonging to distinct \(v\)'s are disjoint and exhaust all positive numerators. For \(s,j\ge0\) and nonnegative \(f\),
\[
 3^{-j}\sum_{v\ge1}K^s f(v/3^j)
       =3^{-(j+s)}\sum_{u\ge1} f(u/3^{j+s}).                       \tag{2}
\]
This is a pointwise formula with extended nonnegative sums. It follows by iterating the one-step preimage partition. The same \(K\) is the Perron operator on real densities for the random affine map \(x\mapsto 1/2+3x/2^{e+1}\) with independent \(\Pr(e)=2^{-e-1}\). The probability times the inverse real Jacobian is \(1/3\). No choice of a representative of an almost-everywhere density enters (1)–(2).

For positive **integer** \(N\), let \(h_N(x)=N^{-1}1_{\{0<x\le N\}}\). If \(u\) is uniform through \(N3^r\), then for every ordinary \(y\ge1\)
\[
 \Pr\{T^{\sigma_r}(u/3^r)=y\}=K^r h_N(y),\qquad
                 \sum_{y\ge1}K^r h_N(y)=1.                         \tag{3}
\]
Here \(\sigma_r\) is the \(r\)-th odd departure, not necessarily the first date at which the rational happens to be an integer. The [entrance clock theorem](RATIONAL_ENTRANCE_CLOCK.md) estimates \(\sigma_r\) beyond the first complete binary period. Equation (3) is unconditional elementary arithmetic.

## A trace bound and its limitation

For \(N=2^k,\ r=k/(2-\log_2 3)+v k^\gamma+O(1)\), fixed \(v>0,\ 1/2<\gamma<1\), put \(\sigma=\sigma_r\). At a fixed \(t\) on \(\{\sigma=t\}\) write \(Y=N3^r2^{-t}\). The source probability of \(Y>1\) is \(O(\exp(-c_{v,\gamma}k^{2\gamma-1}))\): at \(L=\lfloor\log_2(N3^r)\rfloor\) the ample initial numerator grid gives pointwise domination by twice the fair word law, and \(r-L/2\gg k^\gamma\). If \(Y\le1\), the contribution of one \(t\) to the mass at \(y\) is
\[
 Y^{-1}\Pr_{\rm fair}\{Q_t=r,\ w_t=1,\ y-Y\le B_w<y\}.
\]
As in (3)–(4) of the entrance-clock note, coupling to an independent stationary seed in \([0,1]\) bounds this by \(C_\alpha(1+|\log Y|)(1+y)^{-1-\alpha}\). Every formal numerator before the \(r\)-th odd is at most \(N3^r\), so the maximum possible \(t\) is \(r(1+\lfloor\log_2(N3^r)\rfloor)=O(k^2)\). In particular
\[
 \Pr\{T^\sigma(u/3^r)\in E\}
 \ll_{v,\gamma,D,\alpha} k^{-D}
       + k^4\sum_{y\in E}(1+y)^{-1-\alpha}                          \tag{4}
\]
for every \(E\subseteq\mathbf N_{>0}\), each fixed \(0<\alpha<1,\ D>0\). The \(k^{-D}\) term bounds the entire early event before summing over \(E\). The pointwise factor is polynomial, not uniform in \(k\). If \(E\) is a hypothetical bad component, (4) concerns the rational source population; (2) does not identify it with the ordinary integer source density.

## Why a component-colored trace is insufficient by itself

If \(C\) is a bounded nonnegative invariant coloring of the ordinary integers, \(C(Tx)=C(x)\), then for any nonnegative \(f\)
\[
 \sum_{y\ge1}3\,1_{\{y\equiv2\ (3)\}}C(y)Kf(y)=\sum_{x\ge1}C(x)f(x).
                                                                    \tag{5}
\]
Indeed \(x=2^e(2y-1)/3\) ranges precisely through the ordinary integer predecessors of \(y\) under the first odd-ending step, and every integer \(x\) has exactly one such \(y\). Consequently the signed starting-trit defect \(\sum C(y)(3\,1_{\{y\equiv2\}}-1)Kf(y)\) equals \(\sum C(y)(f(y)-Kf(y))\) whenever the sums are finite.

The following calculation connects this identity with the repository's established Mellin flux. For \(1<\beta<2\) set
\[
 H_\beta(x)=(1+x)^{-\beta}-(1+2x)^{-\beta}.
\]
The dyadic preimage series in (1) telescopes exactly, giving \(K H_\beta(y)=c_\beta(1+y)^{-\beta}\) at every integer \(y\ge1\), \(c_\beta=3^{\beta-1}2^{-\beta}\). This test was supplied by the sprint's structural team. Suppose \(C\) is the indicator of an invariant set of natural density \(d_C\). Taking \(\beta\downarrow1\) in (5) gives
\[
 \log(4/3)d_C
   =\sum_{y\in C}\frac{3\,1_{\{y\equiv2\ (3)\}}-1}{1+y}
       +\sum_{y\in C}\frac1{(1+y)(1+2y)}.                            \tag{6}
\]
The signed sum may always be read as its Abel limit in \(\beta\); the written signed trit estimate in PR215 also gives convergence in increasing physical order. To verify the limit split \(\sum_C(H_\beta-KH_\beta)\) into \((1-c_\beta-2^{-\beta})\sum_C(1+y)^{-\beta}\) and the remainder \(\sum_C(2^{-\beta}(1+y)^{-\beta}-(1+2y)^{-\beta})\). The first tends to \(\tfrac12\log(4/3)d_C\) by natural density and differentiation, while the second tends to minus one half the last sum in (6) by dominated convergence.

The preexisting unshifted physical Mellin identity gives the same signed obstruction, with a physical-order proof using renewal. [PR215, equation (5), at the pinned head](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase5/NATIVE_MELLIN_RIGIDITY.md)

Thus the signed trits on the intervening ordinary intervals can carry a term of size \(d_C\). Proving a terminal tail bound for (3) does not by itself force that term to vanish or prove \(d_C=0\).

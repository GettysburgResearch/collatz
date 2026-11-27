# The isolated terminal at 1 and its first-return Mellin transform

Two widths of the original geometric-word Poisson test isolate the terminal integer 1 with a power-saving error, before taking any stationary limit. The resulting macroscopic jump and the residue of the stationary endpoint transform measure the same ordinary basin density. The stationary transform also has at least one genuine nonreal lattice pole.

## Removing every other terminal at finite depth

Use the [word statistic and Poisson normalization](POISSON_SOURCE_PROBE.md), the scaled seed and basin density of the [clock spectrum](POISSON_CLOCK_SPECTRUM.md). In particular, the Schwartz function \(g\) has zero integral, \(I=\int_0^\infty g\ne0\), and \(g_R(u)=g(u/R)/R\). Put
\[
 k=\lfloor8\log R\rfloor,\quad q=3^k,\quad
 t_-=R^{-2},\quad t_+=R^{-1},\quad
 \eta=1-8\log(10/9)>0 .
\]
If a positive odd \(x\) ends somewhere other than 1, the departed states through depth \(k\) are all at least three, including repetitions, because 1 is fixed. Thus
\[
 A_k(x)x=U^kx\prod_{j<k}\frac{3U^jx}{3U^jx+1}\ge (9/10)^k.
\]
A negative odd retains \(A_k(x)|x|\ge1\), since the affine intercept is nonnegative and the terminal is a negative integer. At either width the scaled convolution row at every terminal other than 1 therefore has \(s=t/(R A_k(x))\le R^{-\eta}|x|/R\). By Fourier inversion, \(\|g*P_s-\pi g\|_\infty\le C_gs\). On \(|x|/R\le R^{\eta/3}\) the normalized sum of errors is \(O_g(R^{-\eta/3})\). The complementary sum of the two row magnitudes is also \(O_g(R^{-\eta/3})\), by the uniform majorant \(C_g(1+|x|/R)^{-2}/R\). Consequently, if \(\Delta_R=\mathcal D_k(g_R,t_-)-\mathcal D_k(g_R,t_+)\),
\[
 \Delta_R=
 q\,\mathbb E_w\!\left[\mathbf1_{Y_w=1\bmod q}
 \int g(v)
       (P_{t_-}-P_{t_+})(A_w Rv+B_w-1)\,dv\right]
       +O_g(R^{-\eta/3}).                                             \tag{1}
\]
Each residue-compatible word gives exactly one integer source for terminal 1. Equation (1) retains precisely these words, with their original probabilities. It uses only deterministic inequalities on the other rows. For \(D=\log(4/3)\) one has \(1<D(8-1/D)<2\), while \(\log(10/9)(8-1/D)<1\). The ordinary passage theorem in the clock spectrum therefore identifies the limit of both sides of (1) as \(\pi I d_1/2\), with \(d_1\) the relative odd density of convergence to 1.

## A stationary first-return residue for the same density

Let \(M_y=h(y)\mu_y\) be the unnormalized stationary joint real fibre at a specified positive odd ternary unit. Write \(d_y\) for relative odd predecessor density. At every nonperiodic unit \(y\) the known natural-density inverse law \(Q_y\), the real offset \(r=R_\infty\), and \(\kappa=D/2\) give
\[
 M_y(dr)=\kappa d_y(y-r)\,Q_y(R_\infty\in dr),\qquad
 \int \frac{dM_y(r)}{y-r}=\kappa d_y .                                \tag{2}
\]
Indeed the canonical path law has derivative \(d_y W_\infty/\beta_y\) relative to \(Q_y\), where \(W_\infty=(y-R_\infty)/y\), and the trace is \(h(y)=\kappa y\beta_y\). The uniform nonperiodic endpoint gap puts \(y-r\ge c_0 y\) on the support, for an absolute \(c_0>0\). These are consequences of the existing change of measure. [Weaver 19, (F3), (F9), (F13)](https://rstation.ai/problems/collatz/papers/19) · [Weaver 102, (27)–(29)](https://rstation.ai/problems/collatz/papers/102)

At 1 put \(u=1-r\), \(\widetilde M=(r\mapsto1-r)_*M_1\), and \(\lambda=3/4\). Write \(z_e=(2^e-1)/3\) and \(A_e=3/2^e\). The sole cycle parent has \(e=2\); for even \(e\ge4\) all other parents are nonperiodic. In sums over these latter indices omit \(3\mid z_e\), whose stationary mass is zero and whose ordinary predecessor set is a singleton. Set
\[
 E=\sum_e A_e\big(r\mapsto A_e(z_e-r)\big)_* M_{z_e}.
\]
The canonical inverse transfer and the exact affine defect give
\[
 \widetilde M=E+\lambda(s_\lambda)_*\widetilde M,\qquad s_\lambda(u)=\lambda u.
                                                                         \tag{3}
\]
This is the first-step form of the known periodic circuit decomposition. It gives \(E(\mathbb R)=(1-\lambda)h(1)\) and \(\operatorname{supp}E\subset[c,1]\), \(c=15c_0/16>0\), by \(A_e z_e=1-2^{-e}\). [Weaver 19, (F11)–(F12)](https://rstation.ai/problems/collatz/papers/19)

The disjoint noncycle parent basins have total density \(d_1\). To justify the countable sum, first keep parents whose least odd ancestor is at most \(M\). There are finitely many, since their basins are disjoint. For any omitted parent, the entire basin lands first below \(M\) at 1. The upper density of such sources is \(O(M^{-\delta})\) by the uniform single-landing bound, taking the source scale to infinity at fixed \(M\) before sending \(M\to\infty\). The nonunit direct parents themselves number \(O(\log X)\) below \(X\). Every source other than 1 that reaches 1 has a well-defined last noncycle parent. This proves the claimed summation and, by positivity and (2),
\[
             \int u^{-1}\,dE(u)=\kappa\sum_e d_{z_e}=\kappa d_1 .     \tag{4}
\]
[Weaver 102, (2)–(3) and the common-landing argument for Proposition 6](https://rstation.ai/problems/collatz/papers/102)

For \(\Re s>0\), summing the positive-measure dilation series from (3) gives
\[
 Z(s)=\int_{(0,1]}u^{s-1}\,d\widetilde M(u)
      =\frac{\int u^{s-1}\,dE(u)}{1-e^{-Ds}},
 \qquad \operatorname*{Res}_{s=0} Z(s)=\frac{d_1}{2}.                 \tag{5}
\]
Absolute convergence follows at once by using \(\Re s\) and the compact exit support. The numerator is entire. Although (3) fixes the total exit mass, (5) involves its reciprocal moment. The exact evaluation of that moment as \(D/2\), equivalent to \(d_1=1\), remains open.

At least one nonreal point \(2\pi i m/D\), \(m\in\mathbb Z\setminus\{0\}\), is a genuine pole. Each fixed nonperiodic fibre in the countable exit mixture is singular with respect to Lebesgue measure, by the integer-fibre word and synchronization results. Thus the probability \(u^{-1}E/(\kappa d_1)\) is singular on \([c,1]\). Its pushforward by \(u\mapsto\log(u)\bmod D\) is singular as well, since the logarithm is Lipschitz there and wrapping takes null sets to null sets. A singular circle probability cannot have all nonconstant Fourier coefficients zero. At each nonzero coefficient the denominator of (5) has a simple zero and the numerator is nonzero. In particular \(\widetilde M((0,t])/t\), exactly multiplicatively periodic for \(0<t<c\) by (3), is nonconstant. A constant ratio there would make \(\widetilde M\) a constant multiple of length on that interval, producing only its real pole in (5); the rest of the Mellin integral is entire. [Integer real-fibre singularity and inputs](REAL_FIBRE_AND_FRONT.md)

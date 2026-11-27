# The Gaussian profile at the first Poisson jump

The first jump of the original signed Poisson statistic has a Gaussian transition through a window of order the square root of the source logarithm. Its width is independent of the power of the Poisson scale. In contrast, the scalar cutoff probability for the unconditioned independent geometric total has a width growing with that power. The actual first-hit density remains in the jump's amplitude.

Put \(D=\log(4/3)\), \(\kappa=D/2\), \(L=\log R\), and let \(E\) be the unnormalized exit measure on the defect \(u=1-R_\infty\) in the [first-return formula](FIRST_RETURN_POISSON.md). In particular \(E\) lives in \([c,1]\) for some \(c>0\), and \(\int u^{-1}\,dE=\kappa d_1\). Let \(\Phi\) denote the standard normal distribution function and set
\[
                  \sigma^2=2(\log2)^2/D^3 .
\]
For any \(\beta>0\), real \(\xi\), and Schwartz seed \(g\) of integral zero, put \(g_R(u)=R^{-1}g(u/R)\) and \(I=\int_0^\infty g\). On the stated ordinary inputs, with \(k=\lfloor(1+\beta)L/D+\xi\sqrt L\rfloor\),
\[
        \lim_{R\to\infty}\mathcal D_k(g_R,R^{-\beta})
         =-\frac{\pi I d_1}{2}\,\Phi(\xi/\sigma).                     \tag{1}
\]
We derive the profile using the real correction and both ordinary first-hit clocks at terminal 1. The source is positive and odd in the first-hit estimates. The Poisson statistic itself retains every signed odd source.

## A local limit at the specified first hit

Let \(J(x)\) be the first odd clock at 1, and let \(S(x)\) be the cumulative native division count up to that hit when finite. Put \(p_{j,d}=2^d/3^j\). In the cell \(J(x)=j,S(x)=d\) set \(u(x)=x/p_{j,d}\). This is the exact product of the factors \(3v/(3v+1)\) before the first hit. The simple-path reciprocal bound supplies \(c\le u(x)\le1\) uniformly, after decreasing \(c\) if necessary. For a Lipschitz test \(\varphi\) on this interval set
\[
 m_{j,d}(\varphi)=\frac{1}{p_{j,d}}
  \sum_{\substack{J(x)=j\\S(x)=d}}\varphi(u(x)),\qquad
 g_j(d)=\binom{d-1}{j-1}2^{-d}\mathbf1_{d\ge j}\quad(j\ge1),
 \quad g_0=\delta_0 .
\]
We give \(m\) zero mass at empty cells. The conclusion, uniform over \(j,d\ge0\) with \(p=p_{j,d}\to\infty\), is
\[
       \sqrt{\log p}\,\big|m_{j,d}(\varphi)-g_j(d) E(\varphi)\big|
                        \longrightarrow0.                              \tag{2}
\]
In particular the ordinary harmonic first-hit sum has the coefficient \(\kappa d_1\), by taking \(\varphi(u)=1/u\). PR195 established the corresponding fixed-grade local limit for counts of equal corrected height in a hypothetical escaping component. Here one terminates at a genuine first hit, retains its real mark, and removes the actual loop. The external joint mixing input is the same one-extra-digit, exact-native-clock theorem. Earlier work of Leen and Weaver treats clock laws and phases at the orbit minimum. [PR195, physical-source cancellation](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/PHYSICAL_SOURCE.md) · [PR195, local height law](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/LOCAL_HEIGHT_LAW.md) · [Weaver–Wren, Theorem 6](https://rstation.ai/problems/collatz/papers/48/v1) · [Weaver 175, terminal and clock sources](https://rstation.ai/problems/collatz/papers/175/v1)

First fix a mean-zero test \(b\) on the three residue classes of the physical source, of norm at most one. For any fixed \(A>0\),
\[
 \sum_{j,d}\left|
  \frac1{p_{j,d}}\sum_{\substack{x\ge X,\ J(x)=j\\S(x)=d}}
              b(x\bmod3)\varphi(u(x))\right|
       \ll_{A,\varphi}(1+\log X)^{-A}.                                \tag{3}
\]
For a single octave or subinterval of it, take \(t=\lfloor(\log_2 X)/32\rfloor\). The physical-source calculation in PR195 controls in joint sum norm the signed contribution through \(t\) steps, marked by \((U^tx,S_t(x))\) and weighted by \(f_t(x)/x\). Its bound is \(O_B(t^{-B})\) for every fixed \(B\), for the same mean-zero residue test. Write \(z=U^tx\). The exceptional starts with \(S_t(x)>4t\) have initial reciprocal mass \(O(e^{-c't}+2^{4t}/X)\) by the binary-cylinder count there. On the remaining starts every earlier state exceeds \(X2^{-4t}>1\) for large \(X\), so the first hit can be decided by the future from \(z\). The intercept \(0<B_t<3^t\) gives \(1-f_t(x)=B_t/z\le 2^{4t}/X\). On the basin of 1 we then have \(u(x)=f_t(x)u(z)\) and \(1/p_{j,d}=f_t(x)u(z)/x\). Replace \(\varphi(u(x))\) by \(\varphi(u(z))\), at cost \(O_\varphi(2^{4t}/X)\) on this octave. The weight \(u(z)\varphi(u(z))\) is bounded. Route \((z,h)\) to \((t+J(z),h+S(z))\) when the hit exists and discard it otherwise. This bounded pushforward preserves the sum-norm estimate. Removing or restoring the exceptional set costs its unsigned bound. Summing the octave estimates with \(B>A+1\) gives (3). The finitely many small starts have finite total mass.

The exact next inverse parent at gap \(e\) from \(x\) is \(z=(2^e x-1)/3\); it exists exactly when \(x\equiv2^{-e}\bmod3\). The new cell height and defect are \(p'=2^e p/3\) and \(u'=u-1/(3p')\). Delete the sole candidate self-loop at the empty root. Therefore
\[
                m_j=g_1*m_{j-1}+b_j^\varphi\quad(j\ge1),\qquad
                m_0=\varphi(1)\delta_0,                                \tag{4}
\]
where the convolution is over the native clock. The signed forcing includes the residue discrepancy, the translation of the defect in \(\varphi\), and the one removed loop. Its total absolute mass over all cells is finite. In addition, on cells with \(p_{j,d}\ge X\) its total absolute mass is \(O_{A,\varphi}((1+\log X)^{-A})\).
Indeed the discrepancy uses \(b(x)=\mathbf1_{x\equiv2^{-e}}-1/3\) in (3) with matrix coefficient \(3\,2^{-e}\). The condition \(p\ge\sqrt X\) is a restriction on whole input cells and implies \(x\ge c\sqrt X\) on them. If \(p<\sqrt X\) but \(p'\ge X\), sum the geometric coefficients for \(2^e\ge3\sqrt X\) against the full sum-norm bound (3); there are just two residue tests as \(e\) varies. For the mark translation the absolute contribution per input \(x\) and \(e\) is at most \(3\, 2^{-2e}\operatorname{Lip}(\varphi)/p^2\), since the true parent weight is \(1/p'\). Sum \(1/p^2\le1/x^2\) over the distinct first-hitting sources. The restriction to large \(p'\) again allows the split at \(\sqrt X\) and gives \(O_\varphi(X^{-1/2})\). The omitted loop contributes at only one finite cell.

Iterate (4). An impulse at \((i,b)\) reaches \((j,d)\) with kernel \(g_{j-i}(d-b)\), taken zero at negative lags. The quotient of the two physical heights is \(2^{d-b}/3^{j-i}\). At height ratio at least \(Y\ge2\), this kernel is \(O((\log Y)^{-1/2})\): for lag at least \((\log_2 Y)/10\) use the unimodal point bound, and at smaller lag use the geometric exponential moment at \(3/2\). A fixed shift of the initial cell changes the kernel by \(o((\log p)^{-1/2})\) uniformly at \(p\to\infty\). For large \(j\ge(\log_2 p)/20\) this follows from the spatial difference bound \(\sup_d|g_j(d+1)-g_j(d)|\ll j^{-1}\) and convolution with a fixed number of gaps of finite mean. At smaller \(j\) use the same exponential moment. In the convolution keep finitely many impulses and then bound the remaining signed mass at heights below \(\sqrt p\) by its sum norm times \(O((\log p)^{-1/2})\). The impulse mass above \(\sqrt p\) is rapidly decreasing in \(\log p\). Let the discarded total tend to zero. This is the local smoothing argument in the cited PR195 note and gives (2) with coefficient \(\varphi(1)+\sum_{j,d}b_j^\varphi(d)=\lim_j\sum_d m_{j,d}(\varphi)\).

To identify this coefficient, the full depth-\(j\) original-word measure \(\sum_w A_w\delta_{1-R_w}\) over words compatible with 1 tends weakly to \(\widetilde M\). Explicitly, replacing \(R_j\) by \(R_{j-1}\) costs \(o(1)\): the last increment is at most \(A_{j-1}/2\) and its integrated weight is bounded by the canonical expectation times \(h(1)\sup(\rho_1/h)\), with \(A_{j-1}\to0\) and \(A_{j-1}\le1\). The resulting weighted test equals the canonical expectation of the prefix test times \(h(1)(\rho_1/h)(X_{j-1})\). The ordinary-depth scalar trace and bounded terminal selection give the stated weak limit as in the [ordinary-depth fibre proof](REAL_FIBRE_AND_FRONT.md). Extend \(\varphi\) Lipschitz to \([0,1]\) for this full measure. Removing the initial inverse letter 2 subtracts \(\lambda(s_\lambda)_*\) of the previous full depth, \(\lambda=3/4\). The first-hit limit is exactly \(E\) by the [exit recurrence](FIRST_RETURN_POISSON.md). Thus (2) is normalized without a clock-independence assumption.

## Integrating the native lattice at a fixed ordinary scale

Let \(q\) be continuous with compact support in \((0,\infty)\), and first take it Lipschitz. On any bounded interval of \(s=(j-L/D)/\sqrt L\), sum the true ordinary weights \(q(x/R)/R\) with first-hit time \(j\). Within a cell the appropriate test in (2) is \(\varphi_z(u)=z q(zu)\), \(z=p_{j,d}/R\). Since \(c\le u\le1\), admissible \(z\) range over a fixed positive compact interval. The family is compact in the uniform norm. Formula (2) applies uniformly to it by finite approximation and the point bound for \(m_{j,d}(1)\) there. For each \(j\) there are only boundedly many relevant \(d\). Uniformly on bounded \(s\)-intervals, the central binomial estimate gives
\[
 g_j(d)=\sqrt{D/(4\pi L)}
       \exp\big[-D^3 s^2/(4(\log2)^2)\big]+o(L^{-1/2}).
\]
Here \(d-2j=(L-Dj)/\log2+O(1)\). The remaining finite sum \(\sum_d E(\varphi_{p_{j,d}/R})\) is a continuous periodic function of \((L+j\log3)/\log2\), and its circle average is
\[
       \frac{1}{\log2}\int u^{-1}\,dE(u)\int_0^\infty q(v)\,dv .
\]
The irrational rotation by \(\log_2 3\) averages uniformly in its starting point on every interval of \(j\)'s of length tending to infinity. Step-approximate the smooth Gaussian weight on bounded \(s\)-intervals and use this rotation average on each piece. With \(\int u^{-1}\,dE=\kappa d_1\) the resulting limit is
\[
 \frac1R\sum_{J(x)<\infty}q(x/R)\,
    \delta_{(J(x)-L/D)/\sqrt L}
   \ \Longrightarrow\ \frac{d_1}2\!\int_0^\infty q(v)\,dv\;
                            \mathcal N(0,\sigma^2).                    \tag{5}
\]
For nonnegative \(q\), tightness follows from the known total natural basin density: the mass of the normal limit is the limit of the untruncated ordinary mass. Approximation then permits continuous \(q\), fixed positive annular indicators, and signed tests. This calculation gives a first-hit derivation of the Gaussian clock in the real and native lattice coordinates used here.

On a row in a fixed annulus reaching 1 at \(J\le k\), its terminal slope is \(A_k(x)=\lambda^{k-J}u(x)/x\). The scaled Poisson width therefore has log equal to \(D(k-J)-\beta L+O(1)\). By (5), the transition at \(J=L/D+\xi\sqrt L+O(1)\) sends the limiting fraction \(\Phi(\xi/\sigma)\) of the basin rows to infinite width and the remaining fraction to zero width. One can first omit a strip of width \(2\epsilon\sqrt L\) at the transition, then send \(\epsilon\downarrow0\) using the continuous normal limit. Since \(\beta>0\), the rows with \(J>k\) have vanishing fraction on the basin. All other components stay at zero width by the strict clock comparisons in the [macroscopic spectrum](POISSON_CLOCK_SPECTRUM.md), including its tightness argument for the countably many periodic basins. The signed sum of the zero-width rows on the full lattice tends to zero. The uniform row bound there allows truncation to fixed annuli and then removal of the truncation. This proves (1).

The leading Fourier cutoff in the same statistic is \(k\log_2 3+(1+\beta)L/\log2\). Standardizing its displacement from the iid total mean \(2k\) by the iid deviation \(\sqrt{2k}\) gives \(-\xi/(\sigma\sqrt{1+\beta})+o(1)\). Thus the actual transition and this scalar cutoff comparison have different widths. Formula (2) retains the local correlation that fixes the former. Its coefficient still contains the reciprocal moment (4) of the first-return note, and neither limit evaluates \(d_1\) as one.

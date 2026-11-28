# Physical clocks of subcritical collisions and the equal-total critical boundary

## Subcritical local limit retaining clock separation

Fix \(0<r<1/2\) and write \(u=r^2,\ \theta=1-u\). Each gap under \(Q=\mathrm{Geom}(\theta)\) has mean \(a=1/\theta\) and variance \(\sigma^2=u/\theta^2\). Let \(A_n(s,d)\) be the ordered collision mass in the normalization of \(U_n\), restricted to total \(s\) on the first word and \(s+d\) on the second. There is a nonnegative sequence \(T_d\) with \(\sum_dT_d=U_\infty\) and \(\sum_d e^{c|d|}T_d<\infty\) for some \(c>0\), such that
\[
 \sup_{s\in\mathbb Z}\sum_{d\in\mathbb Z}
 \left|\sqrt n\,A_n(s,d)-T_d\frac1{\sigma\sqrt{2\pi}}
              \exp\left(-\frac{(s-an)^2}{2\sigma^2n}\right)\right|
                         =O_r(n^{-1/2}).                               \tag{1}
\]
Consequently under the normalized collision law, conditional on each exact \(|s-an|\le B\sqrt n\), the difference \(d\) has total-variation distance \(O_{r,B}(n^{-1/2})\) from \((T_d/U_\infty)_d\). At \(d=0\), for the true integer-translation fusion population of the odd \(Q\)-source,
\[
 \sup_{|s-an|\le B\sqrt n}
     \left|\mathbb E_Q(K_n\mid S_n=s)-\mathbb E_Q K_\infty\right|
                         =O_{r,B}(n^{-1/2}).                           \tag{2}
\]
The conditional expectation on the left is a uniform-composition statistic: at each given total every genuine word has the same probability. Its mean over positive starts in a complete binary period gives the same statistic, with all companions positive if that interval starts above \(2^s\). Thus (2) controls fixed physical-clock rows throughout \(1<a<4/3\). [Original-source population identity](../phase10/INTEGER_FUSION_POPULATIONS.md)

To prove these assertions, define \(\Gamma_k(j,d)\) by retaining the ordered colliding pairs of depth k with first unequal outer letters, first total j and second total j+d, with their original \(U_k\) weights. At k=0 take mass one at j=d=0. Its total over j,d at k>0 is \(Z_k\). Peel every equal outer pair until the first disagreement or the end. Each such letter has normalized squared mass \(Q(e)\). Writing \(\pi_m\) for the sum distribution of m iid \(Q\)-gaps, with \(\pi_0=\delta_0\), this gives the exact identity
\[
                       A_n(s,d)=\sum_{k=0}^n\sum_j
                              \Gamma_k(j,d)\pi_{n-k}(s-j).              \tag{3}
\]
By exponential split decay, \(\sum_{j,d}\Gamma_k(j,d)\le Ce^{-ck}\). For any fixed sufficiently small \(b>0\) the crude mass \(\sum_{j,d}e^{b(j+|d|)}\Gamma_k(j,d)\) is at most \(M_b^k\): ignore the collision test, use \(j+|d|\le 2s_w+s_v\) and the original geometric moment on each word. Hölder interpolation between these estimates gives a \(\delta>0\) with
\(\sum_{k,j,d}e^{\delta(k+j+|d|)}\Gamma_k(j,d)<\infty\). Put \(T_d=\sum_{k,j}\Gamma_k(j,d)\). Formula (3) summed over s shows that \(T_d=\lim_n\sum_s A_n(s,d)\), and \(T_0=\mathbb E_Q K_\infty\). [Exponential first-split estimate](EXPONENTIAL_SPLIT_DECAY.md)

For completeness the geometric local limit used in (1) has uniform error \(O_r(m^{-1/2})\) after multiplication by \(\sqrt m\). Its characteristic function is \(\theta e^{it}/(1-u e^{it})\). Near zero its logarithm is \(iat-\sigma^2t^2/2+O_r(|t|^3)\); away from zero on \([-\pi,\pi]\) its absolute value is strictly below one. Fourier inversion and the bound \(O_r(m|t|^3)e^{-c_r mt^2}\) for the central approximation give uniform unscaled error \(O_r(m^{-1})\), including the Gaussian-tail truncation. For \(k\le n/2\), replacing the Gaussian at \(m=n-k,s-j\) by that at \(n,s\) after the \(\sqrt n\) normalization costs at most \(C_r[(1+k)/n+(j+ak)/\sqrt n]\), uniformly in s, by the bounded Gaussian derivative and bounded derivative under multiplicative scale changes. For \(k>n/2\), (3)'s exponentially small suffix mass absorbs the factor \(\sqrt n\). The exponential moment just proved now yields (1). The local limit for \(\pi_n(s)\) has a positive lower leading coefficient on each central window; dividing its \(d=0\) numerator in (1) by \(\sqrt n\pi_n(s)\) proves (2). The clock-separation conclusion follows by the analogous division by the sum over d.

## Exact threshold for the mean number of fused integer translates

For every \(0<\theta<1\), put \(r=\sqrt{1-\theta}\) and \(p=1-r\). With \(P_p\) denoting word probabilities for gaps of success parameter p,
\[
 \mathbb E_\theta K_n=\left(\frac{1+r}{1-r}\right)^n
                 \sum_{s,z}P_p(S_n=s,Z_n=z)^2.                        \tag{4}
\]
Indeed the number of words in a cell of fixed n,s,z equals its total mass divided by a single word's equal probability, under either tilt. Expanding the square shows precisely the \(\theta^n(1-\theta)^{s-n}\) weight of the first word. This is the equal-physical-clock term of the collision identity, including beyond the range of bounded unrestricted renewal.

For \(\theta<3/4\) one has \(r>1/2\). Chebyshev gives a central \(O_p(\sqrt n)\)-sized set of totals with probability at least \(1/2\). Cauchy–Schwarz on its at most \(C_p\sqrt n\,3^n\) cells shows \(\mathbb E_\theta K_n\ge c_\theta[(1+r)/(3(1-r))]^n/\sqrt n\), with base greater than one. For \(\theta>3/4\), (1) or the earlier finite-class real-mark bound gives a finite mean at infinite depth.

At \(\theta=3/4\) the population class is finite almost surely by the real-drift theorem, while its mean is infinite. More precisely let \(\mathcal D>0\) be the integrated distinct-first-branch forcing of the fair law, with full additive Haar probability. Then
\[
 \liminf_{n\to\infty}\sqrt n\,(\mathbb E_{3/4}K_{n+1}-\mathbb E_{3/4}K_n)
     \ge\frac{\mathcal D}{\sqrt{8\pi}},\qquad
 \liminf_{n\to\infty}\frac{\mathbb E_{3/4}K_n}{\sqrt n}
     \ge\frac{\mathcal D}{\sqrt{2\pi}}.                                \tag{5}
\]
Indeed \(r=p=1/2\) and the factor in (4) is \(3^n\). Peeling an identical outer gap contributes exactly the previous depth at the same-total test. The remaining increment sums ordered pairs \(e\ne f\) of distinct first letters. For fair \(\pi_n(s)=P_{1/2}(S_n=s)\), the joint density of the branch indexed by e at total t is \(\pi_n(t-e)L_eG_{n,t-e}\), where \(L_e\) is the weighted density transform \(3\cdot2^{-e}1_{z\equiv2^{-e}\ (3)}g((2^e z-1)/3)\); \(G_{n,s}\) is the fair depth-n ternary density conditional on the exact total. Restrict both suffix real marks by any compactly supported Lipschitz \(0\le F\le1\). Weaver 9/v2 Theorem 18 gives \(G^F_{n,s}\to g_F\) in \(L^2\), uniformly on each central clock window. Each fixed \(L_e\) is bounded on \(L^2\), so the integrated product tends uniformly to \(\int (L_e g_F)(L_f g_F)\,dm\). The two remaining clock factors are \(\pi_n(t-e)\pi_n(t-f)\). Their sum over \(|t-2n|\le B\sqrt n\), multiplied by \(\sqrt n\), tends as n and then B grow to \(1/\sqrt{8\pi}\), by the preceding geometric local limit at variance 2 and the Gaussian integral. Sum first over finitely many distinct e,f, then let \(F\uparrow1\) and exhaust the branches by monotone convergence. The limit of the products is \(\mathcal D\) as stated. Summing the first lower estimate yields the second. [Weaver 9/v2, Theorem 18](https://rstation.ai/problems/collatz/papers/9/v2) · [Integrated critical forcing and slope](../../escape/phase9/EXACT_COLLISION_ENERGY_SLOPE.md)

Together these statements give \(\mathbb E_\theta K_\infty<\infty\) **if and only if** \(\theta>3/4\). In the range \(\theta_*<\theta<3/4\) the almost sure exponential rate of \(K_n\) is zero despite the exponential mean lower bound. The critical mean \(\sqrt n\) lower bound does not establish its matching upper order. In (5) the letters and clocks have their genuine fixed-total joint law, and the proof uses positivity to retain bounded-real contributions. Controlling the discarded large-real or large-deviation contributions on the same \(\sqrt n\) scale is a further question.

There is an upper bound \(o(n)\) at the boundary. The marked finite-clock exactness argument from the companion lane gives, for every fixed M, \(L^1\) convergence of the unrestricted depth-n fair-word density in each clock class modulo M to \(\rho/M\). One can obtain this directly by starting the compact stationary skew system with fair independent ternary Haar and zero mark: after applying the word the old Haar contribution is precisely the uniform lift beyond its n-th digit. The initial law on ternary *units* requires using, for example, the law of the first affine step from full Haar, recording its clock as well. That law is supported on units with density bounded relative to the positive stationary density times the uniform clock; exactness then gives the same limit after n−1 more steps. All original n-word residues on their first n trits agree with the law started at a fixed zero trit tail or at full Haar.

For the two distinct-branch products, requiring the two total clocks to agree modulo M produces a larger nonnegative increment than the exact-clock test. Along any subsequence take further almost-everywhere convergence of each of the finitely many marked densities, and of its transforms by countably many \(L_e\). The products summed over the compatible mark pairs are dominated by \(C^2\sum_{e\ne f}(L_e\rho)(L_f\rho)\): sum the marks first and use the unmarked domination by \(C\rho\) from the unit floor. This forcing is integrable. Therefore dominated convergence gives limit \(\mathcal D/M\) for the modular increment; letting M tend to infinity proves \(\mathbb E_{3/4} K_{n+1}-\mathbb E_{3/4}K_n=o(1)\). This bound does not give the matching local limit in (5). [Finite physical-clock exactness](../../escape/phase10/ORDINARY_LEBESGUE_POINTS.md) · [Fair forcing domination](../../escape/phase9/EXACT_COLLISION_ENERGY_SLOPE.md)

# The marked return resolvent has a rational or natural-boundary dichotomy

Use the all-parent ordinary unit Hilbert space and survival contraction $P$ of [the positive Green theorem](POSITIVE_GREEN_SPECTRUM.md). Let $D$ be the positive diagonal operator with the **original** stopping and terminal weight

\[
        D_x=\frac{\rho_1(x)}{x(3x+1)},\qquad \rho_1(x)=x\bmod3.
\]

It is trace class because $\sum_xD_x<\infty$; the diagonal in the normalized point-mass basis is still $D_x$. Define the scalar trace $H(z)=\operatorname{Tr}[D(I-zP)^{-1}]$ for $|z|<1$. The following alternatives cover all possibilities.

* Finitely many positive cycles give a rational $H$ with no unit-circle poles.
* Infinitely many force the unit circle to be a natural boundary of $H$, even though its series converges absolutely on that circle. Its radial derivative diverges with a fixed imaginary sign on an explicit dense set of angles. The argument needs no assumed distribution of primitive clocks.

A holomorphic continuation across a single boundary point would therefore imply finitely many positive cycles. The dichotomy also holds for the full trace-class perturbation determinant below. The finite alternative includes both the fixed cycle alone and any finite set of further cycles.

## Exact all-parent trace and the clock resonances

Write $p_C$ for least odd period, $h_C$ for total division count, $\lambda_C=3^{p_C}2^{-h_C}=e^{-g_C}$, and $a_C=\sum_{x\in C}D_x$. The $d$-th trace reads precisely the original positive return atoms, since the diagonal entry of $P^d$ is the physical survival weight if $U^d x=x$ and zero otherwise. Thus

\[
 H(z)=\operatorname{Tr}D+\sum_C a_C\frac{\lambda_C z^{p_C}}{1-\lambda_C z^{p_C}},\quad
  \lim_{r\uparrow1}rH'(r)=\mathcal J=\sum_C J_C,\quad
 J_C=\frac{p_Ca_C\lambda_C}{(1-\lambda_C)^2}.                           \tag{1}
\]

The equality with the physical atom selector, convergence of $\sum_C a_C\lambda_C/(1-\lambda_C)$, and the bound $J_C>15/4$ for every extra cycle are proved in [the diagonal extraction](DIAGONAL_CYCLE_MOMENT.md). In particular $H$ belongs to the Wiener algebra of absolutely convergent Fourier series on the closed disk. The following qualitative argument needs only $\inf_C J_C>0$ and $g_C\to0$ along distinct cycles. Both follow already from simple-path packing and weighted Cauchy–Schwarz in that manuscript.

For every positive integer $j$, set $\theta_j=2\pi j\log_2 3$ and $\tau=2\pi j/\log 2$. The crucial congruence for **every** cycle is

\[
                 e^{ip_C\theta_j}=e^{-i\tau g_C}.                        \tag{2}
\]

Indeed $p_C\log3=h_C\log2-g_C$. It is also the exact operator covariance coming from $(U(x)/x)^{i\tau}=3^{i\tau}w_x^{-i\tau}$ on ordinary edges. For $z=re^{i\theta_j}$, the contribution to $-\operatorname{Im}(zH'(z))$ in (1) from $C$ is

\[
  p_C a_C\frac{t(1-t^2)\sin(\tau g_C)}{|1-t e^{-i\tau g_C}|^4},
                    \qquad t=r^{p_C}e^{-g_C}.                            \tag{3}
\]

This follows by multiplying the numerator $t e^{-i\tau g_C}$ of the complex derivative by $(1-te^{i\tau g_C})^2$. For fixed $j$ all but finitely many cycles have $0<\tau g_C<\pi$, so their terms are strictly positive throughout $0<r<1$. Each exceptional term extends through the circle. At $r=1$, divide (3) by $J_C$. The ratio is

\[
   \frac{(1-e^{-2g_C})(1-e^{-g_C})^2\sin(\tau g_C)}
              {|1-e^{-(1+i\tau)g_C}|^4}
          \longrightarrow \frac{2\tau}{(1+\tau^2)^2}>0
                 \quad(g_C\to0).                                        \tag{4}
\]

If infinitely many positive cycles exist, Fatou's lemma applied to the positive tail of (3) now gives $-\operatorname{Im}(r e^{i\theta_j}H'(r e^{i\theta_j}))\to+\infty$ at every $j>0$. The positive real radial derivative diverges by (1), and complex conjugation handles the negative resonances. The angles are dense because $\log_2 3$ is irrational. Any open arc of analytic extension would have bounded derivative near one such point, a contradiction. This proves the asserted natural boundary using the actual geometric damping and the physical clock identity.

The Bell–Lagarias inverse-orbit generating functions index a fixed target's preimages by their ordinary integer **values** and have coefficients zero or one. The trace here indexes **physical odd time** and its coefficients use all exact marked returns with the original weights. A finite family of cycles and any collection of escaping rays always give a rational trace. [Bell and Lagarias, *Acta Arithmetica* 170 (2015), 101–120](https://doi.org/10.4064/aa170-2-1)

## Positive spectral density and the moment

Put $D_{\rm tr}=\sum_{x\text{ nonperiodic}}D_x$. The continuous nonnegative spectral density

\[
 B(\theta)=D_{\rm tr}+\sum_C a_C\frac{1-\lambda_C^2}{|1-\lambda_C e^{ip_C\theta}|^2}
          =2\operatorname{Re}H(e^{i\theta})-\operatorname{Tr}D
\]

has integral $\operatorname{Tr}D$ for normalized Lebesgue measure. Absolute uniform convergence follows from (1). If $b_d=\operatorname{Tr}DP^d$, its $d$-th positive Fourier coefficient is $b_d$. The original first moment has the exact extended-real form

\[
 \mathcal J=\frac12\int_{-\pi}^\pi
       \frac{B(0)-B(\theta)}{1-\cos\theta}\,\frac{d\theta}{2\pi}.
\]

Each coefficient is nonnegative, so Tonelli and the identity $\int(1-\cos(d\theta))/(1-\cos\theta)\,d\theta/(2\pi)=d$ justify the equality. Distributional convergence of the marked rows or boundedness of $B$ does not give the required derivative bound.

## A trace-class perturbation determinant

Fix $u>0$. For $|z|<1$ take the usual Fredholm determinant

\[
 \mathfrak D_u(z)=\det\!\bigl(I+uD(I-zP)^{-1}\bigr),\qquad
 R_C(u)=\prod_{y\in C}(1+uD_y)^{-1}.
\]

Then

\[
 \mathfrak D_u(z)=\prod_{x\in X}(1+uD_x)
       \prod_C \frac{1-R_C(u)\lambda_C z^{p_C}}{1-\lambda_C z^{p_C}}.   \tag{5}
\]

For proof compress to $x\le N$, killing forward edges leaving the finite set. The finite determinant is $\det(I+uD-zP)/\det(I-zP)$ in those coordinates. In the determinant expansion a nontrivial permutation uses complete physical cycles, giving (5) with only cycles retained in full and the product restricted to retained sites. The same result follows by triangularizing the transient finite sites. The cutoff contractions and their adjoints converge strongly to $P,P^*$ after zero extension, hence so do their $|z|<1$ resolvents and adjoints. Multiplication by the trace-class diagonal gives trace-norm convergence of the marked resolvents, first for finite-rank diagonals and then by approximation. Continuity of the Fredholm determinant passes to the limit.

After removing the constant $\prod_x(1+uD_x)$, the logarithm has nonnegative coefficients

\[
 \sum_C\sum_{k\ge1}\frac{1-R_C(u)^k}{k}\lambda_C^k z^{kp_C}.             \tag{6}
\]

Its absolute sum on the unit circle is finite since $1-R_C^k\le k(1-R_C)\le ku a_C$. Thus the determinant extends continuously and without zeros to that circle. At a resonance as in (2), its logarithmic radial derivative contribution is

\[
 p_C\left(\frac{v}{1-v}-\frac{R_Cv}{1-R_Cv}\right),\qquad
 v=t e^{-i\tau g_C}.
\]

The negative imaginary part is the integral, for $s$ from $R_C$ to one, of

\[
       p_C\frac{t(1-s^2t^2)\sin(\tau g_C)}{|1-s t e^{-i\tau g_C}|^4}.
\]

For distinct cycles $a_C=O(g_C^2)$ by the stopping identity, $1-R_C\sim u a_C$, and hence $1-R_C=o(g_C)$. Uniformly for $R_C\le s\le1$ and $t=e^{-g_C}$, $1-s t\sim g_C$, $1-s^2 t^2\sim2g_C$, and $|1-s t e^{-i\tau g_C}|\sim|1+i\tau|g_C$. The limit of this one-cycle negative imaginary part divided by $J_C$ is consequently $2u\tau/(1+\tau^2)^2$. The same positive-tail and Fatou argument shows that the logarithmic derivative of $\mathfrak D_u$ diverges at the dense resonances if infinitely many cycles exist. Since its boundary values are nonzero, analytic continuation of the determinant would continue its local logarithm. For finitely many cycles (5) is rational up to its constant factor.

No holomorphic continuation across a unit-circle arc has been established for the actual determinant. A dense singularity here would detect infinitely many positive cycles and would persist in the presence of arbitrary escaping components.

The [exact finite arithmetic controls](check_green_spectrum.py) check the ordinary integer Green matrix and determinant sections, rational-cycle stochastic laws and characteristic polynomials, and the signed resonance numerator. [Recorded counts](../../../reports/astra-global-20261128/cycles/GREEN_SPECTRUM.json)

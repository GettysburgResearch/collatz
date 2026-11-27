# A Poisson probe for one specified ordinary source

The original geometric word law can retain an individual ordinary integer after signed real input smoothing and ternary periodization. Its limit distinguishes escape at that integer, allows every positive cycle, and has an explicit one-sided clock-frequency cutoff. The cancellation needed to rule out a positive escape has not been proved.

Use \(P_t(s)=t/(s^2+t^2)\), of integral \(\pi\), and \(e(s)=\exp(2\pi i s)\). Let \(f\) be a Schwartz function on the real line with \(\int f=0\). It can be signed or complex. At depth \(k\) write \(q=3^k\), draw the independent original positive geometric gaps \(w=(e_1,\ldots,e_k)\) in outermost-first order, and write
\[
   F_w(u)= A_wu+B_w,\qquad A_w=q2^{-d},\qquad d=\sum_{i=1}^ke_i.
\]
Thus the word probability is \(2^{-d}\), and \(Y_w=B_w\bmod q\) is the original ternary quotient. For \(t>0\), form the finite-depth real/ternary test
\[
 \mathcal D_k(f,t)
   =q\,\mathbb E_w\int_{\mathbb R} f(u)
       \sum_{\substack{y\in2\mathbb Z+1\\ y\equiv Y_w\ (q)}}
            P_t(F_w(u)-y)\,du .                                         \tag{1}
\]
The lattice sum is absolutely convergent and uniformly bounded for fixed \(q,t\). The source has been retained in the integration variable. In particular (1) uses a signed real seed and the original geometric words, not the stationary real marginal in place of that seed. The affine identifications and unit seed geometry of Paper 19 motivate this choice. [Weaver, Paper 19, §§3–4 and 9–10](https://rstation.ai/problems/collatz/papers/19/v2)

## Exact ordinary-source formula and limit

Write \(U\) for the accelerated map on signed odd integers and \(A_k(x)=3^k2^{-S_k(x)}\) for its multiplier along its actual first \(k\) odd steps. Every odd \(y\) in (1) gives a signed odd integer \(x=(y-B_w)/A_w\), and conversely these are precisely the integers following the reversed word and landing at \(y\). For a direct check let \(C_w=2^d B_w\), an odd integer for \(k>0\). The odd sources for this word occupy the unique class \(x_w\bmod 2^{d+1}\) satisfying
\[
                    3^kx_w+C_w\equiv 2^d\pmod{2^{d+1}}.                \tag{2}
\]
An odd lift gives the actual intermediate valuations, by backwards reconstruction from its odd terminal value. Increasing \(x_w\) by \(2^{d+1}\) increases the terminal integer by \(2q\). The classes across words partition all signed odd integers. Because \(q\Pr(w)=A_w\) and \(A_w P_t(A_w v)=P_{t/A_w}(v)\), this gives the exact equality
\[
             \mathcal D_k(f,t)
             =\sum_{x\in2\mathbb Z+1}(f*P_{t/A_k(x)})(x).               \tag{3}
\]
Fubini is justified before cancellation by the uniform fixed-\(q,t\) bound for the periodized kernel applied to \(|f|\).

There is an absolute summable bound in the ordinary label, uniform in all positive kernel widths,
\[
               \sup_{s>0}|(f*P_s)(x)|\le C_f(1+|x|)^{-2}.
                                                                         \tag{4}
\]
Use \(\int f=0\) to subtract \(P_s(x)\). On \(|u|\le|x|/2\) use \(\sup_s |P'_s(v)|\ll |v|^{-2}\) and \(\int |uf(u)|\,du<\infty\). On the remaining region use rapid decay of \(f\), \(\int P_s=\pi\), and \(\sup_s P_s(x)\ll1/|x|\). For bounded \(x\) use \(\pi\|f\|_\infty\).

On a positive eventual cycle the actual slope tends to zero: its positive periodic multiplier over a lap is strictly below one by the affine identity with positive offset. On a positive escaping orbit,
\[
 A_k(x)=\frac{U^kx}{x}\prod_{j<k}\frac{3U^jx}{3U^jx+1}\longrightarrow\infty
\]
by uniform reciprocal packing for simple positive paths. On a negative orbit with distinct states \(|U^kx|\to\infty\) and \(U^kx=A_k(x)x+B_w\) gives \(A_k(x)\ge |U^kx|/|x|\). A negative cycle instead has multiplier strictly above one. Thus every signed odd negative vertex has \(A_k(x)\to\infty\), independently of whether its trajectory is eventually periodic. Since \(P_s*f\to\pi f\) pointwise as \(s\downarrow0\) and \(P_s*f\to0\) uniformly as \(s\to\infty\), (4) yields
\[
  \boxed{\lim_{k\to\infty}\mathcal D_k(f,t)
    =\pi\sum_{x<0\ {\rm odd}} f(x)
      +\pi\sum_{x>0\ {\rm odd\ escaping}} f(x).}                         \tag{5}
\]
The only orbit statistic in the second sum is escape. [Positive simple-path reciprocal estimate and sources](../../astra-unconventional-20261126/boundary/COLLISION_SOURCE.md)

For a specified odd \(a>0\) take a smooth compactly supported function with value one at \(a\) and zero at the other odd integers, then compensate its integral by a bump in a separate interval disjoint from the odd integers. Its limit in (5) is exactly \(\pi\) for escape of \(a\) and zero for eventual periodicity. One can also choose a real Schwartz interpolant with compact Fourier support away from zero. Take \(g(u)=\operatorname{sinc}((u-a)/2)\,\phi(u-a)\) with \(\operatorname{sinc}(s)=\sin(\pi s)/(\pi s)\), \(\phi(0)=1\), and \(\phi\) Schwartz with smooth Fourier transform supported in \([-1/16,1/16]\). The support of \(\widehat g\) lies in \([-5/16,5/16]\). For any fixed \(c>5/16\), \(f(u)=g(u)\cos(2\pi c(u-a))\) has integral zero and unchanged odd integer values.

## The binary Fourier phases and an actual-clock cutoff

Use \(\widehat f(\xi)=\int f(u)e(-\xi u)\,du\). Apply Poisson summation separately to (3) on each class (2), initially with a compactly supported smooth \(\widehat f\) supported away from zero. The arithmetic series is
\[
 \mathcal D_k(f,t)
 =\frac\pi2\sum_{w}2^{-d}\sum_{\ell\ne0}
       \widehat f(\ell/2^{d+1})\,
       e(\ell x_w/2^{d+1})\,\exp(-\pi t|\ell|/3^k).                    \tag{6}
\]
The exponential damping is independent of the word total. The sum is absolutely convergent for fixed \(k\): the damping bounds the inner sum by \(O_t(3^k\|\widehat f\|_\infty)\) and \(\sum_w2^{-d}=1\). Source interpolation also fixes the sign in (2) and the Fourier convention in (6).

Suppose \(a\) actually escapes, and set \(d_a=S_k(a)\). In the preceding construction one can take the moving complex modulation
\[
             f_k(u)=g(u) e\bigl(c_k(u-a)\bigr),\qquad
             c_k=\lambda A_k(a)=\lambda\,3^k2^{-d_a},\quad\lambda>0 .
\]
Then \(c_k\to\infty\) and \(\int f_k=0\) eventually. The bound (4) is uniform since \(|f_k|=|g|\), and its proof only uses absolute moments and the zero integral. At every other odd integer \(x\) the row in (3) tends to zero, by \(g(x)=0\) if its width tends to zero and by the \(L^1\) bound if it tends to infinity. At \(a\), change variable \(u-a=t v/A_k(a)\) and use dominated convergence to obtain
\[
               \lim_k\mathcal D_k(f_k,t)=\pi e^{-2\pi t\lambda}.        \tag{7}
\]
This argument also applies to any \(c_k/A_k(a)\to\lambda\) with \(c_k\to\infty\). Equation (7) describes what a putative escaping ordinary word would force on the *specific* signed exponential sum (6).

For \(f_k\) as displayed, terms occur only at
\(\ell/2^{d+1}\in[c_k-5/16,c_k+5/16]\). Thus their damping is at most \(\exp[-c_{t,\lambda}2^{d-d_a}]\) for all large \(k\). The total contribution from \(d>d_a+2\log_2(k+2)\) tends to zero absolutely. Indeed for each \(d\) there are \(O(2^d)\) inner lattice frequencies, and \(\binom{d-1}{k-1}\le2^d\) words. After multiplying by \(2^{-d}\), the bound is
\(O(\sum_{d>d_a+2\log_2(k+2)}2^d\exp[-c_{t,\lambda}2^{d-d_a}])=o(1)\), since \(d_a\le k\log_2 3+O_a(1)\) on escape. The remaining lower-clock terms retain the binary phases (2). Absolute control of the truncated word count is insufficient: the particular ordinary word of \(a\) is among them at every depth. No cancellation estimate proving the vanishing needed against (7) is available here.

## Arbitrarily high order readout at finite depth

Fix any positive integer \(M\). There is a Schwartz entire interpolant \(g\) of bounded Fourier support \([-B,B]\) with \(g(a)=1\), \(g(z)-1=O((z-a)^M)\) at \(a\), and zeros of order at least \(M\) at all other signed odd integers. For example, take the \(M\)-th power of the preceding sinc factor times a Schwartz function of compact Fourier support equal to one at zero, and multiply by the degree-\((M-1)\) Taylor polynomial of its local reciprocal at \(a\). This preserves the zeros, rapid real decay and compact Fourier support.

For \(f_c(u)=e(c(u-a))g(u)\), all \(c\ge 2B+1\), and **every** depth \(k\) and width \(t>0\),
\[
   \mathcal D_k(f_c,t)=\pi\exp[-2\pi c t/A_k(a)]+O_{a,g,M}(c^{-M}).    \tag{8}
\]
The constant does not depend on any valuation, any orbit classification or \(t\). Fourier inversion on the positive band gives, for all real \(x\) and \(s>0\),
\[
   (f_c*P_s)(x)=\pi e(c(x-a))e^{-2\pi c s}g(x+i s).                    \tag{9}
\]
For \(0<s\le1\) at the odd integer labels, Taylor's theorem along the vertical segment and the uniform rapid decay of \(g^{(M)}(x+i v)\), \(0\le v\le1\), give
\[
 |g(x+i s)-\mathbf1_{x=a}|\le C s^M(1+|x-a|)^{-2}.
\]
For \(s\ge1\), two integrations by parts in the compactly supported Fourier integral give the same bound with the additional factor \((1+s)^2e^{2\pi B s}\). Increasing the constant absorbs the single subtraction at \(x=a\). After multiplying by \(e^{-2\pi c s}\), both estimates are \(O(c^{-M}(1+|x-a|)^{-2})\) uniformly in \(s>0\). Apply (9) in (3) with each row's own width and sum this absolute error. The main term is exactly the one in (8).

For a fixed total \(d\), Paper 42 supplies exponential decay for the *mean absolute* normalized source Fourier coefficient on an exponentially large frequency set, also for count-conditioned sources. In (6), grouping the words by \(d\) multiplies the corresponding frequency average by \(\binom{d-1}{k-1}\). On the full dyadic frequency group, the average absolute coefficient of the uniform probability on any nonempty set of \(N\) residues is at least \(1/N\), by exact Fourier inversion at one member. Consequently an absolute-frequency estimate applied on the whole group cannot give an error smaller than the reciprocal source multiplicity. The signed pairing with the specified positive label in \(\widehat f\) remains essential. [Weaver, Paper 42, Theorem 1 and the count-bridge estimates](https://rstation.ai/problems/collatz/papers/42)


## Finite signed normalization check

The [direct checker](check_poisson_probe.py) uses the seed
\(e(2(u-a))\operatorname{sinc}((u-a)/2)^4\). It has a compact cubic-spline Fourier density, vanishing at both edges of its positive band, and sufficient real decay for (3) and (6). On the odd lattice its analytic row is
\[
 (f*P_s)(x)=\frac{e^{-2\pi s}(1-e^{-\pi s})^4}{\pi^3(x-a+is)^4}.
\]
One side sums this expression on actual signed ordinary orbits with \(|x|<2048\). The other side enumerates exponent compositions, solves (2), replays their actual valuations and Fourier transforms their binary residue indicators. The absolute bound for the two truncated tails is below \(2.7\cdot10^{-12}\) in all twenty tests at depths one through five. The [retained numerical rows](../../../reports/astra-six-hour-20261127/escape/poisson_probe.tsv) agree within that bound. This is a floating-point check of signs, normalizations and arithmetic indexing.

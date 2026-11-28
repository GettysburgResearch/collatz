# Interior digit rigidity and a physically tagged boundary countermodel

The source method is tame_orbits's binary-window theorem for Collatz orbit statistics. That paper proves joint times-two/times-three invariance after averaging digit heights, transports entropy of a stationary shortcut law, and shows that even single-height Haar statistics can coexist with biased shortcut parity. It credits earlier window-ranking work of Nashida and successors. The application here concerns finite positive *grid-periodic* integers, where period versus height gives a definite positive entropy contribution at the full physical bit width. The converse construction below uses two coupled digit bases, a deterministic mechanical calendar, true folded odd tags, and the upward and downward rounding laws. [tame_orbits, rStation 170, Theorems 1–2 and Propositions 5–6](https://rstation.ai/problems/collatz/papers/170)

### Finite periodic grids force a Haar component

Take an integer \(F_K\) orbit of least period \(q\), sampled uniformly in time, and let \(x\in[K,2K)\) be its fundamental label, \(\theta=\log_2(x/K)\). Put \(L=\lceil\log_2(2K)\rceil\) and choose \(j\) uniformly from \(1,\ldots,L\). For \(K\to\infty\), every subsequential limit of \((\theta,\{x/2^j\})\) has an angle-Haar times digit-Haar component of mass at least \(1/3\). More precisely the mass is at least the lower limit of \(\log_2 q/L\) along the subsequence. The same argument applies to the folded integer columns of a true two-grade cycle.

The physical edge is \(2^b x'=3x+r\) with \(b\in\{1,2\}\) and bounded \(r\). Multiplication by two in the window shifts \(j\) by one, so the endpoint loss is \(O(1/L)\). Multiplication by three sends the window within \(O(2^{-j})\) of the window at height \(j-b\) of the next label. The angle advances by \(\gamma+O(1/K)\), \(\gamma=\log_2 3\), and the variable height shift loses at most two terms per time fiber. Thus the limiting joint law is invariant under \((\theta,u)\mapsto(\theta,2u)\) and \((\theta,u)\mapsto(\theta+\gamma,3u)\) on the two circles.

The distinct \(L\)-bit labels have entropy \(\log_2q\). For any fixed \(k\), partition each word into disjoint length-\(k\) blocks in each of the \(k\) possible starting offsets, allowing two end fragments of length less than \(k\). Subadditivity, summed over these offsets, gives total window-block entropy at least \(k\log_2q-O(k^2)\) before dividing by \(L\). Entropy concavity passes this lower bound to the mixed height law. To handle mass at dyadic partition endpoints, take a weak subsequence of the ordinary zero-padded symbolic binary expansions of the windows. Shift invariance holds by deleting the first symbol. Fixed cylinders are clopen, so the limiting length-\(k\) entropy is at least \(k\liminf\log_2q/L\). The binary evaluation map onto the circle has fibers of cardinality at most two and preserves entropy of invariant laws. Sending \(k\to\infty\) gives the same lower bound for normalized doubling entropy. The grid clock obeys \(0<a/q-\gamma=O(1/K)\); the cited irrationality exponent at most three gives \(\liminf\log_2q/L\ge1/3\). [Chudnovsky, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)

In the joint ergodic decomposition, a component's digit marginal is jointly ergodic under times two and times three. Entropy is affine under this invariant decomposition. Rudolph's theorem identifies every positive-doubling-entropy digit component with Lebesgue measure, whose normalized entropy is one. If the digit marginal is Lebesgue, disintegration over the angle gives Lebesgue conditionals: they are doubling-invariant, and Lebesgue is ergodic under doubling. The angular marginal is Haar by irrational rotation. Hence the positive-entropy components give the asserted product measure and mass bound. [Rudolph, *×2 and ×3 invariant measures and entropy*, 1990](https://doi.org/10.1017/S0143385700005629)

### Individual scales in the upper third

For each fixed \(\epsilon>0\) the angular star discrepancy on every periodic grid orbit is \(O_\epsilon(K^{-1/3+\epsilon})\). Choose the first continued-fraction denominator \(s\ge K^{1/3-\epsilon/2}\) of \(\gamma\). The previous denominator is smaller, and the irrationality bound gives \(s\le K^{2/3-\epsilon/2}\) for sufficiently large \(K\), after a possibly smaller internal exponent slack. Any block of \(s\) consecutive angles is within \(O(s/K+1/s)\) of a translate of the regular \(s\)-grid by the convergent comparison. Average blocks over all cyclic origins; they may traverse the orbit more than once. This proves the discrepancy estimate.

Fix \(0<\epsilon<1/6\), and let both \(2^j\) and \(3^l\) lie between \(K^{2/3+\epsilon}\) and \(K^{1-\epsilon}\). At **individual** such levels the joint law of
\[
                    (\theta,\{x/2^j\},\{x/3^l\})
\]
tends to the product of three Haar measures, uniformly in the allowed levels. For fixed Fourier indices \(h,m,n\), the angular test function is \(\exp(2\pi i[h\theta+T2^\theta])\), where \(T=K(m/2^j+n/3^l)\). Its variation is \(O_{h,m,n}(1+K^{1/3-\epsilon})\), so the discrepancy estimate with a smaller slack replaces the orbit by Haar angles at error \(o(1)\). If \((m,n)\ne(0,0)\), then \(|T|\to\infty\). For opposite signs at comparable scale this follows from the fixed-rational logarithmic-form lower bound for \(l\ln3-j\ln2+\ln|m/n|\). More explicitly the possible small relative difference is \(|( |m|3^l )/( |n|2^j )-1|\); its nonzero logarithm has size at least \((\log K)^{-O_{m,n}(1)}\). Exact equality is impossible for large \(j,l\) by valuations. The cases of one zero frequency, equal signs, or incomparable scales are immediate. Substitution \(u=2^\theta\) in the resulting angular integral gives decay as \(|T|\to\infty\). If only \(h\ne0\), angular Haar suffices. [Matveev, logarithmic-form bound](https://doi.org/10.1070/IM2000v064n06ABEH000314)

### A biased two-base model with full individual-window Haar limits

Choose a Haar angle and its two-sided irrational mechanical calendar \(b_t\) of slope \(\gamma\). Every \(b_t=1\) is followed by \(b_{t+1}=2\). Partition the dates into pairs \((t,t+1)\) beginning at each one and the remaining singletons. Independently on each pair choose the two tags \((c_t,c_{t+1})\) uniformly from \((1,1),(1,2),(2,2)\); on each singleton choose one of \(1,2\) fairly. This conditional product construction is stationary under a time shift and angle rotation. Its conditional entropy per date is
\[
             (2-\gamma)\log_2 3+(2\gamma-3)>\gamma/3 .
\]
In particular \(e_t=b_t+\log_2c_{t+1}-\log_2c_t\ge1\). The affine equations \(2^{b_t}z_{t+1}=3z_t+c_t\) have unique two-sided compatible dyadic coordinates from the future and ternary coordinates from the past. Equivalently solve \(2^{e_t}x_{t+1}=3x_t+1\) in each ring and put \(z_t=c_tx_t\). The native dyadic \(x_t\) are odd, the ternary \(x_t\) are units, and the companion \(z_t+1\) has the exact high forward digit \(2^{b_t}-3+c_t\). Since every conditional mean tag is at least \(4/3\), the modeled physical coefficient
\[
               (3\ln2)^{-1}\mathbb E[c_t 2^{-\theta_t}]
                   \ \ge (4/3)C>3/8.
\]
For the companion's excess coefficient the extra term \((3\ln2)^{-1}\mathbb E[(2^{b_t}-3)2^{-\theta_t}]\) vanishes by angular stationarity, since \(2^{b_t}2^{-\theta_t}=3\,2^{-\theta_{t+1}}\) on the ideal rotation. Here \(C=1/(6(\ln2)^2)\).

Nevertheless, conditional on the entire calendar, the dyadic window \((z_0\bmod2^j)/2^j\) tends to Haar **at every individual level** \(j\to\infty\); the analogous ternary window tends to Haar as \(l\to\infty\). The two windows jointly tend to product Haar as the two levels grow independently, uniformly in the initial angle. We give the nondegeneracy argument since the physical pair law is not an independent single-letter law.

In the dyadic expansion the future tag at date \(i\ge0\) has coefficient \(-2^{b_0+\cdots+b_{i-1}}3^{-(i+1)}\). In the ternary expansion the past tag at date \(-i-1\) has coefficient \(3^i(2^{b_{-1}+\cdots+b_{-i-1}})^{-1}\). Work at a fixed nonzero integer Fourier frequency \(m\), absorbing the dyadic minus sign. In either case let \(P_i\) be the successive moduli consumed, and \(Q_i\) the successive inverse factors: \((P_i,Q_i)=(2^{b_i},3)\) in the first case and \((3,2^{b_{-i-1}})\) in the second. In the dyadic case shorten the last \(P_i\) to two when needed so that the target modulus is exactly the product. Set \(M_i=\prod_{k=i}^{N-1}P_k\), and choose each coefficient phase \(a_i\in[-1/2,1/2]\) representing
\[
          \frac{m (Q_0\cdots Q_i)^{-1}\bmod M_i}{M_i}\quad(0\le i<N).
\]
Put \(a_N=0\), with any allowed \(Q_N\). The numbers
\[
 v_0=Q_0 a_0-m/M_0,\qquad v_i=Q_i a_i-P_{i-1}a_{i-1}\quad(1\le i\le N)
\]
are bounded integers for fixed \(m\). Multiplying by \(M_i\prod_{k<i}Q_k\) and telescoping gives
\[
               -m=\sum_{i=0}^N v_i M_i\prod_{k<i}Q_k .                \tag{1}
\]
Every weight is a positive \(\{2,3\}\)-unit of size at least \(2^N\).

The number of nonzero \(v_i\) tends to infinity uniformly over these calendars. Otherwise remove vanishing subsums while keeping the fixed nonzero total in (1), then pass to a subsequence of fixed support size and fixed bounded nonzero coefficients. The rational fixed-rank \(S\)-unit equation theorem permits only finitely many ordered nondegenerate solutions with that fixed right-hand side and those coefficients. The individual weights grow without bound, a contradiction. Except for the two end carries, each nonzero \(v_i\) forces at least one of \(|a_{i-1}|,|a_i|\) to be at least \(1/8\). The number of such large phases therefore tends to infinity. [Evertse, Schlickewei and Schmidt, Theorem 1.1](https://annals.math.princeton.edu/2002/155-3/p04)

There is also an effective rate using [the local logarithmic-form estimate](../phase5/PHYSICAL_LOOP_ARMS.md). In the dyadic window put \(P_i=2^{p_i}\), \(E_i=\sum_{k<i}p_k\). For two consecutive nonzero carry indices \(i<j\), the prefix of (1) through \(i\) has the form \(2^{E_N-E_i}V_i\), where
\[
                    V_i=\sum_{k\le i}v_k3^k2^{E_i-E_k},
                    \qquad \log(2+|V_i|)=O_m(i+1).
\]
All later terms are divisible by \(3^j\). Consequently \(3^j\mid m+2^{E_N-E_i}V_i\). Except within \(O_m(1)\) of the terminal index this integer is nonzero by its dyadic valuation if equality were to hold. For \(j>v_3(m)\) the congruence forces \(V_i\ne0\) and \(v_3(V_i)=v_3(m)\). Apply Yu's two-logarithm inequality to the rational 3-adic units \(2\) and \(-V_i/m\), with exponents \(E_N-E_i,1\); it gives
\[
                       j+1\le C_m(i+1)\log(2+N).                     \tag{2}
\]
The finite cases with a rational factor of height zero may be removed directly or by the fixed-base lifting-the-exponent estimate. The case \(j\le v_3(m)\) already obeys (2), and when \(i\) is within the bounded terminal strip (2) is immediate. For the ternary windows the prefix is \(3^{N-i}V_i\), \(V_i=\sum_{k\le i}v_k3^{i-k}\prod_{s<k}Q_s\) again having logarithmic height \(O_m(i+1)\). The tail is divisible by at least \(2^j\). Apply Yu at a prime over two in the fixed field \(\mathbb{Q}(\zeta_3)\), meeting his hypothesis (1.2). The rational units are \(3,-V_i/m\), the exponents are \(N-i,1\), and the valuation on rational numbers changes only by the fixed ramification index. This proves (2) at the other place.

The first nonzero index is bounded in terms of \(m\) by the common prefix-base valuation of every summand in (1), and the last nonzero index is \(N-O_m(1)\) by their common suffix-base valuation. Iterating (2) forces at least \(c_m\log N/\log\log N\) nonzero carries for large \(N\), with effective constants. The same lower bound, after an absolute factor and endpoint loss, holds for large phases. [Yu, *p-adic logarithmic forms and group varieties II*, Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

The characteristic function of a pair at phases \(u,v\) is the average of the three unit exponentials corresponding to \((1,1),(1,2),(2,2)\). Its support differences include \((1,0)\) and \((0,1)\), so its modulus is uniformly below one if either centered argument has magnitude at least \(1/8\). The same holds for a singleton. Independence between blocks and the preceding count bound every fixed nonzero Fourier coefficient in absolute value by \(\exp(-c_m\log N/\log\log N)\) for sufficiently large \(N\). Removing the bounded number of blocks meeting an endpoint leaves the argument intact. In particular, condition on the at most one block straddling the past/future split; the remaining two independent products give the joint conclusion by Weyl's criterion.

This is a model of the arithmetic places and the angle, not a periodic orbit of a single positive integer. It satisfies the physical tag restriction, has more conditional symbolic entropy than the finite-cycle lower bound, and gives both maximal-window rigidity conclusions even at single arbitrarily high digit levels. Those facts alone therefore cannot bound the boundary coefficient by \(3/8\). tame_orbits's single-base biased parity model already demonstrates the analogous distinction for the shortcut source. The additional uniform two-base result here retains the mechanical calendar and folded native pair law. [tame_orbits, Proposition 5](https://rstation.ai/problems/collatz/papers/170)

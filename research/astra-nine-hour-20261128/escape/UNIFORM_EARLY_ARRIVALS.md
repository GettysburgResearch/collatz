# Early first arrivals at a moving target and the untruncated correction mean

**PROPOSED, source-qualified written result.** Write \(D=\log(4/3)\), \(\mu=2/D\), and use the positive shortcut clock. For \(X\ge3\) put \(L=\log X\). Uniformly over **every** positive odd target \(y\), including \(y>X\) and periodic targets, a uniformly sampled positive source \(n\le X\) satisfies
\[
 \Pr(\tau_y(n)\le \mu L-z\sqrt L)
       \ll e^{-c z^2}+C_B(1+z\sqrt L)^{-B},
       \qquad 1\le z\le\mu\sqrt L, \quad B>0.                         \tag{1}
\]
The first-arrival time is infinite when there is no hit. The estimate is for one specified, possibly moving target at a time. There is no union bound over an unbounded target family in (1).

The main input is the *signed* impulse decomposition of the exact ordinary first-arrival rows in PR213. We use its total variation and tail in the original source height, where both bounds are uniform in the target. That written result includes the initial atom and the subtraction of the unique primitive lap at periodic odd targets; its dependencies include the signed physical ternary-source estimate of PR195 and Weaver–Wren's exact-total mixing. We did not rebuild these analytic inputs. The real first-arrival correction floor follows from the elementary packing input cited there. [PR213, pinned text, (3), (5)–(7)](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md)

## Summing the exact clock and grade in one source octave

Begin with odd sources \(X\le x<2X\). For their first arrival to \(y\) write \(j,s\) for the odd grade and physical shortcut time. The full first-arrival row has normalized mass \(m_{j,s}=p^{-1}\#\{x \text{ in row}\}\) at \(p=y2^s/3^j\). Every member satisfies \(c_0p\le x\le p\) for one absolute \(c_0>0\), by simple-path reciprocal packing. Thus the normalized actual source count in the octave up to a clock deadline \(S\) is at most
\[
 C\sum_{s\le S,\ X\le p\le 2X/c_0}m_{j,s},
\]
where the sum includes every \(j\). For each target the input gives a signed array \(c_{i,v}\) supported at nonnegative integer grades and clocks, of uniformly bounded total variation. For \(p_0=y2^v/3^i\) its mass above any \(R\ge2\) satisfies \(\sum_{p_0\ge R}|c_{i,v}|\ll_B(1+\log R)^{-B}\). The exact rows are
\[
        m_{j,s}=\sum_{i,v}c_{i,v}\,g_{j-i}(s-v),\qquad
        g_k(w)=2^{-w}\binom{w-1}{k-1}\quad(1\le k\le w).
\]
Take \(g_0(w)=1_{\{w=0\}}\) and zero elsewhere. These equations hold even if the original group of endpoints is empty. Absolute values of the impulses suffice for an upper bound.

For one impulse use \(h=\log(X/p_0)\) and \(J=\log(2/c_0)\). The possible residual indices satisfy
\[
       h\le w\log2-k\log3\le h+J,\qquad w\le S-v\le S.                  \tag{2}
\]
For each positive \(w\) there are at most \(1+J/\log3\) integer grades. The uniform binomial bound
\[
 g_k(w)\le {C\over\sqrt w}
      \exp\bigl(-c(w-2k)^2/w\bigr)
\]
follows from \(g_k(w)=(k/w)2^{-w}\binom wk\). On \(w/4\le k\le3w/4\), Stirling's bounds give the prefactor and the binary relative entropy is at least \(2(k/w-1/2)^2\). Outside that range the binomial Chernoff bound is exponential in \(w\), absorbing the prefactor after reducing \(c\). For \(r=w\log2-k\log3\),
\[
              (w-2k)\log3=2r-Dw .
\]
The bounded spacing error \(r-h\) in (2) can be absorbed by reducing the Gaussian constant and multiplying its prefactor by a constant depending only on \(J\). Consequently for \(w\ge1\) the summed row at this \(w\) is at most
\[
          C w^{-1/2}\exp[-c(w-\mu h)^2/w].
\]
Its sum over \(w\ge1\) is bounded uniformly in all real \(h\). For \(\mu h\le2\) compare the upper tail with an exponential. For \(a=\mu h>2\), the central range \(a/2\le w\le2a\) is a discretized Gaussian sum divided by \(\sqrt a\); the left tail costs \(O(\sqrt a e^{-ca})\) and the right tail costs \(O(1)\). The \(w=0\) term costs at most one.

Set \(S=\mu L-z\sqrt L\). At impulses with \(\log p_0\le z\sqrt L/(2\mu)\) one has \(h\ge L/2\) and, throughout \(1\le w\le S\), \(\mu h-w\ge z\sqrt L/2\). Since \(w\le\mu L\), half the Gaussian exponent pays \(e^{-c'z^2}\); summation of the other half is still uniformly bounded. The zero-time term cannot occur for large \(L\) because (2) excludes it. The complementary impulses cost \(O_B((1+z\sqrt L)^{-B})\) by their source-height tail and the uniform whole-row sum. This proves (1) on the odd octave. Very large \(y\) incurs no extra term. In particular its possible impulse at \((0,0)\) has absolute weight \(1/y\).

## Initial twos and the full source range

For an all-positive octave write \(x=2^a x'\) with \(x'\) odd. A first hit at a prescribed odd target has clock \(a+\tau_y(x')\) and the odd source has log scale \(L'=L-a\log2\). For \(a\le c_1z\sqrt L\), choose \(c_1>0\) so small that \(L'\ge L/2\) and \((\mu\log2-1)a\le z\sqrt L/2\) throughout the stated range of \(z\). The residual deadline is at most \(\mu L'-z\sqrt L/2\). Apply the odd-octave bound and sum with the factor \(2^{-a}\). If the reduced \(z\) is below one, the trivial bound is absorbed by increasing the absolute constant; if the residual deadline is negative the event is empty. The omitted integers are divisible by a prescribed \(2^{\lfloor c_1z\sqrt L\rfloor+1}\), so their fraction is \(O(e^{-c z\sqrt L}+X^{-1})\). This is absorbed in (1).

For \(1\le n\le X\), split into dyadic octaves below \(X\). At octave distance \(j\le c_2 z\sqrt L\), the scale is \(L'=L-(j+1)\log2\), differing by at most \(z\sqrt L/(2\mu)+O(1)\) for sufficiently small \(c_2>0\). The same early deficit estimate applies, now with the geometric source weights of the octaves. The remaining initial segment has relative size \(O(e^{-c z\sqrt L})\). Integer endpoints and the bounded range of small \(L,z\) can be covered by adjusting constants. This proves (1) on the original source interval.

## Pooled periodic sites and convergence of every correction moment

All periodic sites, pooled over all cycles, satisfy
\[
       \#\{x\le H:x\ { \rm periodic}\}\ll H^{49/50},\qquad
       \sum_{x\ { \rm periodic}}\frac1x<\infty .                         \tag{3}
\]
This pooling follows because \(T^k\) is injective on the **entire** set of periodic sites: two periodic points with the same image lie in the same cycle, where the map is a permutation. Take \(k=\lceil\log_2 H\rceil\). Each length-\(k\) word has at most one source through \(H\) by the native parity bijection. Words with more than \(3k/5\) odd inputs contribute at most \(2^{H_2(3/5)k}\), with \(H_2(3/5)<49/50\). At smaller odd count every image is at most \(3^{3k/5}+(3/2)^k\): the linear part is \(3^q2^{-k}x\), and the upper envelope of the additive part is realized by iterating the affine odd branch on zero. Both bases are below \(2^{49/50}\). Count the distinct small images once, add high-count sources, and sum over dyadic shells for (3). The unrestricted image bound and this periodic consequence already appear in PR211. [PR211, passage using periodic injectivity](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/SYNCHRONIZATION.md)

At \(t=\lfloor\mu L+u\sigma\sqrt L\rfloor\), with fixed real \(u\), (1) and integration of its tail give, for every fixed \(r\ge1\),
\[
 \sup_{X\ge3,\ y\ { \rm odd}}\Big\|
          (t-\tau_y)_+/\sqrt L\Big\|_{L^r}<\infty .
                                                                         \tag{4}
\]
Take the positive part as zero at an infinite first-arrival time. Large \(z\) beyond the time-zero threshold cost zero, and the polynomial tail in (1) can be taken at any exponent greater than \(r\).

For every source the departed sites before its first cycle visit are distinct, including the whole prefix if no cycle has yet been hit. They contribute at most \((1+\log(2+t))/3\) to the exact \(E_t\) in the companion paper. Every remaining odd site \(y\) is periodic, and it can be counted at most \((t-\tau_y)_+\) times. Therefore the \(L^r\) norm of \(E_t/\sqrt L\) is uniformly bounded by Minkowski's inequality, (4), and the convergent series \(\sum_{y\ { \rm periodic},\ y\ { \rm odd}}\log(1+1/(3y))\) from (3). One may truncate to finitely many sites before applying Minkowski and then use monotone convergence. The same argument uniformly bounds the contribution above a spatial cutoff \(H\) by \(O_{r,u}(H^{-1/50})\) after normalization.

All finite positive moments in the critical law now converge: for moment order \(k>0\), use (4)'s consequence at an exponent \(r>k\) to get uniform integrability. In particular, with \(\phi,\Phi\) the standard normal density and distribution function,
\[
  \lim_X \frac{1}{X\sigma\sqrt{\log X}}\sum_{n\le X} E_t(n)
       =[u\Phi(u)+\phi(u)]\sum_{C\ { \rm cyclic}}d_C A_C.                   \tag{5}
\]
At each fixed periodic site \(y\) the visit count differs from \((t-\tau_y)_+/P_C\) by at most one. Thus summing the fixed-target first-arrival clocks gives exactly the same normalization: (3)–(4) permit the sum over periodic sites, and the transient part is negligible. An escaping component contributes zero on the observable's scale even if it carries positive ordinary source mass. The impulse norm estimate proves (1) and allows moment passage; it gives no identity forcing the coefficient in (5) to be \(D/2\). [Critical correction law and the below-center parity event](CRITICAL_CORRECTION.md)

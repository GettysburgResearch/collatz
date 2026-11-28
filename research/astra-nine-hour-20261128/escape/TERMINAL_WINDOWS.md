# Ordinary parity in the terminal window of the descent

**PROPOSED, source-qualified written theorem.** Sample a uniform positive source at most \(X\). In the notation of [the critical correction law](CRITICAL_CORRECTION.md), put \(L=\log X\), \(b=\sigma\sqrt L\), \(a_1=D/2\), \(\gamma=a_1/\log3\), \(\tau=\tau_{m(n)}(n)\), and \(t_u=\lfloor\mu L+u b\rfloor\). For every fixed \(U\),
\[
  \sup_{|u|\le U,\,t_u\le\tau}
  \frac{|(F_\tau-\tau/2)-(F_{t_u}-t_u/2)|}{b}
            \longrightarrow 0\quad\text{in probability}.                  \tag{1}
\]
The supremum of the empty set is zero. This is a centered parity bound on the *actual last part* of the descent at square-root-logarithmic time resolution. The statement allows every possible positive component. A two-scale comparison of genuine first landings supplies the time resolution in (1).

## Source imports

We use the joint minimum and first clock law (4) in the companion note, Inselmann's uniform log-height approximation (Theorem 1.1), and the relative first-landing estimate of PR213. For the last input write \(L_R(x)\) for the first **odd** state at most \(R\), including the cemetery on failure, after deleting initial twos. For an odd octave \([Z,2Z)\) and also for an all-positive octave, the imported estimate gives
\[
 \sup_{0\le g\le1}|\mathbb E g(L_R(x))-\nu_R(g)|
    \ll (\log(Z/R))^{-1/9}+C_B(\log(Z/R))^{-B}
\]
when \(\log(Z/R)\ge2\). The constants and starting separation are independent of the cutoff and the test. In particular the test may be an arbitrary deterministic property of the eventual forward path of the **label**. The same reference proves equality of the limiting odd and all-positive label laws. This is a source-qualified import involving exact-clock third-adic mixing. [PR213, relative first landing, (1), source pin 5ac2b4a7](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md) · [Inselmann, Theorem 1.1](https://arxiv.org/html/2402.03276v3)

## Typical prefixes from a fresh source

Use \(z\) uniform odd in \([Z,2Z)\), \(Z\to\infty\), and let \(\tau_*(z)\) be its first global minimum time. With probability tending to one,
\[
 \tau_*(z)/\log Z\longrightarrow\mu,\qquad
 H(z):=\max_{j\le\tau_*(z)}|F_j(z)-j/2|=o_P(\log Z).                  \tag{2}
\]
For the first assertion the full-population exceptional set of any fixed proportional clock error has density zero by the joint minimum law. Its intersection with an odd octave has conditional probability \(o(1)\), because that octave contains a positive proportion of all integers through \(2Z\). The same transfer applies to Inselmann's estimate. Written for physical shortcut time, that estimate gives, for arbitrary \(\eta>0\), simultaneously for \(j\le\mu\log z\) on a density-one population,
\[
   |\log T^j z-\log z+a_1 j|\le\eta\log z .
\]
Up to \(j\le(\mu-\delta)\log Z\), choose \(\eta<a_1\delta/3\) and use \(\log z=\log Z+O(1)\). Every state on that prefix exceeds a positive power of \(Z\), so the cumulative log correction is \(o(1)\). The affine identity gives centered parity at most \((\eta\log z+o(1))/\log3\) there. On the remaining times through \(\tau_*\) the centered count changes by at most one half per step, for at most \((\delta+o_P(1))\log Z\) steps. Take arbitrarily small fixed \(\delta,\eta\) to obtain (2).

## Transfer of a terminal segment

Take \(Z=R^2\) first. At the deterministic time \(j_0=\lfloor(5/4)\mu\log R\rfloor\), the same height law puts the actual state at most \(R^{0.9}\) with probability tending to one. Equation (2) gives \(\tau_*(z)=(2\mu+o_P(1))\log R\). If that state is even, follow its even steps to the next odd state. This wait ends by the odd minimum, and is at most \(4H(z)\), since the centered count decreases by one half on each consecutive even step. The first odd landing at or below \(R\) therefore has occurred by time \(j_0+o_P(\log R)\).

If \(y=L_R(z)\ne\dagger\), every earlier odd state exceeds \(R\). Each earlier even state is at least its next odd state, either above \(R\) or equal to \(y\). In particular the earlier sites are all strictly above \(y\). This also applies when the source has leading even steps. Consequently \(m(z)=m(y)\), and the first global minimum clock is the landing time plus \(\tau_*(y)\). Subtracting two centered prefix counts bounds \(H(y)\le2H(z)\). We have proved that the following properties of the landed label hold with probability tending to one in the fresh octave, for each fixed \(\epsilon>0\):
\[
   y\ne\dagger,\qquad \tau_*(y)\ge(\mu/2)\log R,\qquad
                      H(y)\le\epsilon\log R.                           \tag{3}
\]
Neither the time taken to land nor the preceding source trajectory is part of the label test.

Now set \(R=\lfloor\exp(Kb)\rfloor\), for fixed \(K>0\). Its logarithm tends to infinity and is \(o(L)\). Use the uniform first-landing estimate once at the fresh scale \(Z=R^2\) and once on each of the original all-positive octaves \([X/2^{i+1},X/2^i)\), with \(i\) in an arbitrary fixed finite range. Both approximations refer to the same \(\nu_R\), and all logarithmic separations tend to infinity. The remaining sources have arbitrarily small total proportion by taking sufficiently many fixed octaves. Rounding endpoints costs \(o(1)\). Thus (3) transfers to the original sample \(n\le X\). In particular \(H(L_R(n))=o_P(\log R)\) at each fixed \(K\).

For any \(\rho>0\) choose \(M_0\) with \(\limsup\Pr(|\tau-\mu L|>M_0b)<\rho\) by the Gaussian clock. Then fix \(K\) so large that \(K\mu/2>M_0+U+1\). On the resulting high-probability event (3) the time from landing to the minimum exceeds \(\tau-t_{-U}\), so the whole part of the sampled window before the minimum lies after first landing. The centered count on any subsegment from landing to the minimum is bounded in absolute value by \(2H(L_R(n))=o_P(b)\) at this fixed \(K\). Sending \(\rho\) to zero proves (1). No interchange of a growing \(K\) with the original-source limit is required.

## A law on the whole critical window

Define the continuous piecewise linear profile of a fixed positive start \(m\) by interpolating
\[
 f_{m,X}(j/b)=(F_j(m)-j/2)/b\qquad(j\ge0).
\]
These functions are \(1/2\)-Lipschitz and vanish at zero. Every sequence \(X\to\infty\) has a subsequence on which all profiles, for all fixed \(m\), converge uniformly on compact intervals to functions \(f_m\). Along such a subsequence the actual path, with linear interpolation between adjacent physical times, satisfies
\[
  \left(\frac{2(F_{t_u}(n)-t_u/2)}{\sqrt{t_u}}\right)_{|u|\le U}
    \Longrightarrow
  \left(G+\gamma^{-1} f_M((u-G)_+)\right)_{|u|\le U}                  \tag{4}
\]
in the uniform topology. Here \((M,G)\) is the independent minimum and Gaussian pair in the companion note. The original source interval and the physical clock are deterministic. Only the profiles of hypothetical unbounded ordinary paths may require passage to a subsequence.

Indeed, the simple segment to first minimum has log correction \(O(\log(2+\tau))\). The minimum is tight and \(\log(X/n)=O_P(1)\). Writing the log product at the minimum gives
\[
 F_\tau(n)-\tau/2=\gamma(\tau-\mu L)+o_P(b).
\]
Before the first minimum insert (1), and after it insert the exact next \(t_u-\tau\) steps from \(m\). The interpolation error is \(O(1/b)\) after normalization. On compact clock-deviation ranges and a finite set of minima the profile convergence is uniform. Truncate both ranges, apply joint convergence of minimum and clock, and then release the truncations. The normalizing constant is \(2\gamma\sigma/\sqrt\mu=1\).

On a bounded future with eventual odd fraction \(\beta_C\), the profile is \(f_m(s)=(\beta_C-1/2)s\). On an escaping future its scaled log height is nonnegative and
\[
 f_m(s)=\gamma s+\frac{1}{\log3}
                \lim \frac{\log T^{\lfloor s b\rfloor}(m)}{b},
\]
along the selected subsequence, uniformly on bounded \(s\). This again follows from the simple-path log correction. Under universal convergence, the full process in (4) is the single constant-in-\(u\) random function \(G\). Thus the complete ordinary-source Gaussian limit under convergence, including the late half of the critical layer, follows from the imported trajectory estimates. Equality of even the single strict lower-tail test of the companion note would conversely imply convergence. The law (4) does not determine that equality.

## The variance transition at fixed multiples of logarithmic time

For every fixed \(0<\kappa\le\mu\) the empirical variance of \(F_t(n)/t\) tends to zero for \(t=\lfloor\kappa\log X\rfloor\), regardless of the eventual positive components. Its empirical mean tends to one half. For \(\kappa<\mu\) this follows from the prefix height argument proving (2), with \(n\le X\) after discarding a small lower tail. For \(\kappa=\mu\), the centered count at \(\tau\) is \(O_P(b)\) as above and the two clocks differ by \(O_P(b)\). Boundedness yields moment convergence.

For **every** fixed \(\kappa>\mu\), the same vanishing variance is equivalent to universal convergence under the companion note's positive-basin import. The empirical mean has liminf strictly above one half if any counterexample exists. Indeed \(\tau=(\mu+o_P(1))L\), and the prefix to \(\tau\) has centered count \(o_P(L)\). At a fixed bad minimum \(m\) the entire future stays above or at three. A length \(h\) prefix from \(m\) has
\[
   2^h T^h(m)\le m(3+1/3)^{F_h(m)},\qquad T^h(m)\ge m.
\]
Thus every such prefix has odd fraction at least \(p=\log2/\log(10/3)>1/2\). At a good minimum, equal to one, the centered count on every future prefix is bounded by one. Tightness of \(\tau\) on its stated scale gives a separation of at least \((1-\mu/\kappa)(p-1/2)\) between the limiting good value and the lower edge of the bad population. The two populations have positive density if a counterexample exists. For instance, the variance is half the expectation of the squared difference between two independent samples, which gives a strictly positive liminf. Under convergence the only population has limiting value one half. This identifies the exact change in the fixed logarithmic multiplier for the earlier superlogarithmic variance criterion. It leaves the post-critical variance value open.

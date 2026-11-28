# Ordinary integers at every dyadic corrected height on an escaping grade

**Written deduction from the pinned ordinary posterior and the fixed-total atom floor.** If an ordinary positive odd orbit escapes, each sufficiently large dyadic corrected-height level of its synchronous class contains exponentially many distinct ordinary integers. They lie in a relative real interval shrinking to zero. With the proposed mixed-modulus floor of checkpoint one the same statement holds in every moderately growing odd arithmetic progression. The counting and growth statements without a progression use only the earlier pure ternary atom floor.

**Precedence.** PR193's graded correction theorem already proves the unmodulated lower bound \(c_m(4/3)^\ell/\sqrt{\ell}\) at every sufficiently large dyadic level, including the first-hitting argument and uniform approach of the selected real marks to one. It also identifies the full fixed-grade correction accumulation sets. The additions below are the same-level count in growing odd progressions, the growth-sensitive counting exponent (4) and its fractional-moment implication (5), and the stated concentration consequences for the original zero-overshoot posterior in (6). [PR193, graded correction sets and large equal-clock classes, equation (2)](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/GRADED_CORRECTION_SETS.md)

Let \(m\) be a positive odd unit, \(a_j=U^jm\) an injective orbit, \(A_j=\sum_{i<j}v_2(3a_i+1)\), \(\Gamma_j=\{x>0:x\text{ odd},U^jx=a_j\}\), and \(\Gamma=\bigcup_j\Gamma_j\). Set \(d=\log(4/3)\) and
\[
 P(x)=x\prod_{i\ge0}\left(1+\frac1{3U^i x}\right),\qquad
 B(Y)=\#\{x\in\Gamma:x\le Y\}.
\]
On this component \(P(x)<\infty\), \(P(Ux)=3\,2^{-v_2(3x+1)}P(x)\), \(P(a_j)/a_j\to1\), and \(Z=\sum_{x\in\Gamma}P(x)^{-1}<\infty\). In fact \(\sum_{\Gamma}x^{-1}<\infty\). For the units this follows from disjoint predecessor basins and their \(c/x\) density floor. For each odd multiple of three under consideration its image is a unit at grade one, and
\[
 \sum_{e:\,x=(2^e y-1)/3\in\mathbb N}x^{-1}
 \le \frac6y\sum_{e\ge1}2^{-e}.
\]
The unit antichain bound at grade one handles these terms. [Pinned posterior theorem, including grade antichains](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-unconventional-20261126/global/POSTERIOR.md) · [Pinned trace profile](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-unconventional-20261126/boundary/TRACE_PROFILE.md)

## Every sufficiently large dyadic level

The true inverse-word real intercept for \(x\in\Gamma_j\) is \(\beta_j=a_j-3^j2^{-S_j(x)}x\), where \(S_j(x)\) is the total of its first \(j\) valuations. Fix the central total \(s=2j\). The bounded-real ordinary row gives, for all large \(j\), at least
\[
 c\frac{\exp(dj)}{\sqrt j M}
 \quad\text{distinct }x\in\Gamma_j,\quad
 x\equiv u\bmod M,\quad S_j(x)=2j,\quad
 (a_j-F)\exp(dj)\le x\le a_j\exp(dj).                         \tag{1}
\]
Here \(F,c,\delta>0\) are absolute, \(M\) is odd and \(\log M\le\delta j\), and \(u\) is arbitrary. For \(M=1\), (1) follows from the external pure ternary bounded-real joint floor. For varying odd \(M\), it uses the mixed-conductor extension. The identity for \(x\) and the injectivity of the word-to-source map at fixed depth are ordinary-integer identities. [Weaver and Wren, paper 48 v2, bounded-real selected-word construction](https://rstation.ai/problems/collatz/papers/48) · [Mixed-conductor floor, equation (5)](../ARITHMETIC_PROGRESSION_FLOOR.md)

Every source counted at this total has exactly
\[
    P(x)=P(m)2^{k_j}=P(a_j)\exp(dj),\qquad k_j=2j-A_j.           \tag{2}
\]
Write \(h=2-\log_2 3>0\). From \(P(a_j)\ge1\) and \(A_j\ge j\) we have
\[
 hj-\log_2P(m)\le k_j\le j,\qquad k_{j+1}-k_j\le1,\quad k_0=0.
\]
Thus every positive integer \(\ell\) is attained. If \(j=j(\ell)\) is its first hitting time, then
\[
             \ell\le j(\ell)\le(\ell+\log_2P(m))/h .
\]
The lower bound follows from \(k_j\le j\), the upper bound directly from the lower bound for \(k_j\) at this same time. Although \(k_j\) need not be monotone, no upward jump can skip an integer.

Consequently each large level \(P(m)2^\ell\) contains at least \(c_m(4/3)^\ell/(M\sqrt{\ell})\) distinct odd sources in each class modulo any odd \(M\le\exp(\delta\ell)\). They satisfy \(x/P(x)\to1\) uniformly among the selected points as \(\ell\to\infty\), because (1) and (2) place the ratio in \([(a_j-F)/P(a_j),\,a_j/P(a_j)]\) and \(a_j\to\infty\). All these sources reach the *same* physical target \(a_{j(\ell)}\) after the prescribed number of odd steps.

Taking \(\ell=\lfloor\log_2(Y/P(m))\rfloor\) shows for all sufficiently large \(Y\) that
\[
 B(Y)\gg_m Y^{\log_2(4/3)}(\log Y)^{-1/2}.                       \tag{3}
\]
The same lower bound divided by \(M\) applies to each arithmetic progression in the indicated range. It concerns the original synchronous grade and gives a lower bound at every large height.

## Growth along the original orbit

Set \(g=\liminf_{j\to\infty}(\log a_j)/j\); the elementary \(a_j+1\le(3/2)^j(m+1)\) gives \(0\le g\le\log(3/2)\). Choose a subsequence realizing this lower limit, and set \(Y_j=a_j\exp(dj)\). Then (1) for \(M=1\) gives
\[
    \limsup_{Y\to\infty}\frac{\log B(Y)}{\log Y}
       \ \ge\ \frac{d}{d+g}.                                      \tag{4}
\]
In particular, subexponential lower growth of the specified escape forces the counting exponent of its synchronous class to be exactly one even though its reciprocal sum converges. If \(\sum_{x\in\Gamma}x^{-s}<\infty\) for some \(0<s<1\), then \(B(Y)\ll_sY^s\) and
\[
            \liminf_{j\to\infty}\frac{\log a_j}{j}
                         \ \ge\ d\,\frac{1-s}{s}>0.                \tag{5}
\]
There is an even more direct one-scale conclusion: (1) gives \(a_j^s\gg_s \exp((1-s)dj)/\sqrt j\) from that same fractional moment, for every large \(j\). At present the antichain input controls \(s=1\). Fractional moment estimates for the sequence of off-ray incoming branches have a different index set. They do not give (5)'s premise for all of \(\Gamma\).

## Absolute row floors and actual posterior mass

Write \(Q_j(x)=1_{\Gamma_j}(x)/(P(x)\sum_{\Gamma_j}P(b)^{-1})\), and \(Q(x)=1_\Gamma(x)/(P(x)Z)\). The pinned posterior gives total variation convergence \(Q_j\to Q\). Every fixed \(x\in\Gamma\) eventually belongs to all \(\Gamma_j\), with
\[
   S_j(x)-A_j=\log_2(P(x)/P(m)),\qquad
   \frac{\beta_j(x)}{a_j}
       =1-\frac{P(a_j)}{a_j}\frac{x}{P(x)}
       \longrightarrow 1-\frac{x}{P(x)}>0.                        \tag{6}
\]
The strict inequality follows from the first positive product factor at \(x\). For every \(\epsilon_j\downarrow0\), the event \(\beta_j(x)\le\epsilon_j a_j\) has \(Q_j\)-probability tending to zero, by exhausting \(Q\) with finite sets of actual sources. Also \(A_j\le j\log_2 3+\log_2P(m)\), so \(Q_j\{|S_j-2j|\le\sqrt j\}\to0\). Indeed each fixed source's excess in (6) is constant while the gap from \(2j\) grows linearly.

For any integer moduli \(q_j\to\infty\), the push-forward of \(Q_j\) to \(\mathbb Z/q_j\mathbb Z\) has total variation distance from uniform tending to one. If a finite set of \(K\) atoms carries \(1-\epsilon\) of \(Q\), its projection carries at least \(1-2\epsilon\) of \(Q_j\) eventually and at most \(K/q_j\) under uniform. This argument also shows why a pointwise *absolute* arithmetic-progression floor and exponential growth of (1)'s ordinary counts are compatible with concentration of nearly all the original posterior mass. The entire bounded-real, central-clock region used by (1) is outside that mass in the limit. A source-level closure would need a bound on the actual macroscopic intercept and physical clock in (6).

# Lower bounds for synchronous first meetings at the median Collatz clock

Use the shortcut \(T(2n)=n,\ T(2n+1)=3n+2\). The sources are two independent uniform positive integers through \(X\). Set \(D=\log(4/3)\) and \(H_X=\lfloor 2\log X/D\rfloor\), with natural logarithms. Two distinct sources first meet at date \(t+1\) if their first equal values occur then. The **1,4 event** means that their values at date \(t\) were 1 and 4, in either order. Every count below concerns actual integer trajectories.

**Proposed lower bound.** For every fixed \(\epsilon>0\) and every sufficiently large \(X\), there are at least \(X^{2-\epsilon}\) unordered pairs of starts at distance greater than \(3X/16\) whose first meeting uses 1 and 4 by \(H_X\). The new step is a deterministic dilation and counting argument. The asymptotic uses Shaik's positive-density stopping estimate at each fixed rate above the critical rate. A separate explicit finite inequality uses Lau's stopping estimate. A positive limiting probability follows under stronger timing inputs, with an explicit but very small constant. The near-quadratic count permits a fraction tending to zero. None of the estimates reaches the \(1/8\) threshold.

## A finite construction using two dilations

Take a set \(S\) of distinct positive odd integers \(m\le X/16\). Let \(y_m\) be the largest \(4^j m\le X\), and put \(z_m=y_m/16\). Retain only cores for which \(y_m\) reaches 1 by \(H\). Both maps from the retained cores are injective because the odd part recovers \(m\). The lower band is \((X/64,X/16]\) and the upper band is \((X/4,X]\). Every cross pair has the advertised separation.

Write \(a_m\) for the first hitting time of 1 from \(z_m\). From \(y_m\) it is \(a_m+4\), by four genuine halvings. Two hits on 1 of the same parity but different dates force a first meeting through 1 and 4. If the later hit is at \(v\), then at date \(v-2\) the earlier arm is at 1 and the later arm is at 4. Indeed 2 is the only predecessor of 1, and the only predecessors of 2 are 1 and 4. Equality earlier would persist to \(v-2\), which is impossible. At \(v-1\) both are at 2.

Let \(b_t=\#\{m:a_m=t\}\), \(s_i=\sum_{t\equiv i\ (2)}b_t\), and \(s=s_0+s_1\). Counting with the lower source first gives distinct unordered pairs. A guaranteed count is
\[
 G=s_0^2+s_1^2-\sum_t b_t b_{t+4}\ \ge\ \tfrac38 s^2.                 \tag{1}
\]
For each parity, split dates by the parity of \(\lfloor t/4\rfloor\). An edge from \(t\) to \(t+4\) crosses this partition. Each unordered pair of dates contributes at most once. The sum of tie products is at most the product of the two part masses, hence at most \(s_i^2/4\). Finally \(s_0^2+s_1^2\ge s^2/2\). This handles arbitrary concentrations and correlations of the seed hitting times.

### An explicit input and a near-quadratic count

Lau v2 gives at least \(\lfloor M/L\rfloor\) odd \(m<M\) reaching 1 within \(a\log m\) accelerated odd steps, where \(a=3.4881\) and \(L=2^{2^{2^{163}}}\). Write \(J\) for the actual number of those steps. Along the path before its first visit to 1 the odd values are distinct and at least 3. Their additive corrections have sum
\[
 E=\sum_{x\ {\rm odd\ on\ the\ path}}\log(1+1/(3x))
 \le [1+\log(1+J)]/6.
\]
In increasing order the \(i\)-th such value is at least \(2i+1\), and the harmonic-sum bound also covers the empty path. Multiplying the true transitions gives \(\tau_1(y_m)\log2=\log y_m+J\log3+E\) in the shortcut clock. Consequently if \(1\le M\le X/16\) is an integer and
\[
 a\log M\log3+[1+\log(1+a\log M)]/6
       \le H_X\log2-\log X ,
\]
(1) supplies at least \(3\lfloor M/L\rfloor^2/8\) unordered, separated first meetings through 1 and 4. For every fixed \(\theta<1/(aD)=0.9965481\ldots\) with \(\theta>0\), \(M=\lfloor X^\theta\rfloor\) meets this condition eventually. The identity \((2\log2/D)-1=\log3/D\) gives this threshold. [Lau, explicit theorem, v2](https://hexagonmath.org/2610.00249v2)

The same odd cores also give disjoint pairs at several scales. If \(16^K M\le X\), the numbers \(y_m/16^j\) are integers for every \(1\le j\le K\), because \(4^{2K}m\le X\). Each \(j\) has its own lower band and every band lies below \(X/16\). Writing \(u_m=\tau_1(y_m)\), the lower hit dates are \(u_m-4j\). For each \(j\), there are \(s_0^2+s_1^2\) same-parity pairs before removing equal hit dates, where \(s_i\) counts upper dates of parity \(i\). Across all \(j\), a pair of upper dates with positive difference causes a tie for at most one \(j\). Thus all the removals together cost at most \((s_0^2+s_1^2)/2\), by counting the ordering with the larger date first. The total is at least \((K/2-1/4)s^2\) for \(K\ge1\). The one-band estimate (1) is sharper when \(K=1\).

This gives an explicit power and logarithmic factor from Lau. Set \(\theta_*=1/(aD)\), \(b=1/(6a\log3)\), and take \(M=\lfloor c_0 X^{\theta_*}/(\log X)^b\rfloor\) for a sufficiently small absolute \(c_0>0\). The term \(-ab\log3\,\log\log X\) in \(a\log M\log3\) cancels the upper bound's \(\tfrac16\log\log X\). The constant \(a\log3\,\log c_0\) absorbs the remaining bounded term and the cutoff floor. Taking \(K=\lfloor\log(X/M)/\log16\rfloor\asymp\log X\) gives, for all sufficiently large \(X\),
\[
  \#\{\text{separated first meetings via 1 and 4 by }H_X\}
       \gg L^{-2}X^{2\theta_*}(\log X)^{1-2b}.
\]
All lower bands used here remain at distance greater than \(3X/16\) from every upper source.

Shaik's theorem supplies a positive proportion of starts through \(M\) reaching 1 within \(c\log M\) **ordinary** steps, with a common positive lower density, for every fixed \(c>3/D\). For clarity, discard starts below \(\delta M\) and multiples of \(2^K\), with \(\delta\) and \(2^{-K}\) small compared to that proportion. Taking odd parts leaves \(\gg_c M\) distinct odd cores \(m\asymp_c M\), with multiplicity at most \(K\). If \(R\le c\log M\) is the ordinary hitting time from such a core, its shortcut time is \(R-J\), so
\[
 J\log6=R\log2-\log m-E
 \ \le\ (c\log2-1)\log M+O_c(1).
\]
The coefficient \((c\log2-1)/\log6\) tends to \(1/D\) as \(c\downarrow3/D\). Fix \(0<\theta<1\) and choose \(c\) close enough that \(\theta(c\log2-1)/\log6<1/D\). With \(M=\lfloor X^\theta\rfloor\), the logarithmic slack absorbs \(E=O_c(\log\log M)\), the floor of \(H_X\), and the fixed constants. The lifted starts therefore reach 1 in time. Formula (1) gives \(\gg_\theta X^{2\theta}\) pairs for all sufficiently large \(X\). Choosing \(2\theta>2-\epsilon\) yields the stated result. This deduction uses the fixed-\(c\) theorem with the limit in \(X\) taken first. It supplies neither a bounded timing excess at \(c=3/D\) nor a uniform onset as \(\theta\) approaches one. [Shaik, positive density at every rate above the critical rate](https://doi.org/10.5281/zenodo.22871622)

## Where an order-\(X^2\) lower bound must come from

Write \(A_t(r)=\#\{n\le X:T^t n=r\}\), \(A_t=A_t(1)\), and \(B_t=A_t(4)\). The only distinct incoming branches of a shortcut value have the form \(r,3r+1\) with \(r\) odd. For the known cycle, \(A_{t+2}=A_t+B_t\) and \(A_{t+1}=A_t(2)\). Squaring and summing gives the finite identity
\[
 2\sum_{t<H} A_tB_t
 = A_H(1)^2+A_H(2)^2-A_0(1)^2-A_0(2)^2-\sum_{t<H}B_t^2.             \tag{2}
\]
The left counts ordered first meetings via 1 and 4. In particular a finite collection of witnessed hitting-time cohorts gives a rigorous lower bound. Equality of the two arms before their purported first meeting would persist, so there is no charge at two dates.

The proposed cut-clock estimate of PR #211 gives an obstruction to counting *other* first meetings. Cut the outgoing edge of the minimum of each cycle and let the integer clock \(s\) gain one on every retained edge. If a first meeting is off every cycle, neither arm could have crossed a cut, and the starting clocks agree. This holds at every date, including on escaping components. With \(N_X(C,k)\) the component and cut-clock counts, the number of these ordered pairs over **all dates together** is at most
\[
 \sum_{C,k} N_X(C,k)^2
 \le X\sum_C \max_k N_X(C,k)
 \ll X^2/\sqrt{\log(2X)} .
\]
The same input gives \(\max_t B_t\ll X/\sqrt{\log(2X)}\), since reaching 4 at date \(t\) means first reaching 1 at \(t+2\). The cohorts visiting 4 are disjoint. Thus \(\sum_{t<H}B_t^2\ll X^2/\sqrt{\log(2X)}\), uniformly in \(H\). A first meeting on a hypothetical extra cycle is a separate contribution. [PR #211 at 4b44cded, clock bound (1)](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase3/CLOCK_DISPERSION.md)

One sufficient estimate can be stated for **one start**. Set \(F_X=(A_{H_X}(1)+A_{H_X}(2))/X\), the fraction already on the known cycle at the deadline. Unconditionally, two independent starts agree at that date with probability at least
\[
 \frac{A_{H_X}(1)^2+A_{H_X}(2)^2}{X^2}\;\ge\; F_X^2/2.
\]
Thus \(F_X\ge1/2-o(1)\) would give the required \(1/8-o(1)\) collision lower bound. With PR #211's bound on the tie cohorts, (2) places the same lower bound on first meetings via 1 and 4 up to \(O(1/\sqrt{\log X})\). Under PR #214's entry law \(F_X\to d/2\), so this single-source route needs full density of the basin of 1.

There is a stronger source-qualified asymptotic. Let \(d\) be the natural density of starts reaching 1. The phase-restricted entry law of PR #214 gives asymptotic mass \(d/4\) at each of 1 and 2 at \(H_X\). It holds with each source further restricted to \(n\le uX\), giving mass \(ud/4\) relative to \(X\), for fixed \(0<u\le1\). To see this, the two median cutoffs differ by a bounded number of dates. At the earlier cutoff the two phases have equal limiting mass, and entries in the intervening bounded window have vanishing mass by the continuous entry-clock law. Hence the endpoint-1 and endpoint-2 measures on \(n/X\) both converge weakly to \((d/4)\,du\). Independence gives product measures. The boundary of \(\{|u-v|\ge\lambda\}\) has area zero. The off-cycle first-meeting bound and the \(O(X)\) diagonal remove all endpoint-equal pairs in the known cycle except those that first meet via 1 and 4. For \(0\le\lambda<1\) this yields
\[
 \lim_{X\to\infty}\Pr(\text{first meeting via 1 and 4 by }H_X,\
                     |n-m|\ge\lambda X)
              =(1-\lambda)^2\,d^2/8.                                  \tag{3}
\]
Lau's odd lower bound implies \(d\ge2/L\). For each fixed \(j\) double his odd inputs by \(2^j\) up to \(X\), add over finitely many disjoint odd-part valuations, and then let the finite cutoff increase. Thus (3) gives **at least \(1/(8L^2)\)** for distance at least \(X/2\), and \(1/(2L^2)\) without a separation restriction. The timing and phase laws in (3) remain imported written inputs. The new lift bound (1) does not use them. [PR #214 at 504d29d3, synchronous phase and entry law](https://github.com/GettysburgResearch/collatz/blob/504d29d399efa941a62006d1ea4635385ce6bb5f/research/astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md)

## An elementary bound before the median

An independent finite certificate uses no positive-density or timing theorem. Let \(B=2^t\), \(t=\lfloor\log_2(X/6)\rfloor\ge1\). In the full block \([B,2B)\), the odd starts with \(s\) odd departures in their first \(t\) steps number \(M_s=\binom{t-1}{s-1}\). Indeed a prefix of \(j\) parities fixes one residue modulo \(2^j\). The two lifts differing by \(2^j\) have endpoints differing by the odd integer \(3^s\), giving opposite next parities. Starting with the odd parity proves the count.

For these starts \(T^t n\) is at least \(3^s\) and strictly below \(2\cdot3^s+(3/2)^s\). The linear part is \(3^s n/B\). Each of the \(s\) additive odd-step contributions is largest when its departure is as late as possible, giving total at most \((3/2)^s-1\). After the first odd step, the endpoint is a unit modulo 3. Let \(W_s\) count the positive integers prime to 3 in the stated half-open range. Write \(M_s=q_sW_s+r_s\) with \(0\le r_s<W_s\). Balancing integer occupancies gives at least \(W_sq_s^2+(2q_s+1)r_s\) ordered pairs of base starts with equal endpoints. Map a base pair \((n,m)\) to the low/high pair \((n,3m+1)\). The upper input agrees with \(m\) after one step, so the new pair meets by \(t\). It has gap at least \(B>X/12\), endpoints at most \(X\), and its ordering is uniquely recoverable. Summing the integer bound over \(s\) counts distinct unordered pairs.

This is \(\gg X^{2\log_2(1+1/\sqrt3)}/\sqrt{\log X}\), with exponent \(1.315006\ldots\). Indeed \(W_s\le2\cdot3^s\), and the sum dominates \(\frac16\sum_j\binom{t-1}{j}^2 3^{-j}\). Normalize \(\binom{t-1}{j}3^{-j/2}\) by \((1+1/\sqrt3)^{t-1}\). The resulting binomial law puts a fixed positive mass on \(O(\sqrt t)\) integers around its mean by Chebyshev's inequality. Cauchy–Schwarz gives the stated lower bound. These early pairs may meet away from 1 and 4.

## Verification and open estimate

[Exact checks](check_bounds.py) use integer arithmetic and explicitly bounded orbits. At \(X=2^{71}\), the binomial certificate gives **11,891,154,435,379,815,164,267,506** unordered separated pairs by date 68. At \(X=2^{24}\), the two-dilation certificate retains 368,777 odd cores and proves **66,378,698,319** unordered first meetings via 1 and 4 by date 115. At \(X=2^{20}\) the program counts exactly **13,571,079,303** such first meetings from the bottom to the top quarter by date 96, among \(68,719,476,736\) possible cross pairs. These are finite statements at different cutoffs and sampling conventions.

[MedianMerger.lean](MedianMerger.lean) imports the pinned PR #214 `AffineOrbit.lean`. It formalizes the per-pair first-meeting sum, the finite population identity (2), the odd separated lift, the four-step delay, the first meeting forced by distinct same-parity first-hit dates, the bipartite bound on four-step ties, and the final three-eighths inequality. The stopping-time inputs, their combination with the finite lemmas, the multiple-band deduction, and the limits are written proofs. Run `python -B check_bounds.py` from this directory for the integer certificates. Run `python -B check_lean.py --lean <lean-executable> --mathlib <built-mathlib-directory>` to rebuild both local Lean modules and audit the eleven named results. The replay used Lean 4.34.1 and the mathlib cache from PR #214.

The remaining lower bound is \(1/8-o(1)\) for the unrestricted ordered-pair probability. The fast-seed construction at \(M=X^\theta\) loses a factor \(X^{-2(1-\theta)}\) in its normalized count. The published estimates used here give no uniform timing slack at \(\theta=1\). Formula (3) still contains the unknown \(d\), and the numerical floors above do not prove \(d=1\).

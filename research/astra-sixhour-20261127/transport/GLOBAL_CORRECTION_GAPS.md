# A common null set for all simple ordinary segments

**Status.** Written deduction conditional on the new fixed-root closed-null theorem and its named synchronization, passage and inverse-chain inputs. The bound allows the source, target, depth and component all to vary. It gives an exact moving-strip upper bound on a set of relative positions of full Lebesgue measure.

For a finite odd Syracuse path \(x,Sx,\ldots,S^k x\), define its correction
\[
          f(x,k)=\prod_{i<k}\frac{3S^i x}{3S^i x+1}.
\]
Call the segment simple if all \(k+1\) displayed odd states are distinct. Let \(E\) be the closure in \([0,1]\) of its corrections over all positive simple segments, including \(k=0\). Then
\[
                              |E|=0.                                  \tag{1}
\]
In particular every interval inside \((0,1)\) has an open subinterval missed by *every* finite positive simple path, independently of both endpoint heights.

Fix \(0<\delta<1\). By uniform orbit-set sparsity, the sum of \(\log(1+1/(3u))\) over odd vertices \(u>B\) in any simple segment tends uniformly to zero as \(B\to\infty\). For example the uniform count \(O(X^{1-\epsilon})\) for vertices up to \(X\), followed by a dyadic sum, suffices. This applies also when the full forward orbit is ultimately cyclic: the finite simple segment has bounded multiplicity in the ordinary shortcut orbit counting proof. One can truncate just before the final odd arrival when counting shortcut states: no intermediate even vertex can repeat unless its next odd state repeats, except for a prospective meeting with the final arrival, which is odd. [Weaver, Paper 176, §4](https://rstation.ai/problems/collatz/papers/176)

Choose \(B\) making this logarithmic sum strictly less than \(-\log(1-\delta/2)\). Every simple segment with \(f(x,k)\le1-\delta/2\) visits an odd \(m\le B\). Split the segment at that vertex. Its first correction belongs to
\[
                      D_m=1-K_m/m ,
\]
where \(K_m\) is the closure of all real offsets of finite first-hit inverse words into \(m\), including the empty word. The first-hit condition holds because the given segment is simple. \(D_m\) is compact null by [PR193, fixed-root closed support](https://github.com/GettysburgResearch/collatz/blob/2796977d3f02ad57daeb7510f16da29527f9afde/research/astra-six-hour-20261127/escape/CLOSED_CORRECTION_SUPPORT.md). At a multiple of three the first hit can only have depth zero, so \(D_m=\{1\}\).

The second correction is a member of \(T_m=\{f(m,\ell):\ell\ge0\}\cup\{\lim_{\ell\to\infty} f(m,\ell)\}\). Monotonicity gives the limit; this set is countable and compact, including for a cyclic \(m\). The product \(D_mT_m\) is compact as a continuous image and null as a countable union of scalar multiples of \(D_m\). Thus
\[
               E\cap[0,1-\delta]\ \subset\
                       \bigcup_{m\le B,\ m\ {\rm odd}} D_mT_m .
\]
For a limit point near the endpoint \(1-\delta\), use the wider preliminary band \(f\le1-\delta/2\) just chosen. The right side is a finite union of compact null sets. Taking \(\delta\downarrow0\) through a sequence and adding \(\{1\}\) proves (1).

At a nonperiodic odd terminal \(y\), every finite canonical inverse prefix is simple. Its relative offset equals \(1-f\), hence the whole infinite canonical fibre has
\[
                        \operatorname{supp}\lambda_y/y
                 \ \subseteq\ 1-E,                                    \tag{2}
\]
where the notation on the left means the support after real dilation by \(1/y\). Consequently for every compact \(I\subset (0,1)\setminus(1-E)\) and every fixed \(L>0\) there is \(Y(I,L)\) such that
\[
        \lambda_y([t y-L,t y+L])=0\qquad(t\in I,\ y>Y(I,L)) .          \tag{3}
\]
Indeed the relative perturbation is \(L/y\) and the distance of \(I\) from the compact \(1-E\) is positive. This uses the actual integer-conditioned canonical fibres. No averaged target law occurs in (3). On a putative escape the limiting centres in [the strip lower bound](UNIT_STRIPS.md) are necessarily in \(1-E\). In fact they equal \(1-(m-r)/P(m)\), and the relevant bilateral corrected marks belong to \(E\). The singular concentration mechanism singles out precisely this exceptional family of slopes.

## Allowing arbitrarily many laps distinguishes infinitely many cycles

Let \(E_{\rm all}\) be the closed correction set obtained by allowing all finite positive odd segments, including repetitions. If there are finitely many positive cycles, \(E_{\rm all}\) is compact null. Indeed, for each such cycle let \(q\in(0,1)\) be its full-lap correction. A path with repeats can have a whole number of complete laps removed, leaving a simple path (possibly empty). Its correction lies in \(q^\ell E\). The closure of these possibilities belongs to \(\{0\}\cup\bigcup_{\ell\ge0}q^\ell E\), a compact null set. A finite union over cycles together with \(E\) suffices.

If there are infinitely many positive cycles, \(E_{\rm all}=[0,1]\). Distinct cycles are disjoint, so their minimum odd vertices tend to infinity along a sequence. The sum of logarithmic corrections around one lap is then \(o(1)\) by the uniform reciprocal tail used above, applied to the distinct odd departures (equivalently omit the repeated final vertex). Their positive lap multipliers \(q_i<1\) tend to one. For any \(t\in(0,1)\), take nonnegative integers \(\ell_i\) nearest to \(\log t/\log q_i\). The actual repeated laps give \(q_i^{\ell_i}\to t\); also \(1\) is an empty correction and \(0\) is approached by repeating the known cycle. This dichotomy does not determine how many cycles exist and places no unconditional new bound on their number.

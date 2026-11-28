# A common-depth cubic residue for first arrivals of ordinary sources

Let \(m_{n,s}(y)\) be the mass of the actual odd starts first hitting the specified odd target \(y\) at the simultaneous odd/native clock \((n,s)\), each counted with weight \(3^n2^{-s}/y\). Every source at this depth has a unique endpoint and total. Define the unconditioned physical statistic
\[
 S_3(n)=\sum_{y\ge1\ {\rm odd}}\sum_{s\ge0}m_{n,s}(y)^3.
\]
With the signed-source and passage estimates specified below,
\[
 \boxed{\displaystyle
 \lim_{n\to\infty}\frac{S_3(n)}{\log n}
     = \frac1{4\pi\sqrt3}\sum_{C\ {\rm escaping}}H_C^3 .}             \tag{1}
\]
Here \(H_C>0\) is the negative-grade mass in the actual escaping component. The sum is finite by [PR 195, LOCAL_HEIGHT_LAW (4)–(5)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/LOCAL_HEIGHT_LAW.md). With **all positive starts** and their initial halving clocks, multiply the right side by 8. All logarithms without a base are natural.

The count can be cut off at \(x\le 2^{32n+O(1)}\) with \(O(2^{-n})\) error in the cube sum. In particular it is obtainable by finite ordinary iteration and arithmetic to this accuracy, with no escape test. Thus absence of an escaping orbit is equivalent, on the cited written inputs, to the strictly sublogarithmic bound \(S_3(n)=o(\log n)\). The known 1-basin alone contributes \(o(\log n)\), even though it already has a positive cubic residue when *all* clocks are summed at a *single* fixed root. Nontrivial periodic components, if any, are also removed by the common-depth first-visit filter.

The new ingredients are the target-uniform first-arrival bound, its co-moving local limit, the geometry of one original source per common-depth cell, and the transfer of an actual time cutoff through the relative-landing ladder. None of the external analytic statements is formalized here.

## Octave bounds at one exact time

Put \(p=y2^s/3^n\) and sort the rows by \(2^k\le p<2^{k+1}\), \(k\ge0\). The [uniform first-arrival estimate](SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md) gives \(m_{n,s}(y)\le C(1+k)^{-1/2}\); every contributing source has \(c_0p\le x\le p\). At fixed \(n\) no input is counted twice, so the total row mass in one octave is bounded by a constant. The sum of cubes in that octave is \(O((1+k)^{-1})\).

There is an exponential bound when \(k\ge32n\), \(n\ge1\). The positive endpoint gives \(s< k+1+n\log_23\). At most \(\binom{s}{n}\) paths have these clocks, also with initial halvings allowed: choose the \(n\) odd positions among \(s\) native departures, and zero choices if \(s<n\). The word and endpoint determine at most one integer. Thus \(m_{n,s}(y)\le 2^{-k}(e(k+1+2n)/n)^n\le2^{-k/2}\) at \(k\ge32n\). The last inequality follows from \(\log_2(e(u+3))\le u/2\) for \(u\ge32\). The cubic octave sum is \(O(2^{-k})\). All omitted inputs above \(2^{32n+1}\) belong to such rows, so removing them changes the sum by \(O(2^{-32n})\). This also proves finiteness of \(S_3(n)\) at each positive depth.

## Bounded-height landing on a physical odd clock

Write \(W_Y\) for a uniform odd start in \([Y,2Y)\), \(J_r\) for its first odd time at or below \(r\), with \(+\infty\) on failure. There is an absolute \(D\) such that, for \(Y\ge r^\alpha,\ \alpha=1001/1000\), any sufficiently large \(r\) and any \(B>0\),
\[
         \Pr(J_r(W_Y)>D\log Y)\ll_B(\log r)^{-B}.                     \tag{2}
\]
The local estimate in [the relative sparse-passage note](RELATIVE_SPARSE_PASSAGE.md), developed for the ordinary octave and valid whenever \(u\le Y\le u^{\alpha^2}\), gives \(\Pr(J_u(W_Y)>0.1\log u)\ll u^{-\epsilon}\), with integer clocks rounded down. We use the *duration* of every segment. For \(r_i=r^{\alpha^i}\) and \(r_N\le Y<r_{N+1}\), the top segment to \(r_{N-1}\) obeys this local bound. For \(i=N-2,\ldots,0\), test a landing \(z\le r_{i+1}\) by the event \(J_{r_i}(z)>\lfloor0.1\log r_i\rfloor\), which includes failure and vanishes if \(z\le r_i\). At the fresh ordinary source \(W_{r_{i+2}}\), the tested success at \(r_{i+1}\) with overlong next segment forces \(J_{r_i}(W_{r_{i+2}})>\lfloor0.1\log r_i\rfloor\). Thus its expectation in the successful passage law at \(r_{i+1}\) is \(O(r_i^{-\epsilon})\). Apply the uniform relative first-landing comparison [Weaver 12, §6, (15)](https://rstation.ai/problems/collatz/papers/12) to the same nonnegative test at \(Y\) and \(r_{i+2}\), both at least \(r_{i+1}^\alpha\). Solving the fresh lower estimate for its positive functional and using the upper estimate at \(Y\) gives \(O_B((\log r_i)^{-B})\) there. Once upper failures are charged on their own segment, a union bound costs \(O_B((\log r)^{-B})\). On all remaining original trajectories the total duration is at most
\(0.1\sum_{i=0}^{N-1}\log r_i\le0.1\log Y/(\alpha-1)\).
This proves (2), for example with \(D=101\); no fresh-start assumption was used for the intervening sites.

For arbitrary positive starts first strip their initial powers of 2. For a source octave with \(X\ge r^{2\alpha}\), slice by \(x=2^a u\), \(u\) odd. Slices with \(2^a\le\sqrt X\) use (2) at \(Y=X/2^a\ge r^\alpha\), all with duration bound \(D\log X\). The other slices have total uniform probability \(O(X^{-1/2})\). The counted clock here is the number of odd departures, independent of these initial halvings. Their native times are retained in the row label.

## Upper coefficient, including delayed terminating paths

Fix large \(r\) and an integer \(k_r\) such that each octave in \([c_0 2^k,2^{k+1}]\), for \(k\ge k_r\), can be covered by a bounded number of source octaves with bottom height at least \(r^{2\alpha}\). Fix \(\delta>0\) small enough that \(D\log(2^{k+1})\le n/2\) when \(k_r\le k\le\delta n\) and \(n\) is large. Sources in such a \(p\)-octave that do not reach an odd state at most \(r\) by physical odd depth \(n/2\) have total row mass \(O_B((\log r)^{-B})\). Indeed (2) gives this fraction in each of the covering source octaves, while every atom has weight at most \(1/x\); the possible large initial-halving error is absorbed at these starting heights. This bound is for the *same* inputs as the rows. Removing them changes the cubic sum in that octave by at most \(3\max m^2\) times their total mass, thus by \(O_B((\log r)^{-B}/(1+k))\).

There are only finitely many odd states at most \(r\). Those with eventually periodic forward orbits have only finitely many distinct states on their entire future, and have visited all of them after a finite number of odd steps from their first arrival at that small state. The maximum of these finite delays over this finite subset is finite without assuming that all small states are eventually periodic. No retained source passing such a site by \(n/2\) can have a first visit at depth \(n\), for all sufficiently large \(n\) depending on \(r\).

The other small states feed finitely many escaping components \(C\). In each choose an escaping base \(a_C\) on one such ray and write \(y_N=U^Na_C\). Every remaining small state in that component merges into this ray after a bounded number of steps with bounded grade offset, uniformly for this finite list. Thus for all large \(n\) the endpoint of every retained source in that component is a \(y_N\) with
\(n/2-O_r(1)\le N\le n+O_r(1)\).
Its row at physical grade \(n\) and native time \(s\) is included in the full corrected cell at \(v=N-n,\ l=s-A_N\), and its first-hit weight equals \(1/(f_Np^*)\) with \(f_N=y_N/P(y_N)\to1\) and \(p^*=P(a_C)3^v2^l\). Distinct such observed rows in a component map to distinct \((v,l)\). Consequently their combined cubes are at most
\[
 (1+o_r(1))\sum_C\sum_{v=-n}^{O_r(1)}\sum_l M_{C,v}(l)^3 .
\]
Use the cropped cubic residue (3) of [the clock spectrum](FIRST_ARRIVAL_ROW_SPECTRUM.md) after reflection \(j=-v\). With all positive starts the corrected table has net \(2H_C\), as proved there. The octaves \(k<k_r\) cost \(O_r(1)\). The middle interval \(\delta n<k<32n\) costs \(O_\delta(1)\) by the \(1/(1+k)\) bound, and the far interval costs exponentially little by the word count. Divide the full sum by \(\log n\), take the upper limit and then \(r\to\infty\). The accumulated error \(O_B((\log r)^{-B})\) vanishes, and the finite component sum is at most the right side of (1). The identical reasoning restricted to sources in any eventually periodic basin, or their union, gives zero upper coefficient there; finite rows cannot mix different components.

## Lower coefficient from the same moving targets

Take any finite list of distinct escaping components, one actual odd ray in each. For \(k\) between a fixed large lower cutoff and \(n/2\), use the target \(y_{N}\) with \(N=n-k\) and clock \(s=A_{N}+l\), \(|l-2k|\le B\sqrt k\). At fixed \(n\) these are distinct endpoints or native times, since each ray is simple. Their corrected heights are \(p^*=P(a_C)3^{-k}2^l\), with \(\log p^*=k\log(4/3)+O_B(\sqrt k)+O_C(1)\). By [the moving first-arrival local law](MOVING_FIRST_ARRIVAL_LOCAL_LAW.md), their actual masses equal \(H_C g_k(l)+o_{B,C}(k^{-1/2})\) uniformly as \(k,N\to\infty\). In the all-positive population the coefficient is \(2H_C\). For fixed \(B\), the sum of their cubes over the indicated \(l\)'s is consequently
\[
 \frac1k\left(H_C^3\int_{-B}^{B}\phi(z)^3\,dz+o_{B,C}(1)\right),
 \qquad \phi(z)=(4\pi)^{-1/2}e^{-z^2/4}.
\]
The error summed in \(k\), after division by \(\log n\), vanishes by the uniform two-parameter estimate. The harmonic sum through \(n/2\) has leading coefficient one. Let \(B\to\infty\) and increase the finite component list. Since \(\int\phi^3=1/(4\pi\sqrt3)\), this gives the lower bound in (1).

The unresolved inference is an arithmetic upper bound \(S_3(n)=o(\log n)\) for the full original first-hit statistic, independently of a classification of the bounded ordinary landing states. Equation (2) permits those finitely many states to have escaping orbits. A positive answer to that arithmetic bound would exclude escape; periodic components would still require their own cycle exclusion.

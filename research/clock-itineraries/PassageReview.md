# Sharp first visits and the fates of binary prefixes

**The positive Collatz conjecture remains open.** This investigation uses the shortcut map \(T(2n)=n\), \(T(2n+1)=3n+2\). A strict first low at target \(b\) and clock \(h\) means \(T^h(x)=b\) and \(T^i(x)>b\) for every \(i<h\). All sources and targets in the routing theorems are ordinary integers.

## Which finite affine families can reach a prescribed target?

Fix the anchoring start \(x\) and any finite list of starts \(m_i x+c_i\), with nonnegative integer coefficients. There is a threshold after which **every** supplied clock works for **every** positive target coprime to three, simultaneously as a strict first low on every arm, **if and only if every \(m_i\) is a power of three**. All intercepts are allowed. For admissible slopes one may also prescribe \(x=r+2^\ell3^g t\), with \(t>0\), before supplying the clock or target. At a target divisible by three, distinct starts cannot meet on the same clock. Its only predecessor is its double. [Lean classification](mathlib/PassageClassification.lean)

The construction tracks expressions \(A+3^p t\) on a common binary progression. For two expressions with slope ratio \(3^k\), write the larger-slope expression as \(3^k\) times the smaller plus a signed offset \(c\). Shared even steps halve a nonzero even \(c\). Once \(c\) is odd, select the bit making the smaller-slope arm odd and the other even. This removes one power of three from the ratio. An odd step on both arms releases the case \(c=0,\ k>0\). At equal slope an odd positive separation \(d\) can be replaced by a nonnegative separation at most \((3d-1)/4\), and an even separation halves. Induction merges the entire list. [Lean proof of finite fusion](mathlib/PassageFusion.lean)

Suppose the common endpoint is \(a+3^q t\). To reach \(b\) after another \(h\) steps, choose \(1\le i\le2\cdot3^q\) with \(2^i\equiv2^h b-3a\pmod{3^{q+1}}\). The right side is a unit, and two generates the unit group. This gives \(2^h b=2^i+3(a+3^q t)\). The suffix has exactly one odd departure. For sufficiently large \(h\), all states before the target exceed \(b\), including the states before the common endpoint. If the merging prefix has length \(H\) and translation \(r\), the resulting parameter satisfies

\[
3^{q+1}x+2^H(2^i+3a)=2^{H+h}b+3^{q+1}r.
\]

Thus the absolute error in locating \(x\) near \(2^{H+h}b/3^{q+1}\) is bounded independently of \(h,b\). Necessity follows by comparing affine slopes on one sufficiently high binary progression. [Exact routing equation](mathlib/PassageRouting.lean)

Earlier work established fixed-pattern first hitting at one, quantitative counted fusion, and affine mergers on prescribed cylinders. PR #212 appeared during this investigation. Its updated Lean proofs cover finite translates with equal odd counts in mixed binary and ternary source classes, including placement in relative height windows. It gives additional coprime steering and near-minimum-time counts in writing. The classification above treats arbitrary finite lists of inhomogeneous arms, requires a strict low at every arm, and checks the finite-family construction and converse in Lean. [Duran](https://doi.org/10.5281/zenodo.23003524) · [Valbuena](https://doi.org/10.5281/zenodo.23025885) · [Weaver](https://rstation.ai/problems/collatz/papers/124/v1) · [PR #146 affine classification](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md) · [PR #212 finite blocks](https://github.com/GettysburgResearch/collatz/blob/e082b95a503d622bbbd121801f6bcadcab50df05/research/astra-infinite-descent-20261127/merger/FINITE_BLOCKS.md)

## Exact first clocks for consecutive intervals

The table gives the **least** clock that works for every positive target coprime to three. Every later clock also works. To add \(d\) steps, first target \(2^d b\), then follow its halvings to \(b\).

| Consecutive starts | Least clock | Target missed one step earlier | Ternary classes in the upper certificate |
|---:|---:|---:|---:|
| 2 | 7 | 8 | 4 |
| 3 | 15 | 1 | 30 |
| 4 | 23 | 3365 | 182 |
| 5 | 24 | 14507 | 178 |

For example, 12 and 13 first reach one at step seven. At step six the complete set of starts first reaching eight from strictly above is \(\{168,170,512\}\). The upper certificates cover all ordinary lifts of each ternary class and check the inequality at every earlier step. The lower certificates enumerate the whole constrained inverse tree of the displayed target. [Soundness theorems](mathlib/PassageIntervals.lean) · [Four optimality proofs](mathlib/PassageIntervalData.lean) · [Independent certificate regeneration](passage_interval_replay.py)

## What a counterexample would force on a fixed binary path

Let \(f(n)\) indicate that \(n\) reaches one. Under failure, recent external results give \(f\) an ordinary natural density \(0<d<1\). Existence is a separate input from positivity of both fates. The Lean implications explicitly take this density premise. [Sultanow, Corollary 4](https://www.preprints.org/manuscript/202610.2552) · [Mazur, positive lower density of predecessors](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

Since \(f(2n)=f(n)\), each time a dyadic cell splits, only its right child can change the label. The average over sufficiently fine descendants of any fixed cell tends to \(d\), by subtraction of two prefix counts. Comparing the parent labels with the descendant averages charges a definite amount, greater than \(\min(d,1-d)/2\), to a finite set of later octaves beyond **each** initial octave. Consequently

\[
\sum_{\substack{n\ge1\\ f(2n)\ne f(2n+1)}}\frac1n=\infty
\]

whenever the conjecture fails. A bound summable with this weight would settle the conjecture. PR #146 previously derived a reciprocal-sum obstruction for odd tripling disagreements by a rotation argument. The finite inequality here charges only the specified even-start adjacent edges and gives an explicit amount beyond each scale. [Multiscale and harmonic theorems](mathlib/PassageBoundary.lean) · [PR #146 density argument](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_DENSITY.md)

PR #213 gives a source-qualified way to bound how long this mass can be postponed. Its first permanent-entry law has counting error \(O((\log X)^{-\sigma})\) for some \(\sigma>0\). The cemetery event is convergence to one. Indeed, a nonconvergent odd orbit stays at least three, so its cumulative division exponent satisfies \(A_j\le\log_2 x+j\log_2(10/3)\). The sequence \(A_j-7j/4\) attains a maximum, after which the permanent gate holds relative to that maximum. A convergent orbit eventually has division exponent two at every odd step. Thus, under the cited inputs, the counting function of the basin is \(dX+O(X/(\log X)^\sigma)\). For \(2^k\le n\le2^{k+1}\), divide the error at \(2^j n\) by \(2^j\). It is \(O(2^k/(k+j)^\sigma)\), uniformly. Taking \(j=\lceil C2^{k/\sigma}\rceil\) in the finite bound forces at least \(\min(d,1-d)/2\) mass between octaves \(k\) and \(k+j\), for sufficiently large \(C\) and \(k\). This still allows the upper bounds known for finite-time coalescence failures. [Lean finite error transfer](mathlib/PassageFrontier.lean) · [PR #213 first-entry law and dependencies](https://github.com/GettysburgResearch/collatz/blob/de6384b4a232b996add4f5c620929d06a1982e90/research/astra-diagonal-frontier-20261127/mass/FIRST_PERMANENT_ENTRY_LAW.md)

Append independent fair bits to any fixed positive integer written in binary. Under failure, the probability that **every** successive prefix through depth \(j\) converges tends to zero. The same holds for persistent nonconvergence. Taking a countable union over possible last changes gives infinitely many changes of fate on almost every infinite continuation. The kernel checks both finite-depth limits. Conversely, a positive limiting fraction of entirely convergent continuations from even one prefix suffices for universal convergence. [Binary survival theorems](mathlib/PassageBinaryRays.lean)

One natural attempt to certify such continuations admits a sharp obstruction. Take \(2^j\le x<2^{j+1}\). Ask whether, for some unrestricted clock \(h\), the path from \(x\) at \(j+h\) agrees in both endpoint and number of odd departures with the path from one at \(h\). **Testing \(h=0,2,4\) decides the entire question.** Such an \(x\) first reaches one at \(H=j+2q\) with at most two odd departures \(q\). Lean bounds the number of such starts by \(1+(j+2)+\binom{j+4}{2}\). The proof first reduces the only possible three-odd case to a visit to five at time \(j+2\). Both earlier odd inputs would be at least seven. The trajectory inequality would then require \(4\cdot7^2\cdot5<2\cdot22^2\), or \(980<968\). [Three clocks and quadratic cover](mathlib/PassageTwoOdds.lean) · [Initial phase reduction](mathlib/PassageAligned.lean) · [Earlier basin phase identity](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/BASIN_PHASE.md)

There is also an exact written count. Put \(A(t)=\#\{(r,s)\in\mathbb N_0^2:6r+2s\le t\}\), with \(A(t)=0\) for negative \(t\). The number of aligned starts in the octave is
\[
N_j=1+\lfloor j/2\rfloor+A(j-1)+A(j-6)=j^2/12+O(j).
\]
The zero-odd start is \(2^j\). With one odd departure, the last odd input is \(y=(2^e-1)/3\), where \(e\ge4\) is even and \(e\le j+2\). The source is \(2^{j+2-e}y\). With two, the earlier odd input is \(w=(2^f y-1)/3\), and the source is \(2^{j+4-e-f}w\), with \(f\ge1\) and \(e+f\le j+4\). Integrality requires either \(e=6r+4,\ f=2s+1\) or \(e=6r+8,\ f=2s+2\). In each case \(y,w>1\), so the backward construction gives the claimed first hit. The one-odd sources have ratio to \(2^j\) equal to \(\frac43(1-2^{-e})\), and the two-odd ratio is \(\frac{16}{9}(1-2^{-e}-3\cdot2^{-e-f})\). Both lie in \([1,2)\). Reading the odd positions on the forward trajectory recovers the gaps uniquely. Finally \(A(t)=t^2/24+O(t)\) by summing \(\lfloor(t-6r)/2\rfloor+1\). Consequently this particular certificate covers a vanishing fraction of the \(2^j\) binary continuations at depth \(j\).

There is an explicit family of sharp single-clock results. A reference \(a=2^k\) first makes \(k\) halvings, so alignment in its cell is equivalent to root alignment at depth \(j+k\). Extend any equality past those initial halvings in either direction of this equivalence. The relevant root ratios are restricted to \([1,1+2^{-k})\). With one odd departure the smallest possible ratio is \(5/4\). With two it is \(3/2\), attained at \(e=4,f=1\). Therefore for \(k\ge2\) the **only** aligned continuation is \(x=2^{j+k}\), detected already at reference clock zero. For \(a=2\) the count is \(1+\lfloor(j+1)/2\rfloor\) and the sharp single detecting clock is two. Every one-odd first arrival at \(j+3\) passes through two at \(j+2\) with its one odd step already spent. The example \(x=5,j=1\) needs reference clock two. At \(a=1\), clock four ends at one and its only incoming shortcut step is the even step from two. Hence clock three detects every alignment as well. The example \(x=3,j=1\) fails at reference clock two and succeeds at three. Earlier marked agreements persist, so these witnesses prove sharpness. [Lean proof of the sharp single clock at one](mathlib/PassageRootClock.lean)

### Changing the reference prefix

Fix a positive reference \(a\) whose trajectory first reaches one at time \(L\) with \(Q\) odd departures. For an aligned \(x\) with \(a2^j\le x<(a+1)2^j\), let \(H,q\) be its first arrival time and odd count. Extending both paths around the \(1,2\) cycle gives \(H+2Q=j+L+2q\). The native bound \(2^L12^q<(a+1)4^Q10^q\) now bounds \(q\) independently of \(j\). At each allowed \(q\), the clock is fixed and at most \(\binom Hq\) inverse words are available. Thus the number of aligned descendants is polynomial in \(j\) for each fixed convergent reference. [Lean fixed-reference theorem](mathlib/PassageFixedPrefix.lean)

The occupation bound gives a uniform comparison across references. Write \(R(u)=\prod(1+1/(3v))\) over the odd inputs \(v\) before the first visit to one. A first-arrival path has distinct states. The finite dyadic bound \(300\cdot206^k\) for the count through \(256^k\) makes \(\sum_v1/v\) uniformly bounded by a geometric series. Thus \(1\le R(u)\le C\) with an absolute \(C\). The trajectory identities \(2^H=x3^qR(x)\) and \(2^L=a3^QR(a)\) give
\[
(4/3)^{q-Q}=\frac{x}{a2^j}\frac{R(x)}{R(a)}\ \in [1/C,2C].
\]
In particular \(|q-Q|=O(1)\) uniformly over all convergent references and all depths. This written consequence uses the elementary finite occupation theorem. [Native uniform dyadic bound](mathlib/PassageGateSublinear.lean)

### All references, including a hypothetical escaping one

Fix any positive integer \(a\). An extension \(a2^j\le x<(a+1)2^j\) is aligned if its endpoint and odd count at \(j+h\) agree with those of \(a\) at \(h\), for some \(h\). **There is a single finite clock \(h_a\) detecting every aligned extension at every depth \(j\).** Thus at most \(\binom{j+h_a}{g_a}\) of the \(2^j\) extensions are aligned, where \(g_a\) is the odd count from \(a\) through \(h_a\). This is an unconditional written theorem. Its analytic estimate follows by geometric summation of the native finite occupation bound. PR #212's compact correction set suggested considering the union over clocks. The argument here uses the particular ordinary reference and does not assume a fate for it. [Uniform finite distortion and high-vertex bound](mathlib/PassageGateDistortion.lean) · [PR #212 correction sets and their inputs](https://github.com/GettysburgResearch/collatz/blob/e082b95a503d622bbbd121801f6bcadcab50df05/research/astra-infinite-descent-20261127/escape/FAIR_CLOCK_DIFFUSION.md)

Write \(\beta=\prod_v3v/(3v+1)\) over odd departures of a segment. A path of length \(m\) and odd count \(g\) from \(z\) to \(y\) has \(\beta=3^g2^{-m}z/y\). Initial halvings have no effect. Thus \(\beta_x/\beta_a=x/(a2^j)\) at every common continuation of a marked meeting. Every simple path has correction bounded below by an absolute \(c>0\). The sum of \(1/v\) over departures exceeding \(256^k\) tends uniformly to zero on such paths, by comparison with \(\sum_{i\ge k}300\cdot206^{i+1}/256^i\).

Suppose the orbit of \(a\) never repeats. Every aligned \(x\) shares its future and also never repeats. Its decreasing correction has a limit \(\beta_\infty(x)\ge c\). The ratio gives \(x/2^j=a\beta_\infty(x)/\beta_\infty(a)\). The right endpoint of the binary interval gives a strict uniform gap from one for these \(\beta_\infty(x)\). Indeed write \(y_t=T^ta\), let \(u_t\) be its cumulative odd count, and put \(Z_t=2^t(y_t+1)/3^{u_t}\). An odd step preserves \(Z_t\), and an even step adds \(2^t/3^{u_t}\). There is a first even step after \(k=v_2(a+1)\) initial odds. Since \(y_t\to\infty\) by nonrepetition and \(2^ty_t/3^{u_t}\to a/\beta_\infty(a)\), this yields
\[
a/\beta_\infty(a)\ge a+1+(2/3)^k,\qquad
\beta_\infty(x)<\frac{a+1}{a+1+(2/3)^k}<1 .
\]
The high-vertex bound therefore forces each aligned \(x\) to visit some odd \(v\le B(a)\).

Only finitely many such \(v\) occur. For each, choose a common site \(T^{r_v}(v)=T^{s_v}(a)\). Their futures meet because an aligned \(x\) visits \(v\). For such an \(x\), extend this site forward beyond both the original marked meeting and the visit to \(v\). Nonrepetition makes the time difference from \(a,v\) to that site unique and invariant when both continue. The difference in odd counts is invariant as well. Subtracting the common continuation shows that \(x\) reaches the chosen site at \(j+s_v\) with the same odd count as \(a\) at \(s_v\). More explicitly, if \(x\) visits \(v\) at \(m\), then \(m+r_v=j+s_v\) and the odd counts of the two paths agree there. Take \(h_a=\max_v s_v\). Any equality at an earlier clock persists to \(h_a\).

If \(a\) is eventually periodic, choose a fixed odd cycle point \(b\), extend the common path to \(b\), and split each trajectory at its first visit to \(b\). Write \(P,D\) for the length and odd count of one lap and \(H_z,q_z,\gamma_z\) for the first-arrival clock, odd count and correction from \(z\). First-arrival products are in \([c,1]\). The full-lap product is \(0<\lambda<1\). The difference \(t\) of the completed lap counts from \(x,a\) has finitely many possibilities because \(\lambda^t=(x/(a2^j))\gamma_a/\gamma_x\in[c,2/c]\). The marked equality gives \(q_x=q_a-Dt\) and \(H_x=j+H_a-Pt\). Choose one integer \(M\) so large that \(M\ge0\) and \(M+t\ge0\) for all possible \(t\). Then \(h_a=H_a+MP\) is a simultaneous detecting clock for the whole binary interval. From \(x\), undertake \(M+t\) laps after its first arrival at \(b\).

At a detecting clock the terminal state and grade are fixed, and each parity word has at most one source. This proves the stated polynomial count even for a hypothetical escaping or nontrivially periodic reference. The closure of all aligned \(x/2^j\) is also countable and compact. At the detecting clock the correction from \(x\) is a product of exactly \(g_a\) elements of the countable compact set \(\{1\}\cup\{3v/(3v+1):v\ge1\}\), and the reference correction is fixed. Every open subinterval of \((a,a+1)\) therefore contains a closed binary interval avoiding the normalized aligned starts at every depth. The proof gives an existence statement for \(h_a\). At \(a=1\) the sharp single clock is three. Ordinary convergence only requires an eventual visit to one.

### The exact boundary for wider intervals

For any finite real \(B>a\), consider all integers \(a2^j\le x<B2^j\). A single reference clock detects every marked alignment on this whole range **if and only if**
\[
\exists t\ge0,\qquad A_t=\frac{2^t T^t(a)}{3^{u_t}}> B,
\]
where \(u_t\) counts the odd departures from \(a\). This is a written extension of the preceding argument. At any length, \(A_t=a/\beta_t\) is nondecreasing. On an eventually periodic orbit the lap correction is strictly below one, so \(A_t\to\infty\). Bounded lap differences give a detecting clock on every finite range by replacing the ratio bound 2 with \(B/a\). On a nonrepeating orbit \(A_t\uparrow A=a/\beta_\infty(a)<\infty\). If \(B<A\), then every aligned source has \(\beta_\infty(x)<B/A<1\). The same finite collection of small odd vertices gives one clock.

The converse is constructive. If all \(A_t\le B\), challenge any proposed clock \(H\). Choose \(h>H\) with \(g=u_h>u_H\), which is possible since a positive trajectory has infinitely many odd departures. Set \(y=T^h(a)\). Take arbitrarily large \(j\) with \(3^g\mid 2^j-1\), and put
\[
x=a+2^h y(2^j-1)/3^g .
\]
The first \(h\) parity bits agree with those of \(a\). Ordinary affine transport gives \(T^h(x)=2^j y\). After \(j\) halvings \(x\) aligns at \(h\). For \(j+H\ge h\), its odd count at \(j+H\) is still \(g>u_H\), so the test at \(H\) fails. Finally \(x/2^j=A_h+(a-A_h)/2^j\) lies in \([a,B)\), since \(a<A_h\le B\). This includes the exact boundary \(B=A\). Thus a nonrepeating ordinary reference would have an exact finite boundary in window width, while an eventually periodic reference admits a detector in every finite window. [Affine transport identity](TowerFrontierAffine.lean)

## Remaining pointwise implications

* Specific prescribed Mersenne sources have strictly smaller canonical visitors which physically meet both designated trajectories. The proof covers 33 disjoint progressions in the delayed family and attains the lower bound of eleven upper odd steps for its synchronized return. A separate theorem produces arbitrarily late delayed parameters at which any smaller canonical visitor would exceed a supplied lower odd-step budget. Its existence at those parameters remains open. [Fixed-source descent](PassageDescent.md) · [Unbounded cost](PassageDescentAnchor.lean)
* The entropy bound for low visits on a single simple orbit constrains its ordinary occupation. In the native five-eighths gate, arrivals born one depth later already realize the order of the entire future reserve. A finite bound for several moving floors also applies simultaneously to periodic points. The written summation bounds critical occupation on each simple orbit. It still leaves the fate of an old source open. [Occupation](PassageGateOccupation.md) · [Fractional moments and hypotheses](PassageGatePressure.md) · [Native reserve](PassageGateReserve.md) · [Moving-floor packing](mathlib/PassageGateMoving.lean)
* Closing successively longer prefixes of one ordinary orbit creates many arithmetically independent rational denominators. This also occurs at nonreturn times on the \(1,2\) cycle. A contradiction for an escaping path would require an arithmetic restriction distinguishing these situations. [Native denominator theorems and external number theory](PassageOrbit.md)

The latest branch updates give exact short rank-midpoint comparisons for a restricted hypothetical cycle, classify discounted postpeak mergers across clocks, extend finite-pattern placement, and describe the distribution of first permanent entry. A positive atom at an old ordinary source remains possible. On the web, the November prime-orbit paper controls the minimum reached by almost all primes. A first visit to one for an individually prescribed prime remains open. [PR #193](https://github.com/GettysburgResearch/collatz/pull/193) · [PR #201](https://github.com/GettysburgResearch/collatz/pull/201) · [PR #211](https://github.com/GettysburgResearch/collatz/pull/211) · [PR #212](https://github.com/GettysburgResearch/collatz/pull/212) · [PR #213](https://github.com/GettysburgResearch/collatz/pull/213) · [Bondurant-David](https://doi.org/10.5281/zenodo.24286158) · [Tao](https://arxiv.org/abs/1909.03562)

The late checkpoint in PR #213 also gives an equivalent condition on finite rational sums for a four-sevenths odd-frequency gate. A least nonconvergent ordinary integer \(m\) would add the same \(1/m\) to every sufficiently deep sum. The fresh entropy and inverse-arrival estimates still permit that contribution. [Native gate statement, formal equivalence and open estimate](https://github.com/GettysburgResearch/collatz/blob/290494b2880b7e1903324503cfcc96fc7ad9905c/research/astra-diagonal-frontier-20261127/NATIVE_GATE.md)

Elsenhans's November 24 journal article reports computations on random inputs with up to a billion decimal digits. Weaver's November 25 work gives finite exception budgets for segments and an arithmetic interval for paradoxical lengths. These address actual finite trajectories. None supplies the vanishing mass of permanently surviving ordinary sources required above. [Elsenhans](https://doi.org/10.1007/s40993-026-00811-5) · [Finite exception budgets](https://rstation.ai/problems/collatz/papers/226) · [Paradoxical lengths](https://rstation.ai/problems/collatz/papers/231)

## Reproducing the checks

From the repository root, run the following with a built Mathlib checkout matching Lean 4.34.1. The first command checks every local module from source and audits its declared theorem dependencies. The second regenerates the interval certificates and the lower-bound witnesses. [Native check receipt](../../reports/clock-itineraries-20261127/passage-native.json)

```sh
python -B research/clock-itineraries/check_fresh_lean.py --mathlib /path/to/built/mathlib --lean /path/to/lean --jobs 4
python -B research/clock-itineraries/passage_interval_replay.py
```

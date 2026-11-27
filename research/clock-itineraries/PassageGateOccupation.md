# Occupation of one ordinary path and synchronized ancestors of a prescribed target

Let \(T(x)=x/2\) on even integers and \(T(x)=(3x+1)/2\) on odd integers. Write \(c_h(x)\) for the odd departures among the first \(h\) ticks. Take an arbitrary finite segment of a positive ordinary trajectory whose listed states are pairwise distinct. With \(\theta=H_2(\log_3 2)=0.9499555\ldots\), one has the uniform written bound
\[
 \#\{\text{listed states}\le X\}\ll X^\theta/(\log(2X))^{3/2}
 \qquad(X\ge1).                                                     \tag{1}
\]
This includes visits separated by excursions arbitrarily far above \(X\). The input is only the deterministic shortcut map. Previous finite-path bounds and an entropy estimate with an arbitrary positive exponent loss appear in the [earlier occupation argument](HourCycleOccupation.md) and [finite records, T-A3-651](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/astra-three-routes/pass3/FINITE_RECORDS.md).

## Dyadic recursion on the same path

Integer rounding gives \(T^hx\le3^{c_h(x)}\) whenever \(1\le x\le2^h\). More generally \(x\le2^h t\) implies \(T^hx\le3^{c_h(x)}t\). Induct on \(h\). On an even first tick take the smaller packet parameter \(t\) unchanged. On an odd first tick, \((3x+1)/2\le3\cdot2^{h-1}t\) because the odd \(x\) is strictly below the packet's even upper bound. This stronger rounding avoids an affine-offset error. [HourTower.lean](HourTower.lean)

For \(h\ge1\) set \(k_h=1+\lfloor\log_3(2^{h-1})\rfloor\) and \(B_h=\sum_{d=k_h}^h\binom hd\). The parity bijection gives exactly \(B_h\) positive inputs in the full packet \([1,2^h]\) with at least \(k_h\) odd departures. Every other listed state \(x\le2^h\) has \(T^h x\le2^{h-1}\). Shifting its index forward by \(h\) is injective. Only the last \(h\) indices can land beyond the segment. Thus, with \(V_h\) the number of listed states at most \(2^h\),
\[
 V_0\le1,\qquad V_h\le B_h+V_{h-1}+h.                              \tag{2}
\]
The finite recurrence and the resulting explicit bound on a fixed source's exit clock are kernel-checked. The native histogram proof also covers every translated packet of length \(2^h\) with odd stride. A separate finite bound for a forward-invariant set multiplies the smaller-packet term by its maximum fiber multiplicity on the native transfer. [PassageGatePacking.lean](mathlib/PassageGatePacking.lean)

In (2), \(k_h=(\log_3 2)h+O(1)\), with \(\log_3 2>1/2\). The ratio \(\binom h{d+1}/\binom hd\) is uniformly below one for \(d\ge k_h\) and \(h\) large. Stirling's formula gives \(B_h\asymp 2^{\theta h}(1+h)^{-1/2}\), including the bounded rounding error. Summing (2) over the preceding dyadic levels is a geometric sum with the same order. For example, levels at least \(h/2\) have comparable square-root denominators and all lower levels cost \(O(h2^{\theta h/2})\). This gives (1) with the weaker denominator exponent \(1/2\).

The integer bound \(V_{8k}\le300\cdot206^k\) follows already from the binomial moment \(\sum_d2^d\binom hd=3^h\). For \(8k<h\le8(k+1)\), \(k_h>5k\) because \(3^5<2^8\), so \(B_h\le3^h/2^{5k}\le6561\cdot206^k\). Summing the eight levels and using \(k+1\le206^k\) proves the numerical induction. Hence an injective positive orbit starting at the prescribed \(x\) has some \(T^i(x)>256^k\) with \(i\le300\cdot206^k\). [PassageGateSublinear.lean](mathlib/PassageGateSublinear.lean)

The same argument counts the union of **all** periodic sites in one bound. The exact clock is injective on this union: if two periodic points have the same image after \(h\) ticks, advance to a common multiple of their periods beyond \(h\). Thus (2) applies with one smaller-packet term and no end correction. Both the bound \(300\cdot206^k\) for the whole union and the general invariant-set theorem are kernel-checked in the same module. The sharper written bound (1) follows for the whole periodic set by the same argument below, keeping this injectivity at every clock.

## Using every prefix to attain the critical moment

Put \(p=\log_3 2\) and choose a real \(A>1/\theta\). For \(0\le t\le h\), let
\[
 \ell_t=L+\lceil A\log_2(1+\min(t,h-t))\rceil ,
 \qquad W_h=2^{\theta h}(1+h)^{-3/2}.
\]
Fix a sufficiently large integer \(L\) as specified below. For large \(h\) all \(\ell_t\le h/2\). Discard at most the last \(h\) starting indices of a finite path. If a remaining source \(x\le2^h\) has a prefix with \(3^{c_t(x)}\le2^{t-\ell_t}\), integer rounding gives \(T^tx\le2^{h-\ell_t}\). At each fixed \(t\) the index shift is injective, so these sources contribute at most \(\sum_{t=0}^h V_{h-\ell_t}\), even when the same source qualifies at several clocks. The other sources have \(c_t(x)-pt\ge-p\ell_t\) for every prefix and \(u=c_h(x)-ph\ge-pL\).

To count their words, give the bits independent Bernoulli parameter \(p\). For the centered walk \(S_t=c_t-pt\), and for the walk with the opposite sign, the following bound holds for fixed \(b>0\) and \(x\ge0\):
\[
 \Pr\{x+S_t\ge-b\log(1+t)\ \text{for }t\le m\}
      \ll_b (1+x)/\sqrt{1+m}.
\]
Here are details of the logarithmic boundary estimate. The flat-boundary survival bound is \(O((1+x)/\sqrt{1+m})\) for either sign by the interval-exit argument in the [ballot proof](PassageGatePressure.md). Denote the first curved-boundary violation by \(\tau\). Relaxing to the flat floor \(-b\log(1+m)\) bounds \(\Pr(\tau>m)\) by \(C(1+x+b\log(1+m))/\sqrt{1+m}\). Thus \(\tau<\infty\) almost surely and summation of this bound divided by \(1+m\) gives \(\mathbb E\log(1+\tau)\ll_b1+x\). The increments have absolute value at most one, so \(x+S_\tau\ge-b\log(1+\tau)-1\). Stopping the centered martingale at \(\tau\wedge r\), where \(r=\lfloor m/2\rfloor\), now gives \(\mathbb E[(x+S_r)\mathbf1_{\tau>r}]\ll_b1+x\). Conditional on survival to \(r\), apply the flat estimate on the remaining steps at floor \(-b\log(1+m)\). The numerator after averaging is at most
\[
 C_b(1+x)+C_b(1+\log(1+m))
       \frac{1+x+\log(1+m)}{\sqrt{1+r}}\ll_b1+x .
\]
This proves the displayed curved estimate.

Split the \(h\) steps into three blocks of comparable length. The first block must stay above the logarithmic boundary with initial bank \(p(L+1)\). At a fixed endpoint \(u\), the last block read backwards has the same condition for the opposite signed increments, with initial bank \(u+p(L+1)\ge0\). These conditions concern independent disjoint blocks. Once their increments are fixed the middle must attain one particular count, of probability \(O((1+h)^{-1/2})\) by the binomial formula and Stirling. The resulting probability per endpoint is \(O_{A,L}((1+\max(u,0))(1+h)^{-3/2})\). A length-\(h\) word with excess \(u\) has inverse probability \(2^{\theta h}((1-p)/p)^u\). Since \(p>1/2\), summation over the unit-spaced endpoints \(u\ge-pL\) gives \(O_{A,L}(W_h)\) remaining words. Parity bijectivity gives at most one source per word in the packet.

The smaller packets consume only a fixed fraction of \(W_h\), because
\[
 \sum_{t=0}^h\frac{W_{h-\ell_t}}{W_h}
 \le 2^{5/2-\theta L}\sum_{j=1}^{\infty} j^{-A\theta}<1/2
\]
for a suitable \(L\). Strong induction on \(h\) now absorbs \(h+O_{A,L}(W_h)\) into the other half of \(C W_h\), enlarging \(C\) to cover the finitely many small packets. This gives (1). The same proof applies to the periodic set, with no end correction. For a forward-invariant set with uniformly bounded multiplicity \(B\) at every clock, multiply the sum by \(B\) and enlarge \(L\). The exact moving-barrier recursions on a simple finite path, on an invariant set with injective shifts, and on all positive periodic sites are kernel-checked. The curved-boundary probability estimate and its asymptotic induction are written proofs. [PassageGateMoving.lean](mathlib/PassageGateMoving.lean)

Taking the first \(n\) sites of any nonrepeating source and inverting (1) gives a lower bound \(\gg n^{1/\theta}(\log(2n))^{3/(2\theta)}\) on their maximum. On every finite simple path or injective ray, dyadic summation gives
\[
 \sum_{v\ge M} v^{-s}\ll_s M^{\theta-s}(\log(2M))^{-3/2}\quad(s>\theta),
 \qquad
 \sum_{v\ge M}v^{-\theta}(\log(2v))^\delta
       \ll_\delta (\log(2M))^{\delta-1/2}\quad(\delta<1/2).           \tag{3}
\]
The variable \(v\) runs over the path's sites. In particular the critical sum with \(\delta=0\) converges uniformly. The ordinary product of the odd-step correction factors \(1+1/(3v)\) is bounded by an absolute constant on every such path. Its contribution from states above \(M\) is \(1+O(M^{\theta-1}(\log(2M))^{-3/2})\).

A separate explicit calculation is fully kernel-checked. The sum of reciprocals of actual visited states at least \(256^k\) is at most \(316416(206/256)^k\). When every departed odd state clears that floor, the same path satisfies
\[
 2^n T^n(x)\le 3^{c_n(x)}x\exp[105472(206/256)^k].
\]
The Lean proof sums finite bands, converts their rational reciprocal bound to the real product, and verifies its exact affine transport. [PassageGateDistortion.lean](mathlib/PassageGateDistortion.lean)

## Consequences for first violations and predecessor density

For the global constant on paths with every departed state above one, Nikzad, Frinkle and Bagherzadeh's Theorem 2.22 gives the stronger explicit residue bound \(4/3\). Their Theorem 2.10 also gives the strict interior version of the dyadic endpoint bound used in (2). The native proof here supplies a uniform error tending geometrically to zero with the floor. [Nikzad, Frinkle and Bagherzadeh, Theorems 2.10 and 2.22](https://hexagonmath.org/pdf/2611.00033v1)

For an odd source \(m\), put \(D_j=A_j-7j/4\), using the exact division clocks of its Syracuse orbit. Before the first arrival at one, if \(D_j\) sets a strict record among earlier \(D_i\) or gives the first positive value, its preceding odd trajectory up to that point can be taken simple. Indeed a repetition before this first record would trap the trajectory on a lap entirely above one. The elementary lap identity gives \(A_{\rm lap}/p\le\log_2(10/3)<7/4\) at odd phases \(\ge3\). A phase on a later lap has smaller \(D\) than the identical phase one lap earlier. If the endpoint is one, use the simple pre-first-arrival path. The associated shortcut segment is also simple up to that arrival or first repeated odd state, by determinism. The exact height identity and (3) now give
\[
D_j\le\log_2(C m)-(7/4-\log_2 3)j.
\]
Thus any initial positive violation before reaching one occurs by \(\log_2(Cm)/(7/4-\log_2 3)\). For a late gate failure on an orbit reaching one, subsequent exponent-two laps supply the positive drift. The largest pre-entry value of \(D_j\) is nonnegative since \(D_0=0\), so its earliest attaining index obeys the same cutoff. This removes the additive logarithmic correction in the earlier bound. [PR 201, old-source first failure](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/infinity-20261127/mass/OLD_HEAD_FIRST_FAILURE.md)

If the predecessor densities \(\delta_v=\mathsf d\{x:T^j x=v\text{ for some }j\ge0\}\) exist for \(1\le v\le X\), averaging (1) yields \(\sum_{v\le X}\delta_v\ll X^\theta/(\log(2X))^{3/2}\). On a periodic eventual orbit, count the preperiod and just one lap. On an injective orbit, increase the finite prefix to exhaust its visits. The same upper bound applies before taking densities at every finite source cutoff. A positive density attached to each fixed point of a single sparse escaping ray is compatible with this estimate.

For a hypothetical component disjoint from one, let \(m\) be its least odd state and \(\beta=2^{7/4}/3>1\). A first failing date \(j>N\) on the odd-word gate must start at \(x\ge m\beta^j/C\) by the same distinct-path product estimate. By the sharp principal-source count in [the pressure proof](PassageGatePressure.md), the combined reciprocal mass of all distinct such principal sources in that component is
\[
 O\big((m\beta^N)^{d-1}(1+\log m+N)^{-3/2}\big),\qquad d=H_2(4/7).
\]
This replaces the smaller component-dependent base \(2^{7/4}/(3+1/m)\) in the earlier estimate and adds the polynomial factor from the stopped binary gate. It still allows the permanent first-power contribution of \(m\). [PR 213, whole-component first failures, equation (6)](https://github.com/GettysburgResearch/collatz/blob/de6384b4a232b996add4f5c620929d06a1982e90/research/astra-diagonal-frontier-20261127/mass/GLOBAL_RECENT_COHORT.md)

## Actual exact-clock fibers inside a fixed predecessor set

Assume that the predecessor set of a fixed target \(m\) has positive lower density \(\delta\). For every sufficiently large \(h\), at least \(c_\delta 2^h\) inputs \(x\le2^h\) reaching \(m\) satisfy \(x\ge c_\delta 2^h\) and
\[
 |c_h(x)-h/2|\le C_\delta\sqrt h.
\]
Indeed discard the lowest \(c_\delta 2^h\) integers and use the exact binomial histogram with Chebyshev's inequality on the whole packet. Choose constants so the removed sets cost at most half the guaranteed predecessor count. This argument requires only a lower density, without a density assertion on a prescribed upper half.

No selected \(x\) has yet visited \(m\) by time \(h\) when \(h\) is large. More precisely, if \(2^h\le Dx\) and \(T^t x=m\) with \(t\le h\), the nonnegative affine offset gives
\[
 2^{h-t}3^{c_t(x)}\le Dm,\qquad
 c_h(x)\le\lfloor\log_2(Dm)\rfloor+\lfloor\log_3(Dm)\rfloor .
\]
Use fixed integer \(D\ge1/c_\delta\). Its \(h\)-th image \(y\) is therefore still a genuine ancestor of \(m\). The lower affine bound and the upper integer rounding show
\[
  D^{-1}3^{c_h(x)}\le y\le3^{c_h(x)} .
\]
By pigeonhole, some such ordinary \(y\) at height \(3^{h/2+O_\delta(\sqrt h)}\) has at least
\[
 c_\delta(2/\sqrt3)^h \exp[-C_\delta\sqrt h]
\]
distinct same-clock inputs from this packet. Cauchy–Schwarz gives a sum of squared fiber counts at least \(c_\delta(4/\sqrt3)^h\exp[-C_\delta\sqrt h]\) on these selected sources. The finite no-early-hit and actual target-preserving pigeonhole statements are [native Lean theorems](mathlib/PassageGateAncestors.lean). The density hypothesis for each unit target is supplied, with its stated mixing input, by [Wren, Theorem 1](https://rstation.ai/problems/collatz/papers/10/v3). A uniform version under its lower bound \(c/m\) follows by Hoeffding in place of Chebyshev, taking \(D\ll m\), replacing \(C_\delta\sqrt h\) by \(C\sqrt{h\log(2m)}\), and requiring \(h\ge C\log(2m)\).

This synchronized concentration occurs also for \(m=1\). It supplies a large fiber whose endpoint is a later ancestor of the prescribed \(m\). The nonlinear side comparison of PR 193 instead requires a lower bound on the original inverse transfer at the **specified sibling** \(s(a_j)\), at exactly the same odd depth as a specified forward orbit. At depths whose overshoot above \(j\) tends to infinity, its weighted ancestor law tends weakly to Haar. At depth \(j\) the fixed seed retains an atom. Equation (3) also shows why a side-to-trunk floor of only \(a_j^{-\theta}\), even multiplied by \((\log(2a_j))^\delta\) with \(\delta<1/2\), is itself summable along every injective ray. The required divergence on some putative escaping ray remains unproved. [PR 193, same-depth sibling proposal](https://github.com/GettysburgResearch/collatz/blob/98d56bd87db75bf98c8f59abf3973101dd056d27/research/astra-diagonal-20261127/operator/SIBLING_COMPARISON_PROPOSAL.md) · [PR 193, ordinary ancestor equilibrium](https://github.com/GettysburgResearch/collatz/blob/98d56bd87db75bf98c8f59abf3973101dd056d27/research/astra-diagonal-20261127/escape/ORDINARY_ANCESTOR_EQUILIBRIUM.md)

Under PR 213's stated relative-passage and no-return inputs, every later nonperiodic unit \(z\) on a hypothetical escaping ray rooted at \(a\) has \(q_z\ll_{a,\epsilon}z^{-1+\epsilon}\) for its auxiliary inverse no-return test. This uses the fixed positive lower predecessor density of \(a\) and its monotonicity along the ray. Equation (3) gives, for \(0<\epsilon<1-\theta\),
\[
 \sum_{z\text{ on this ray},\ z\ge M}q_z
    \ll_{a,\epsilon} M^{\theta-1+\epsilon}(\log(2M))^{-3/2} .
\]
The same estimate applies after restriction to permanent phases. The exponent uses the sparser population on a single ordinary path. The supplied lower no-return mass is only of reciprocal-height order, which is summable here. [PR 213, ordinary no-return exponent](https://github.com/GettysburgResearch/collatz/blob/de6384b4a232b996add4f5c620929d06a1982e90/research/astra-diagonal-frontier-20261127/mass/ORDINARY_NO_RETURN_EXPONENT.md)

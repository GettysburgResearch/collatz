# The critical square-root logarithmic Hausdorff measure of nonmerging source pairs is zero

Let \(T\) denote the shortcut Collatz map on \(\mathbb Z_2\). A canonical state \(z=(s,D)\), \(s\ge0\) and \(D\in\mathbb Z\), starts its physical coordinates at \(x,3^s x+D\). Track the initial odd-count lead \(s\) on the second coordinate. Simultaneous application of \(T\), with the orientation swap at a level crossing, defines the canonical level and offset. Absorption is the first visit to \((0,0)\), when the physical states and the adjusted counts agree. Write \(E_z\) for the bases \(x\in\mathbb Z_2\) on which this canonical process is never absorbed.

**Written deduction from David Leen's two October 9 preprints.** For every fixed integer canonical state, including \((1,0)\) for the pair \((x,3x)\),
\[
      \mathcal H^g(E_z)=0,\qquad g(2^{-t})=2^{-t}\sqrt t\quad(t\ge1).        \tag{1}
\]
Use the usual dyadic metric and set \(g(r)=r\sqrt{\log_2(1/r)}\) at small positive radii. The same upper bound holds for the set on which the two physical values never agree at a common shortcut time, and after restriction to odd bases. An unequal-slope value coincidence at any fixed finite word can involve at most one base, since it is an affine equation in that base. The union of those additional coincidences is countable. Finite-level survivor counts themselves give a bounded critical covering cost. To get its vanishing, the proof uses large values of the level on an infinite history.

## Checked source inputs and scope

1. Leen's *Quantitative synchronization of Collatz trajectories*, “Fresh labels and exact cylinders”, identifies each labelled history of length \(t\) with one dyadic cylinder of diameter \(2^{-t}\). Under Haar measure its mass is \(2^{-t}\) and the residual base is again Haar. The two possible labels are distinguished even when the state transitions coincide. [Zenodo 23268755, October 9, 2026](https://doi.org/10.5281/zenodo.23268755)
2. Leen's *Exact rates in Collatz synchronization*, Theorem 7.2, “Harmonic capacity and conditioned histories”, proves for the full absorption time \(A\)
\[
 \sqrt t\,\mathbb P_z(A>t)\longrightarrow c h(z),\qquad
 c=2/\sqrt\pi,\qquad h(z)=s+\mathbb E_z M,
\]
where \(M\) counts future level-zero departures into positive excursions. The function \(h\) is harmonic, finite, positive at every live state and zero at absorption. Its Doob law \(\nu_z\) assigns a labelled cylinder \([w]\) of depth \(t\) mass \(2^{-t}h(z_w)/h(z)\), with \(z_w\) its end state. This proves Haar-almost-sure absorption for \((x,3x)\) with the sharp square-root tail. On odd bases the first step goes from \((1,0)\) to \((1,-1)\) in Leen's offset convention. The adjusted count lead matters for converting a shortcut clock to the unaccelerated clock. [Zenodo 23268751, October 9, 2026](https://doi.org/10.5281/zenodo.23268751) · [explicit earlier application to the same pair, November 4](https://rstation.ai/r/collatz/posts/2?after=buQ2uW_A5TjNQd5h)
3. Leen's *Late synchronization and the geometry of Collatz families*, proposition “Fixed-level physical meander”, starts at any fixed \((s,D)\), \(s\ge1\). For its first physical return \(R\) to zero, \(\sqrt t\,\mathbb P_{s,D}(R>t)\to cs\). Conditional on \(R>t\), the level at \(t\) divided by \(\sqrt{t/2}\) tends in law to the time-one value \(V\) of a standard Brownian meander. The latter has the Rayleigh density \(v e^{-v^2/2}\) for \(v>0\). The proposition includes initial holding and uses the physical shortcut clock. [Zenodo 23268753, October 9, 2026](https://doi.org/10.5281/zenodo.23268753)

The October 9 Zenodo records' original TeX files were retrieved and matched to the MD5 checksums in their record metadata. Their SHA-256 values, in the order of these three inputs, are `2dd65fc17137f55d49d6cc9dc283660b524368a43182dc4a52901d12cd5056bd`, `d2f961635d339a4b215c82b1f2f8b9ca53143043f4c58b9aa67290f46056996e`, and `555a0bec4756feb08dc84f8d2e002a675db8a496acbe63ce6e489cb93363bd64`. The three inputs are imported written results. No external Lean source was rebuilt for this deduction. Paper 175, Theorem 3, had already used the square-root absorption tail to get zero measure at smaller logarithmic gauges for a different real terminal-coordinate carrier. [Paper 175](https://rstation.ai/problems/collatz/papers/175)

## Local domination by the capacity law

Fix a live initial state. After a fixed labelled prefix \(w\) of length \(k\), all descendants which survive a further \(n\) steps cover \(E_z\cap[w]\). Their total critical cost is
\[
          2^{-k}\sqrt{k+n}\,\mathbb P_{z_w}(A>n)
                      \longrightarrow c\,2^{-k} h(z_w).
\]
Taking the Hausdorff limit gives \(\mathcal H^g(E_z\cap[w])\le ch(z)\nu_z([w])\), including absorbed prefixes. The same bound holds on open sets by their disjoint cylinder decomposition. Finite Borel regularity of \(\nu_z\), or a countable covering by open cylinders of arbitrarily small total mass, then gives
\[
                  \nu_z(F)=0\quad\Longrightarrow\quad
                      \mathcal H^g(E_z\cap F)=0                      \tag{2}
\]
for every Borel set \(F\). The constant in local domination is independent of the fixed prefix.

## High levels on the infinite surviving law

Let \(s_t\) denote the level at raw date \(t\), set to zero after absorption. For every fixed \(L>0\) and every live \(z\),
\[
  \liminf_{t\to\infty}\sqrt t\,\mathbb P_z(s_t>L\sqrt t)
                         \ge ch(z)\,\mathbb P(V>\sqrt2 L).            \tag{3}
\]
For an initial positive-level excursion use source input 3 with its weight \(s\). Enumerate also every finite labelled history ending in a genuine departure from zero to level one. Give each such history its Haar cylinder probability as weight; their sum is \(\mathbb E_zM\) by counting departures. For a fixed history ending at time \(k\), restrict to its next excursion staying positive through \(t\) and reaching level \(>L\sqrt t\) there. Conditional on that history, the input gives the limit with weight one, since \((t-k)/t\to1\) and the Rayleigh law has no atom at the threshold. At each \(t\) these retained events are disjoint: the excursion containing \(t\) has a unique start. Histories ending after \(t\) contribute zero. Apply Fatou's inequality to the countable sum; the total weight is \(s+\mathbb E_zM=h(z)\). This proves (3) without an onset uniform in the initial state.

At depth \(t\) the capacity tilt multiplies Haar probabilities by \(h(z_t)/h(z)\), and \(h(z_t)\ge s_t\). Hence (3) gives
\[
 \liminf_{t\to\infty}\nu_z\{s_t>L\sqrt t\}
                   \ge c L\,\mathbb P(V>\sqrt2 L)>0.                 \tag{4}
\]
The lower constant is independent of \(z\). After any fixed live prefix, the conditional law is exactly the capacity law started at its end state. For the event of exceeding \(L\sqrt t\) infinitely often in the original clock, apply (4) with \(2L\) to the future clock; the fixed time shift is eventually absorbed. The probability of infinitely many exceedances is at least the limsup of the single-time probabilities. Thus the event has conditional probability bounded below by one positive constant on every positive-mass prefix. Martingale convergence of conditional probabilities to the event indicator forces that indicator to equal one almost surely. Taking all positive integer \(L\) gives
\[
                  \limsup_t h(z_t)/\sqrt t=+\infty
                           \qquad \nu_z\text{-almost surely}.         \tag{5}
\]

For any \(M_0>0\), cover the set in (5) by the first cylinders after depth \(n\) with \(\nu_z([w])/g(2^{-|w|})>M_0\). Every path in (5) is covered. The stopping cylinders are disjoint, so their total gauge cost is at most \(1/M_0\). Let \(n\) and then \(M_0\) tend to infinity. This proves zero critical measure on the set in (5), and (2) supplies the discarded paths, proving (1). If \(z=(0,0)\) the survivor is empty.

# Ordinary source currents, rare gates and the final proof boundary

**Collatz remains open.** This checkpoint follows `7af83b786636abba2f44fe8c81441153331377fc`. The final part of the six-hour session returned to escaping ordinary trajectories, using three parallel attacks and separate fresh reviews. The [sixth checkpoint](SIXTH_CHECKPOINT.md) retains the finite height-one cycle theorem through odd period `10^1000` and its 959-row Lean arithmetic certificate.

The positive results here concern actual ordinary sources and exact finite cylinders. The countermodels identify the extra step needed to pass from such cylinders to one fixed positive integer. The new infinite arguments are written mathematics. The existing 30-module Lean packet remains the formal endpoint; its theorems do not acquire these new analytic claims automatically.

## 1. Every large inverse gain comes from a finite set of ordinary sources

For positive odd $y$, let

$$
q(y)=\frac1y\max\left\{\frac{3^k}{2^{A_k(v)}}:v>0\text{ odd},\ U^k(v)=y\right\}.
$$

Every finite visitor clock is allowed. The empty visit supplies gain one. A nonempty visit has $y>gv$, so any maximizing visitor begins at $v\le1/q(y)$. Repeated cycle laps reduce the gain; a maximum is attained among finitely many first arrivals.

On an escaping component, the corrected height

$$
\Phi(v)=v\prod_{i\ge0}\left(1+\frac1{3U^i(v)}\right)
$$

is finite and has a minimum $P_C$. Once a minimizing source meets an escaping ray, $q(y)$ decreases strictly to $1/P_C$ along that ray. This yields a complete description of every positive superlevel: up to finitely many targets it is a finite union of escaping tails. Equality at the limiting threshold is included, since the approach is from above. In particular

$$
q(y)\longrightarrow0\quad(y\to\infty,\ y\text{ odd})
\quad\Longleftrightarrow\quad
\text{every positive ordinary orbit is bounded}.
$$

The same equivalence holds if only the liminf of the maxima on dyadic octaves is zero; the proof also works on intervals $[Y,3Y/2+1)$. Boundedness permits nontrivial cycles. The criterion's vanishing side is unproved. Weaver's Papers 177, 178 and 207 are explicitly credited for the gain, corrected height and minimizer; the added result describes the full ordinary superlevels and their limit spectrum.

[Full theorem](pointwise/INVERSE_GAIN_ESCAPE_SPECTRUM.md) · [independent graph and mathematical review](../../reports/six-hour-20261127/INVERSE_GAIN_SPECTRUM_INDEPENDENT_REVIEW.md).

## 2. A sharper bound on the adaptive Green sum over ordinary sources

PR193's adaptive Green current sums the actual weights of all incoming ordinary paths. Before a source's ternary representative becomes its physical state, let $a(v)$ be the product of its prefix boosts. The new estimate is

$$
\sum_{\substack{v\le V\\v\text{ odd}}}a(v)^p\le C_p V
\qquad\text{whenever }p>0\text{ and }b(13)^p<3.
$$

This is a uniform average over the ordinary source interval. It follows from the exact dyadic cylinders and the original-law bound $\mathbb E(1/r_j)\le(j+1)3^{-j}$, rather than an independence assumption after the source digits have been consumed.

For the normalized unrounded current $u$ with exponent $s=3/2$, it gives

$$
\boxed{q(y)^{3/2}\le u(y)\le C\sqrt{q(y)}}
$$

at every nonperiodic positive odd target. The contribution of sources $v>M$ is uniformly $O(M^{-1/2})$. This removes the previous small exponent loss. If each source is counted only at its first arrival, both bounds hold at every positive odd target, including periodic ones. The full current at a nontrivial cycle instead diverges; that case is kept separate.

Each escaping component has one positive unrounded limiting current, and at most four rounded limiting currents arising from the two clock parities. Their total unrounded mass is finite. The unrounded current increases along the ray, while each rounded current increases along its fixed recurrent clock-parity subsequence. The limits are approached strictly from below, so equality at a superlevel threshold is excluded. The direction is the opposite of the gain ratio in Section 1 and is recorded explicitly.

This comparison connects the sum over all sources to the maximal visitor. It does not prove that the maximum decays. [Proof and finite controls](pointwise/ADAPTIVE_GREEN_COMPONENT_SPECTRUM.md).

## 3. The source norm cannot be separated from the gate

For an original geometric word of length $n$, let $m$ be its principal odd source, $A$ its division sum and $G$ its positive affine correction. Put

$$
Z_n(z)=\frac{2^A}{m+zG},\qquad
W_n=\{4A_j\le7j\text{ at every prefix}\}.
$$

The required trace is the joint quantity $\mathbb E[\mathbf1_{W_n}Z_n(z)]$. For the unfiltered centered payoff, the exact moment exponent is

$$
\lim_n\frac1n\log\mathbb E Z_n(0)^p
=\max(0,p-1)\log4.
$$

Removing a fixed finite list of starting integers does not change it. More strongly, an exact eight-edge inverse certificate constructs genuine principal windows entirely above any fixed floor, all of which go to one on the next odd step after the window. They already prevent the separated Hölder estimate from tending to zero for $p\ge4/3$, including every fixed nonnegative tilt $z$.

The independent forward enumeration checks 200,000,000 word/class pairs and the same exact minimum as the reverse recurrence. This is an elementary construction independent of the conjecture. It does not claim those inverse windows individually pass $W_n$; that is exactly why the result concerns separating two marginals.

A separate compatible two-place example uses the rational cycle $23/5,37/5,29/5$. Its finite words have genuinely positive principal integer lifts, satisfy the gate, and stay uniformly high as the depth grows. The starts and terminals converge in the dyadic and ternary rings while their ordinary reciprocal contributions vanish. There is no one positive integer realizing the infinite word.

[Corrected active manuscript](pointwise/PRINCIPAL_SOURCE_PRESSURE_OBSTRUCTION_CORRECTED.md) · [fresh review](../../reports/six-hour-20261127/INDEPENDENT_PRINCIPAL_PRESSURE_REVIEW.md) · [one literal valuation correction](../../reports/six-hour-20261127/PRINCIPAL_PRESSURE_CORRECTION.md).

## 4. Entropy obtained from actual physical positions

Take a simple ordinary shortcut segment with $P$ states. Within an interval of diameter less than $2^m$, different states have different length-$m$ parity windows. Their empirical entropy is therefore exactly the logarithm of their number. Conditional entropy bounds turn this fact into a quantitative lower bound on parity mismatches at short lags.

If the whole segment has height at most $P^{B+o(1)}$, every limiting parity process has entropy at least $1/B$ bits per shortcut step and mean parity $\log_3 2$. The more general result needs no global height cap: if a positive fraction $\alpha$ lies in at most $P^{\gamma+o(1)}$ arbitrary moving intervals of width $P^{B+o(1)}$, where $\gamma<1$, the entropy is at least $\alpha(1-\gamma)/B$.

Thus a zero-entropy ordinary limit requires $P^{1-o(1)}$ occupied physical cells at every fixed polynomial scale. For each fixed $\epsilon>0$, the fraction of phases lying in cells of occupancy at least $P^\epsilon$ tends to zero. This is a restriction on an actual ordinary path. It does not rule out that degree of spread. The separate digit-window consequence imports Paper 170's measure-rigidity theorem with its odd weighting and its order of limits intact.

[Finite interval, process entropy and critical trace](pointwise/TRANSIENT_ENTROPY_AND_CRITICAL_TRACE.md) · [physical-cell extension](pointwise/PHYSICAL_CELL_ENTROPY.md).

## 5. A sharp obstruction to completing the proof from statistics alone

There is a family of transcendental dyadic starting points of Hausdorff dimension $H_2(\log_3 2)$ with strictly critical-safe prefixes, polynomial real affine growth, and every finite prefix realized by a positive ordinary source that later reaches one. Their least positive cylinder sources nevertheless grow as $2^{n-o(n)}$.

These words can pass every fixed-order moving Bernoulli correlation test on every admissible calendar whose length divided by $\log n$ tends to infinity. This scale is sharp: uniform one- and two-point tests alone force that ratio to diverge. The converse is a finite Gram-matrix rank argument; the construction uses fixed-weight permutations and sparse adaptive transpositions.

The real, dyadic and finite ordinary realizations are different objects. None of these is an escaping positive integer. They show that these statistical and finite-realization conclusions can all hold while the fixed ordinary source disappears.

[Dimension and moving tests](pointwise/MOVING_LAG_CRITICAL_COUNTERMODELS.md) · [sharp calendar scale](pointwise/SHARP_MOVING_CORRELATION_SCALE.md).

## 6. The actual joint gate: physical concentration and fractional moments

This estimate keeps the source and gate together under the original probabilities. At any fixed slope $1<a<2$ put

$$
W_n(a)=\{A_i\le ai\ (1\le i\le n)\},\quad
d=H_2(1/a),\quad \gamma=2^{-a(1-d)},\quad p_c=1+\log_2\gamma.
$$

For any fixed $z\ge0$ and any prescribed polynomial failure probability, almost every accepted principal word has

$$
m\ge 2^{an}/\operatorname{poly}(n),\qquad
x_i\ge 2^{a(n-i)}3^i/\operatorname{poly}(n),\qquad
Z_n(z)\le\operatorname{poly}(n).
$$

The simultaneous logarithmic height error is $O(\sqrt{n\log n})$. The endpoint has the sharper bounds $3^n/\operatorname{poly}(n)\le x_n<2\cdot3^n$. For each fixed positive linear tolerance the failure probability is exponentially small; the exponent is allowed to depend on that tolerance. These are actual ordinary integer trajectories attached to the sampled principal words, with no assumed randomness on a fixed orbit.

For each fixed $z\ge0$, the full accepted population, including the rare complement, satisfies

$$
\boxed{\lim_{n\to\infty}\frac1n\log
 \mathbb E[\mathbf1_{W_n(a)}Z_n(z)^p]=\log\gamma
 \quad\text{for every real }p\le p_c.}
$$

At $a=7/4$, $p_c\approx0.97415$. The proof counts source shells using both the prefix gate and the *total* number $A_n-n$ of even shortcut departures. At $p_c$ it gives a polynomial conditional moment bound; power means and negative-power Jensen supply every smaller real power. For $p_c<p<1$, the upper exponential rate is at most $(p-1)\log2$, with a further polynomial saving from the exact divisibility of a long odd run. The certified endpoint is not claimed to be optimal.

[Conditional physical profile](pointwise/RARE_GATE_PHYSICAL_PROFILE.md) · [full joint moment proof](pointwise/JOINT_GATE_FRACTIONAL_PRESSURE.md) · [physical sparse-even improvement](pointwise/SPARSE_EVEN_GATE_REMAINDER.md) · [fresh moment review](../../reports/six-hour-20261127/INDEPENDENT_SHARP_GATE_MOMENT_REVIEW.md).

### Why passing to the first power is a genuine new obligation

Let $M_n(p,z)$ denote the joint moment and $J_n(z)=M_n(1,z)$. If $p_n\uparrow1$ with $n(1-p_n)\to\infty$, then $M_n(p_n,z_n)\to0$ for every nonnegative tilt sequence, even if permanently safe ordinary sources exist. For fixed $z$, along a bounded $n(1-p_n)$ layer its vanishing is instead equivalent to the first-moment vanishing. Thus taking powers closer to one does not by itself bridge the gap.

At this specific slope $7/4$, PR201's centered trace $J_n(0)$ tends to zero if and only if Collatz holds. For each fixed $z>0$, $J_n(z)$ tends to zero if and only if every ordinary orbit is eventually periodic. The second criterion permits additional cycles. Neither vanishing assertion is established here.

For $p_n=1-\tau/n$, a sharper identity records the slopes of any actual nontrivial cycles:

$$
\lim_n\bigl(M_n(p_n,0)-M_n(p_n,1/n)\bigr)
=\sum_{m\in\mathcal P_{\rm cyc}}\frac1m\,2^{-\tau\alpha_{C(m)}},
\qquad \alpha_C=A_C/P_C.
$$

The right side is a finite positive measure's Laplace transform. Every nontrivial ordinary cycle has a permanently safe least phase, so contributes an atom; escape cancels from this difference without assuming an escape speed. The formula leaves the measure's vanishing undecided. [Boundary-layer proof](pointwise/FIRST_POWER_BOUNDARY_LAYER.md) · [independent review](../../reports/six-hour-20261127/INDEPENDENT_FIRST_POWER_LAYER_REVIEW.md).

## 7. Full physical floors and exact moment pressure

The unfiltered moment result extends to every real power and to an entire physical window above a fixed floor $H$. Define

$$
R_H=\max\left(3,\sup_{C:\min C>H}2^{A_C/P_C}\right),
\qquad R_H(z)=\begin{cases}R_H&z=0,\\3&z>0.\end{cases}
$$

The supremum is over actual positive odd cycles, with the empty contribution omitted. For each fixed $z\ge0$ and fixed real $p$, the exact exponent is

$$
\lim_n n^{-1}\log\mathbb E[
\mathbf1_{\{\min_{i\le n}x_i>H\}}Z_n(z)^p]
=\max(0,p-1)\log R_H(z).
$$

For a diverging floor $H_n$ with $n^{-1}\log_2H_n\to\alpha<\log_2 3$, it becomes
$\max(0,p-1)(\log_2 3-\alpha)\log2$. No assertion is made at the boundary $\alpha=\log_2 3$. The $p>1$ lower bound uses Inselmann's published full odd-clock density envelope, with its source and time range checked explicitly. The elementary upper and low-power estimates are recorded separately. These statements refine physical-floor dependence; the earlier terminal harmonic moment in Weaver's Paper 176 is prior work.

[Fixed physical floor](pointwise/HIGH_FLOOR_PRINCIPAL_PRESSURE.md) · [all remaining powers](pointwise/HIGH_FLOOR_REMAINING_POWERS.md) · [moving floor](pointwise/MOVING_FLOOR_PRINCIPAL_PRESSURE.md) · [fresh review](../../reports/six-hour-20261127/HIGH_FLOOR_PRESSURES_INDEPENDENT_AUDIT.md).

## 8. Genuine rational cycles can match every prescribed local limit

The statistical countermodels admit genuine positive primitive rational periodic closures, with only $O(\log n)$ extra bits after a prescribed length-$n$ prefix. The real starting phases can lie in a fixed compact positive interval. Their cyclic moving tests retain the sharp calendar scale, and their full reduced denominators satisfy $d_n=2^{n+o(n)}$. In fact that denominator statement holds simultaneously for every sublinear closing suffix whose resulting real phases remain bounded.

More strongly, fix a dyadic source in the constructed full-measure transcendental family. One can independently prescribe a positive real limit, a ternary unit limit, and integral limits at every prime at least five. The resulting primitive positive rational cycles approach that dyadic source and all the prescribed individual coordinates, retain polynomial peak height and the full denominator exponent, and eventually have no denominator factor at any *fixed* prime. The prime divisors of their growing denominators escape to infinity. This is coordinatewise local convergence, not a common positive integer or convergence in the restricted adelic topology.

The finite-place construction uses the translation by $1/4$ generated by the two branch orders modulo integers coprime to six. A separate ternary reset and a slowly growing irrational-rotation tuning word set the remaining targets. The denominator argument conditions on independent reference blocks and enumerates sparse adaptive edits; it never assumes those edits remain independent.

These are precise obstructions to proving integer termination from finite local compatibility, strong moving statistics, or the leading denominator exponent alone. The missing integer source or finer denominator control remains explicit.

[Compact true cycles](pointwise/COMPACT_POSITIVE_PERIODIC_SHADOWS.md) · [all short closures' full denominators](pointwise/FULL_DENOMINATOR_SHORT_CLOSURES.md) · [every local coordinate](pointwise/ALL_PLACE_PRIMITIVE_CYCLE_APPROXIMATION.md) · [independent reconstruction](../../reports/six-hour-20261127/INDEPENDENT_ALL_PLACE_CLOSURE_REVIEW.md).

## 9. The exact Lean proposal remains an ordinary all-source statement

Write $E_j(n)=\sum_{i<j}v_2(3U^i(n)+1)$. The existing Lean packet proves the equivalence between convergence of every positive odd source and

$$
\boxed{\forall n>0\text{ odd},\ \exists j,\quad 7j<4E_j(n).}
$$

Its complementary permanent-safe predicate is defined on the actual orbit, and every bad source reaches a permanently safe suffix within the explicit bit-length bound. The right-hand proposition is not assumed as an axiom and is not proved here. It is the remaining universal obligation.

[Ordinary equivalence](pointwise/PermanentSafeOrdinary.lean) · [bounded suffix clock](pointwise/PermanentSafeBitClock.lean) · [formal replay receipt](../../reports/six-hour-20261127/ROOT_LEAN_WAVE6.json).

The [root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE7.md) records the source identities, mathematical reconstructions, independent checks, subsequent extensions and current repository intake. Each criterion leaves its required vanishing or extinction estimate explicit.

The final [first-moment proposal](NEXT_FIRST_MOMENT_TARGET.md) makes a quantitative finite continuation-loss estimate explicit, proves its sufficiency while leaving its arithmetic bound open, and records a verified terminating-source obstruction to widening the gate toward slope two. It also states the separate numerator-discrepancy target for rational closures. These are proposed next obligations, not added universal conclusions.

# Checkpoint 9: complete integer fibres, physical coalescence and finite-memory barriers

This is the ninth checkpoint of the nine-hour pass ending on 28 November 2026 at 07:56:49 UTC. Its published parent is `42a7493a35ba43ae3f72f92e69d4b4cdee14b5a4`. Three GPT-6.2 Astra agents with ultra reasoning worked on separate tracks. The coordinator reconstructed the written arguments and reviewed every new finite formal interface before the aggregate replay.

**The Collatz conjecture remains unresolved.** The results below address complete ordinary endpoint fibres, genuine physical grade paths, the limits of randomized finite controllers, and uniform real-cap estimates at actual integers. Some assertions use named analytical inputs from the research repository or the cited papers. The exact Lean statements have narrower, explicit finite scopes.

## 1. Count every ordinary source sharing the same actual endpoint

Let `T` be the shortcut map, let `k_j(n)` count its odd departures through date `j`, and choose `n` uniformly from `[X,2X)`. For `2^N=o(X)`, let `K_j(n)` count **every** `m` in that same octave satisfying `T^j(m)=T^j(n)`. The [complete source-fibre theorem](../../research/astra-global-20261128/cycles/ORDINARY_SOURCE_FIBRES.md) gives, simultaneously for `j<=N`,

\[
 \log K_j(n)=j\log2-k_j(n)\log3+O_{\Pr}(\log N).
\]

For a fixed finite list of affine inputs `A_i n+b_i`, require the same `m` to preserve the entire endpoint vector. Its complete joint fibre instead satisfies

\[
 \log K_{\rm joint,j}(n)
    =j\log2-\max_i k_j(A_i n+b_i)\log3+O_{\Pr}(\log N).
\]

The lower bound counts the joint vector directly on its common affine line at each fixed grade tuple. Intersecting several separately large fibres would not prove it. Upper bounds come from the actual finite counted classes and their real displacement budget. The single-source argument uses elementary native arithmetic, binomial bounds and the usual fair-walk invariance principle. The independent Brownian statements for distinct nonsmooth multipliers use this pass's earlier pair joining theorem.

Write `a=log(4/3)/2` and `b=log(3)/2`. A typical joint fibre has logarithm `aN+o(N)`. Its centered path, divided by `sqrt(N)`, converges to `-b max_i B_i` for distinct nonsmooth base classes. In particular, when `sqrt(N)2^N=o(X)`, the conditional Shannon entropy of a second nonsmooth actual endpoint given the first is

\[
       \frac{\log3}{2\sqrt\pi}\sqrt N+o(\sqrt N).
\]

This is information about complete endpoint values on ordinary finite intervals. It is different from earlier real/ternary seed-fibre results, which are credited in the manuscript.

## 2. Physical paths join at the smooth-multiplier crossing

For inputs `A_i 3^{e_i} n+b_i`, normalize each fixed odd base by `3∤A_i`, suppose `e_i/sqrt(N)->u_i` and `log(2+|b_i|)=o(N)`, and retain the complete paths

\[
 Z_i^N(m/N)=\frac{2(e_i+k_m(A_i3^{e_i}n+b_i))-m}{\sqrt N}.
\]

The [path-valued theorem](../../research/astra-global-20261128/cycles/COALESCING_GRADE_PATHS.md) identifies their joint limit: independent systems of coalescing Brownian motions, one system for each common normalized base. Within a base, two particles join at their first meeting. Different bases remain independent through crossings. For Haar sources this holds on any fixed bounded physical horizon; for ordinary intervals through date `sN`, the stated transfer requires `2^{floor(sN)}=o(X)`.

The proof keeps native grade martingales, controls their covariance before first slope resonance, and then applies the published moving-translation synchronization bound on the fresh tail at that resonance. The integer state difference there has subexponential height. Thus genuine equal-state fusion follows in `o_Pr(N)` additional dates. Tightness controls the grade separation during that delay. A nonnegative limiting gap martingale identifies the resonance with the first Brownian meeting.

PR214 already gives the corresponding **scalar two-source merger probability**, with a stronger ordinary interval cutoff. This checkpoint credits that result. Its additional conclusion is the full finite-family path law and the coexistence of coalescing smooth classes with independent nonsmooth classes.

The separate [precritical pair-word theorem](../../research/astra-global-20261128/cycles/PRECRITICAL_PAIR_WORDS.md) reaches the full physical critical clock `log(X)/a`: every fixed pair of length-`k` parity words at nonsmooth affine ordinary sources has synchronous empirical frequency `4^{-k}`. A quantitative native line-incidence estimate survives successive physical rebasing epochs. This gives empirical pair words through that clock; it does **not** assert a joint Brownian limit beyond the direct binary horizon.

## 3. Rare ordinary grade tails and the geometry of fusion

The [tilted fusion note](../../research/astra-global-20261128/cycles/TILTED_FUSION.md) explicitly credits PR215's earlier general same-bias affine classification. Its ordinary conditional conclusion is that the intersection of simultaneous upper-grade tails, relative to one tail, tends to the mass of the greatest common submeasure of the affine tilted laws. For a smooth family this retains both the counted-fusion mass and the exact geometric overshoot factor. For a nonsmooth pair the coefficient vanishes. The moving nondecrease application uses the physical critical tilt and a stated logarithmic-form separation input.

The [translation-class theorem](../../research/astra-global-20261128/cycles/FUSION_GEOMETRY.md) also gives the following distinctions for nonfair bias `p`:

* The expected class occupancy in any integer interval of length `H` is at most `C H^γ`, where `γ=log_2(1+2sqrt(p(1-p)))<1`.
* Above `p=log_3(2)`, the entire integer-translation fusion class is finite almost surely. A finite real upper boundary and mass transport to its rightmost member prove this.
* In the separate range `H_binary(p)>p log(3)`, the class is infinite with exponential finite-stage growth.
* An exact near-critical grade bridge admits an exponential moving-displacement synchronization bound with denominator `log(2+|h|)+|k-t log_3(2)|+t^{2/3}`.

The gap between the two finite/infinite regimes remains open. These generic conditional laws do not determine the fate of a specified exceptional integer.

## 4. Actual endpoint entropy measures the escaping population

For `U_X` uniform in `{1,...,X}`, let `I_t=-log Pr(T^t(U_X)=T^t(U_X)_{sampled})` denote the sampled endpoint self-information. With `L=log X` and `mu=1/a`, the [terminal information theorem](../../research/astra-global-20261128/cycles/TERMINAL_INFORMATION.md) proves at `t=mu L+u sqrt(L)+o(sqrt(L))`

\[
 I_t/\sqrt L\ \Longrightarrow\ (b\sqrt\mu\,G-au)_+.
\]

The expectations converge too. At every tested time later than the critical clock by a quantity whose ratio to `sqrt(L log L)` tends to infinity,

\[
       \frac{H(T^t(U_X))}{\tfrac12\log\log X}\longrightarrow d_E,
\]

where `d_E` is the total escaping-component density. No upper restriction on that late date is required. The proof uses PR215's stopped native law and PR213's nonperiodic atom bound and periodic total-variation law. A new integrated self-information tail bound provides uniform integrability. It does not infer entropy continuity from a small total-variation error on a growing support.

Consequently, an **independently proved** `o(log log X)` entropy upper bound at the ordinary date `(log X)^2` would exclude escapes, using positive predecessor density for every component. That upper bound has not been established. The equality above identifies a concrete unresolved ordinary statistic, rather than removing its possible escaping contribution.

## 5. Finite hidden memory cannot track the inverse optimum

The [stochastic controller theorem](../../research/astra-global-20261128/broad/STOCHASTIC_CONTROLLER_REGRET.md) extends the previous deterministic result. A controller sees `W` ternary digits and has `M` internal states, with a time-homogeneous kernel and fresh conditional randomization. For almost every original geometric source of any mean `1<b<=a_*`, its probability of tracking the unrestricted native optimum within a sufficiently small linear cost error is exponentially small. The supremum includes all such kernels and initial states, chosen separately for each supplied source and horizon.

The uniform finite-state mechanism is elementary. A native packet forces `M` repeated gap-one decisions at the same observed row, followed by a gap-five decision at that row. If `A` is the substochastic hidden transition for one and `v<=1-A1` is the exit probability vector, then

\[
                  (M+1)\lambda A^M v\le M.
\]

A word probability envelope multiplies this loss over disjoint packets. A Rényi source bound and Borel–Cantelli then cover the uncountable family of controller parameters at once. The proof also covers finite-dimensional quantum internal memory with classical rows and outputs: positivity and a telescoping exit-effect inequality give the same bound. It assumes no persistent ancillary memory outside the stated dimension.

Below and at the real-drift threshold `b=log_2(3)`, the resources may grow logarithmically with the horizon under the explicit packet-rate condition, with stretched-exponential success bounds. Ordinary integer representatives have the full dimension exponent `H(b)/log(3)` at all tested depths. The unrestricted stationary inverse optimum itself remains unknown.

The [inverse-overlap criterion](../../research/astra-global-20261128/broad/CRITICAL_OVERLAP_AND_ROUTING.md) supplies a direct positive target. For the original tilted source versus additive ternary Haar overlap `O_j(b)`, if `b<L`, where `L` is the unrestricted optimum, then

\[
 \limsup_N\frac{\sum_{j\le N}O_j(b)}{\log N}
        \le\frac{2}{3D(\mathrm{Geom}(L)\Vert\mathrm{Geom}(b))}.
\]

Divergence of the left side at `b=a_*` would settle `L=a_*`. Exact common-clock route and posterior-entropy identities expose two other sufficient tests. None of those asymptotic tests is proved here. An exact, untruncated finite geometric recurrence does certify `O_7(a_*)>0.33384`; a single finite depth cannot resolve the criterion.

The [native translation note](../../research/astra-global-20261128/broad/NATIVE_TRANSLATION_SINGULARITY.md) retains explicit priority for PR215's qualitative affine classification and logarithmic steering. Its additional finite-scale interface includes a physical word representation for all integer-affine maps and overlap bounds from the source ambiguity `E_N`, with `E_N=O(log N)` below `b=log_2(3)` and `O(sqrt N)` at that real threshold. The entropy-critical mean `a_*` is larger; no critical rate strong enough to settle the optimum is asserted.

## 6. More slow terminating integers in every large octave

Using Wren's published width-22 integer slack and the published stationary transfer, [the ordinary octave theorem](../../research/astra-global-20261128/broad/SLOW_TERMINATING_OCTAVES.md) gives, for every sufficiently large `X`, at least:

| Terminating integers in `[X,2X)` | Shortcut stopping-time lower bound |
| --- | --- |
| `X^(1/4750)` | `tau(m)>14.92 log m` |
| `X^(1/950)` | `tau(m)>14.9 log m` |

The local calculation retains the full binary entropy of a rare alternate action and uses the already published slack to strengthen the same certified policy slope. It imports the giant all-row certificate; that certificate was **not** regenerated in this pass. The exact rational control checks all 48 reduced row/baseline choices and both strict coefficient/count pairs. This is a comparison with the specific cited transfer and its printed parameters, not a claim to a global record or an effective first octave.

## 7. Compact real divergence and genuine integer protection

The [compact real divergence construction](../../research/astra-global-20261128/escape/COMPACT_REAL_DIVERGENCE.md) proves infinite essential supremum in every open ternary unit cylinder for every nonempty real open restriction, despite the published finite `L^q` bounds. On one dense Haar-null `G_delta`, finite rows diverge for all these restrictions and for every exact central clock in `|d-2n|<=c sqrt(n)`, `c<2`. The simultaneous small-cap divergence locus has Hausdorff dimension at least `H_2(log_3(2))=0.949955...` in every unit ball. The proof uses retained real-and-clock floors and prefix-free side exits of critical continuations.

It also constructs genuine integer first-landing spikes at arbitrarily small relative real correction. Direct parents of any specified odd unit can be chosen. Thus even the known minimum-one population has unbounded upper linear density at zero. An escape would impose a different requirement: the [minimum endpoint theorem](../../research/astra-global-20261128/escape/NATIVE_MINIMUM_ENDPOINT.md) forces a lower bound `c t log(1/t)` at **every** sufficiently small scale, additive over any finite set of escaping components. A separating upper subsequence has not been proved. Finite first moment of the limiting ordinary minimum law is equivalent to all positive trajectories entering finitely many cycles; the needed finite moment is also open.

At actual odd integer targets, the [common-landing cap theorem](../../research/astra-global-20261128/escape/COMMON_LANDING_CAP.md) gives a uniform bound over **all finite depths**. After dividing by the target and correcting for periodic laps, a row with absolute intercept at most `B<=y/2` is bounded by the mass of one specified genuine landing label at any floor `M<=y/[12(1+B)]`. The resulting power bound is uniform in depth. An antichain version allows summing separately optimized depths and controls the low-relative-cap contribution of all genuine escaping last exits.

For arbitrary finite real windows, a finite family of unit-origin inverse words is dominated by its true stationary fibre after enlarging each window at that word's own multiplier scale. This extends the stationary interval modulus to truncated finite rows; small inverse origins remain an explicit obstruction. None of these low-cap or truncated bounds controls the full macroscopic escaping contribution.

## 8. Formal scope, independent review and reproduction

Four new Lean modules have complete local source review:

| Module | Kernel-checked finite content |
| --- | --- |
| [NativeSourceFibre.lean](../../research/astra-global-20261128/cycles/NativeSourceFibre.lean) | Actual quotient identity, low endpoint range, common high quotient, complete counted-fibre equivalence and simultaneous affine-list lifting. |
| [HiddenWaitingPacket.lean](../../research/astra-global-20261128/broad/HiddenWaitingPacket.lean) | Substochastic exit mass and `(n+1)p<=M` over a linearly ordered field. The quantum and asymptotic source arguments remain written. |
| [TranslationWords.lean](../../research/astra-global-20261128/broad/TranslationWords.lean) | Same-length physical Boolean-word representations of every integer shift and `3^m x+d`. It does not formalize measure singularity or positive branch legality. |
| [NativeMarkedLeaves.lean](../../research/astra-global-20261128/escape/NativeMarkedLeaves.lean) | Every actual departure factor bounds total survival, small intercept excludes low departures, nonunit promotion preserves odd landing, and the exact quarter-slope intercept identity. |

The aggregate receipt records a fresh strict build with the pinned Lean 4.34.1 and Mathlib checkout, and audits every local declaration, including private declarations, against the allowed axioms `propext`, `Classical.choice`, and `Quot.sound`. The bounded replay reruns every exact finite control both normally and with Python optimization, comparing outputs. Runtime guards remain active in both modes. The integrity validator and exact published-tree receipts are separate from the mathematical review.

The [review ledger](CHECKPOINT_09_REVIEW.json), [Lean receipt](CHECKPOINT_09_LEAN.json), [bounded receipt](CHECKPOINT_09_BOUNDED.json), and [integrity receipt](CHECKPOINT_09_INTEGRITY.json) give the frozen scope and hashes. The [frontier refresh](../../research/astra-global-20261128/broad/FRONTIER_20261128_0530.md) records which concurrent work has priority and which recent claims were only inspected at abstract or PR-description level. The larger polynomial-offset and signed-rational attempts remain outside this checkpoint until their independent reviews are complete.

### Frozen replay results

The fresh aggregate completed from 05:44:13 to 05:47:32 UTC on 28 November: **54 Lean modules and 1,525 declarations, including 273 private declarations**, all within the three allowed standard axioms. All **37 finite Python programs passed in 74 normal/optimized runs**, with identical paired outputs. The review ledger hashes **201 scientific source files** and records coordinator review of **107 Markdown sources**. Previously checked, unchanged C++ controls retain their earlier receipts; no new C++ result is claimed here.

The scientific freeze is local commit `62e516ef609a9efc69ebfdf6267e73230fe54ada`, tree `4a8023c5520ddf89351ccb1b905089c52abd5799`. The integrity receipt passed all eleven selected structural and bounded regression commands against that clean freeze. Publication adds this receipt and records the resulting exact remote tree separately.

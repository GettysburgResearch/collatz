# Research handoff — 27 November 2026

**Collatz is unresolved.** The requested six-hour pass produced a connected native formal foundation, stronger written cycle restrictions, physical collision laws, and a shorter source-compression clock. None of these proves that every positive integer reaches one. The [claim guide](../../research/astra-diagonal-frontier-20261127/README.md) and [coordinating review](REVIEW.md) give the full statements, qualifications and checks.

The working map is the shortcut map: halve an even input and send an odd input to `(3x+1)/2`. Odd acceleration is used only where explicitly stated. Native time and the number of odd departures remain separate. Main was pinned at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The intake inventoried 146 open PR heads; this was complete metadata coverage, not a claim to have independently checked every historical proof. Three GPT-6.2 Astra agents at ultra reasoning developed the source-mass, cycle-arithmetic and descent directions, with coordinating reconstruction and cross-lane review.

## The strongest results to preserve

### 1. An exact criterion connected to ordinary integers

The [native packet](../../research/astra-diagonal-frontier-20261127/NATIVE_GATE.md) proves the complete source budget

\[
J_N+V_N+\sum_{k<N}D_k\le9,
\qquad V_k\le48(99/100)^k.
\]

All sets, births, deaths and weights are defined on actual positive integers. The mass `J_k` converges to the reciprocal mass `R` of the permanently passing ordinary sources. The formal criterion says that for every positive `L` there is a finite row with `L≤2^k` and `J_k<1/L` if and only if Collatz holds. Such a row certifies all inputs through `L`. The reserve controls future arrivals above an old source cutoff. It does not give a time by which every old temporary source must leave.

The unsupported assertion is exactly `R=0`, or existence of all those finite certificates. A computable decreasing upper envelope is already available. Constructing another upper envelope without forcing its limit to zero does not close this obligation.

### 2. Cycle width and the lifetime of each reference component

The [width theorem](../../research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE.md) gives `liminf X/s≥3` along any unbounded family of primitive positive ordinary cycles. Here `s` and `X` are the least and greatest odd phases. All native valuations are allowed. Its [rate](../../research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE_RATE.md) bounds the deficit to three by a sixth root of an explicit height/period discrepancy estimate. The constants and finite threshold are unevaluated.

The central device is an integer stencil with a zero of order six and positive coefficient mass six. The exact rank calendar forces either a forbidden interval of zero sixth differences or height at least a constant times the sixth power of the period. The published BLS logarithmic-form bound gives the incompatible power `5.116201`. The scalar polynomial and calendar steps have formal kernels; the full asymptotic argument remains a reviewed written deduction with its published input.

The [upper bundle](../../research/astra-diagonal-frontier-20261127/arithmetic/UPPER_BUNDLE.md) forces one exact reference rotation at every cutoff `(X+1)/2≤N≤4s−1`. The [component-lifetime theorem](../../research/astra-diagonal-frontier-20261127/arithmetic/PLATEAU_COMPONENTS.md) computes the exact birth/death interval `[M_R,B_R)` of an unchanged reference orbit and proves `limsup B_R/M_R≤2`. A separate entropy argument gives the stricter endpoint limitation for a component carrying the particular ordinary clock.

These are restrictions on individual components. A full rotation plateau can persist while its components change. The ordinary successor construction itself supplies many such replacements. Counting all `p` vertices of each replacement as new would be incorrect: consecutive components share `p−1` vertices. Natural angular and integer budgets can pay for those replacements. The complete-plateau exclusion is still missing.

### 3. A finite collision statistic that detects escaping charge

The source-qualified [square and cubic spectra](../../research/astra-diagonal-frontier-20261127/mass/SLOW_SOURCE_CHARGE_SPECTRUM.md) identify the critical growth coefficients of physical first-arrival collisions with the corresponding escaping-component moments. The [first-merge law](../../research/astra-diagonal-frontier-20261127/mass/FIRST_MERGE_CHARGE.md) disintegrates this energy over the first actual common vertex, retaining its future survival product.

The [premerge theorem](../../research/astra-diagonal-frontier-20261127/mass/PREMERGE_TIGHTNESS.md) proves total-variation tightness on those ordinary vertices before checking their shared future. It includes periodic targets with exactly one primitive-lap correction. Its finite statistic `B_q(X,T)` uses only ordinary forward iteration and exact rational weights. For `q=2,3` and every prescribed integer schedule `T(X)→∞`,

\[
\frac{B_q(X,T(X))}{b_q(X)}
\longrightarrow c_q\sum_{C\ \mathrm{escaping}}H_C^q,
\]

where `b_2(X)=sqrt(log X)` and `b_3(X)=log log X`. Total variation before the future makes the error uniform in the additional clock. Thus even a double-logarithmic postmerge schedule works. This is a two-sided asymptotic, with no effective error modulus or certified finite-height upper bound.

The remaining ordinary root is not discarded by this reduction. On a hypothetical escaping root its infinite survival product is positive. An independent upper saving for this particular physical statistic would be consequential; the packet identifies it but does not prove it.

### 4. Compression at a linear logarithmic deadline

Under Paper 92 version 1's canonical real-source concentration estimate, the [compression proof](../../research/astra-diagonal-frontier-20261127/linear/linear_clock_compression.md) gives

\[
G_{10^7\lceil\log_2 H\rceil}(H)
\le K H^{H_2(\log_3 2)-0.000006}.
\]

`G` counts distinct pairs of actual endpoint and accumulated odd count from an arbitrary translated interval of `H` original sources. The prior result with this exponent used the square of the logarithmic clock. Widening the high-count threshold gives a fixed proportional shrinkage in each remaining image interval's logarithmic length, so the recursion fits a linear logarithmic deadline. The exponent and clock constant are explicit; `K` and the onset are ineffective. Root and mass lane independently checked the deduction against the primary inputs.

The result preserves the least member of every occupied synchronized row. It does not force that particular member to acquire a smaller partner.

## Controls that a future closing argument must survive

The [terminating grade classification](../../research/astra-diagonal-frontier-20261127/linear/terminating_synchronized_grades.md) is exact: for inputs with furnished visits to one, equality of `N−2J` is equivalent to eventually sharing both the native clock and odd count. Both directions are formally connected to the actual map. Under the stated exact-total floor, unbounded odd terminating sources have no smaller synchronized partner at any time. For the elementary example 27, the first-hit clocks are `(70,41)`, so its grade is `−12`; every smaller positive has grade between zero and four.

The [unit shielding reconstruction](../../research/astra-diagonal-frontier-20261127/linear/unequal_clock_shield.md) concerns a prior result, credited to PR146 at `f431078244e868dc699fad011044f0d5e7f76437` and its formalization in PR211. If `x≡−1 mod 2^k` and `x≡1 mod 3^h`, any smaller visitor to its `i`th initial endpoint needs more than `i+h` odd departures, regardless of its native clock. The alternative proof and exact terminating controls here are not a novelty claim. The final source refresh caught and corrected this attribution before publication.

The genuine merge `13,53→5` also prevents a universal vanishing estimate based only on incoming branches. To distinguish escape, a proposed bound must control what happens after those branches have merged.

## The next precise obligations

| Route | Sufficient missing result | Boundary already established |
|---|---|---|
| Native mass | Force `J_k` below every prescribed reciprocal threshold, equivalently `R=0`. | The arrival reserve and source-cutoff error are exponentially small, but old ordinary atoms remain. |
| Physical collision energy | Prove an independent saving below the identified square or cubic growth scale. | Premerge roots are tight and source marks are controlled; their shared ordinary future is retained. |
| Unequal-clock descent | Produce an actual smaller source in at least one eligible lower corrected-height row of a supplied minimal component. | For an escaping base `b`, deleting `h` odd and `ell` native steps gives corrected height `P(b)3^h2^(-ell)`. The useful cone is `(log₂3)h<ell<2h`, with this height below `b`. Following the observation farther leaves that height fixed. Large-height moving-root asymptotics do not assert occupancy of this particular cell. |
| Complete cycles | Exclude the full same-rotation plateau, or obtain another complete-denominator contradiction. | Individual components have short lifetimes, but can be replaced. A partial factor or a rational positive word is not an integer cycle exclusion. |

No additional runtime, routine test or unperformed finite census is being represented as the missing step. These are mathematical assertions about every fixed ordinary source or every complete ordinary cycle.

## Evidence and final source scope

The [closing manifest](checkpoint7/CUMULATIVE_VERIFICATION.json) covers **22 Lean modules, 172 public theorem roots and 28 registered finite checkers**. It checks all current source and receipt hashes and all supplied frozen outputs. Evidence is cumulative; unchanged earlier proofs and expensive controls were not rerun simply to change their date. Lean 4.34.1 uses warnings as errors and disabled implicit parameters. Its audited roots use only `propext`, `Classical.choice` and `Quot.sound`. Mathlib objects were reused from the pinned source; no cold dependency rebuild or independent LeanChecker run is claimed.

The [final source refresh](FINAL_SOURCE_REFRESH.json) records the unchanged main pin, later PR211 and PR212 heads, the full guide reads, and the exact prior shield source. Their latest reported formal counts are not imported into this packet. Clean repository validation and exact remote tree comparison are separate publication checks and do not verify mathematics.

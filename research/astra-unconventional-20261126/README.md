# Three attacks on the ordinary arithmetic boundary

**Research checkpoint, 26 November 2026. Universal Collatz termination remains OPEN.** This packet starts from the complete PR 193 tree at `4cc06e7d8fdec923eed73a26b1e9d680c9f701d1` and the current scientific heads recorded in the [intake](../../reports/astra-unconventional-20261126/PR_INTAKE.json). Its purpose is to attack the common missing arithmetic condition with different tools: simultaneous digit windows and point spacing, real and nonarchimedean boundaries, and positive inverse-transfer measures. Three GPT-6.2 Astra agents developed the attacks in parallel; the coordinating agent reconstructed the new arguments and built the formal kernels independently.

The shortcut map is $T(n)=n/2$ on even inputs and $T(n)=(3n+1)/2$ on odd inputs. The odd map strips the full power of two from $3n+1$. Physical clocks, odd clocks, folded ranks, and inverse-word lengths are explicitly distinguished in the individual proofs. None of the conclusions below is an unconditional proof of termination.

**Closing proposal:** [CLOSING_PROPOSAL.md](CLOSING_PROPOSAL.md) gives the exact escape statistic, its fixed modulus-eight cancellation target, the surviving cycle obligation, and the boundary of the Lean verification. The final transfer attack is developed in [COLLISION_SOURCE.md](boundary/COLLISION_SOURCE.md) and [DYADIC_INCREMENT.md](arithmetic/DYADIC_INCREMENT.md). These retain the actual ordinary sources and the distinct-parent terms. [SMALL_SIGNED_CARRY.md](arithmetic/SMALL_SIGNED_CARRY.md) gives a nonzero polylogarithmic signed carry for the bounded candidate family.

## Results to read first

### Holonomic rigidity on the full finite-exponent graph

The final algebraic attack uses every ordinary odd division exponent through an arbitrary finite ceiling $E$. In the coordinate $t=(x-1)/2$, the exact branch is $2^e v+r_e\mapsto3v+d_e$, with the residues given in [ALL_GAPS_MAHLER.md](arithmetic/ALL_GAPS_MAHLER.md). A circulation has one generating series $C_e$ per edge type and satisfies

$$
\sum_{e=1}^E X^{r_e}C_e(X^{2^e})
=\sum_{e=1}^E X^{d_e}C_e(X^3).
$$

Every ternary coefficient section of depth $k$ is a finite sum of binary sections of depths between $k$ and $Ek$. This includes cancellations between different incoming branches and is checked in Lean. A finite-pole argument proves that every rational solution is polynomial over every field. In characteristic zero, the Adamczewski–Bell theorem gives the same conclusion for a finite-dimensional binary section span.

[HOLONOMIC_RIGIDITY.md](arithmetic/HOLONOMIC_RIGIDITY.md) proves the stronger written result: **every formal complex D-finite solution is polynomial**, even with arbitrary signed coefficients and without assuming convergence at the origin. Levelt–Turrittin slopes cannot persist under both section scales: a positive slope would repeatedly require $s/3^k=t/2^l$ inside a fixed finite set. Regular singularity then gives convergence. Actual singularities of all continuations similarly become odd-order roots of unity; a missing dyadic cylinder eliminates them. The argument at infinity gives polynomial growth. The resulting polynomial flows are exactly finite sums of actual cycle indicators.

The weighted version permits fixed nonzero incoming and outgoing factors. A finite cycle contributes precisely when its product of weight ratios is one. At the ratios $3/2^e$ the homogeneous holonomic kernel vanishes. Multiplying an unweighted cycle by its height introduces an inhomogeneous carry, so this spectral statement does not eliminate the original cycle. **Which nontrivial polynomial cycle indicators exist remains open.** The [two-branch analysis](arithmetic/MIXED_MAHLER.md) also records automaticity, the exact polynomial incidence equation and the obstruction to a universal bounded-offset descent.

### Ordinary exclusion of periodic boundary patterns

For an invariant Boolean label on positive integers, an opposite-colored adjacent pair has exactly one opposite-colored dyadic child. Following it gives a persistent real boundary, with the same two ordinary colors at every resolution. [DYADIC_BOUNDARY.md](global/DYADIC_BOUNDARY.md) derives exact digit restrictions and proves why multiplication by $3/2$ can destroy persistence and create new boundaries. Taking a closure does not repair that failure of invariance.

[PAIRED_BOUNDARY.md](boundary/PAIRED_BOUNDARY.md) supplies an ordinary realization argument beyond finite local tests. At a rational boundary, compare its two sides at different dyadic levels chosen to have the same odd-step count along their signed rational references. If each reference enters a nonzero cycle, the resulting genuine positive pair has fixed separation and a common center $B+C3^{m\Delta}$. This sequence is dense in a dyadic open coset and therefore meets a finite counted-fusion cylinder from the cited full-measure synchronization theorem. Opposite ordinary colors are impossible.

The same argument bounds repetitions of each such periodic word after a bit breaking its left continuation, and excludes it from a boundary's shift limit set. The worked word $01010111$ survives all universal finite counted-fusion tests on its rational references, yet the ordinary argument excludes it. A separate exact certificate bounds its repetitions after a break by 819188 using 32 fusion cosets at precision at most 24; this worked exclusion uses the finite certificate in place of the general full-measure input.

The remaining rational cases include dyadic and eventually alternating boundaries, as well as signed references which are unbounded. [ZERO_ARM.md](global/ZERO_ARM.md) shows that a dyadic or alternating boundary would force the color of $3^j p$ to differ from that of its fixed positive ordinary anchor $p$ for density-one exponents $j$. It also derives the isolated-center behavior after dyadic magnification. Fixed-gap fusion does not prove a return to the anchor's color. Genuinely aperiodic boundaries remain unexcluded.

### One ordinary cycle, simultaneous binary and ternary windows

[The joint-window proof](arithmetic/README.md) retains every phase of a putative ordinary cycle on the bounded least-tripling-disagreement branch. Let $p$ be its primitive odd period, $s$ its minimum, and $Z_j=2^{2-k_j}x_j$ its integer folded mantissas. For every fixed ε,θ>0, every chronological interval of at least $p^θ$ phases, and independently chosen powers

$$
p^ε\le q=2^a,\ r=3^b\le s/p^ε,
$$

the joint windows $(\{Z_j/q\},\{Z_j/r\})$ tend to Haar measure on the two-torus. The product $qr$ may exceed $s$; the two arrays are read from the same integer at the same time. There is no restriction on the octave mask. For the original odd values the limiting density is at most three, because the band choice can depend on the windows.

The key is an exact amplitude recurrence with variation at most $8/3$ per chronological step. Small-return segments of the rational rank rotation then reduce the Fourier characters to smooth exponential phases. Fixed logarithmic-form bounds and an explicit high-derivative estimate give uniform cancellation. This is a proposed written theorem with the finite amplitude algebra checked in Lean. The bottom binary and ternary digits remain outside its conclusion.

[The inverse-curve argument](arithmetic/INVERSE_WRAP.md) goes further than weak equidistribution. It bounds coincidences of exact integer residues using a positive Fejér kernel and the second derivative of an inverse exponential curve. With $d$ the **complete reduced denominator** of an ordered rational candidate, it gives

$$
d\max\{p^2,s/p^{1/3}\}\gg p^{1000/479}.
$$

For the actual ordinary branch, $d=1$, hence

$$
s\gg p^{1000/479+1/3}.
$$

This combines a new spacing estimate with PR 200's pinned all-depth incoming-word count. The denominator is $d=(2^h-3^p)/\gcd(2^h-3^p,C)$; no selected-factor substitution occurs. The remaining target is a pointwise pair-count estimate over the entire admissible amplitude range. The argument currently controls the range up to $R=O(p^{1/3})$, while the remaining height ceiling allows much larger amplitudes.

### Two moving arithmetic centers, with a uniform separation cost

[The moving-center theorem](arithmetic/MOVING_CENTERS.md) applies the Subspace Theorem to finitely many *fixed* systems of the forms $X,Y,X-Y$. For a fixed finite prime set $S$, write $[n]_S$ for its prime-supported part and $H_S(n)=|n|/[n]_S$. It gives, for arbitrary nonzero $A,B,A-B$,

$$
[\operatorname{lcm}(|A|,|B|)]_S
\ll_{S,\varepsilon}\max(|A|,|B|)^\varepsilon\min(|A|,|B|)H_S(A-B).
$$

After primitive gcd reduction the exceptional rational lines contain only finitely many possible vectors, so the constant is uniform even as both centers move. At an actual ordinary junction this couples the incoming ternary clock and outgoing binary clock; the cost is the prime-to-six part of the separation of their centers. No moving-target version of the Subspace Theorem is assumed.

An adjacent exchange of gaps 1 and 2 changes exactly one carry summand, so the separation is an S-unit, regardless of the rest of the word. Consequently two consecutive equal-clock blocks differing by a single adjacent swap cannot be longer than $(1+o(1))\log_3 s$ on the bounded ordinary branch. The result retains an arbitrary background word and all prime powers. It does not show that every candidate must contain such long near-repetitions.

[The phase-pair extension](arithmetic/PHASE_PAIR_MASS.md) applies to every pair of ranks, including either lifted seam. Write $G_i$ for their positive lifted integer gap and $J_i$ for their signed mark discrepancy. Their exact recurrence is $2^{b_i}G_{i+1}=3G_i+J_i$. Partition the discrepancies into any fixed number of arbitrary groups and let $Y_I=\sum_{i\in I}2^{B_i}J_i/3^{i+1}$. The finite-place Subspace Theorem gives the uniform constraint

$$
2^{B_n+v_2(G_n)}3^{v_3(G_0)}
\le e^{\epsilon(n+\log p)}G_0\prod_I H_{\{2,3\}}(Y_I).
$$

The rank-spacing estimate makes the initial gap dominate every partial discrepancy sum. That fact removes exceptional subspaces one coordinate at a time. In particular, if all nonzero discrepancies occupy a fixed number of intervals and the comparison is longer than a logarithmic window, those intervals must occupy almost the entire window. Frequent scattered discrepancies still satisfy the bound.

[The spatial-window consequence](arithmetic/SPATIAL_WINDOWS.md) promotes the averaged window law to a statement about most individual phases: sample independently from any two growing contiguous intervals of admissible binary and ternary digit positions. On all but a vanishing fraction of phases in any polynomial-length chronological interval, that integer's positional empirical law tends to product Haar. It is also asymptotically independent of every depth-independent phase mark. The proof uses extremality of Haar among jointly invariant measures. It does not supply independence at one fixed depth or at the bottom digits.

[The two-residue circuit theorem](arithmetic/RESIDUE_CIRCUITS.md) uses the low counts of allowed binary and ternary residue classes as a bipartite graph. For two moduli of size about $p^{31/15}$ it produces $p-O(p^{199/200})$ independent integer relations, each of coefficient norm at most 1000, which vanish on the actual cycle heights and are separately balanced in every marked residue class at both primes. A small integer-quotient pigeonhole step retains exact equality even when the product of the moduli is below the height. The resulting near-relations on the ideal exponential rank curve are insufficient on their own: explicit finite-difference polynomials give almost as many independent small forms. The unresolved inference must use the two exact residue balances as well.

### The real boundary is wide; the joint arithmetic boundary is structured

[The record entrance proof](boundary/RECORD_ENTRANCE.md) treats the full alphabet of strict record blocks of bounded length $J$. Its unrestricted real future is an interval, and its real and ternary two-sided boundary is a full product. Thus a proposed exclusion based on a thin real projection would fail. The real and binary coordinates instead share the *same* future word. Their joint graph has an exact dimension obtained from algebraic separation and Hochman's entropy theorem, with the pressure and separation hypotheses stated in the proof.

For $J=2$, the ordinary endpoint $n=6t-1$ has precisely two allowed record moves:

$$
2u\longmapsto3u,\qquad 8u+7\longmapsto9u+8.
$$

These are exact arithmetic rules, with disjoint forward domains and inverse images. The binary and ternary marginal dimensions add to approximately $0.989481<1$. That inequality alone does not exclude an ordinary integer. A separate Diophantine argument applies the Bugeaud–Evertse–Győry theorem to the same integer at a switch: after $a$ copies of the first move and before $b$ copies of the second,

$$
3^a2^{3b}\le t^{1+ε}
$$

for all sufficiently large such junctions. There is an analogous reverse-switch estimate and an extension to each fixed pair of periodic macro words. Uniform short-run aperiodic scripts are still allowed by these inequalities.

[The all-record extension](boundary/ALL_RECORDS.md) removes the bound on record-block length: the full binary entrance set has dimension $θ=H_2(1/\log_2 3)$ and zero Hausdorff measure at that dimension. Its joint real–binary graph has dimension $1+θ$, again with zero measure at the critical dimension, and every actual ordinary escape enters this graph with its own source and clocks. The covering cost loses a fixed factor at each completed record. Turning that loss into ordinary exclusion still requires control of the possibly unbounded time before the next record.

[The strip argument](boundary/STRIP_ENTROPY.md) proves that an injective shortcut segment confined to $[X,3^{1+η}X]$, $0\leη\le1$, has at most $X^{η+o(1)}$ states. Any limiting parity process from polynomially long confined segments has a measurable irrational eigenvalue. The actual bounded cycle strip is too wide to infer subpower length from this result.

[The component measure](boundary/TILTED_TRACE.md) adds a real coordinate to the earlier scalar trace. It gives a finite purely atomic measure whose individual atoms recover every ordinary unit source in an escaping component. Both scalar tilted criteria in the beginning of that file are **prior PR 192 work**, explicitly identified by full commit and path. Their singular expectation has not been bounded here.

### Finite inverse-transfer measures and the exact ordinary support condition

[The operator proof](global/README.md) considers

$$
L_s f(z)=2^{-s}f(2z)+(3/2)^s1_{z\equiv2\pmod3}f((2z-1)/3).
$$

It constructs continuum many mutually singular, finite, purely atomic positive fixed measures of $L_s^*$, simultaneously for every $s>1$, on nonrational ternary points. A negative ordinary shadow supplies a polynomial estimate on the side branches of an expanding all-odd spine. The construction can retain actual binary parity, integral coordinates at every prime, and a positive locally finite real coordinate with the expected power-law atom sizes. Consequently these local properties cannot, by themselves, eliminate an escaping ordinary component.

The same proof classifies **all** finite positive fixed measures supported on positive ordinary integers: each escaping component contributes exactly one positive ray, proportional to its corrected-height weight $P(n)^{-s}$; eventually periodic components contribute zero. The corrected-height construction is prior project work, cited at its frozen source.

A sharper recognition statement needs only the binary coordinate. If a finite fixed measure assigns positive mass to a fiber with an eventually-zero positive binary expansion, its projected ordinary orbit is injective and escapes. The other coordinates may be diffuse. Conversely an escaping ordinary orbit gives such a measure. The shifted identity

$$
Tn+\tfrac12=a_n(n+\tfrac12)+\tfrac14
$$

produces a strictly increasing score and is formalized in Lean. Excluding these particular fibers, rather than all ternary or adelic fixed measures, is the outstanding measure-theoretic target. It would address escape; nontrivial positive cycles require a separate exclusion.

### An exact posterior and the moving-target onset law

[The posterior theorem](global/POSTERIOR.md) retains one fixed positive odd source $m$, its actual odd orbit $y_k$, and its actual valuation sum $A_k(m)$. Let $p_k$ be the ternary residue law of independent geometric exponents. Under the cited uniform finite-residue atom floor, the reciprocal posterior

$$
R_k(m)=2^{A_k(m)}p_k(y_k\bmod3^k)
$$

increases to a finite limit if $m$ escapes, and grows exponentially if $m$ is eventually periodic. In the escaping case the limit is $P(m)Z_0$, where $Z_0$ is the reciprocal corrected-height mass of the whole synchronous ordinary class. The conditional source laws converge in total variation to an explicitly given countable distribution. On infinite geometric word space that distribution is singular, with a mean-one likelihood martingale tending to zero almost surely. Thus the proof identifies precisely why a typical-word argument does not control the retained ordinary word.

[The trace-profile theorem](boundary/TRACE_PROFILE.md) gives more than a fixed-index posterior. Let $a_n$ be one hypothetical escaping odd unit ray, $Z_v$ its full grade masses, and $\rho_k=3^kp_k$. The ordinary predecessor density inputs give

$$
\sup_{k\ge0}\left|\frac{\rho_k(a_n)}{P(a_n)}-Z_{n-k}\right|\longrightarrow0 .
$$

The approximation is uniform over **every depth**, including depths moving with the target. It uses antichains of ordinary sources and the density of branches that join the ray later. The future masses satisfy $Z_v\to0$ as $v\to+\infty$. The fixed-integer trace supplies a positive past Cesàro limit $H$, with $h(a_n)/P(a_n)\to H$. Consequently, for every fixed $\lambda>0$,

$$
\frac{1}{h(a_n)\lfloor\lambda n\rfloor}
\sum_{k=1}^{\lfloor\lambda n\rfloor}\rho_k(a_n)
\longrightarrow (1-1/\lambda)_+ .
$$

The onset clock is the actual odd travel time from the original ordinary source. The stronger fixed-target absolute Cesàro theorem also yields a Bernoulli limit for the normalized individual trace values when depth is sampled uniformly over this interval. Weaver's ordinary-depth fixed-target convergence strengthens the past-grade Cesàro limit to $Z_v\to H$ as $v\to-\infty$: every moving offset with $k-n\to+\infty$ has normalized trace tending to one, and every offset with $n-k\to+\infty$ has limit zero. These are source-qualified written deductions.

[The collision-energy theorem](global/COLLISION_ENERGY.md) sums over every positive odd representative at depth $k$, retaining the original geometric exponent law. For first-hit weights $L_k$ and every fixed $r>1$ it proves

$$
\frac1k\sum_{\substack{0<y<2\cdot3^k\\y\ {\rm odd}}}
\left(\frac{L_k(y)}y\right)^r
\longrightarrow \sum_{C\ {\rm escaping}}H_C^r,
\qquad H_C=\frac{\log(4/3)}2\,d_C ,
$$

where $d_C$ is the existing weighted logarithmic component mass. Targets outside a finite union of actual trajectories have a uniformly small first-hit ratio; a first-moment bound controls their total contribution. This permits exhaustion over all targets and all components. For thresholds outside an explicitly described countable set, the number of first-hit ratios above threshold is eventually an **exact affine function of $k$**, with slope equal to the number of components above that amplitude.

Repeated visits to all positive cycles contribute only $o(k)$ in aggregate to the difference between raw and first-hit harmonic mass, even if there are infinitely many cycles. Thus the completely raw statistic, requiring no orbit classification,

$$
\frac1k\sum_{\substack{0<y<2\cdot3^k\\y\ {\rm odd}}}
\frac{(\rho_k(y)/y)^2}{1+\rho_k(y)/y}
\longrightarrow
\sum_{C\ {\rm escaping}}\frac{H_C^2}{1+H_C}.
$$

An independent zero-limit estimate for this explicit finite-law statistic would exclude every ordinary escape under the stated inputs. The identity does not supply that estimate. Positive cycle exclusion remains a separate requirement.

[The ordinary renewal theorem](boundary/ORDINARY_RENEWAL.md) samples actual odd ancestors of a fixed escaping target. Up to any growing physical horizon $L=o((\log X)^{1/8})$, their entire parity window approaches the fair conditioned-odd law. Their visible record count converges in total variation to a geometric law with continuation probability $2/3<p\le47/64$, even though each sampled ordinary source has infinitely many records. A critical tilt reaches the zero-critical-measure record set but fails the required critical Frostman bound. The proof keeps the order of the sampling and time limits explicit.

[The transverse construction](global/TRANSVERSE.md) shows that a hypothetical escape supports a finite fixed measure dominating full ternary Haar on one specified positive ordinary binary fiber. Its entire ternary marginal is absolutely continuous. The exact masses of all other positive ordinary binary fibers are computed, including the grade-dependent factor on the past. Removing the remaining nonordinary inverse children loses stationarity. Absolute continuity of the ternary marginal alone therefore does not supply the missing ordinary exclusion.

## What is formalized

The common [Lean driver](check_lean.py) builds twelve new modules with fresh project objects against Lean 4.34.1 and the pinned Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. All **77 public theorem declarations** are audited, including attributed public helper theorems. Only `propext`, `Classical.choice`, and `Quot.sound` occur in their axiom inventories.

| Module | Public theorems | Checked content |
|---|---:|---|
| [FrozenAmplitude](arithmetic/FrozenAmplitude.lean) | 7 | Integer folding, amplitude recurrence and variation, finite telescoping, incoming residues and residue coincidences |
| [MovingCenters](arithmetic/MovingCenters.lean) | 7 | Affine concatenation, arbitrary-background adjacent carry swap, physical junction numerators and repeated centers |
| [PhasePair](arithmetic/PhasePair.lean) | 4 | Lifted-gap recurrence, exact endpoint numerator, arbitrary additive grouping and grouped endpoint identity |
| [MixedMahler](arithmetic/MixedMahler.lean) | 5 | Physical two-branch coefficient balance, missing rows and closure of the binary kernel under arbitrary ternary sections |
| [AllGapSections](arithmetic/AllGapSections.lean) | 5 | Arbitrary finite incoming sums, composition of sections and the full depth bounds $k\le l\le Ek$ |
| [BoundaryKernel](boundary/BoundaryKernel.lean) | 9 | Actual odd-step retention, appended clocks, source-address injectivity and squared atom weight |
| [RecordTwo](boundary/RecordTwo.lean) | 7 | Exact two-branch ordinary dynamics, disjointness, expansion and repeated-block equations |
| [NegativeShadow](global/NegativeShadow.lean) | 3 | Unique visit clock to the reflected root and the finite-path gain bound |
| [OrdinaryFibers](global/OrdinaryFibers.lean) | 3 | Shifted shortcut identity, score increase and injectivity from a positive fiber |
| [OddPosterior](global/OddPosterior.lean) | 4 | Disjoint ordinary predecessor classes, persistence of synchronous sources, accumulated clocks and relative weights |
| [DyadicBoundary](global/DyadicBoundary.lean) | 21 | Unique changing child, forbidden low bits, lifted endpoints, actual tripling defect, power-ray identities and signed-reference magnification |
| [PairedBoundary](boundary/PairedBoundary.lean) | 2 | Arbitrary-length positive rise identities and the paired finite coalescence used in the boundary digit restriction |

These finite kernels do not formalize Matveev, the exponential-sum estimates, Hochman's theorem, the S-part theorem, the measure constructions, the analytic trace laws, the full periodic-boundary exclusion or the holonomic classification. The [review and verification record](../../reports/astra-unconventional-20261126/REVIEW.md) separates written proofs, finite controls, Lean checks and repository integrity.

## Scope of the re-evaluation

The [intake](../../reports/astra-unconventional-20261126/PR_INTAKE.json) inventories 169 PRs and pins the six scientific heads changed since the previous intake. We read their relevant new packets and the strongest existing target formulations. This was a source and direction review, not a replay of every historical theorem or experiment. The previous long PR description is preserved in [the archive record](../../reports/astra-unconventional-20261126/PREVIOUS_PR_DESCRIPTION.json).

The project-wide missing step remains ordinary realization at all depths. The three current targets retain it explicitly: full-denominator cancellation on one cycle, positive-integer entry into the record attractor, and finite eigenmeasure mass on an eventually-zero binary fiber. None is replaced by average behavior, varying finite witnesses, or local solvability.

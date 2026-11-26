# Three attacks on the ordinary arithmetic boundary

**Research checkpoint, 26 November 2026. Universal Collatz termination remains OPEN.** This packet starts from the complete PR 193 tree at `4cc06e7d8fdec923eed73a26b1e9d680c9f701d1` and the current scientific heads recorded in the [intake](../../reports/astra-unconventional-20261126/PR_INTAKE.json). Its purpose is to attack the common missing arithmetic condition with different tools: simultaneous digit windows and point spacing, real and nonarchimedean boundaries, and positive inverse-transfer measures. Three GPT-6.2 Astra agents developed the attacks in parallel; the coordinating agent reconstructed the new arguments and built the formal kernels independently.

The shortcut map is $T(n)=n/2$ on even inputs and $T(n)=$3n+1$/2$ on odd inputs. The odd map strips the full power of two from $3n+1$. Physical clocks, odd clocks, folded ranks, and inverse-word lengths are explicitly distinguished in the individual proofs. None of the conclusions below is an unconditional proof of termination.

## Results to read first

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

## What is formalized

The common [Lean driver](check_lean.py) builds six new modules with fresh project objects against Lean 4.34.1 and the pinned Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. All **36 public theorem declarations** are audited. Only `propext`, `Classical.choice`, and `Quot.sound` occur in their axiom inventories.

| Module | Public theorems | Checked content |
|---|---:|---|
| [FrozenAmplitude](arithmetic/FrozenAmplitude.lean) | 7 | Integer folding, amplitude recurrence and variation, finite telescoping, incoming residues and residue coincidences |
| [MovingCenters](arithmetic/MovingCenters.lean) | 7 | Affine concatenation, arbitrary-background adjacent carry swap, physical junction numerators and repeated centers |
| [BoundaryKernel](boundary/BoundaryKernel.lean) | 9 | Actual odd-step retention, appended clocks, source-address injectivity and squared atom weight |
| [RecordTwo](boundary/RecordTwo.lean) | 7 | Exact two-branch ordinary dynamics, disjointness, expansion and repeated-block equations |
| [NegativeShadow](global/NegativeShadow.lean) | 3 | Unique visit clock to the reflected root and the finite-path gain bound |
| [OrdinaryFibers](global/OrdinaryFibers.lean) | 3 | Shifted shortcut identity, score increase and injectivity from a positive fiber |

These finite kernels do not formalize Matveev, the exponential-sum estimates, Hochman's theorem, the S-part theorem, or the measure constructions. The [review and verification record](../../reports/astra-unconventional-20261126/REVIEW.md) separates written proofs, finite controls, Lean checks and repository integrity.

## Scope of the re-evaluation

The [intake](../../reports/astra-unconventional-20261126/PR_INTAKE.json) inventories 169 PRs and pins the six scientific heads changed since the previous intake. We read their relevant new packets and the strongest existing target formulations. This was a source and direction review, not a replay of every historical theorem or experiment. The previous long PR description is preserved in [the archive record](../../reports/astra-unconventional-20261126/PREVIOUS_PR_DESCRIPTION.json).

The project-wide missing step remains ordinary realization at all depths. The three current targets retain it explicitly: full-denominator cancellation on one cycle, positive-integer entry into the record attractor, and finite eigenmeasure mass on an eventually-zero binary fiber. None is replaced by average behavior, varying finite witnesses, or local solvability.

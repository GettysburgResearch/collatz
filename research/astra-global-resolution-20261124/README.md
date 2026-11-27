# Global Collatz continuation: one directed return, rational companions, and collision energy

**Research checkpoint, 24 November 2026. Full Collatz convergence remains OPEN.**

This continuation adds a complete Lean reduction for the positive ordinary integers, a pointwise rational-comparison theorem, and source-qualified laws separating cyclic from escaping collision mass. It builds on the current PR193 checkpoint and the latest interfaces from the repository. [Repository intake and connections](LATEST_CONNECTIONS.md) · [Exact source pins](SOURCES.json)

Use the shortcut map
\[
 T(n)=
 \begin{cases}
 n/2,&n\equiv0\pmod2,\\
 (3n+1)/2,&n\equiv1\pmod2.
 \end{cases}
\]
Write \(C=\{n>0:\exists j,\ T^j(n)=1\}\). Shortcut convergence is equivalent to convergence for the usual Collatz map.

## 1. A kernel-checked criterion on the actual basin of one

The strongest fully formalized conclusion is
\[
 \boxed{\quad C=\mathbb N_{>0}
 \quad\Longleftrightarrow\quad
 \forall k\ge0,\quad
 36k+8\in C\ \Longrightarrow\ 72k+17\in C.\quad}
\]

The declaration is **`SingleReturn.collatzIffEvenChild`** in [SingleReturn.lean](rewriting/SingleReturn.lean). The displayed implication itself is still unproved. The theorem quantifies over all positive ordinary inputs and uses the actual existential orbit definition of reaching one.

Here is the construction. For \(x=8u+7\), three genuine steps on \(7x\) give
\[
 56u+49\longmapsto84u+74\longmapsto42u+37
       \longmapsto7(9u+8).
\]
The same quotient \(H(x)=9u+8\) equals \(T^3(3x)\). A six-row descent argument initially uses this return together with a second return after five steps. A larger certificate removes that second assumption entirely.

Its **291 arithmetic progressions** cover every integer from 2 upward. Each has a literal path to a smaller positive integer using ordinary steps, reverse ordinary steps, and only the directed extra move
\[
 8u+7\longrightarrow9u+8.
\]
Convergence propagates backwards along such a path if \(9u+8\in C\Rightarrow8u+7\in C\). The proof checks the domain of every rule on its entire progression, verifies exhaustive subdivision, and then applies strong induction. There are 52 distinct words and 3,483 moves. Every endpoint is at most \(118/123\) of its source; the Lean proof needs only strict descent.

The elementary identity \(T^2(8u+7)=2(9u+8)+1\) turns the remaining implication into a binary-child condition. Simultaneous ordinary steps replace the pair \(9r-1,18r-1\) at \(r=2s\) with the pair at \(r=3s\), lowering \(v_2(r)\) by one. At odd \(r=4k+3\), the two inputs meet explicitly at \(27k+20\). Only \(r=4k+1\), the boxed condition, remains.

This is a conditional descent certificate for the full domain. It does not supply the missing transfers by induction on their inputs: 156 leaves can request a transfer above the original source. For example the path from \(122875\) uses one at \(20970919\). The quotient branch itself is already present in Yolcu–Aaronson–Heule, equation (10); earlier repository multiplier criteria are also credited. The claim here is the elimination of the second directed return and the explicit complete formal cover, with its final physical refinement.

[Argument and prior work](rewriting/SEVEN_RETURN.md) · [Six-row proof](rewriting/SevenReturn.lean) · [Independent review](collision/REVIEW_REWRITING.md)

A direct attempt to close the boxed condition is recorded in the [residual-limit supplement](arithmetic/RESIDUAL_GHOST.md). An elementary construction gives infinitely many convergent left arms in every binary parameter class. Combining it with the pinned finite pair-fusion lemma gives pairs with both arms convergent, but with arbitrarily late first meetings. Along suitable such pairs the dyadic companion limits are \((-4/3,-51/5)\). Thus a uniform meeting cutoff or closedness of triadic-companion membership cannot supply the missing implication. This changing-source construction is not a fixed positive counterexample. [Independent supplement review](collision/REVIEW_RESIDUAL_GHOST.md)

## 2. Rational comparison at one prescribed ordinary integer

**PROPOSED written theorem, independently reviewed.** For the actual orbit from \(n\), let
\[
 e_i=T^i(n)\bmod2,\quad P_i=\sum_{j<i}e_j,\quad
 A_i=\frac{2^{i+P_i}}{3^i},\qquad
 D(n)=\sum_{i\ge0}e_i A_i\in\mathbb Z_2.
\]
The series is always defined, before the orbit's fate is known. This uses the dyadic-companion interface of PR182 at its pinned current head.

For a reduced rational candidate \(a/b\), write its positive odd denominator as \(b=3^h m\), with \(3\nmid m\), and put
\[
 \alpha=\log_2 3-1,\quad
 s=\frac{-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)}{\log3}
       =0.6177244\ldots,\qquad
 F(m)=\frac{m^s}{\sqrt{\log(2m)}}.
\]
For every **incorrect** candidate,
\[
 v_2\!\left(D(n)-\frac ab\right)
 \le C\left[1+\log(n+1)+\log(|a|+2)+\log b+F(m)\right].
\]
The absolute constant is effective from the argument; no numerical value is asserted. A reduced even denominator is immediately incompatible with dyadic integrality. The existing explicit triadic bound remains preferable when \(m=1\).

The proof drives a rational trial by the actual physical bits. Long agreement forces that trial onto a fixed denominator grid and forces many visits to a bounded positive interval. A legal past with enough odd bits severely limits the number of such grid points. A repeated trial phase either certifies a repeated actual orbit state or forces a finite bound on further agreement through an exact dyadic congruence.

This gives a **terminating equality test for any supplied rational**, including a correct candidate, within the stated order of trajectory steps. A correct rational also bounds the actual preperiod and period. It does not decide whether a correct rational exists. In particular, the imported implication from universal triadic rationality to universal convergence is not discharged.

The same packing argument yields an individual bound for positive primitive companion cycles whose logarithmic gap is at least \(\eta L\):
\[
 L\ll_\eta F(b_*),\qquad
 b_*\gg_\eta L^{1/s}(\log(2L))^{1/(2s)}.
\]
It also bounds the **sum of least periods of all such cycles at one fixed reduced denominator** by \(O_\eta(F(b_*))\). Every hypothetical nontrivial physical cycle, and every sufficiently long periodized prefix of one fixed escaping orbit, satisfies the required positive-gap condition. The denominator \(b_*\) is the companion denominator; it is not the reduced denominator of the physical cycle.

[Full pointwise proof](arithmetic/README.md) · [Formal finite identities](arithmetic/CompanionPacking.lean) · [Independent review](collision/REVIEW_ARITHMETIC.md)

### Complete denominators at exact clocks

**PROPOSED written theorem, with identified Diophantine inputs.** At every fixed interior parity density \(p/A\), both the physical reduced denominator and the companion reduced denominator achieve their respective full exponential scales outside an exponentially small fraction of marked words. This includes both signs, arbitrary clock gcd, and conditioning on primitivity. It strengthens an entropy-scale fixed-weight bound and credits the previous full-scale result with mixed weights.

There is also a uniform comparison of the two complete raw divisors:
\[
 \log\gcd\left(\left|2^A-3^p\right|,
                   \left|2^{A+p}-3^A\right|\right)=o(A).
\]
This applies Corvaja–Zannier's Subspace Theorem consequence to
\[
 U=2^A/3^p,\qquad V=2^{A+p}/3^A.
\]
Their exponent determinant \(p(A+p)-A^2\) never vanishes at the specified positive integer clocks, excluding the exceptional multiplicative subgroups. All prime powers remain in the gcd. Lagarias's quantitative logarithmic separation supplies the polynomial height bound needed for the fixed-clock count. The Subspace Theorem asymptotic is not assigned an effective universal threshold.

These almost-every-word statements still allow the rotations of an exceptional individual integer cycle. They do not establish cycle exclusion.

[Complete denominator argument](arithmetic/CLOCK_FIBERS.md) · [Exact literature interfaces](SOURCES.json)

## 3. Physical collision energy isolates cyclic mass

**PROPOSED, SOURCE-QUALIFIED written theorems.** Draw \(U,V\) independently and uniformly from \([X,2X)\). Under the specified fixed-floor, first-landing, orbit-sparsity and pair-fusion inputs, the lexicographically first common ordinary vertex is tight on the event that the two orbits meet. Both meeting clocks differ from their respective global-minimum clocks by tight errors. The argument retains the partner's entire actual orbit as one landing test.

Let \(d_C\) denote the ordinary density of a component and \(p_C\) the least shortcut period when it is cyclic. Escaping components carry an integer time phase. The new base-three-octave comparison spreads this phase:
\[
 \sum_{C\ {\rm escaping}}\sup_j
 \Pr\{U\in C,\ s(U)=j\}\ll(\log X)^{-1/2}.
\]
Cyclic phases instead become uniform modulo their periods. Consequently, at
\[
 H_X=\left\lceil
 \frac{2\log X}{\log(4/3)}
       +B\sqrt{\log X\log\log X}
 \right\rceil
\]
for sufficiently large fixed \(B\), or at any later deterministic clock,
\[
 \Pr\{T^{H_X}U=T^{H_X}V\}
 \longrightarrow \sum_{C\ {\rm cyclic}}\frac{d_C^2}{p_C}.
\]
These conclusions do **not** require the extra Gaussian-clock assumption discussed separately in the collision note.

Write \(p_{X,h}(z)=\Pr(T^hU=z)\). The exact two-parent identity is
\[
 \sum_z p_{X,H}(z)^2=
 \frac1X+
 2\sum_{h<H}\sum_{y\equiv2\pmod3}
       p_{X,h}(2y)\,
       p_{X,h}\!\left(\frac{2y-1}{3}\right).
\]
Under the specified positive-density input for every existing component, full convergence is equivalent to the lower bound
\[
 \limsup_{X\to\infty}
 \sum_{h<H_X}\sum_{y\equiv2\pmod3}
       p_{X,h}(2y)\,
       p_{X,h}\!\left(\frac{2y-1}{3}\right)\ge\frac14.
\]
**This lower bound remains OPEN.** The finite identity and the limiting description identify the needed quantity but do not prove its size.

The same phase argument applies to PR202's long synchronized blocks in a hypothetical escaping component. Different roots give disjoint blocks, and a positive-proportion root selection preserves phase dispersion even if their union is rare in the original interval. Within one block all starts meet at one clock; across independently chosen blocks synchronous collision still has probability \(O((\log X)^{-1/2})\). This prevents an invalid upgrade of that construction to the displayed lower bound.

[Collision proofs and exact dependencies](collision/README.md) · [Finite Lean identities](collision/ClockCollision.lean) · [Independent review](arithmetic/REVIEW_COLLISION.md)

## Verification and scope

The fresh driver compiled **24 public theorems in four new Std-only modules** with official Lean 4.34.1 and warnings treated as errors. It printed their complete axiom dependencies; only `propext`, `Classical.choice` and `Quot.sound` were allowed. There are no proof placeholders in this packet.

| Module | Public theorems | Formal scope |
| --- | ---: | --- |
| `CompanionPacking.lean` | 4 | Arbitrary-word affine recurrence, bounded-past uniqueness, integer clock cutoff, repeated-trial congruence budget |
| `ClockCollision.lean` | 9 | Iterates, unique offsets, floor traces, common-clock block disjointness, actual predecessors and histogram, period-two classification, energy algebra and telescoping |
| `SevenReturn.lean` | 8 | Six-row arithmetic cover under its two directed transfer assumptions |
| `SingleReturn.lean` | 3 | Complete one-way cover, actual convergence equivalence, modulus-36 refinement |

The infinite packing, asymptotic counting, phase-distribution and imported analytic theorems are written mathematics. The Lean audit does not certify those arguments. The optional Gaussian refinements retain an explicit additional assumption because the full primary source was not retrievable.

Both exact Python controls passed in normal and optimized mode with byte-identical output. The arithmetic control checked 777 physical necklaces, 1,320 bounded companion phases and 50,814 literal agreement steps, plus the separate minimum encodings recorded in its output. The rewriting control replayed all 291 progression identities, every move and the exhaustive period of 995,328 residues.

Run only the new packet:
```bash
python -X utf8 -B research/astra-global-resolution-20261124/check.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --out /path/outside/this/packet
```

[Kernel and exact-control receipt](../../reports/astra-global-resolution-20261124/kernel/CHECKS.json) · [Coordinator review](../../reports/astra-global-resolution-20261124/ROOT_REVIEW.md)

The three possible closing steps above are alternative routes: prove the directed ordinary implication, establish triadic rationality at every ordinary source, or prove the collision lower bound under its stated inputs. None is silently assumed here.

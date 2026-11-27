# Whole-denominator laws, stronger cones, and fast ordinary clocks

**PROPOSED research; the universal Collatz assertion remains open.**
This checkpoint adds an all-modulus distribution theorem for the complete
cycle denominator, a sharper signed energy that strengthens the ordinary
postpeak cone, a merger-or-exit estimate for wider starting bands, and
elementary families of ordinary first-hit predecessors with controlled
clocks. Every probabilistic statement identifies its sample space. Every
ordinary merger retains a positive integer source and its actual orbit.

## The complete reduced denominator has a uniform-residue model

Choose uniformly a binary word of length `n` and weight `u`, with
`ε≤u/n≤1−ε`. Let its affine numerator be `C`, put
`D=|2^n−3^u|`, and let `G=gcd(C,D)`, `d=D/G`. The written
[denominator law](cycles/phase4/DENOMINATOR_LAW.md) proves, uniformly
over every modulus `g` prime to six and every residue `a`,

\[
 \left|\Pr(C\equiv a\pmod g)-\frac1g\right|
                  \le C_\epsilon e^{-c_\epsilon\sqrt n}.       \tag{1}
\]

It then proves the stronger statement about the **whole cancelled factor**:
the total variation distance between the law of `G` and `gcd(R,D)`,
where `R` is uniform modulo `D`, is at most the same form of stretched
exponential bound. Equivalently the complete reduced denominator is close
in total variation to

\[
                      \Pr(d=e)=\frac{\varphi(e)}D,
                         \qquad e\mid D.                       \tag{2}
\]

The mean cancellation obeys

\[
 \mathbb E\log G
   =\sum_{p^j\mid D}\frac{\log p}{p^j}
        +O_\epsilon(ne^{-c_\epsilon\sqrt n})=O_\epsilon(\log n).
\]

The proof of (1) uses two complementary mechanisms. For small moduli,
pair adjacent bits and condition on the number of ones in each pair.
Mixed orientations give independent Fourier factors. A short recurrence
forces a frequency of definite size in every logarithmic block; the
pair at its first occurrence remains unexposed. For large moduli, a
short erased interval can have at most one completion with its prescribed
weight and numerator residue. An elementary sieve truncated at
`O(√n/log n)` distinct prime factors upgrades the divisor marginals to
the full histogram without paying for every divisor separately.

[PairFrequency.lean](cycles/phase4/PairFrequency.lean) checks the finite
frequency escape mechanism. The concentration, sieve, and asymptotic
histogram are written proofs, independently reconstructed by the root and
the rigidity lane. The Python controls check exact finite Fourier,
completion, divisor, and histogram identities; they are not proofs of the
asymptotic bounds.

For any fixed noncommuting dictionary of binary blocks, with every label
used a positive proportion of the time, the
[block-alphabet extension](cycles/phase4/BLOCK_ALPHABETS.md) identifies
the exact congruence obstruction. If `κ_ij` is the numerator change on
swapping adjacent blocks and `H=gcd |κ_ij|`, the model is uniform on the
appropriate coset modulo `gcd(D,H)`. The completely commuting case is
deterministic and is handled separately. For blocks `10,110`, `H=6`,
so the uncorrected model (2) applies. Nonunique binary parsing in a
general dictionary does not change the declared labelled-word sample.

Sultanow's residue model, the fixed-prime research discussion, and the
classical numerator injectivity result receive explicit prior credit.
This is not a claim that a statistical cycle model is itself new.

### Why this still does not exclude an integer cycle

An integer cycle requires the single event `d=1`. The error in (1) or
(2) is much larger than `1/D` near critical weight. Indeed the actual
probability has lattice spacing `1/binomial(n,u)`, exponentially larger
than `1/D` in that regime. A relative asymptotic for that atom cannot
hold uniformly: the atom is either zero or at least one sample word.
An additive small error can leave isolated integer candidates. The note
also distinguishes small total variation of the **gcd law** from the
numerator residue law modulo the entire exponentially large `D`; the
latter has sparse support and can have total variation tending to one.

## A stronger kernel-checked cone from signed energy

The corrected energy is `400x²` on the negative dyadic ray through
`−3`, `441x²` on the ray through `−5`, and `450x²` elsewhere.
It satisfies `E(2x)=4E(x)` and `E((3x+1)/2)≥2E(x)` at every signed
odd input other than `−1`. The odd/even exponent ratio is sharp on the
signed `−5,−7,−10` cycle. This yields an integer-power trap while keeping
the prefix even count and the tail even count separate.

Retaining their joint ordinary budget gives the improved sufficient
heights below. Here the original source is `n=2^H v−1`, the upper
postpeak word has `q` evens and `f` odds, and its offset fiber is maximal.

| Ordinary statement | Earlier sufficient height | New sufficient height |
|---|---:|---:|
| Exact discounted same-offset merger criterion | `21q+3` | `6q+3` |
| Protection of `K` extra odds from `3^K | n−s`, `s∈{0,1}` | `21q+9K+3` | `6q+3K+3` |
| Exact finite scaled selector up to grade `H+f+K` | `21q+9K+3` | `6q+3K+3` |
| Finite prepaid bonus `b` | `21q+9(K+b)+3` | `6q+3(K+b)+3` |

The selector retains its additional source cutoff `2n≥K(1+3^K)`.
The prepaid result retains its finite prefix certificate and margin.
For the already verified 648-source certificate, `K≥84` and
`H≥6q+3(K+12)+3` force every smaller visitor to use more than
`H+f+K+12` odds. Neither physical clock is bounded.

See [the complete energy proof and bookkeeping](root/phase4/MIRROR_ENERGY.md),
[MirrorEnergy.lean](root/phase4/MirrorEnergy.lean), and
[SharpCone.lean](root/phase4/SharpCone.lean). The underlying ramp and
prepayment architecture retains its PR146 credit. Its negative-five note
also already proves the same optimal odd gain for signed paths ending at
that cycle. This checkpoint repairs the small reflected state 3, makes
the potential exactly homogeneous on all dyadic rays, and applies the
universal endpoint trap to the stronger cones. The earlier optimal gain
and signed-cycle mechanism are not claimed as new.

## A smaller ordinary merger or an exit from a wider band

For sufficiently large positive `X`, the
[band theorem](descent/postpeak/band/BAND_MERGERS.md) proves that by
`O_ε(X^(ρ/3+ε))` shortcut steps the orbit of `X` either meets an orbit
starting from a positive integer below `X`, or exits `[X,RX]`.
The displayed `ε>0` is small enough to keep the exponent below `1/3`.

| Band ratio `R` | Sufficient `ρ` | Exponent before `ε` |
|---|---:|---:|
| `9/2` | `0.818621…` | `0.272873965…` |
| `81/16` | `0.907614…` | `0.302538283…` |
| `2^(5/2)` | `992/1000` | `0.330666667…` |
| `2^(51/20)` | `997/1000` | `0.332333333…` |

The first ordinary mechanism is elementary. An `OEE` factor at `x`
meets the source `(x−1)/4` after one lower step. While the upper factor
stays in `[X,6X]`, that source is below `X`. Consequently a surviving
in-band path contains no consecutive even departures. Exact fourth-copy
energy calculations for the resulting rotation-indexed word language,
combined with the explicitly cited located-window Subspace Theorem
argument, bound the number of possible ordinary window starts. A repeated
state would contradict the cited two-log estimate at these exponents.

If exit occurs before a merger, the homogeneous coefficient sequence has
the same first-exit date and direction. At `R=81/16` its comparison band
must be `[1,R)`, since four initial odd steps give an exact upper-boundary
coefficient and a strictly positive physical correction. The other rows
have no attainable upper resonance. The onset is ineffective, and an
upward exit supplies no subsequent descent assertion.

The 32-support and 220-support certificates use exact integer powers,
not floating-point decisions. A separate bank contains 446 exactly
verified longer ordinary merger factors, each valid in a sixfold band
at `X≥61`. It does **not** supply a sixfold global energy estimate.
[BandParents.lean](descent/postpeak/band/BandParents.lean) proves the
short merger and one 29/28-step native merger; the remaining finite
factors are checked by exact Python arithmetic. Weaver 181/223 and the
reported Chudnovsky theorem are external analytic inputs, not newly
formalized results in this checkpoint.

## Elementary moving-target predecessor clocks

Fix a positive odd target `y` prime to three and `M≥y`. The
[source-clock bank](rigidity/phase5/SOURCE_CLOCK_BANK.md) constructs,
for `X/M` sufficiently large, a family `E⊂[X,2X)` of distinct ordinary
first-hit predecessors of `y` with

\[
 |E|\asymp(X/M)^s,\qquad
 \max_k\frac{\#\{x\in E:d_y(x)=k\}}{|E|}
                  \ll\frac1{\sqrt{\log(X/M)}},\qquad s>\tfrac12.
\]

Constants and the construction are uniform in the moving target and
threshold. An exact finite inverse bank has positive real prefix growth
and a rational pressure certificate above one at exponent `1/2`.
Independent block times, stopping at a height crossing, and a final
dyadic lift produce the family and its clock dispersion. The dispersion
is relative to this constructed family. It is not asserted for arbitrary
sparse subsets of the target's predecessor set.

The threshold property is a first **odd** landing at or below `M`;
when `M=y` the construction also gives the corresponding physical first
landing. For general `M`, the final even states can enter that band
before the terminal odd target. Exact first visits to `y` are retained
in every case. This distinction is explicit in the proof and fixtures.

## The first two terms at the fastest clock edge

Write `θ=log₂3`, `L=log₂(X/y)`, and let `a_y(X,k)` count sources in
`[X,2X)` first reaching `y` at time `k`. For small fixed `δ>0`, the
[elementary edge estimate](rigidity/phase5/FAST_CLOCK_EDGE.md) proves,
uniformly in the target, that a bounded absolute clock window around
`(1+δ)L` has maximal atom with logarithmic exponent

\[
 \frac1L\log_2\max_{|k-(1+\delta)L|\le B}a_y(X,k)
   =\frac\delta\theta\log_2\!\frac{e\theta}{3\delta}
                       +O(\delta^2)+o_\delta(1).                 \tag{3}
\]

The proof explicitly enumerates admissible inverse valuations. Every
unit target has two possible exponent classes in each six consecutive
integers. A weak-composition count produces actual positive first-hit
paths. Lifting them into one shell cancels their variable odd-word clock,
leaving at most two exact arrival clocks. The upper count retains the
possible final nonunit child. No mixing theorem is assumed in (3).
The statement does not assert a fixed-`δ` limiting rate.

Earlier central-clock source bounds and positive-density predecessor
results remain credited in the lane's comparison. These fast-clock
families can be built for any target, including one on a hypothetical
exceptional component. They provide no connection from that target's
future to the known cycle.

## Verification and the first remaining obligations

The root's fresh Lean replay and normal/optimized Python replays are
archived in [checkpoint4 execution evidence](../../reports/astra-reciprocal-rigidity-20261127/checkpoint4/README.md).
The algebraic energy and ordinary consumers are kernel theorems; the
distribution, sieve, fourth-moment, stopping-line, and asymptotic count
arguments remain written proofs with the stated external inputs.
Repository regressions check structural integrity and their bounded
fixtures, not the truth of those analytic arguments.

The global gaps remain concrete: turn an additive rare-denominator law
into exclusion of every integer atom; show that every source reaches an
effective smaller-merger configuration; or establish the original
same-source first-power extinction condition. None is inferred from a
typical-word statement, a constructed predecessor family, or an upward
band exit.

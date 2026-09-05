# Natural-density almost-bounded orbits in logarithmic time

> **Import verdict: EXTERNAL SOURCE-QUALIFIED; no contradiction found in a full-paper structural audit.** The central natural-to-logarithmic passage transport is technically deep and was not independently reconstructed line by line or rebuilt in Lean here.

## Exact theorem surface

For the raw Collatz map

\[
\operatorname{Col}(n)=\begin{cases}
n/2,&n\text{ even},\\
3n+1,&n\text{ odd},
\end{cases}
\]

and the odd-to-odd Syracuse map

\[
\operatorname{Syr}(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}
\qquad(n\text{ odd}),
\]

the paper proves one uniform clock for every diverging threshold function.

### Odd Syracuse form

If `f(N)→∞` along odd integers, then an odd-relative natural-density-one set of odd `N` has

\[
\operatorname{Syr}^m(N)<f(N),
\qquad
m\le C_{\mathrm{Syr}}\log N,
\]

where

\[
C_{\mathrm{Syr}}=\frac{501501}{5000\log 2}<145.
\]

### Raw Collatz form

If `f(N)→∞` on all positive integers, then a natural-density-one set of positive `N` has

\[
\operatorname{Col}^m(N)<f(N),
\qquad
m\le C_{\mathrm{Coll}}\log N,
\]

where

\[
C_{\mathrm{Coll}}=\frac{1509503}{5000\log 2}<436.
\]

The quantifier order is important: one absolute clock is chosen before `f`; the density-one set may depend on `f`.

### Quantitative fixed-target form

For every

\[
0<d<\frac5{143},
\]

there is `C_d` such that the ambient proportion of odd `N≤x` whose Syracuse orbit stays above `N_0` throughout the stated logarithmic schedule is at most

\[
C_d(\log N_0)^{-d}.
\]

The exact retained specialization is

\[
d_0=\frac{6993}{200000}=0.034965,
\qquad
\frac5{143}-d_0=\frac1{28600000}>0.
\]

### Raw square-root time window

For a natural-density-one set, there is a raw hit below `sqrt(N)` with

\[
\frac{\log N}{2\log 2}<m\le C_{\mathrm{Coll}}\log N.
\]

The lower inequality is pointwise for every raw hit below `sqrt(N)`, not merely for the selected density-one witness.

## Proof architecture

The work extends Tao's first-passage framework in four stages.

1. **Natural versus harmonic source laws.** The same multiplicative source block is equipped with a flat counting law and a reciprocal/harmonic law.
2. **Phase discrepancy.** A Diophantine lower bound for multiples of `log_2 3` controls the endpoint phases created by changing source weighting.
3. **Common passage profile.** Exact bands, affine endpoint laws, a local Gaussian approximation, and terminal reconstruction put both source laws near one branch- and band-independent profile.
4. **Exact source mixture and totalization.** Weighted band errors sum without a band-count loss; the possible top endpoint, no-hit sentinel, and real-floor perturbations are charged explicitly.
5. **Timed geometric telescope.** Passage across a sequence of scales retains an integer clock and the same logarithmic-rate exponent.
6. **Growing threshold.** Freeze a sufficiently large finite target after choosing a density tolerance; the fixed-target estimate then gives natural density one for arbitrary `f→∞`.
7. **Two-adic fiber transfer.** Write `N=2^aM` with `M` odd and transfer the Syracuse conclusion to raw Collatz time.
8. **Deterministic lower clock.** The inequality `N≤2^m Col^m(N)` gives the square-root lower bracket.

The difficult new content is the first four stages. The downstream density and clock conversions are comparatively transparent once the natural-counting passage law is available.

## Diophantine bottleneck

The phase input is written

\[
\|q\log_2 3\|_{\mathbb R/\mathbb Z}
\ge c q^{1-\kappa}.
\]

Rhin's exponent `13.3` gives `kappa=14.3=143/10`. Erdős–Turán discrepancy contributes `N^{-1/kappa}`. The physical valuation tube has square-root scale, halving the exponent once more, so the transport permits

\[
d<\frac1{2\kappa}=\frac5{143}.
\]

The independent terminal approximation also imposes `d<1/20`, but with the current Rhin input the phase guard is tighter.

The paper reports an exact formal reconstruction of the weaker large-height Rhin statement from Padé data, followed by symbolic finite absorption. It does not install the printed theorem as an axiom and does not claim Rhin's sharper `7.616` line without an effective handoff.

## Error ledger and constants

The band-local genuine passage law is within `7R_d(B)` of a common profile. Exact source mixing and top-endpoint control raise this to `8`; comparison of two laws gives `16`; one Hahn decomposition for full `l1` gives `32`. Real-floor perturbations produce the displayed transport constants

```text
scheduled no-hit prefactor: 184
passage-transport prefactor: 384256
scheduled power exponent:   1/32000
transport log exponent:     any d < 5/143
```

The import checked the numerical and rational identities behind the clocks, the `d_0` margin, the relationship `C_Coll=3 C_Syr+1/log 2`, and the pointwise lower-clock algebra.

## Raw-time conversion

For `k` Syracuse steps from odd `M`, let `W` be the total stripped two-adic valuation. The exact raw simulation time from `2^aM` is

\[
j=a+k+W.
\]

Since

\[
2^W\operatorname{Syr}^k(M)\le4^kM,
\]

one has

\[
W\le2k+\frac{\log M}{\log 2}.
\]

Together with `a+log M/log2=log N/log2`, this gives

\[
j\le3C_{\mathrm{Syr}}\log N+\frac{\log N}{\log 2}
=C_{\mathrm{Coll}}\log N.
\]

This is a worst-case uniform conversion, which explains the factor three and the remaining large constant.

## Trust and reproducibility boundary

The manuscript prints frozen formal worktree commit

```text
f386357d453ac4dcf91242b76252d88a5a729906
```

while the public ProofAtlas source page identifies immutable checked-source commit

```text
ca3dd0d63920411213403092aecc6946619eb082
```

for the accepted public package. The public evidence record reports a 599-file, 182,625-nonempty-line first-party Lean closure, build success, no unfinished proof steps, and only `propext`, `Classical.choice`, and `Quot.sound` in the theorem axiom profile. No `native_decide` trust point is reported for this theorem cone.

This import verified the source metadata, statement surface, PDF bytes, and small exact arithmetic. It did not rebuild the 599-file closure or independently audit every formalized band estimate.

## Exact limitations

- Natural density one may leave infinitely many exceptional inputs.
- The theorem gives descent below a growing threshold, not arrival at one and not eventual convergence.
- For a fixed threshold `N_0`, the quantitative upper bound is proportional to the counting endpoint `X`; it only makes the coefficient small as `N_0` grows.
- The threshold at which the transport estimates become valid and the final fixed-target prefactor are existential.
- The construction is profoundly asymptotic: one internal schedule has `m_0(B)=floor(log B/100000)`, so it is not intended as a practical finite-range bound.
- Neither upper clock is claimed sharp.
- Typical-orbit control does not imply the resident fixed-source statement `SC*`.

## Repository crosswalk

### `SC*`

`SC*` fixes a single source and asks for one coefficient-subcritical prefix. The natural-density theorem controls almost every source for each threshold function. A hypothetical counterexample may lie in the exceptional set, so the quantifier mismatch is exact and decisive.

The relevant reusable component is not the density-one endpoint by itself, but the **conditional passage transport**. If it can be made uniform inside the nested residue cylinders generated by a fixed all-supercritical source, it may supply the missing source-conditioned stopping estimate.

### Ordinary extraction

Density arguments do not create one ordinary all-depth seed and do not resolve a least-root sequence. However, a cylinder-uniform version with summable error could potentially prove escape of least representatives rather than merely small ambient measure.

### `FC*` and cycles

The theorem does not inspect the complete denominator, common displacement, or cycle equation. A nontrivial cycle is compatible with a density-one almost-bounded statement because the cycle and its basin may be sparse.

## Improvement program

### N1. Prove a power-saving fixed-height bad-set bound

Define, for fixed `H`,

\[
B_H(X)=\#\{N\le X:N\text{ odd and }\operatorname{Syr}^m(N)>H
\text{ for every }m\le C\log N\}.
\]

The decisive target is

\[
B_H(X)=O_H(X^\beta)
\qquad\text{for some }\beta<1.
\]

With the present predecessor exponent, `beta<0.901` would prove Collatz by the bridge in `synthesis-and-roadmap.md`. If inverse exponents approach one, any fixed `beta<1` would suffice.

This is substantially stronger than replacing logarithmic density by natural density: it asks for quantitative thinning in the counting endpoint for each fixed floor.

### N2. Parameterize and optimize the block ratio

The proof freezes `alpha=1001/1000`. The geometric clock carries a factor on the order of `1/(alpha-1)`, which is the main source of the constants `145` and `436`. Rebuild the transport theorem with symbolic `alpha`, determine its admissible interval, and optimize the exact clock/error tradeoff. Even a modestly wider block ratio could reduce the clock by an order of magnitude.

### N3. Use a sharper effective phase input

Formalize Rhin's sharper `7.616` line with an explicit crossover, or use a modern effective linear-form estimate specialized to `(log2,log3)`. In the current architecture this would change the phase cap to approximately `0.0580`, after which the terminal guard `d<0.05` becomes binding. Therefore the phase and terminal improvements should be developed together.

### N4. Remove the square-root tube loss

The exponent is halved because discrepancy is applied on a tube of length about the square root of the scheduling scale. Possible routes include:

- continued-fraction/Ostrowski discrepancy specialized to `log_2 3`;
- a two-dimensional exponential-sum estimate that treats valuation and phase jointly;
- van der Corput differencing before the physical-tube restriction;
- a local limit theorem with phase built into the kernel rather than charged afterward.

Any improvement from `1/(2kappa)` toward `1/kappa` directly strengthens the fixed-target rate.

### N5. Improve terminal reconstruction

The `1/20` terminal-coverage exponent will become the bottleneck after a sharper Rhin input. Tighten the full-prefix tube, exact-to-nominal atom replacement, and exterior aggregation so that the final rate is controlled by the Diophantine term rather than a technical terminal estimate.

### N6. Extract effective thresholds and constants

Replace eventual absorptions by explicit inequalities, track the phase constant and finite handoff, and emit a checker-readable threshold ledger. This is necessary before any scale-dependent `N_0=N_0(X)` argument can be used safely.

### N7. Condition on arithmetic cylinders

Prove the natural/harmonic transport uniformly after conditioning on a prescribed parity or residue prefix. The target is a distortion estimate whose constants grow slowly enough with the cylinder depth to be summable or to force least-root escape. This is the most direct route from the paper's machinery to resident `SC*`.

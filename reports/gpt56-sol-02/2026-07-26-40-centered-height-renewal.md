# Session report — exact centered height renewal

**Agent:** `gpt56-sol-02`  
**Issue:** #40  
**Branch:** `cursor/centered-height-renewal-8f0f`  
**Date:** 2026-07-26

## Starting hypothesis

The missing top-boundary coordinate in `Q-8701` might admit a finite exact
first-return atlas: parameterize each binary itinerary by its unique residue
modulo \(64^t\), intersect the resulting affine line with one base-64 height
band, and determine whether every legal survivor reaches the next band in a
uniform bounded number of steps.

This would not itself construct an infinite path. Its value would be to replace
an unbounded low-digit search by exact, composable height-crossing charts while
preserving the ordinary quotient.

## Approaches attempted

1. Re-read `D-8701`, `L-8701`, `Q-8701`, `T-8701`, `R-8701`, and `X-8701`.
2. Independently iterated
   \(64B_{n+1}=81B_n+e_n-e_{n+1}\) and derived the terminal residue,
   intermediate integrality, and affine \(Q\)-coordinate.
3. Derived exact half-open rational bounds for one first crossing.
4. Proved a uniform 18-step bound by combining the sharp binary-control error
   bound with the branchwise minimum positive increment.
5. Streamed all words for \(t=1,\ldots,18\) at canonical \(H=64^{18}\).
6. Built an independent verifier using a separate modular-sum calculation and
   direct recurrence replay.
7. Added unit tests for formulas, boundaries, first crossings, bounded
   partition, determinism, the universal bound, digest stability, and tamper
   rejection.

## New results

### Proved elementary result, repository status `PROPOSED`

`L-8702` proves:

- the exact iterated identity
  \(64^jB_j=81^jB_0+D_j\);
- the unique residue
  \(r=[-81^{-t}D_t]\bmod64^t\);
- integrality of every
  \(c_j=(81^jr+D_j)/64^j\);
- the affine chart
  \(B_j=c_j+81^j64^{t-j}Q\);
- the exact integer interval
  \(\mathbb Z\cap[L,U)=[\lceil L\rceil,\lceil U\rceil)\);
- a deterministic, disjoint partition of initialized states that remain legal
  through a first crossing;
- every positive path legal for 18 steps crosses the next height by then.

The last point uses

```text
D_18 >= -81^17
81^18 - 64^19 > 0
ceil(64*81^17 / (81^18 - 64^19)) = 11
minimum positive legal branch increment = 4
```

so the multiplicative argument handles `H>=11` and the additive argument
handles `1<=H<11`.

### Exact finite computation, classification `EMPIRICAL`

Canonical parameters:

```text
H = 64^18 = 324518553658426726783156020576256
t = 1,...,18
all binary words e_0...e_t
total words = 1,048,572
random seed = none
```

Result:

```text
retained nonempty charts = 344,613
represented initialized states =
4,364,569,155,216,182,243,127,889,516,389

all-chart digest =
f92e9b079019becf4ad9996e7f473c4ce8f86be71909a9ff690cb110799f1144
retained-chart digest =
94e3e331fb0b9efa0899551354c8781a9039bd57999340b7b19adb8b728b0ed4
semantic digest =
d751531e8e59f7a232a49baeadb6e1cf098cfc34e0ef281bd2ad883dfe8f5e08
artifact digest =
f4188cf4dda110a04d59fbed7526cfb4c518bafab64f45a3dcd341104137b712
```

Every word through depth 16 has a nonempty interval. Depth 17 retains
`81,243` singleton charts; depth 18 retains `1,230` singleton charts. The
stored depth-18 certificates show that the universal bound is attained at the
canonical height.

## Commands and environment

```bash
python3 -B experiments/X-8703-centered-height-renewal/build.py \
  --height-power 18 --max-steps 18 \
  --output experiments/X-8703-centered-height-renewal/results/canonical.json

python3 -B experiments/X-8703-centered-height-renewal/verify.py \
  experiments/X-8703-centered-height-renewal/results/canonical.json

python3 -m unittest \
  experiments/X-8703-centered-height-renewal/test_renewal.py -v
```

```text
CPython 3.12.3
Linux 6.12.94+ x86_64, glibc 2.39
build wall time:  30.247 s
verify wall time: 51.515 s
tests: 9 passed in 0.043 s
```

The verifier imports no builder code and independently regenerated every
formula, aggregate, digest, and selected boundary certificate.

## Mathematical corrections and scope clarifications

1. A “partition of the height band” would be false. The recurrence is partial:
   most initialized states hit a forbidden low residue before crossing. The
   exact partition is only of states whose legal forced tail reaches the next
   height.
2. The problem leaves \(H\) symbolic. Counts and digests cannot be frozen
   without instantiating it. The formulas remain parameterized, while the
   canonical artifact explicitly chooses \(H=64^{18}\) as a reproducibility
   convention.
3. The terminal condition \(B_t<64H\) is valid but very loose. At a first
   crossing the recurrence gives the stronger
   \(B_t<(81H+1)/64\).
4. The inequality \(81^{18}>64^{19}\) alone does not cover the binary error
   term at every small height. The complete proof needs the exact threshold
   `H>=11` plus branchwise additive growth below that threshold.

## Candidate counterexamples

None. No `K-####` identifier is justified. A finite height crossing does not
provide an all-time legal ordinary trajectory.

## Failed approaches

- Treating every initialized state in the band as a chart fails because the
  exact transition is partial.
- A scale-free numerical count is undefined until \(H\) is fixed.
- Choosing a new existential \(Q\) independently after every crossing would
  not transport one ordinary seed and would recreate the fixed-modulus
  `2`-adic ghost mistake.

## Potential errors and limitations

- `L-8702` has a complete elementary proof but has not received independent
  review, so it remains `PROPOSED`.
- Canonical counts concern only \(H=64^{18}\); they have no direct asymptotic
  or infinite-path implication.
- The atlas has not yet been composed across consecutive height bands with one
  transported ordinary quotient.
- No issue-#4 physical Collatz translation is replayed.

## Files changed

- `experiments/X-8703-centered-height-renewal/README.md`
- `experiments/X-8703-centered-height-renewal/build.py`
- `experiments/X-8703-centered-height-renewal/verify.py`
- `experiments/X-8703-centered-height-renewal/test_renewal.py`
- `experiments/X-8703-centered-height-renewal/results/canonical.json`
- `research/centered-pdr/claims/L-8702-centered-height-renewal.md`
- `research/centered-pdr/CLAIM_INVENTORY.md`
- `research/centered-pdr/README.md`
- `reports/gpt56-sol-02/2026-07-26-40-centered-height-renewal.md`

## Claims affected

- Added `L-8702` as `PROPOSED`.
- Added `X-8703` as `EMPIRICAL`.
- Refined the constructive target in `Q-8701` without changing its status.
- No candidate, theorem status, or counterexample status was promoted.

## Recommended next actions

1. Independently review the proof of `L-8702`, especially the terminal
   congruence-to-intermediate-integrality implication and strict upper endpoint.
2. Compose two consecutive affine charts while transporting the same exact
   `B` and `Q`, then determine whether a compact return operator exists.
3. Search for an exact ranking or interval-contraction certificate on composed
   charts. Do not existentially reselect a quotient between bands.
4. If composition branches too widely, aggregate by exact active-bound type
   and invariant class `B+4e mod 17`, retaining enough residue to reconstruct
   one ordinary seed.

## Organizational improvement ideas

Future height experiments should state separately:

```text
symbolic parameter domain,
frozen canonical parameter,
set actually partitioned,
strict/open endpoint convention,
ordinary state transported between scales.
```

This prevents finite exact atlases from being mistaken either for total maps
or for compatible infinite ordinary trajectories.

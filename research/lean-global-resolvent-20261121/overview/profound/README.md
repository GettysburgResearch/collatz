# The next global step: same-source mergers and retained boundary mass

**Checkpoint 10. Full Collatz remains OPEN.** This pass pursued three
parallel global attacks against the refreshed repository and a recent
literature criterion. It produced a complete unbounded merger family,
an all-depth first-crossing bound, and an exact distinction between endpoint
estimates that erase an escaping source and a shrinking-weight window that
retains it. Four new proof modules contain **50 audited public statements**;
the stronger infinite-sum and asymptotic conclusions retain the written
proof boundaries below.

## 1. A real repair of the remaining head-three induction branch

PR177's refreshed head-three note exhibited a smaller merger partner whose
newly extracted source certificate had a larger grade. Checkpoint9's
same-source target induction removes the need for that replacement.

For the original supplied query

\[
S=4q,\qquad 3q+1=8u,\qquad n=8q-1,
\]

put `v=9u-1=2^h r`, where `h>=1` and `r` is odd, and
`x=2v-1`. The new Lean module proves `0<x<n`, `T^4 n=4v-1`,
and the exhaustive physical split:

| Phase | Actual shortcut transport | What is paid |
|---|---|---|
| `3^(h+1)r=4z+3` | `T^(h+8)n=T^(h+3)x=3z+2` | The smaller target closes the original query at its unchanged source grade. |
| `3^(h+1)r=4z+1` | `T^(h+8)n=9z+2`, `T^(h+3)x=z` | The smaller partner proves `Basin z`; `Basin (9z+2)` remains open with the original source constraints. |

Every complete source prefix `[3,3]`, with any remaining tail, is in the
successful phase:

\[
T^{10}(8q-1)=T^5(18u-3),\qquad 18u-3<8q-1.
\]

The opposite phase is not a hidden successful rule: Lean also proves that
`h>=3` forces `z>n`. Neither the basin proof of `z` nor the numerical
decrease to `x` supplies an unpaid larger interval around `z`.

[Proof and exact residual](HEAD_THREE_TARGET.md) ·
[Lean module](lean/Collatz/HeadThreeTarget.lean).

## 2. A sublinear first-crossing kernel with no depth cutoff

For `H>=2` and `q>=H`, retain boundary integers `n<H` that immediately
cross the floor, remain above it, and first hit `q`. Their actual branch
coefficient is `omega_q(n)=3^s/2^A`. The whole late boundary satisfies

\[
\sum_{\substack{n\in E_H(q)\\A_q(n)\ge\lfloor\log_2H\rfloor}}
 \omega_q(n)
\le\frac{3q}{2H-1}(6499+2H^{19/20}).
\]

Every boundary source is late if `q+1>H(3/2)^floor(log_2 H)`.
Taking `H=2^floor(log_3 q)` therefore controls **all** hitting clocks and
all valuations at once:

\[
\boxed{\sum_{n\in E_H(q)}\omega_q(n)
 =O\!\left(q^{1-(\log_3 2)/20}\right)
 =O(q^{0.968454\ldots}).}
\]

Each boundary source is charged once at its unique first hit. The bound
does not identify distinct upstream original sources or count additional
circuits around periodic targets. Lean verifies the actual-map and
finite-cardinality interface; the displayed power saving substitutes the
separately pinned elementary native no-descent count.

[All-depth proof](ALL_DEPTH_FIRST_CROSSING.md) ·
[Lean module](lean/FirstCrossingBound.lean).

## 3. The potential carried into that boundary is the remaining issue

The ordinary canonical inputs give `PG=G`, `h=G/q`, and a harmonic
reference `delta nu<=h<=nu`, with `delta=exp(-200/3)`. On the nonperiodic
odd-unit domain define

\[
\mathcal K(q)=\sum_{n\in E_{H(q)}(q)}\omega_q(n)G(n),
\qquad H(q)=2^{\lfloor\log_3q\rfloor},
\]

retaining the unit boundary sources. Prefix-free harmonicity gives
`K(q)<=G(q)`. If one fixed source `p` escapes, its last odd upcrossing
below `H(q_i)` along its actual forward orbit gives a boundary atom with

\[
G(n_i)\ge\delta\nu(p)\frac{2H(q_i)-1}{3},\qquad
\boxed{\mathcal K(q_i)\ge\delta^2\nu(p)q_i.}
\]

Thus the sublinear unweighted kernel and a linear weighted contribution
can coexist. The arriving potential cannot be replaced by one. Using
PR175's global finite-forward-orbit cover, the precise source-qualified
criterion is

\[
\mathcal K(q)/q\to0\text{ on nonperiodic odd units}
\quad\Longleftrightarrow\quad
\text{every positive orbit is eventually periodic}.
\]

[Sparse boundary mass and proof](SPARSE_BOUNDARY_MASS.md).
The weighted decay is **OPEN**; this criterion allows additional cycles.

## 4. A shrinking endpoint weight retains the full theorem

The literature's all-centres squared-gain sum `W_t` detects escape.
We prove directly that multiplying each endpoint contribution by
`c^(-sigma)` makes

\[
W_t^{(\sigma)}\to0\quad\text{for every fixed }\sigma>0,
\qquad
\sum_{t\ge1}W_t^{(1)}\le4\pi^2/7.
\]

These are unconditional, including repeated cycle visits. A positive fixed
endpoint power removes an escaping source's signal. The complete
reciprocal-killing telescope is checked in Lean.

There is a different, source-preserving window. Let `B_t` be the
literature's occupation sum censored at the first hit of one. It retains
the original odd-source weight `p^(-2)` and each visit's factor
`(c/3^ceil(log_3 c))^2`, without the survival discount used in `W_t`.
We prove

\[
\boxed{
\sigma_t\ge0,\ \sup_t t\sigma_t<\infty
\quad\Longrightarrow\quad
\bigl[B_t^{(\sigma_t)}\to0\ \Longleftrightarrow\ \text{full Collatz}\bigr].
}
\]

In particular, the concrete sequence `sigma_t=1/t` retains both escapes
and additional cycles. If `t sigma_t->0`, the tilted and unweighted sums
differ by a quantity tending to zero. Finite source-tail inequalities
justify the joint limit. Lean checks the underlying actual-bin height
bound `c+1<=3^(t+1)(p+1)^2`; the limits and full criterion are written
mathematics with their finite ingredients reconstructed.

[Positive fixed tilts](ENDPOINT_TILT_CRITICALITY.md) ·
[Moving window and full-theorem criterion](MOVING_TILT_WINDOW.md) ·
[Survival-budget Lean](lean/SquaredSurvivalBudget.lean) ·
[Bin-height Lean](lean/BinHeight.lean).

An [exact rational evaluator](certify_moving_tilt.py) encloses each complete
finite-bin series at exponent `1/t`. It terminates by the proved bin clock
and bounds omitted **original sources**, without assuming their orbits
converge. The [bin-four enclosure](../../../../reports/2026-11-22-profound-step/bin4-enclosure.json)
is supporting computation, not an asymptotic-decay claim.

## 5. What to attack next

The most direct remaining target in this packet is a uniform bound proving
`B_t^(1/t)->0`. Fixed-positive-exponent decay, even summability, does not
provide it. The arithmetic alternative is to complete the failed
head-three carry while preserving the original supplied certificate and
then finish arbitrary interval coverage. The sparse-boundary route asks
for decay of the arriving canonical weighted mass, and still needs cycle
exclusion if used alone.

[Concrete standalone research questions](STANDALONE_TARGETS.md) state the
objects, quantifiers, and first unsupported conclusion. None is presented
as a proved closure or as a free source reset.

## Evidence and reproduction

The [source and review ledger](SOURCES_AND_REVIEW.md) records the six
refreshed PR heads, direct literature reads, inherited evidence levels,
independent mathematical reviews, and the failed global steps.
[DEPENDENCIES.json](DEPENDENCIES.json) pins every compiled source.

From the repository root, run:

```sh
python -X utf8 -B research/lean-global-resolvent-20261121/overview/profound/check_profound.py \
  --lean /absolute/path/to/lean-4.34.1/bin/lean \
  --mathlib /absolute/path/to/pinned/mathlib4 \
  --out /absolute/path/to/empty/fresh-output \
  --receipt /absolute/path/to/checkpoint10-lean.json

python -X utf8 -B research/lean-global-resolvent-20261121/overview/profound/certify_moving_tilt.py \
  --bin 4 --sources 667 --precision-bits 24 --output /absolute/path/to/bin4-enclosure.json
```

The optional dependency mirror is authenticated against the pinned Mathlib
objects before use. The fresh integrated replay covers 25 jobs: eighteen
reused project imports, four new proof modules, and three separate audits.
The first-crossing module carries its own audit. The 50 new audited
statements comprise 13 merger/rank statements, 21 crossing interfaces,
eight survival-budget statements, and eight finite height statements;
this is not a claim of 50 independent advances.

The [execution report](../../../../reports/2026-11-22-profound-step/README.md)
separates Lean execution, written mathematics, finite enclosures, and the
required clean-checkout repository gate.

# OpenAI's November 24 mathematics release: useful bridges and their limits

**Collatz remains OPEN.** This packet connects selected implementation lemmas from the new OpenAI release to the repository's actual ordinary maps and frontier predicates. It supplies a new family of smaller-base mergers in every positive tower row, an exponential bound on clock failures in complete ordinary rows, and exact finite rank and potential interfaces. It also identifies concrete reasons several apparent routes to universal closure fail.

The positive merger result is more than a change of notation: it excludes arbitrarily large guarded inputs in every row using an actual smaller-base orbit. Its proof is an elementary sibling identity plus a ternary congruence construction. The difficult universal statement has not been obtained from the matrix exponent or Fourier lower bound. The elementary nature of the imported block-rank and Farkas steps is stated explicitly; their upstream association does not make the arithmetic conclusion deeper.

## Start here

| Question | Read |
|---|---|
| What changed mathematically in the Collatz program? | Sections 1–3 below, then [the tensor proof](tensor/README.md) and [clock proof](clock/README.md). |
| Which new OpenAI claims were actually examined, and in what model? | [Release and scope ledger](SOURCES.md). |
| Which proof ideas might transfer? | [Tensor geometry and simultaneous calibration](tensor/README.md#what-the-proofs-actually-use), [Fourier feedback and collision budgets](fourier/README.md), [exact optimization certificates](lp/README.md). |
| What can another agent import and run? | [Lean build and audit](formal/README.md), [finite replay harnesses](#reproduce-and-review), and the three concrete next obligations below. |

The release is pinned at `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, merged November 25, 2026 at 00:18:47 UTC; its manuscripts are dated November 24. This packet starts from Collatz main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Full source heads appear in [SOURCE_PINS.json](../../reports/openai-machinery-20261125/SOURCE_PINS.json). These references distinguish a reproducible assessment from claims about subsequently changed branches.

## 1. A real merger certificate in every positive tower row

The smooth-tower program assumes a first bad input `n=3^r w`: every positive smaller base `b<w`, at every power of three, is already good. An actual meeting of the orbit of `n` with any `3^j b` therefore rules this input out as that first bad tower. The original predicate and goodness transport are imported from PR192, without redefining them to make the new theorem easier.

For **each `r>0` and each supplied lower limit**, the compiled theorem constructs a base `w` above that limit and a comparison base `0<b<w` such that:

* `w` is odd and not divisible by three.
* The previous binary frontier guards hold: `v₂(3^r w+1)=1`, `2≤3^r`, and `3^r w≢85 mod 512`.
* The first odd successor `y` of `n` is a 3-unit and is **larger than the base `w`**. Removing powers of two and three from this first successor therefore does not supply the required smaller base.
* The two actual shortcut trajectories meet:
  `T(n)=T^(2·3^r+1)(3^j b)`.
* Consequently `¬SmoothCore.FirstTower w r` in the original PR192 interface.

Here `T` is the shortcut map, taking `n/2` on even inputs and `(3n+1)/2` on odd inputs. The usual accelerated odd map is `U(n)=(3n+1)/2^v₂(3n+1)`.

The mechanism is explicit. Put `h=3^r`, `B=(4^h−1)/3^(r+1)` and `m=2h`. Then `B` is a positive odd 3-unit. Choose

```math
4^h w+B\equiv0\pmod{3^m},\qquad 3^r w\equiv1\pmod8.
```

There are arbitrarily large such positive `w`. The Lean proof builds the solution one ternary digit at a time, preserving the binary class. Define `b=(4^h w+B)/3^m`; the estimate `3^m>4^h+B` gives `b<w`. The sibling identity

```math
3\bigl(4^h n+(4^h-1)/3\bigr)+1=4^h(3n+1)
```

gives the genuine merger, with the larger sibling equal to `3^(r+m)b`.

For example, `r=1`, `w=1811`, `b=159`, `j=7` give

```math
n=5433,\qquad U(n)=4075>1811,\qquad
T(5433)=8150=T^7(3^7\cdot159).
```

The meeting endpoint is the even integer `8150`; the eventual-convergence predicate transports through that endpoint in both directions. Its parity creates no missing implication.

**Coverage boundary.** For fixed `r`, the construction gives a progression of density `1/(8·3^(2·3^r))` among all positive bases. It is thin, and many bases remain outside it. This theorem does not prove that these individual inputs converge without the smaller-base hypothesis, does not eliminate every candidate, and does not prove universal convergence. The familiar sibling identity is not claimed as a new discovery. The useful addition is the explicit all-row construction, its surviving guards and its connection to the existing proof obligation. [Full proof and necessary resonance condition](tensor/README.md#positive-sibling-mergers-in-every-smooth-tower-row) · [native Lean theorem](tensor/TowerFrontier.lean)

## 2. What rank and the Fourier argument really contribute

An endpoint matrix keeps one row for every original source and its clock, and one column for every **actual integer** endpoint. Its rank equals the number of distinct endpoints. For two such batches, keep output tags to make them independent, then identify only equal integer outputs. The imported block-rank lemma gives

```math
\text{tagged rank}=\text{aligned rank}+
\#\{\text{distinct common endpoints}\}.
```

A strict drop is exactly an actual merger. The arithmetic construction in section 1 supplies such a drop, over every field, in the final theorem. This is a sound certificate interface; an independent inequality forcing a drop for an arbitrary frontier input is still needed. Endpoint incidence alone forgets integer height and fiber multiplicity, so a general tensor-price lower bound cannot fill that gap automatically.

The Fourier proof contributes a second genuine implementation lemma. A finite feedback system with invertible full operator `I−C` and its diagonally masked version, using the same input injection and readout, satisfy a rank-difference bound by the number of changed states. If the retained-source discrepancy is **diagonal**, rank counts the disagreeing sources. The new Lean interface states that diagonal equality as an explicit premise. A dense nonzero matrix can have rank one, and arbitrarily many different ordinary sources can reach one endpoint. Thus rank by itself cannot count bad sources.

The written collision construction is stronger than a small example: at fixed odd depth `k` and total halving time proportional to `k`, ordinary inverse fibers can have `exp(Ω((log k)^2))` distinct starts, in prescribed fixed ternary classes. The endpoint can be chosen to reach 1 in one further odd step. This refutes a general polynomial multiplicity cap for unweighted ordinary inverse fibers. These examples have small relative carry and only one convergence color, so they do **not** refute a cap after the project's high-carry or color-disagreement filters. An agent working on that filtered cap must retain the filter in the statement. [Construction, exact equations and checks](fourier/README.md)

## 3. An exponential complete-row clock bound, with a failed closure test

Let `S_k(a)` be elapsed shortcut time at odd return `k`. PR206's crossing test is

```math
(k+1)3^{6k}<2^{6S_k(a)}.
```

For every odd stride `d>0`, offset `m≥0`, and `n≥0`, examine the `32^n` ordinary sources `a_r=2(dr+m)+1`, `0≤r<32^n`. If `F` fail the test at `k=3n`, the compiled bound is

```math
108^n F\le3125^n,\qquad
\frac{F}{32^n}\le\left(\frac{3125}{3456}\right)^n.
```

The exact pressure identity behind it sums the weight `2^(t−J)3^J` over all `2^t` representatives in an odd-stride row and obtains `5^t`. The proof retains actual ordinary integers and the original odd clock, including its indexing after the first shortcut input. It requires neither random independence along an orbit nor a Fourier lower bound.

The uniform offset gives a written corollary: sources that never cross have upper Banach density zero within each eligible class modulo six. This says their fraction in long intervals tends uniformly to zero. It permits individual exceptional sources. The independent cycle condition in PR206 also remains open.

We tested a plausible attempt to finish the proof using PR207's balanced inverse populations. It fails at an exact hypothesis:

* Every source with `b>0` odd returns and total clock `2b` **passes** the crossing test at that same depth. It contributes nothing to the matching failure count.
* Later tests inherit the original `2b` clock; failure at the terminal does not transfer backward to the original source.
* Even before imposing failure or row localization, the union of the pinned terminal shells with depth `b≤9n` is too small to contradict the upper bound for `n≥9`. The exact integer comparison is in Lean.

This removes a proposed inference rather than disproving the renewal hypothesis. A successful replacement needs a lower bound on the **same original sources, same row and same clock**. [Complete proof, shell calculation and backward countercontrols](clock/README.md)

## 4. Exact optimization certificates and a universally failed ansatz

The OpenAI LP work suggests searching for a small exact certificate before a numerical potential, while retaining one common calibration of all later constraints. We import its actual Farkas implementation. For a finite graph with edge cost `c`, the connected theorem supplies either a rational potential satisfying `p(target)−p(source)≤−c` or a sparse nonnegative balanced circulation of positive cost. The Python harness returns and independently verifies these exact alternatives.

For ordinary odd steps with gap `g`, the control cost is `8−5g`. A fixed finite potential covering every transition would force eventual clock crossing because `2^8>3^5`. The global coverage is a mathematical premise, not a solver option.

Residue-only potentials of this form fail for **every modulus**. The real ordinary step `4m−1 → 6m−1` has gap one and the same residue modulo `m`, so it would require `0≤−3`. Scaling the multiplier preserves the original residue, gives ternary units, and moves the witness beyond any fixed floor. Arbitrarily long finite gap-one controls rule out a fixed-horizon residue-only repair. Those varying finite controls do not constitute one divergent orbit. [LP mechanisms, precise no-go and harness](lp/README.md)

## Three concrete next obligations

| Priority | Precise target | What would count as progress | What this packet already rules out |
|---|---|---|---|
| 1. Cover more actual smaller-base mergers | Given a surviving `w,r`, force an ordinary forward endpoint into a certified predecessor window `2^e y≡1 mod 3^(j+1)` and `2^e y−1<3^(j+1)w`. | A theorem for an explicitly larger source family, with actual clocks and a positive `b<w`; ultimately an exhaustive cover. | Merely duplicating endpoint tensors or counting independent blocks supplies no window occupancy. |
| 2. Make the deletion rank budget count retained sources | Construct a common transfer/readout whose discrepancy is exactly diagonal on the original source labels, and bound deleted states through all relevant depths. | A proved representation plus a summable budget in the source's original measure. | General low rank, unweighted inverse degree caps, and a different representative at each depth are insufficient. |
| 3. Turn finite certificates into an arithmetic family theorem | Use affine source parameters, exact carry conditions and a common finite set of observables to synthesize a certificate valid on whole progressions. | Symbolic coverage and exact coefficients, or a minimal infeasibility witness that improves the proposed ansatz. | A universal fixed residue correction already has actual expanding self-loops; per-query incompatible scalings do not give one potential. |

The more speculative geometric idea is a single tensor-price or LP calibration valid for every future query, with every failed compression charged to a bounded algebraic resource. The missing ingredient is a finite dimension/degree bound that survives new carries and retained source labels. The papers' compactness and tensor-power arguments apply to specified fixed formats or independent batches. Proving that format bound here would itself be a substantial result.

## Reproduce and review

The [formal project](formal/README.md) imports 5 OpenAI and 9 Collatz source files, all pinned byte-for-byte. It compiles eight new mathematical modules and audits 46 public local theorems plus seven imported interfaces. These counts include helpers and controls; they are not a count of independent advances. The headline upstream exponent and complexity proofs are source-qualified, not independently rebuilt in this packet.

From the repository root:

```sh
python -X utf8 -B research/openai-machinery-20261125/fourier/collisions.py
python -X utf8 -B research/openai-machinery-20261125/lp/certificates.py
python -X utf8 -B research/openai-machinery-20261125/clock/replay.py --depth 64 --direct 8
```

Each also runs under `python -O`. The individual files state their finite coverage. For the Lean build and axiom audit use `formal/check.py`; for repository integrity run `tools/validate.py` in a clean complete checkout.

Independent reviews: [tensor and native frontier](../../reports/openai-machinery-20261125/FOURIER_REVIEW.md), [Fourier and clock](../../reports/openai-machinery-20261125/TENSOR_REVIEW.md), [native tower connection](../../reports/openai-machinery-20261125/CLOCK_REVIEW.md), [LP](../../reports/openai-machinery-20261125/LP_REVIEW.md). [Execution evidence](../../reports/openai-machinery-20261125/README.md) keeps build, bounded replays and repository integrity separate.

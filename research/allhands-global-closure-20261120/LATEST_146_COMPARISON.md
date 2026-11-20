# Publication-time comparison with the refreshed PR146

**Status: source inspection and overlap assessment, not independent validation of every new source theorem.**

Initial source for our frozen depth-two note:
`6863d298187af8b2619efbf78cc4b0aa8e627393`.

Refreshed PR146 inspected before publication:
`e238c63a5d57f96bb063b7472498d1977df51951`.

Files read at the refreshed pin:

- `research/upper-bit-mergers/WITNESS_TRANSFER.md`
- `research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md`
- `research/upper-bit-mergers/RANK_THREE_MERSENNE.md`
- the diff of `research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md` against the initial pin.

## Essential overlap: do not claim the family or depth obstruction as new

The refreshed source already contains the central depth-two family and its consequence. Our `DIRECTED_DEPTH_TWO.md` is an independently derived and independently replayed reconstruction of that part of the current source, with an additional explicit whole-orbit separation formulation. It must not be presented as a new discovery of the family, the rank-only obstruction, or the exponential residual problem.

| Frozen local statement | What the refreshed source already contains |
|---|---|
| D2-1: all `x=16k+1>1` with first odd hitting depth two are indexed by `9k+1=2^(6m)` | `WITNESS_TRANSFER.md`, “The odd terminal input and the shortest witnesses,” states this exact characterization and the stopping time `6m+4`. |
| D2-2: the companion reaches `2^(6m+1)−1` after four steps | The same section gives the general four-step companion `2^(a+1)u−1`, with `9k+1=2^a u`, and specializes to `u=1,a=6m`. It also gives the ensuing `6m+1` odd steps to `3^(6m+1)−1`. |
| D2-4: bounded known odd depth does not bound the companion's required odd clock | `WITNESS_TRANSFER.md` already proves this qualitative obstruction, including polynomially many controlled witnesses in every fixed relative interval. `BOUNDED_RANK_TRANSFER.md` extends it to arbitrary fixed ranks and supplies explicit logarithmic lower bounds. |
| No lifted affine merger on the rank-two family | This is stronger than a finite deadline statement and is already proved in `BOUNDED_RANK_TRANSFER.md` for **all** rank-two and rank-three first arms. |

The refreshed witness-transfer note additionally proves a necessary lower coefficient `1+log_2(3)` for a universal linear transfer bound between ordinary stopping times, and records a context-free-language obstruction on the two-odd-step family. Those are source claims, not results of our checker or new contributions from this pass.

## What the local note makes separately explicit

Our D2-3 writes out the complete known orbit of

`n=(16*64^m−7)/9`,

proves its exact maximum `(8*64^m−2)/3`, and compares it with every tripled-arm value through clock `6m+4`. This yields

`T^i(n) != T^j(3n)` for every `i>=0` and `0<=j<=6m+4`.

The quantifier includes arbitrarily late first-arm clocks, not just synchronized clocks and not only affine lifted mergers. We did not locate this exact maximum/separation formulation in the three refreshed files. It is an explicit corollary and verification of the same elementary family, not a claimed major new mathematical direction or a priority claim. Our checker also directly verifies the final odd-event exit valuation and the full known orbit rather than assuming eventual convergence of the companion.

## The source has moved substantially beyond the rank-two family

`BOUNDED_RANK_TRANSFER.md` gives:

- a bilinear clock bound for two parity words;
- an effective bounded-rank decision for the existence of a lifted merger;
- complete exclusion of lifted mergers at source ranks two and three;
- infinite matched rank-four families, and examples at every larger fixed rank;
- a signed-rational test deciding the eventual lifted-merger alternative on a fixed first-arm certificate template;
- automatic recognition and eventual quasipolynomial counting for pairs with two fixed odd-rank budgets.

`RANK_THREE_MERSENNE.md` gives a stronger residual embedding: every Mersenne exponent `q>=819` is represented by a known first arm of exact odd depth three; eighteen fixed signed words cover the exponent classes. It also states a version with an arbitrary supplied odd ternary-unit target t. The short-exponent replay and the source's claimed Lean verification were not rerun here. Convergence of the rank-three companion family remains open in that source.

The inspected change to `THREE_RAY_ONE_SIDED.md` adds a pointer stating that the reverse implication alone also suffices, proved in `REVERSE_BASIN.md`. This comparison did not independently inspect that proof and does not extend a verification verdict to it.

## Publication scope

The mathematical argument and checker are unchanged. The depth-two note
received an attribution-only preface, and its independent reviewer checked
that diff and recorded the new file hash. It is presented as an independently
reconstructed source mechanism plus an explicit whole-known-orbit clock
separation. The overview credits the stronger bounded-rank and rank-three
results in the refreshed source.

The open uniform-J attempt is separate. Neither this comparison nor the refreshed source statements read here supplies our missing legal low-exponent reduction or a smaller-core supplied-source routing bound. No full Collatz proof is asserted.

## Comparison with the other two routes

The separate [reverse-basin comparison](LATEST_REVERSE_COMPARISON.md)
explains why the pure-power reduction supplies no bound on prime creation:
one prime at the initial state is different from bounded support along the
whole actual trajectory. The directed descent includes inverse ordinary
steps, so the positive correction used in the peak theorem cannot be
applied to that augmented path as if it were an ordinary forward segment.

The analytic agent also inspected `BASIN_PHASE.md`,
`GROWING_ADDITIVE_GAPS.md`, and `DEEP_REVERSE_BASIN.md` at the same refreshed
head. The almost-everywhere coalescence estimates still leave a logarithmic
loss that does not establish a finite harmonic or 0.84 oriented defect
moment for a separating invariant. Estimates for varying starts and offsets
do not become that fixed-component moment statement automatically.
The stopping-phase label K changes by plus or minus one on ordinary steps;
it is not a T-invariant label f and cannot be substituted into DC1.

The restricted reverse-basin paths point toward 1. They do not by themselves
provide the bounded reverse returns needed to replace the circulation by
one supported only on those restricted tripling sources. Thus the refreshed
work sharpens the remaining implications without supplying the moment or
prime-support upper bound missing from this packet.

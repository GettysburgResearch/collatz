# Third six-hour checkpoint: exact conditional consumer and source probes

This review concerns the files frozen in `THIRD_MANIFEST.json`. Collatz remains
unproved. Every full-problem conclusion in the new Lean code retains an
explicit unresolved premise.

## Rational finite-sum proposal: conditional theorem verified

The root constructed and compiled the exact rational weight
`c_e=(134/25)*(5/14)^e`. Direct arithmetic gives the ternary integrated ratio
`134/135` and total geometric integral 135. The infinite Haar integral and the
identification with the increasing ordinary finite sums are written arguments;
Lean checks their finite numerical identities only.

`RationalGreen.lean` defines each finite sum directly over actual positive odd
sources and their actual accelerated iterates. The public hypothesis
`FiniteGreenBound` requires one rational constant for every finite depth,
source-height cutoff and positive odd terminal integer. A source's own path is
one nonnegative summand, so the hypothesis bounds its normalized squared weight.
The checked coefficient inequality makes that weight increase by at least
`201/200` at every departure from a state at least 13. An infinite such path
contradicts boundedness. The code then uses checked small trajectories and exact
odd normalization to conclude convergence under the usual full Collatz map.

`PotentialAssembly.lean` contains that full map and a separate generic positive
bounded potential theorem. Neither potential existence nor the finite-sum
bound is proved. No assertion that a Haar-integrable function must be bounded
on ordinary integers enters the argument.

The root also checked the mathematical strength of the gate: write the exact
coefficient as `t_*(3/2^e)^p`, with `p=log₂(14/5)` and `t_*>1`. Finiteness at 1,
together with the retained uniform simple-path reciprocal floor, already
implies a uniform logarithmic odd first-hitting-time bound on every terminating
source. This extra quantitative demand is stated in the proposal. The cited
slow-family results do not refute every logarithmic coefficient; they do not
prove this upper bound either.

## Tilted Green analysis: written identities and explicit obstruction

The root reconstructed the Haar geometric sum, ordinary source formula,
high-cycle multiplier and escaping-ray lower bound in `TILTED_GREEN.md`.
The arbitrary affine images of the negative fixed center -1 retain infinite
Green value, and after a nonlegal exit their even denominators strictly grow.
The explicit family `2^(-d)*((3/2)^(h+1)-2)` is dense in the positive real and
ternary-unit product: a prescribed ternary residue fixes `d` in a progression,
and an irrational real rotation chooses `h,d`. None is an ordinary positive
integer. This rules out a local envelope, without refuting an integer-only
bound.

The source-height estimate for a specified complete negative shadow follows
from `2^(L+1) | b*x+a`. Summing over the corresponding ordinary progression
bounds every subsequent suffix simultaneously, because the deterministic map
sends a source to one target. No assertion that every troublesome positive
word has such a shadow is made. The Lean file verifies finite identities and
inequalities, not density, summability, or the pointwise Green conclusion.

## Poisson probe: exact written transform, numerical normalization check

The root checked the affine scaling, the odd source congruence modulo
`2^(d+1)`, and the factor `pi/2 * 2^(-d)` in the Fourier formula. The original
geometric law is preserved. The absolute ordinary-label bound follows from
the zero mean of the real seed; it permits passage to the orbit-classification
limit. The positive escape clause retains the cited reciprocal packing input.

For a compact positive Fourier band, the exact analytic row is
`pi*exp(2*pi*i*c*(x-a))*exp(-2*pi*c*s)*g(x+i*s)`. High order interpolation zeros
on the odd lattice give the claimed uniform finite-depth error. This reads an
actual specified multiplier; it does not make the signed Fourier sum small.
The remaining short-clock signed cancellation is explicitly open.

The root replayed `check_poisson_probe.py` in both normal and optimized Python.
Their full 20-row TSV outputs match each other and the retained table. The
integer residue construction and gap replay are exact; the two independent
sums use floating point. Analytic truncation tails and a separate empirical
roundoff allowance are enforced. `escape/poisson_root_replay.json` therefore
calls this a numerical formula check, not an interval certificate.

## Cycle surgery: complete denominator and asymptotic scope

Eliminating the unchanged suffix from the two affine fixed-point equations
gives `A*D'*(x-x')=b*K`. Since `A` and `b` are units modulo `D'`, clearing the
new rational fixed point is equivalent to clearing `K/D'`. This gives the
whole reduced denominator, without a prime-independence assumption. The Lean
file checks the identity and simultaneous divisibility.

The sublinear-edit asymptotic additionally retains the cited logarithmic-form
lower bound for `|2^h-3^p|` and the earlier minimum carry cap. A cycle minimum
is polynomial in its length, and a cut can grow by at most
`2^((1-log₃2)*h+O(log h))`: there are at most `h*log₃2` odd increases and the
full-lap correction product is polynomial by distinctness of positive odd
states. Consequently a nonzero edit discrepancy has size small enough to
leave an exponential denominator. The original integer cycle is not excluded.

## Executed formal checks

`LEAN_THIRD.json` records all thirteen modules and 112 public declarations.
Automatic implicit variables are disabled and warnings are errors. All axiom
inventories contain only `Classical.choice`, `Quot.sound`, and `propext`; no
`sorryAx` or added mathematical axiom occurs. Fresh project objects are built
against Lean 4.34.1 and pinned Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The missing cached
`Mathlib.Tactic.Field` object is rebuilt from that source in a fresh temporary
overlay, whose source hash and exit code are recorded. Other pinned dependency
objects are reused. Repository integrity checks and publication receipts are
separate from these mathematical verdicts.

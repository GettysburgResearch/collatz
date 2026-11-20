# Review of the latest closing interfaces

**Disposition: the local derivations below pass, with the preceding
PR146/164 results retained as source-qualified inputs.** The primary AI
agent read the full latest PR146 sieve and seed/multiplier notes and
reconstructed the local arithmetic and energy implications. No review
of every statement in those PRs is implied. The closing result is still
OPEN.

## Frozen artifacts

- `CLOSING_ENERGY_INTERFACES.md`, CI1–CI4:
  `7ec342f0d1d4cc325a43eb7065f5a1a6e64cdd02dfca8a816bc5b78108ef428e`.
- `LATEST_FIVE_REDUCTION_BOUNDARY.md`, Sections 1–3:
  `ebe5eefcc029653b87dcd7581fb3c633caadad439b67fc3a977237c13e319fef`.
- PR146 source head:
  `fd991063721e9c157d318e40bb20131762f7d750`.
- PR164 domain source head:
  `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`.

The paired-prefix cancellation theorem has its separate independent
[localization review](HOMOGENEOUS_LOCALIZATION_REVIEW.md). The unit
return arguments and expanded renewal likewise have separate reviews.

## CI1: exact cancellation, not a new loss estimate

The selected lift `sigma(q)=(2^L q-7)/9` lies in `49 mod64`, is positive,
and is a ternary unit after the stated choice between exponents six
apart. The difference between the two candidates is a unit modulo three,
so both cannot be excluded. The paired two-input words are actual paths
with `U^2(sigma(q))=q`, proving injectivity and exact equality of defects.

For each endpoint, write `r_q=(q/sigma(q))^s`. The source contribution
is exactly `r_q` times its endpoint contribution. Returning to the
endpoint uses exactly `r_q^(-1)`. A full positive inverse-fiber kernel
contains this source and hence cannot make this round trip smaller than
the original endpoint charge. The proof correctly allows omission of
the known zero-defect endpoint 1 when applying a contributing-endpoint
kernel bound; endpoints at least 5 already establish the limitation.

The large-clock sufficient progression begins with exponents `(1,3)`.
It therefore avoids both the initial-two ladder and the three new
initial-`(1,1)` families. Its finite-energy equivalence with the full
domain is the pinned localization interface. No finite upper bound is
derived by restating that equivalence.

## CI2–CI3: the adjacent remainder and its actual summation domain

The reverse triangle inequality used is the ordinary triangle inequality
`j_a(q)<=e(x)+e(q)`. The full inverse fiber has normalized harmonic
weight at most `4/(8-1/5)=20/39` for contributing endpoints. At `q=1`,
the transported `e(q)` term is zero, while the original adjacent charge
is still bounded by `e(x)`. Thus positive summation gives the displayed
bound on `J(X)` with the cutoff `X/2` on its transported charge.

Since the high-valuation domain and `R_12` are disjoint, the upper factor
`59/39` follows. Conversely ER4 gives the factor 8 by finite-cutoff
subtraction. The equivalence of finiteness does not assume summability
in advance.

For the dyadic formulation, every source in `[2^k,2^(k+1))` has reciprocal
height between `2^(-k-1)` and `2^(-k)`. This proves the factor-two
equivalence of the weighted residual sum and the dyadic charge series.
Outside-core visits along one source, or counts of segments at fixed
cores and defect count, do not yet provide these all-source weights or
the requisite assignment with controlled multiplicity. That is an
identified missing step, not a purported counterexample to a future
support-sensitive argument.

## CI4: source-qualified row recursion and the critical retained moment

The pinned sieve explicitly constructs a finite directed dependency path
for every discarded eligible index. Reading it from `Y(k)` to 1, ordinary
edges preserve the invariant label. Each comparison arrow is
`Y(j)->X(j)`, whose positive increment is precisely bounded by `delta(j)`.
For `0<=g<=1` and `g(1)=1`, telescoping gives

\[
\delta(k)\le1-g(Y(k))\le\sum_j N(k,j)\delta(j).
\]

This uses the actual path and its repeated query occurrences; a mere
logical least-failure argument would not justify the displayed metric
row inequality. The pinned source provides that stronger constructive
path. Its antecedent bound implies `j<5k/8` in the index coordinate.

On the retained indices, the source's dyadic count gives a weighted
bound proportional to `sum_h 2^(h(rho-s))h^(-3/2)`. This converges at
`s=rho` as well as above it. The lower cardinality examples include
solved comparisons, so they cannot establish divergent defect energy
below `rho`.

If the proposed weighted column bound were true, reordering nonnegative
terms with the cutoff retained would give the claimed renewal for the
directed energy. That column estimate is explicitly **not proved**.
Finite row lengths and shrinking children do not control incoming
multiplicities from all starting indices. A separate energy propagation
or direct rigidity theorem is also needed. The direction of PR163 FE1
cannot be inverted, and the harmonic PD input cannot be discarded.
These conditions remain visibly conditional in the frozen note.

## The latest Mersenne comparison and the core-escape corollary

For the specified source, `q=(B-1)/5` and `S=3B/2` give
`5U(q)=S+1` and `U(5q)=S-1` by one exact odd transition on each arm.
The supplied least-failure hypotheses certify the first value, not its
neighbor minus two. The known initial target shifts have core one and
all valuation-one edges; they belong precisely to RU's degenerate
exception. A later bounded-defect return is not established.

The stated PR164 mismatches are exact parity and residue consequences
of its advertised guards: the actual parameter has even `k=2m` and
`m=7 mod16`. This audit concerns those direct applications only, not
all possible future compositions.

Finally, for a fixed endpoint and a fixed proportional seed, the lifted
target path has exactly `p` odd transitions. At exponent `b>=2` its last
division is a defect. RU2 therefore counts the paths from each fixed
source core to the fixed terminal core; a finite source-core family
gives the stated factor `|Q_0|`. Distinct lifts have distinct starting
integers. Hence only finitely many can belong to any fixed finite family
of shifted cores, which is exactly the asserted escape conclusion.
This independent reconstruction was also confirmed by the five-transport
agent. It creates no ordinary merger between the two unknown futures.

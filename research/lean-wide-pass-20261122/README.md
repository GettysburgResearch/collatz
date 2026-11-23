# A wider attack on actual transport, complete witnesses, and inverse potentials

**Full Collatz remains open.** This pass starts from PR180 at
`d0349de2108abb7c8fb8393c086610e3372df116`, surveys the repository's research
map and correction record, and freezes an inventory of **all 121 open pull
requests**. Detailed source reading is scoped in the three proof notes
below. The inventory is not a claim that every theorem in every branch was
independently reviewed.

The latest changes included PR177's alphabet-four reduction, PR185's physical
word erasure, PR183's actual entrance renewal, and updates to PR175 and
PR178. Three parallel attacks pursued the global step from these different
directions. The new packet contains **three Lean modules with 22 public
theorems**, alongside written analytic deductions and their explicit
remaining estimates.

## 1. A uniform upper bound on actual marked visits

For the accelerated odd map `U`, let `M(n,N)` count visits to the forced
marked band among the first `N` odd states. There is an absolute constant
`C` such that

\[
M(n,N)\le C\frac{N}{\log(N+2)}
\]

for **every positive odd source and every finite injective prefix**.
The previous density-zero result had an orbit-dependent eventual horizon.
The new finite estimate has no such horizon and needs no predecessor-density
or joint-mixing input.

`ReturnSynthesis.lean` checks the explicit finite Fourier denominator,
Fejer-kernel counting bound, and unchanged-source weighted accounting.
The optimization to the displayed logarithmic rate is written in the note.
It also gives an actual discounted marked occupation bound of order

\[
\frac{\|\mu\|_1}
 {(1-r)\log(1/(1-r))}
\]

before first repetition, retaining each original atom and every endpoint
collision. The corresponding cycle contribution is stated separately.

**The full reference measure does retain cycles.** If the original measure
has finite fourth logarithmic height moment, then for every `eta>0`,

\[
\alpha_\eta=\sum_{j\ge0}
 \frac{\widetilde\nu_j}
 {(j+1)^5[\log(j+2)]^\eta}
\]

has finite fourth logarithmic moment. Here `tilde nu_j` is the **full actual
marked packet**, without deleting repeated sources. After a first repeat,
all later values lie in the earlier finite prefix; the coefficient tail
then cancels its fourth-power height bound. `RepeatedTail.lean` checks that
actual-map containment and height bound. The infinite measure summation is
a separately reviewed written proof.

This supplies an actual finite-moment reference for the newer return
program. It still needs a bound on the **aggregate mass arriving at each
endpoint under induced returns**. A comparison with just one later
occurrence of the same source is quantitatively too weak.

[Full return proof and remaining transport estimate](RETURN_SYNTHESIS.md) ·
[Finite return theorem](lean/ReturnSynthesis.lean) ·
[Retained periodic-tail theorem](lean/RepeatedTail.lean)

## 2. Physical erasure inside the complete supplied-witness induction

Write

\[
n=2^ku-1,\qquad x=2^{k-r}u-1,
\qquad 0<r\le k,\quad x>0.
\]

An actual endpoint identity with **independent clocks**,

\[
T^a(3^{k-r}u-1)=T^b(3^ku-1),
\]

gives the literal ordinary merger

\[
T^{k-r+a}(x)=T^{k+b}(n),\qquad 2x+1\le n.
\]

`WitnessSynthesis.lean` proves that this all-length erasure fits the latest
complete-source interval induction after exactly one physical source
halving. The entire supplied odd certificate is retained, and the exact
initial-even grade decreases. No new convergence certificate is chosen
without justification. The partner may be even, and deletion of the whole
initial run is allowed when it stays positive.

The module also checks the exact unresolved carry `(r,9r+2)`. A small
convergent example demonstrates why equal endpoint clocks would be an
incorrect completeness requirement. The main interface therefore admits
asynchronous clocks from the outset. A total successful dispatcher for the
remaining alphabet-four words has **not** been proved.

[Cross-branch witness synthesis](WITNESS_SYNTHESIS.md) ·
[Exact Lean interface](lean/WitnessSynthesis.lean)

## 3. Canonical potential provenance and complete clock sums

The potential lane combines the previous least-envelope construction with
the repository's ternary stationary-density and arithmetic energy work.
It identifies the canonical envelope almost everywhere with the normalized
stationary density and obtains uniform comparison of the ordinary envelope
with its harmonicization. It also bounds the inverse operator on finite
ternary cylinders while summing **all** prefix clocks, rather than leaving
an arbitrary clock cutoff in the statement.

The resulting estimate retains its resolution term. Neither almost-everywhere
identification nor a finite-cylinder bound is substituted for the missing
upper estimate at every ordinary marked point. The earlier stationary
source explicitly excludes an `L2` upgrade, and cross-component five-energy
still needs an arithmetic comparison.

[Potential and energy synthesis](ENERGY_SYNTHESIS.md)

## Research coverage and the closing steps still needed

The [source snapshot](SOURCE_SNAPSHOT.json) records every open PR's full
head, branch, title, and URL. The research map's ordinary-extraction,
coefficient/cycle, mass/transport, rank-merging, and representation routes
remain distinct. In particular, compatible finite prefixes are not an
ordinary all-time source, a sparse section is not survivor decay, and a
partial erasure language is not a terminating selector.

This pass isolates three concrete global comparisons:

- **Returns:** bound the actual aggregate returned packets by the constructed
  finite-moment reference at the critical return-count scale; retain the
  nontrivial-cycle alternative.
- **Complete witnesses:** cover the remaining alphabet-four source words
  with actual lower-grade mergers, including the unbounded carry phase.
- **Potentials:** retain a marked ordinary upper bound through the critical
  clock/depth limit, including targets that change along a forward path.

None is an axiom or a proved global premise in this packet.

## Reproduction and evidence boundaries

The [dependency manifest](DEPENDENCIES.json) pins six baseline source files
and three byte-identical vendor modules from PR178. The build uses Lean
4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.

```sh
python research/lean-wide-pass-20261122/check_lean.py \
  --mathlib /path/to/built/mathlib4 --lean /path/to/lean \
  --report-dir reports/2026-11-22-wide-pass
```

This recompiles the dependency closure and the three new modules into a
fresh directory, then audits all **22 new public theorems**. It checks
dependency source hashes and rejects nonstandard printed axioms. Warnings
are errors. The optimized asymptotics, infinite measure sums, and potential
analysis remain written mathematics; their absence from the formal replay
is recorded explicitly.

[Lean replay receipt](../../reports/2026-11-22-wide-pass/lean-check.json) ·
[Compiler and axiom log](../../reports/2026-11-22-wide-pass/lean-build.log)

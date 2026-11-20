# Research priorities and the standalone problem key

**OPEN targets; source-qualified comparisons.** The six question files
were prepared earlier in the same discussion and are preserved unchanged.
They omit the project name, links, and the payoff described here. This
separates the mathematical question from its provenance; it does not
hide a hypothesis, supply a theorem, or make recognition impossible.

The [original review and key](../../reports/2026-11-20-certificate-transfer-intake/initial-review-and-problem-key.txt)
is a frozen earlier assessment through PR160. The updates below account
for the supplied material and selected newer PR162--163 arguments. A
source-pinned theorem remains at its own stated status; no full branch
audit or new formal build is claimed.

## Current priority

1. **Adaptive certificate transformation.** Work from an actual finite
   certificate for the source, and permit the output to have larger
   rank and clock. Whole-class coalescence is useful but incomplete.
   The new explicit exceptional family shows why the density-one result
   cannot settle even all four-odd-step sources by that mechanism.
2. **Exact weighted arithmetic or positive occupation.** Retain the
   dependence between a finite word and its small endpoint, or prove
   an actual fixed-input occupation bound. Spatial first-hit capacity
   does not charge repeated time automatically.
3. **Functional-equation rigidity as a separate approach.** A genuinely
   new regularity or continuation theorem would matter. Signed Hardy
   vectors and approximate spectrum are not positive basin indicators.
4. **Prime and carry methods with an actual resource bound.** Necessary
   complexity growth is useful only with an opposing bound along the
   same fixed ordinary input. Bounded source odd rank alone cannot fund
   all exceptional carries in PR162's specified canonical mixed-base
   controller; this is not an exclusion of every representation.

The PDF provides a coherent alternate absorption proof, not a reason to
replace priority 1 by more random-bit simulation. A universal structural
absorption assertion is false even on convergent integer pairs.

## What each question would buy

| File | Logical payoff | What it does not establish alone |
| --- | --- | --- |
| [01: exponential certificates](questions/01_exponential_certificates.txt) | Full-equivalent target, using PR146's deep reverse reduction. | The implication remains open; an algorithm returning UNRESOLVED is not a solution. |
| [02: weighted representatives](questions/02_weighted_representatives.txt) | The stated moment bound suffices to exclude every nonperiodic positive orbit, using the pinned simple-path occupancy theorem. | It does not exclude nontrivial cycles. |
| [03: exponential divisibility](questions/03_exponential_divisibility.txt) | Equivalent to exclusion of every nontrivial positive odd cycle. | It does not exclude divergence. |
| [04: projected functional equation](questions/04_projected_functional_equation.txt) | Full-equivalent invariant-indicator formulation. | A mixed projected equation does not automatically supply two independent Mahler equations. |
| [05: explicit four-term family](questions/05_four_term_family.txt) | A concrete special case of 01; equivalent by finite paths to convergence of every `3^(27s-1)`. | It is not known here to imply full Collatz. Every source lies outside the PDF's coalescent set. |
| [06: restricted rounding map](questions/06_restricted_rounding_map.txt) | Excludes infinite ordinary paths in the stated two-return subsystem if proved. | It does not cover all return schedules or all ordinary trajectories. |

Questions 02 and 03 together would give full convergence through their
stated dependencies. The relaxed exponent `21/10` in 02 is deliberate:
the earlier review derives sufficiency from uniform path occupancy with
exponent `19/20`, since `(21/20)(19/20)=399/400<1`. More generally
`P_q=o(q^(40/19))` suffices. The full derivation, the primitive-trace tail,
and exact source pins are retained in the frozen original key. None of
these open moment estimates is inferred from the new density theorem.

## What the newer repo changes

### PR163: use the same globally least failure

At [PR163, `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md),
the conditional least-failure theorem uses the exact same least eligible
upper antecedent `X_*` throughout. It establishes

\[
176106n<X_*\quad\Longrightarrow\quad n\in C.
\]

It then excludes upper odd rank four from being the globally least
failure, and restricts the fourth valuation to

\[
\{1\}\cup\{3,5,\ldots,77\}\cup\{6,8,\ldots,70\}.
\]

This is compatible with our exceptional-family theorem: a pair can fail
affine coalescence while being handled by a different conditional
minimal-counterexample argument. The source does not prove every
rank-four target converges unconditionally. Do not change its global
minimum into a separate minimum within a chosen rank.

Its [residual kernel](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/REVERSE_CERTIFICATE_KERNEL.md)
leaves an unbounded certified parameter and unbounded input witness.
This is a useful next interface: find an ordinary path from the residual
to the supplied certified value or to the proven initial interval, with
every conditional upper antecedent below the same `X_*`. Uniformly
bounded words are not justified; the source has an explicit obstruction.

### PR162--163: preserve the analytic quantity

PR162's [occupation note](https://github.com/GettysburgResearch/collatz/blob/2279da37ac612dbe049777354cdedb3c0aa03282/research/creative-closure-20261120/occupation.md)
constructs finite first-hit information and spatial capacity, but leaves
the repeated-return occupation bound open. Its signed Hardy constructions
live on known-convergent inverse trees and do not identify a nonconvergent
positive component.

PR163's [five-slice comparison](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md)
supplies the source-pinned implication `D_3(1)<=10000 E_5(1)` for ordinary
invariant metric labels. The missing input is sufficient finite five
energy for a hypothetical separating label. Neither the PDF's density-one
merger theorem nor its excursion estimate supplies that upper bound.
The harmonic rigidity consequence also retains PR160's separately
source-qualified positive-density input, named PD in that work. This
packet does not verify PD or infer it from the unconditional energy
comparison.

## Assignment instructions

Give an agent one question file with a request to prove it, refute it,
or return a narrowly stated new partial theorem. Ask it to identify the
first unsupported implication in an unsuccessful attempt. Permit
arbitrarily long finite output certificates unless a bound is actually
proved. Retain exact integer realizations, positivity, and full
denominators throughout.

Do not assign "prove every relation-chain history absorbs" as the next
lemma. Do not infer failure from an exhausted search cap. A finite table,
an almost-sure result, and a theorem for every ordinary integer have
different quantifiers and different proof obligations.

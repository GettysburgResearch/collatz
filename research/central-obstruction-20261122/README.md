# Direct closure attempts at the remaining Collatz obstruction

**Full Collatz remains OPEN. This pass did not prove universal descent,
eliminate escaping mass, or exclude unrestricted positive cycles.** It aimed
at those closing implications directly. Two proposed universal descent
shortcuts fail on actual positive-integer configurations; the analytic and
cycle attacks retain precise unresolved steps.

The baseline is PR185 at `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`.
The fresh source snapshot includes the new PR175, PR176, PR177 and PR180
heads and the user-requested PR146. Its scope is recorded in
[SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json). This packet adds no assumption
of Collatz, GRH, universal source coverage, or vanishing escape mass.

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

The direct arithmetic goal is to prove, for every ordinary integer `n>1`,
an actual iterate strictly below that same `n`. The source-certificate
program must supply a successful return or smaller merger for every required
target; producing a complete source or a total arithmetic dispatcher does
not establish that assertion.

## What happened to the attempted closing steps

| Direct attack | Outcome | Exact record |
|---|---|---|
| Promote successful repeated-block shadows to universal target descent | A shadow in the actual final head-three residual enters a classical negative cycle with expanding multiplier. An all-parameter original-target no-descent window is proved in Lean. | [Reachable negative shadow](HEAD_THREE_NEGATIVE_CYCLE.md) |
| Choose a maximal source at the permitted grade, then use its complete clock as a universal descent deadline | False even after allowing every lower-grade and equal-grade source replacement. The exact extremal source is 1092, with completion clock 23; target 2047 first descends at clock 58. | [Extremal source clock](EXTREMAL_SOURCE_CLOCK_FAILURE.md) |
| Use actual inverse-height laws or adjacent coalescence to force the last-contact measure to vanish | No vanishing estimate obtained. A fixed original source retains a positive moving-root retracing probability; the required uniformity and arithmetic regularity are not supplied by the cited inputs. | [Escape attempts](ESCAPE_ATTEMPTS.md) |
| Use off-cycle immigration or extremal word rearrangement to exclude arbitrary positive cycles | No unrestricted exclusion obtained. The full renewal denominator normalizes to a positive average, while an adjacent unit transfer destroys the integer-cycle divisibility condition. | [Cycle attempts](CYCLE_ATTEMPTS.md) |

These are outcomes of attempted proofs. The two failed analytical routes
are not counted as new closing theorems, and the arithmetic counterexamples
are not counterexamples to Collatz.

## The reachable expanding shadow

For

\[
q=2048b+429,\qquad n=8q-1=16384b+3431,
\]

the actual source prefix `[3,2,2,1,2]` reaches `r=486b+103`, and

\[
T^{13}(n)=729r-865=729(r-1)-136.
\]

The source gap-two fixed point `r=1` therefore produces target shadow
`-136`. It lies on the classical negative seventeen cycle, which has
seven odd steps in eleven clocks. Its multiplier on the positive high part
is `2187/2048>1`.

The new theorem accounts for every intermediate phase, including the first
three halvings. If `486b+102=2^H d`, then

\[
\boxed{T^j(n)>n\quad\text{for every }1\le j\le13+H.}
\]

Every clock refers to the same original ordinary target. The explicit
written construction in the linked note supplies complete source
certificates for arbitrarily large `H`. Their terminal gap is large, so
existing high-gap source replacements remain available. A separate
kernel-checked complete source with all gaps at most four exhibits one
whole negative cycle in the exact bounded-four domain. No unbounded
bounded-four obstruction, failure of every source replacement, or infinite
positive orbit is asserted.

## Why maximal source selection does not repair the clock claim

The stronger policy was tested because it can discard difficult sources
that admit a larger replacement at the same or a smaller grade. Its full
interval conclusion still fails.

The source `1092=4*273` follows the complete odd word
`[2,3,3,3,1,2,3,4]` after two initial halvings, so it reaches one in
23 ordinary clocks. At its grade, 1092 is the globally largest complete powered source; every
strictly lower grade supplies a source at most 820. This statement covers
all certificate lengths and terminal padding, using the already proved
backward-closed one-gap-four tree.

Consequently `2047` belongs to the genuinely new interval

\[
2\cdot820+1<2047\le2\cdot1092+1.
\]

Nevertheless every positive clock through 57 stays above 2047, and
`T^58(2047)=1067`. Thus the universal deadline fails even at a source that
cannot be improved by the permitted grade order. The written maximality
proof and the finite ordinary-orbit evidence have distinct scopes in the
linked note. This does not exclude a different smaller merger or a
source-return argument using additional information.

## What remains to be proved

A successful constructive route still has to show that every required
ordinary target obtains an actual smaller merger or a justified source
return. The negative-cycle window and the extremal-clock counterexample
must be handled by such a proof; neither can be discarded by the two
refuted shortcuts.

The analytic route still needs an estimate that removes an actual escaping
source atom. The cycle route still needs to rule out full-denominator
integrality for an arbitrary nontrivial positive cycle word. The present
packet does not add either missing conclusion as a premise under a new
name.

## Reproduce the new evidence

The replay compiles only the new modules and their actual dependency
closure, with the pinned Lean 4.34.1 and Mathlib revisions. It checks public
theorem axiom reports, executes the new exact controls in normal and
optimized Python, and runs the required repository gate in a clean complete
checkout. It does not rerun unrelated earlier research packets.

```sh
python -X utf8 -B research/central-obstruction-20261122/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --build-dir /absolute/path/outside/the/checkout
```

The independent arithmetic review and published-checkout execution receipts
are kept with this packet and in
`reports/central-obstruction-20261122/`. Compiler acceptance applies to the
stated Lean declarations, not to the still-open universal conclusion or to
written analytic inputs.

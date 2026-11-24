# Direct attempts at the universal closing step

**Status: OPEN. No universal descent, exclusion of every nontrivial cycle,
or Collatz proof was obtained.** This packet starts from PR182 at
`9b02334f27ff59694a91fe7f018e0aaabad7620b`. Its purpose is to record three
attempts to discharge the remaining universal assertion, including the exact
inferences that failed. These failures are not counted as a proof of that
assertion or as a smaller unresolved exceptional set.

The maps are the positive shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\qquad U(q)=\frac{3q+1}{2^{v_2(3q+1)}}\quad(q\text{ odd}).
\]

## The target kept fixed

If convergence fails, choose its least positive ordinary counterexample
\(q\). Every smaller source converges. A closing argument must produce an
actual forward visit from **this same source** to a smaller positive integer,
or to the finite forward hull of those smaller sources. It must also handle
the possibility that the bad component contains a nontrivial positive cycle.
An escaping-source argument alone does not do that.

The newer critical section in PR197 gives cofinal marked predecessors and
a power-sized drop from each such predecessor. The attempted induction here
asked whether minimizing in the original component makes that drop beat the
original minimum. It does not: minima at an odd-clock level have next-odd
valuation at most two, whereas large critical marks require a much larger
valuation. The critical predecessors are necessarily nonminimal at their
levels. [Exact fixed-floor argument](FIXED_FLOOR.md).

## The attempted global ranks

A valley consists of all consecutive odd shortcut inputs followed by all
consecutive even inputs. For type \((a,b)\), its map is

\[
z=\frac{3^a y+3^a-2^a}{2^{a+b}}.
\]

The valuation of the affine fixed-point defect decreases by exactly
\(a+b\) while that type is held fixed. We tried to turn this into a global
rank, first by charging the current type, then by summing charges over its
entire inverse tree, and finally by taking a rational-height-normalized
supremum.

The ordinary family

\[
512t+91\longmapsto576t+103\longmapsto972t+175
\]

has types \((2,1)\) and \((3,1)\). The first source reservoir is always
five; the next reservoir is \(6+v_2(11t+2)\), hence unbounded. The first
map also increases ordinary height. The attempted local rank therefore
fails on actual positive integers.

An infinite nonnegative atomic charge does not repair the argument under
the stated summable rational-height hypothesis: ordinary CRT witnesses
force every inverse image of a charged center to receive at least the
same weight. The first generation already has infinitely many distinct
images. The full negative-rational supremum is finite, but on positive
odd inputs it equals \(\log_2(n+1)\); its strict-return assertion is the
original first-descent problem again. A restricted tree remains an open
candidate. [Complete rank attempt and limits](GLOBAL_RANK.md).

## The attempted integrality contradiction

For one fixed escaping source, we tried to use all its exact prefix
equations simultaneously in a Subspace Theorem argument. Finitely many
cuts leave a local product bounded below by a positive constant times the
escaping endpoint. Consecutive cuts do give an exponentially small product,
but in growing dimension. The genuine prefix vector already lies on many
explicit rational hyperplanes of height five; containment in exceptional
subspaces is therefore compatible with the proposed orbit. The particular
large-height quantitative theorem also does not apply in this dimension
range. [Exact products, heights and dependencies](INTEGRALITY.md).

We also tried to supply the missing tightness hypothesis in PR192's
positive-integer smooth-summand argument. A uniform carry-queue bound fails
even along arbitrarily long strictly increasing ordinary blocks: the start
can need only two smooth summands, while every subsequent state needs more
than any prescribed number. This follows from a fixed-dimensional unit
equation applied to an explicit ordinary family. The source changes with
the prescribed block, so it leaves the fixed-source asymptotic question
open. [Construction and exact scope](INTEGER_SUMMANDS.md).

## What was checked

Three GPT-6.2 Astra agents developed the distinct closing attempts, then
cross-reviewed the rank and arithmetic arguments. The coordinating agent
reconstructed their key equations, corrected the odd-input domain of the
supremum, narrowed the restricted-tree counterexample to the estimate it
actually refutes, and checked the exact ordinary refill family.

`lean/ClosureDiagnostics.lean` contains only the algebraic debit and inverse
identity, the literal ordinary refill family and its parities, the exact
source reservoir, the increasing-height calculation, the concrete
five-to-nine refill, a positive-weight comparison, and the numerical
restricted-tree transfer obstruction. The general infinite-sum argument,
the supremum identity, the level-minimum argument and the Diophantine
arguments are **written proofs, not Lean formalizations**. No theorem in
the file states convergence.

Run the scoped replay with an already built pinned Mathlib checkout:

```sh
python -X utf8 -B research/central-closure-20261124/checks/replay.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib \
  --receipt /tmp/central-closure-replay.json
```

The exact source pins are in [SOURCES.json](SOURCES.json). Fresh replay and
review records are under `reports/2026-11-24-central-closure/`. Repository
integrity checks validate the checkout, not the mathematics.

The outstanding task remains the universal one: a return or merger below
the original ordinary floor, or a different contradiction for every bad
component. None of the conditional closing hypotheses is discharged here.

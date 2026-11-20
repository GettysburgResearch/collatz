# Search record and exact boundaries

These are bounded computations from the 20 November 2026 investigation.
The successful final statement and its independently checked artifact are in
[PROOF.md](PROOF.md). Runtime depends on the machine and concurrent work;
iteration numbers and integer bounds are the reproducible observations.

## Successful physical searches

The original search starts the full nonnegative physical potential at zero
and updates every unit residue simultaneously by the minimum of its legal
even and robust odd costs, then clips below at zero. It stops only when the
entire integer vector is unchanged.

| Ternary precision | Slope | Fixed point iteration | Maximum full credit | Actual selected maximum odd gap | Independent full-state verification |
|---|---:|---:|---:|---:|---|
| 14 | 15/7 | 599 | 65 | 10 | Passed |
| 15 | 17/8 | 646 | 76 | 10 | Passed |
| 16 | 21/10 | 1119 | 110 | 10 | Passed |
| 17 | 25/12 | 1353 | 133 | 10 | Passed |

The reduced minimum search reproduced the class-two part of the `17/8`
potential at iteration 406, and the `25/12` potential at iteration 856.
For the published `25/12` strategy, the **fixed-policy maximum recurrence**
reproduces that same potential at iteration 202. These are different
recurrences, so the iteration counts are not interchangeable.

The full `25/12` potential was independently checked at all 86,093,442 unit
states. Its O-first physical selector was collapsed into odd gaps on the
entire doubling cycle, and all 258,280,326 gap lifts were checked directly.
The source-dependent terminal repayment and forward replays are separate
checks. See the linked independent receipt for hashes and actual commands.

## Slope-two runs

The reduced minimum recurrence was run at `p=2,q=1` with a limit of 5000
iterations. It stopped early on a strictly positive minimum vector:

| Precision | Iteration | Minimum reduced credit | Maximum reduced credit | Observation |
|---|---:|---:|---:|---|
| 18 | 261 | 1 | 19 | No fixed point produced; positive-minimum stopping condition |
| 19 | 348 | 1 | 20 | No fixed point produced; positive-minimum stopping condition |

These two negative searches have not been independently replayed as large
computations. The printed stopping observations must not be promoted to an
independently verified all-precision lower bound.

For clarity, the stopping condition has a narrow mathematical justification.
On this finite game, any feasible potential can be shifted so that its
minimum is zero; the reconstructed class-one values are always `q` higher
than a permutation of class-two values. Monotonicity bounds every iteration
from zero above by any such feasible potential. Therefore a strictly
positive minimum iterate contradicts feasibility **for this exact finite
physical game**. No conclusion about a larger precision or a different
certificate interface follows. Nothing in this argument is a forward
Collatz statement.

## Other attempted representations

Exact finite-horizon and finite-stopping inverse-word recurrences were
enumerated through depth 17 at cap six, with additional stopping runs at cap
twelve. They did not cover all sources at slope 199/100. A variable-depth
ternary cylinder partition and cycle-guided refinement reduced the state
count but did not produce a sub-two certificate. Those exploratory programs
and failed potentials are not delivered as proof artifacts.

The useful change was the two-action physical representation, followed by
the exact class-one elimination. It reduces the per-iteration work and
permits the compact fixed-strategy certificate. It does not change the
ordinary-source versus inverse-construction boundary.

## Re-run a successful search

Build outside the repository and keep generated tables in scratch:

```sh
c++ -O3 -std=c++17 -fopenmp research/inverse-escape-20261120/search_reduced.cpp -o /tmp/collatz-search-reduced
```

In a scratch directory, run the executable with arguments
`17 25 12 1600 4`. The arguments are ternary digits, budget numerator,
denominator, iteration limit, and thread count. A successful run writes a
native unsigned-16-bit reduced vector. That search output is diagnostic;
the published strategy and its one-byte reconstructed credits are the
portable certificate.

No GPU was available. The deeper slope-two configurations above were run;
precision 20 and higher were not run in this investigation.

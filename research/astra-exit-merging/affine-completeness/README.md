# All-source return liveness and affine-shadow completeness

**PROPOSED pending independent mathematical review. No full Collatz proof.**
Continuation of #128 at `edd48df6e9c678fa4a65b4ed8f41421dfc92518b`;
programme #121. See [the full proof](PROOF.md) and
[the exact sources and limitations](SOURCES_AND_LIMITS.md).

## What is genuinely universal here?

**Pointwise in a hypothetical least counterexample:** after the ordinary
first-odd-run comparison with the fixed smaller source `(N-1)/2`, the #123
or enlarged #125 hard-return mechanism must either merge or leave its
language in finite time. Infinite hard returns are incompatible with the
convergence of that smaller source and its nonresetting physical clock.
The same finite-clock principle allows adaptive switching among ALL smaller
original sources, if each clock is retained. A merger contradicts minimality,
so a finite escape is forced for the stated return languages. This is not
an assertion that the escape has been solved. The observation is elementary,
but removes an unnecessary infinite-return obligation from this route.

**Unconditional in affine templates:** for any finite collection
`A_i*t+B_i`, with positive integer slopes, fixed physical words merge all
members on an infinite parameter set if and only if deleting every factor
of 2 and 3 from each slope leaves the same integer. In that case a terminating
compiler supplies simultaneous merger words in a subprogression of ANY
prescribed arithmetic progression. The source intercepts may have either sign;
positive starting values are enforced by an explicit threshold.

The second result constructs a subprogression. It does NOT force the given
parameter of an arbitrary input to belong to that subprogression. In particular,
no complete successful selector for all positive integers is asserted.

## Read the results

| Statement | Exact contribution | Boundary |
|---|---|---|
| ACS-001 | Fixed convergent companions and advancing clocks rule out infinite core-avoiding return sequences; every least counterexample has a finite #125 escape with its ternary and original-height restrictions. | Uses minimality to know the smaller companions converge; no bound on their stopping times is proved. |
| ACS-002 | Every chart `(3^d*y+b,y)`, `d>=0`, `b` any integer, has a constructed synchronous merger cylinder, with an explicit word-length bound. | Actual fixed parameters do not get to choose their own parities. |
| ACS-003 | Necessary AND sufficient slope criterion for simultaneous uniform merging of arbitrary finite affine collections, even inside a specified non-dyadic congruence. | Nonconstant positive slopes only; no assertion about coalescence of arbitrary constant source tuples. |
| ACS-004 | No entire arithmetic progression is a permanent failure region for a compatible affine collection when arbitrary finite words are allowed. | Topological density of uniform success is not measure one or pointwise coverage. |
| ACS-005 | The all-input boundary and the precise next task. | A scope/handoff statement, not an additional closing theorem. |

The compiler's controlled reductions consume the slope exponent instead of
following an unproved negative-orbit stopping rule. This removes the restriction
`3^d-b>2^d` from the parallel #127 sufficient construction. #127 remains valid
on its own hypotheses. Necessary slope/clock rigidity is credited to AAC-001;
fixed-gap recursion and raw affine grammar are credited to #127/#128.

## Small simultaneous example

For every integer h>=0, put t=205+256h. Then

```text
T^11(8t-5) = T^10(4t-1) = T^8(3t-5) = 81h+65.
```

The first sources are 1635, 819 and 610. All three trajectories merge with
their own clocks; both companions are smaller than the first source.
The same compiler can enforce t=7 mod24, yielding t=6127+12288h and clocks
15/14/12. It does not discard the odd factor in the specified modulus.

The fixed pair (2,1), realized by the compatible templates t+2,t+1 at t=0,
never merges synchronously. Successful subprogressions exist in every dyadic
neighborhood of t=0 anyway. This control prevents a false topological-to-pointwise
conclusion.

## Run

From a complete repository checkout on this branch:

```sh
python -B experiments/X-AEM-006-affine-completeness/run.py --family '[[8,-5],[4,-1],[3,-5]]' --ap '[7,24]'
python -B -S experiments/X-AEM-006-affine-completeness/run.py --full acs-full.json --check experiments/X-AEM-006-affine-completeness/canonical.json
python -B -S experiments/X-AEM-006-affine-completeness/verify.py acs-full.json --summary experiments/X-AEM-006-affine-completeness/canonical.json --self-test
```

The first command synthesizes a certificate; it is not a test of convergence
at every t in the input progression. Windows shells may require their usual
JSON quoting convention. Only Python's standard library is required.

The finite corpus has 6,825 rows: 1,713 type certificates, 388 compatible
multi-source certificates, 625 incompatible-slope classifications, 4,095
all-source entry checks with both return languages when applicable, and four
core-phase controls. Full rows are regenerated, not committed as a large file.
Every successful cylinder is checked symbolically on the full progression,
and then replayed at three positive ordinary members. This finite evidence
supports implementations, not universal mathematical quantifiers.

## What to pursue next

The finite escapes of ACS-001 are the pointwise target. To rule them out one
needs a restart or companion-switch mechanism preserving the ORIGINAL source
inequality and nonresetting clocks. ACS-003 supplies templates even within a
specified failure cell, but may select a different integer inside that cell.
That distinction cannot be repaired by a larger finite atlas alone.

All prior files and review statuses are unchanged. Actual execution details,
including prepublication checker hardening, are in
[the validation receipt](../../../reports/astra-exit-merging-06/validation.json).

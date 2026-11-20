# Independent reconstruction of the binary-run core argument

Reviewer: the fixed-source-drift mathematical agent, separately from the
author of the arithmetic core. This is mathematical reconstruction and a
bounded independent implementation, not proof-assistant verification or
external peer review.

## Reviewed bytes and verdict

| File | SHA-256 |
|---|---|
| `research/fixed-integer-descent/arithmetic.md` | `df7869013ba19ebba068e9e15cda5f3c7374d9ef1cb4090d7cf26d998188a315` |
| `research/fixed-integer-descent/modular_hitting.md` | `bb757b452a003969dd9dde4668cc6c57f649260fbdc68341ebb01723c9f25785` |
| `experiments/fixed_integer_arithmetic.py` | `ad62ca23d040b067e20a8e235b61d8406e6ba8ff39da5cf49446379832c37557` |

The local proof claims **RC-1--RC-4 are VERIFIED in their stated scope**.
The transfer clauses of M1 and M3 are likewise verified, conditional in M3
on the specified finite modular and core certificates. RC-5's inference
from complete core enumeration and uniform outside-core clocks is valid.
This review does not independently rerun the cap-five or cap-six complete
enumerations, or the modulus-`2^24` scans. Later file versions do not
automatically inherit these byte-scoped verdicts.

## Reconstruction

1. **Homogeneous run escape.** The order calculation gives exactly the
   subgroup `1 or 3 mod 8` among odd residues modulo `2^m`; the second
   coset is `5 or 7 mod 8`. The displayed representatives lie in the
   required cosets, lie below `2^(2R+3)`, and both they and their
   decrements have more than `R` one-runs. Reducing to low bits does not
   create additional one-runs. Subtracting one from an odd residue does
   not borrow through the modulus. These facts verify the uniform clock
   `J_R` and include the zero value at `u=delta=1,j=0`.

2. **Signed cut.** Independently expanding the affine recurrence gives
   `P_(j+1)=3P_j+2^A_j`. Positive shadows satisfy `P_(j+1)<=4P_j`;
   negative shadows satisfy `2|P_j|<=|P_(j+1)|<3|P_j|`. In both cases
   the strict terminal cut controls every earlier cut and makes
   `A_j<D`. The valuation comparison at the next step is strict, so
   cancellation cannot change the claimed odd-event clock. Borrowing
   for a negative lower block leaves the upper block `3^j u-1`, as
   required. The equality example `5 -> 1` correctly excludes replacing
   the strict guard by a weak one.

3. **Complete run parsing.** Before a zero-run, the prefix is odd and
   the positive lower block is strictly below `2^(D-ell)`. Before a
   one-run, the preceding prefix is even and the negative lower block
   lies in `[-2^(D-ell),0)`. These are exactly the inequalities needed
   by the two respective credit estimates. The leading one-run uses
   prefix zero, and a terminal one-run gives lower block `-1`, so the
   proof does not omit either boundary. For an input within the cap,
   the relevant homogeneous hitting time is positive. Every first
   inadmissible length therefore produces an actual positive-orbit
   cap exit at a positive clock no larger than `J_R`.

4. **All-time conclusion.** A permanently capped actual orbit cannot
   visit an outside-core state, since such a state has a certified
   future cap exit. Its odd states therefore lie in one finite set.
   Eventual repetition or reaching killed 1 follows. The converse
   from an eventually periodic positive orbit to bounded run count is
   immediate from its finite value set. Even steps do not alter the
   number of one-runs. No assertion about an initially capped orbit
   remaining capped is used.

5. **Uniform finite clocks.** The maximum of an inside-core replay
   clock and a uniform outside-core escape clock covers every input.
   This correctly yields the stated 68/107 alternatives from their
   respective finite certificates. A modular maximum good-run length
   `H` gives first bad index at most `H`, not `H+1`; the indexing in
   M1 is correct. An exit can increase the integer value, so neither
   clock is a first-descent theorem. The Mersenne control proves that
   a run-count-only first-descent clock is impossible.

6. **Independent inverse basin.** All odd predecessors of a unit
   target form the stated `m -> 4m+1` fan, and appending binary `01`
   adds precisely one one-run. Thus the fan cutoff is complete. This
   inverse construction cannot discover a separate cycle; the paper
   correctly relies on forward replay of the full core for that part.

## Independent finite execution

The separate implementation
[review_run_core_from_drift.py](review_run_core_from_drift.py) uses a
breadth-first tree, a binary-string transition count, and repeated integer
halving for the odd map. It compares complete generated sets, not only
cardinalities, with the production generator through cap four. It then
replays every source using its own literal odd map and compares the
resulting finite counts with the preserved report.

| Cap | Complete sources | Reach 1 within cap | Largest odd clock | Directly replayed odd edges |
|---:|---:|---:|---:|---:|
| 1 | 4 | 1 | 1 | 3 |
| 2 | 76 | 12 | 8 | 149 |
| 3 | 1268 | 79 | 19 | 3160 |
| 4 | 32620 | 556 | 42 | 71884 |

All comparisons passed. The exact output is
[run-core-review.json](run-core-review.json). Command actually executed:

```bash
python -X utf8 -B reports/2026-11-20-fixed-integer-descent/review_run_core_from_drift.py
```

## Remaining uncertainty

No global run cap has been established for one arbitrary fixed positive
integer. The finite core can also contain a hypothetical nontrivial
cycle at a larger cap; termination of the finite procedure does not
exclude every possible such output. Those are genuine missing global
arguments, rather than defects in the finite-core proof reviewed here.

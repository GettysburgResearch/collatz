# X-9501 — exact finite audit of the H block system

**Experiment ID:** X-9501  
**Agent:** `gpt56-h-01`  
**Issue:** [#17](https://github.com/gfreund123/collatz/issues/17)  
**Status:** EMPIRICAL  
**Created:** 2026-07-21

## Research questions

Over a finite exact word box, do the independently implemented formulas agree?
Specifically:

1. Does the direct ghost residue equal the recursive suffix residue?
2. Does the affine word formula equal exact stepwise simulation?
3. Does the computed cylinder representative realize every prescribed letter?
4. Does the proposed signed-displacement inequality hold?
5. Do all tested contracting cylinders descend at their least positive
   H-admissible representative?

## Command

```bash
python run.py \
  --max-length 6 \
  --max-letter 5 \
  --output results/summary.json
```

## Environment

- Python 3.13.5
- standard library only
- exact Python integers; no floating point is used in any mathematical check
- deterministic exhaustive enumeration; no random seed

## Parameter range

All nonempty words of length at most 6 over

```text
r in {0,1,2,3,4,5}
```

were checked. The total is

```text
6 + 6^2 + ... + 6^6 = 55,986 words.
```

## Output digest

The committed summary reports:

```text
words checked:                     55,986
contracting words:                 25,751
expanding words:                   30,235
direct/recursive residue checks:  55,986
exact simulation checks:           55,986
displacement checks:               55,986
contracting descent checks:        25,751
all-zero equality cases:                 6
SHA-256 digest:
6499fb520760c68ed024d0bd34e3ff6913eb341b083e8a79bf3bac640ac12a47
```

## Interpretation

No finite counterexample was found to the proposed signed-displacement theorem.
The direct and recursive exact-cylinder constructions agreed throughout the
box, and every tested contracting cylinder descended at its least positive
H-admissible representative.

This is strong adversarial evidence for `C-9501`; it is not a proof. The current
universal proof attempt still needs the word-specific mixed-sign
carry-rectangle lemma recorded as `Q-9501`.

## Limitations

- The word length and letter range are finite.
- The search cannot exclude a first counterexample outside the box.
- Passing all checks does not repair a logical gap in an induction proof.
- The script tests the exact arithmetic model; it does not search the full
  Collatz map or claim a counterexample/convergence result.

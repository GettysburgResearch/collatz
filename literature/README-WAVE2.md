# Literature audit wave 2 index

Use `LITERATURE.md` as the top-level entry point and `LIVE_REPO_REVIEW_WAVE2.md` for the current six-program synthesis.

## New imported theorems

- `LIT-KTHM-0015` accelerated affine monoid
- `LIT-KTHM-0016` rational-base address identity
- `LIT-KTHM-0017` positive cycle-mean phase potentials
- `LIT-KTHM-0018` finite clopen-cover obstruction
- `LIT-KTHM-0019` subsequential images of regular languages
- `LIT-KTHM-0020` exact closure decision for a fixed DFA
- `LIT-KTHM-0021` maximal safety kernel
- `LIT-KTHM-0022` short canonical witness
- `LIT-KTHM-0023` exact accelerated-cycle equation
- `LIT-KTHM-0024` tensor-radius refutation and corrected separation theorem
- `LIT-KTHM-0025` match-bound scope
- `LIT-KTHM-0026` tilted finite-state transfer bound
- `LIT-KTHM-0027` graph-directed compact attractor and non-application

## New live claim maps

- `claim-maps/PR3-WAVE2.md`
- `claim-maps/PR11.md`
- `claim-maps/REGULAR.md`
- `claim-maps/IDEAS-8-9.md`
- `claim-maps/TERMINATION-WAVE2.md`

## Validation

Run:

```bash
python3 literature/check_literature.py
python3 literature/check_literature_wave2.py
```

The second-pass suite preserves branch-qualified native IDs and does not promote any native status.
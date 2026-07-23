# X-8405 — Intrinsic top-boundary audit

**Status:** `EMPIRICAL / EXACT FINITE INTERFACE AUDIT`  
**Claim interface:** `L-8407`, `T-8404`, `T-8405`

This standard-library checker reconstructs the complete finite arithmetic behind the intrinsic phase/core normalization and its nineteen-bit quotient transition.

## Coverage

```text
intrinsic ordinary cells:              504
section g=1 cells:                     432
section g=7 cells:                      72
proposed target transitions:         3,024
zero input top residues:                 0
zero output constants sigma:            11
coarse ordered branch pairs:             36
minimum coarse quotient growth:         149
maximum coarse quotient growth:       6,803
```

For every intrinsic cell and every proposed next phase, the checker proves by exact integer arithmetic that:

1. exactly one next cell is compatible;
2. the displayed `kappa` is integral;
3. the input top residue `rho` and output constant `sigma` satisfy
   ```text
   2^19 q' = 3^A q + kappa;
   ```
4. every lifted ordinary core replays exactly;
5. no transition has `rho=0`;
6. after the state scaling used in `L-8407`, every legal step is increasing above the exact thresholds
   ```text
   g=1: 4,271,324
   g=7: 3,212,050.
   ```

The audit also replays the frozen 15-transition quotient path whose initial value has only 13 base-`2^19` digits.  It refunds two complete top cells and then exits.  It is finite evidence, not a survivor.

## Replay

```bash
python3 -B experiments/X-8405-intrinsic-top-boundary/run.py \
  --check-results \
  experiments/X-8405-intrinsic-top-boundary/results/canonical.json
```

Canonical semantic digest:

```text
5af2cc52001aeff14d070ffeb37edf7399a92ac06ba23752bf34b8c480c3a29b
```

## Interpretation boundary

The experiment validates the finite formulas and exhausts the 3,024 local transitions.  It does **not** prove that one finite quotient survives all future transitions, produce a divergent seed, or resolve Collatz.

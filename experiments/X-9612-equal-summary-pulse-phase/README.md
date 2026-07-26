# X-9612 — Equal-summary pulse phase verification

This standard-library checker independently reconstructs the exact arithmetic
interfaces used by:

- `L-9608` — narrow equal-summary zero-carry collapse;
- `L-9609` — cycle-minimum finite target sieve;
- `T-9608` — cycle exclusion for every fixed-weight negative-three pulse
  grammar with at most five `A` letters.

Run from the repository root:

```bash
python3 -B experiments/X-9612-equal-summary-pulse-phase/verify.py
```

Expected output:

```text
all independent L-9608/L-9609/T-9608 checks passed
```

The program uses exact Python integers and imports no authoring module. It
checks finite interfaces and exceptional target tables; the unbounded theorem
is proved in the claim files rather than inferred from computation.

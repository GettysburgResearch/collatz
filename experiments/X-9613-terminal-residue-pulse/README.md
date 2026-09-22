# X-9613 — Terminal-residue pulse verification

This standard-library checker independently reconstructs the exact arithmetic
interfaces used by:

- `L-9610` — the terminal modulo-27 cycle-minimum sieve;
- `T-9609` — all-repetition cycle exclusion for every fixed-weight
  negative-three pulse packet with at most thirteen `A` letters.

Run from the repository root:

```bash
python3 -B experiments/X-9613-terminal-residue-pulse/verify.py
```

Expected output:

```text
all independent L-9610/T-9609 checks passed
```

The checker uses only Python integers and imports no authoring module. It
exhausts the four finite exceptional alphabets after the general theorem has
removed every other packet in scope. The universal conclusion rests on the
claim proofs, not on a bounded repetition scan.

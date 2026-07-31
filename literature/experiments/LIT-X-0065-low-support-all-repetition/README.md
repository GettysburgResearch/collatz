# LIT-X-0065 — all-repetition low-support pulse ladder

This exact standard-library packet certifies every finite arithmetic inequality used by `LIT-KTHM-0065`.

## Frozen theorem range

```text
P3=(1,2):
  exactly s upward pulses, 4 <= s <= 11;
  no nontrivial positive cycle;
  the possible all-two lifts are the trivial n=1 cycle.

P11=(1,1,1,2,1,1,4):
  exactly s upward pulses, 4 <= s <= 48;
  no positive-cycle hit.
```

Pulse positions, rotations, repetition lengths, and positive pulse heights are unrestricted inside those support ranges.

## Proof layers checked

For each support size, the builder certifies:

1. the exact largest-gap exponent;
2. the nontrivial positive-cycle product gate at small repetitions;
3. the sharpened direct gate using the least possible total pulse
   \[
   t_0=\max\{s,\lfloor r\log_2(3^k/2^A)\rfloor+1\};
   \]
4. an exact residue-period proof of the cofinal Legendre inequality;
5. the source-audited Matveev cutoff with constant `748000000`;
6. the complete upper continued-fraction rows below `200000000000`;
7. every ordinary comparison inequality;
8. every exceptional convergent family by an exact finite residue-period base check.

The broad native pulse-numerator identity remains a mathematical dependency and should be reconstructed independently before theorem status promotion.

## Replay

```bash
python3 literature/experiments/LIT-X-0065-low-support-all-repetition/summary.py \
  --output /tmp/LIT-X-0065.json

python3 literature/experiments/LIT-X-0065-low-support-all-repetition/verify.py \
  /tmp/LIT-X-0065.json
```

Expected output:

```text
LIT-X-0065 INDEPENDENT VERIFICATION PASSED
a401ec3c97d511f2384a8b95307322d3e4e01ff871454f8d5859b8c6919feb35
```

`summary.py` and `verify.py` share no module. The verifier uses a separately written certified logarithm implementation and reconstructs every coverage and convergent partition.

The detailed derived JSON is intentionally regenerated rather than committed; its semantic digest and scope are frozen in `results/manifest.json`.

## Status boundary

The packet proves exact inequalities and finite logical coverage. It does not by itself prove the general distributed-pulse numerator formula, construct a positive cycle, or resolve Collatz.

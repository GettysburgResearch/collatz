# LIT-X-0060 — Matveev `log 2/log 3` source specialization

This exact standard-library artifact:

1. proves the safe source constant
   ```text
   e*30^5*2^(7/2) < 748,000,000;
   ```
2. certifies strengthened repetition cutoffs for `T-8255` and `T-8260`;
3. certifies the fixed-support rate thresholds `18` and `117`.

All logarithms use rational atanh-series intervals. The source theorem itself is not reproved.

```bash
python3 run.py --check-results results/canonical.json
```

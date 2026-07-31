# LIT-X-0065 — verified-floor fixed-support pulse closure

This exact artifact supports `LIT-KTHM-0065`.

## Scope

It combines:

- the branch-qualified verified floor
  \[
  N_*=4\cdot3^{44}+2;
  \]
- the general largest-gap pulse inequality;
- the source-audited Matveev specialization;
- exact continued fractions for
  \[
  \log_2(9/8),\qquad \log_2(2187/2048);
  \]
- two complementary convergent-family rejections.

It certifies:

```text
P3=(1,2):
  every nontrivial positive cycle with fixed pulse support 1..18 is excluded;

P11=(1,1,1,2,1,1,4):
  every positive cycle with fixed pulse support 1..117 is excluded.
```

The trivial `P3` all-2 lift at repetition equal to the support is retained.

## Replay

```bash
python3 -B -m py_compile \
  literature/experiments/LIT-X-0065-verified-floor-fixed-support/run.py \
  literature/experiments/LIT-X-0065-verified-floor-fixed-support/verify.py

python3 -B literature/experiments/LIT-X-0065-verified-floor-fixed-support/run.py \
  --check-results \
  literature/experiments/LIT-X-0065-verified-floor-fixed-support/results/canonical.json

python3 -B literature/experiments/LIT-X-0065-verified-floor-fixed-support/verify.py \
  literature/experiments/LIT-X-0065-verified-floor-fixed-support/results/canonical.json
```

Expected verifier output:

```text
LIT-X-0065 INDEPENDENT VERIFICATION PASSED
c730cce495223542e2d15e424ca0ba94996c2d0382289baab3604344abe8b179
```

The verifier imports no author-side module.

## Dependency boundary

The artifact verifies every exact inequality and continued-fraction row after
three declared interfaces:

1. the imported verified range `N_*`;
2. the native distributed-pulse divisor identity;
3. Matveev's source theorem as specialized in `LIT-KTHM-0060`.

It does not independently rerun the `2^71` convergence computation or
reconstruct the native pulse cocycle from raw Collatz iteration.

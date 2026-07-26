# X-9614 — Two-sided pulse-boundary phase floor

This exact certificate supports:

- `L-9611`, the two-sided source/output phase theorem;
- `T-9610`, cycle exclusion for every aligned fixed-weight negative-three pulse grammar with at most `243` letters `A` per macro.

The computation is a **phase table**, not a cycle-period or orbit-prefix scan.
It exhausts all suffix/prefix pairs at depths five, eight, and ten, then checks the exact parameter inequality for `14<=a<=243` at the least contracting pulse count.

Run from the repository root:

```bash
python3 -B experiments/X-9614-two-sided-phase-floor/run.py \
  --check-results \
  experiments/X-9614-two-sided-phase-floor/results/canonical.json

python3 -B experiments/X-9614-two-sided-phase-floor/verify.py \
  experiments/X-9614-two-sided-phase-floor/results/canonical.json
```

Expected terminal lines:

```text
X-9614 canonical results match
all independent X-9614 two-sided phase checks passed
```

Frozen SHA-256 values:

```text
run.py
24dd23cae3a916205e9b7c3f5fc92b5a298a10a8851ba9a5b625b6360bede9d4

verify.py
21d34c51eb66ef0e456e9f1f7df3f5fc9d19bdac3544def3a14cca0499aa19ee

canonical.json
ee70952f9b8edfafcf775a985a71b072ddb94787e55dc3d977c14d858703e4ec

semantic payload
296074c8e5f59c11bc1de1c7d0d89084ae79012381ff1d850fb611281fe0cf06
```

The verifier imports no generator module. It reconstructs word cylinders by iterative residue lifting rather than the generator's closed affine formula.

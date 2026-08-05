# X-8301 — Exact ordered-jump decoder at accelerated length 185

Experiment ID: `X-8301`  
Agent: `gpt56-cycle-02`  
Issue: #9  
Classification: **EXACT FINITE COMPUTATION**

## Research question

After the 92-local-minimum constraint reduces length 185 to the `AA` and `DD` skeletons, does any excess valuation height and positive cycle multiplier satisfy the exact accelerated cycle equation?

## Replay

```bash
python3 -B experiments/X-8301-cycle-185-decoder/run.py \
  --check-results \
  experiments/X-8301-cycle-185-decoder/results/canonical.json

python3 -B experiments/X-8301-cycle-185-decoder/verify.py \
  experiments/X-8301-cycle-185-decoder/results/canonical.json
```

No third-party packages are required.

## Frozen scope

```text
AA direct heights: 17..30
DD direct heights: 16..30
reference height: 31
AA uniform multipliers: 1..539801
DD uniform multipliers: 1..566791
```

At the reference height every multiplier in both full uniform ranges fails only by an unavailable suffix valuation. The maximum inspected valuations are 36 and 38, while the height-transfer moduli begin at powers 308 and 309.

## Digests

```text
run.py:
b9f6b00484c21d924312335e651a7c7e2839f93e1058b552bae99de3e3b42a8e

canonical.json:
698589884a93f16325449d6eb1f1a89ce3ef88f413792867ea8807099e0c733a
```

## Boundary

The script proves no statement about accelerated lengths other than 185. The infinite-height conclusion uses the explicit stability proof in `T-8301`; the computation supplies the finite reference certificate.

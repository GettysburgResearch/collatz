# X-9403 — Demand-tree and stationary ghost-stage verification

Experiment ID: X-9403  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: D-9403, L-9405, T-9407, T-9408  
Classification: exact finite verification and interface replay

## Research question

Do the exact stack demand map and the stationary supply-demand matching map
behave as scaled `2`-adic tree isometries, and what residue novelty follows
along bounded `17/18` stage schedules?

## Environment

- Python 3.11 or newer;
- standard library only;
- exact modular integer arithmetic and `Fraction` real-sign checks;
- no network, random sampling, solver, or external data.

## Replay

```bash
python3 -B -m py_compile experiments/X-9403-demand-tree/run.py
python3 -B experiments/X-9403-demand-tree/run.py \
  --check-results experiments/X-9403-demand-tree/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9403-demand-tree/run.py \
  --write-results experiments/X-9403-demand-tree/results/canonical.json
```

Canonical SHA-256:

```text
1a2908bab06d6ae0db096a9516b87b953eb4f96823fdb2ea0ab71fa0686d1962
```

## Frozen scope

1. **Demand permutations.** Complete images at depths `1,2,3`, totaling
   `16,644` stage classes, plus valuation checks.
2. **Six-bit lifts.** Every parent at depths `1` and `2`; `16,640` child
   evaluations proving all `64` next digits occur once per parent.
3. **Stationary matching contexts.** Complete context permutations through
   depth `3`; unique roots for thirty-two ordinary context values.
4. **Ghost stages.** Compatible unique lifts through depth `8` for eight
   selected positive contexts.
5. **Positive-quadrant sign.** Exact rational negativity for the matching
   context associated with ordinary stages `m=0,...,127`.
6. **Schedule novelty.** Every one of the `2^12` increment words over
   `{17,18}`, replayed at three demand depths with all eligible pair checks.

## Interpretation boundary

The experiment exactly verifies its frozen finite arithmetic.  The universal
valuation and isometry statements rest on the written proofs.  Neither the
proofs nor the experiment rule out an actively steered infinite stack tower,
construct an M1 witness, or resolve the Collatz conjecture.

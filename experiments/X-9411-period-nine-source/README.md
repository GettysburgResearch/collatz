# X-9411 — Period-nine source and period-ten interface audit

Experiment ID: `X-9411`  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: `L-9412`, `T-9417`, `L-9413`, `R-9406`, `R-9407`, `Q-9413`  
Classification: exact finite verification and source-parameter replay

## Research question

Does the exact periodic stack reduction satisfy the inspected
Väänänen–Wallisser hypotheses precisely through dimension nine, and what
arithmetic ceilings remain at the first uncovered period ten?

## Replay

```bash
python3 -B -m py_compile experiments/X-9411-period-nine-source/run.py
python3 -B experiments/X-9411-period-nine-source/run.py \
  --check-results experiments/X-9411-period-nine-source/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9411-period-nine-source/run.py \
  --write-results experiments/X-9411-period-nine-source/results/canonical.json
```

Canonical SHA-256:

```text
787f91b5cb328f67dac5f71ee89af2a858572493a27b5d61a6504a480e599897
```

## Frozen scope

1. Exact endpoint-nine inequalities:
   `64^93>81^88` and `559^2-325*31^2=156`.
2. Exact endpoint-ten failure:
   `64^20<81^19` and `401-20^2=1`.
3. Numerical source thresholds through dimension twelve.
4. All `165` phase-pair orbit-separation checks through period ten.
5. Thirty exact direct-versus-phase finite decomposition identities, including
   displayed periods nine and ten.
6. The generic scalar phase exponent `9/log_2(81)`.
7. The zero-height-cost adjacent-order ceiling through period fifteen, with
   exact boundary checks at periods six, seven, and ten.

## Interpretation boundary

The script validates its frozen integer and rational arithmetic. It does not
prove the Väänänen–Wallisser theorem, the universal period-nine corollary, the
generic scalar Padé lemma, or period-ten irrationality. It does not produce an
ordinary Collatz counterexample or resolve the conjecture.

# X-9405 — Sparse stack partial-theta verification

Experiment ID: X-9405  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: L-9407, T-9410, Q-9409  
Classification: exact finite verification and bounded complexity profiling

## Research question

Does the active one-cylinder construction agree exactly with the sparse
survivor-code series, and does the bounded-increment support exhibit the
quadratic exponent and factor-complexity behavior used by T-9410?

## Environment

- Python 3.11 or newer;
- standard library only;
- exact arbitrary-precision integer and modular arithmetic;
- no network, solver, or random sampling.

## Replay

```bash
python3 -B -m py_compile experiments/X-9405-sparse-partial-theta/run.py
python3 -B experiments/X-9405-sparse-partial-theta/run.py \
  --check-results experiments/X-9405-sparse-partial-theta/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9405-sparse-partial-theta/run.py \
  --write-results experiments/X-9405-sparse-partial-theta/results/canonical.json
```

Canonical SHA-256:

```text
df2543be76c294397dcce6819c1d4551a811407a7835b7d2e1997866b0283c67
```

## Frozen scope

1. **Series/cylinder identity.** All 336 one-through-three-edge schedules over
   heights `{0,1,2,3}`. The backward context cylinder, the sparse `Phi` partial
   sum, and the context partial-theta sum agree at every selected bit.
2. **Balanced prefix interface.** A deterministic Fibonacci `17/18` directive
   at seven checkpoints through twelve stages.
3. **Exponent bounds.** The exact support boundaries through 200 stages are
   checked against the universal `153/162` quadratic envelopes.
4. **Factor complexity.** Exact infinite-word factor sets at lengths
   `512,1024,2048,4096`, using the fact that once every gap exceeds the factor
   length, all later factors contain at most one `1`.
5. **Theorem envelopes.** Every finite profile is checked against T-9406's
   lower construction and T-9410's universal upper bound `n^2+n+1`.

## Interpretation boundary

The finite checks validate the frozen algebraic and combinatorial interfaces.
They do not prove the universal claim files, establish `2`-adic irrationality
or transcendence of the partial-theta value, construct an ordinary stack
context, or resolve the Collatz conjecture.
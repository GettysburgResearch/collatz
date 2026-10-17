# X-9406 — Direct truncation and S-adic transfer verification

Experiment ID: X-9406  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: T-9411, L-9408, R-9402, Q-9410  
Classification: exact finite verification and bounded standard-word replay

## Research question

Do sparse partial sums have the exact reduced height and `2`-adic error claimed
by T-9411, and do the skew S-adic transfer-polynomial identities of L-9408 hold
under concatenation and repeated standard-word blocks?

## Environment

- Python 3.11 or newer;
- standard library only;
- exact integers and `Fraction` arithmetic;
- no network, solver, or randomness.

## Replay

```bash
python3 -B -m py_compile experiments/X-9406-truncation-transfer/run.py
python3 -B experiments/X-9406-truncation-transfer/run.py \
  --check-results experiments/X-9406-truncation-transfer/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9406-truncation-transfer/run.py \
  --write-results experiments/X-9406-truncation-transfer/results/canonical.json
```

Canonical SHA-256:

```text
41844251e54fb6c84735d3fd64677439ab5ec1b6e273373cc69186549724f0e6
```

## Frozen scope

1. **Direct truncations.** Nine balanced-prefix checkpoints through stage 24.
   At each checkpoint the script verifies:
   - the numerator is coprime to the exact denominator `81^H_K`;
   - the first omitted term gives exact error valuation `6H_(K+1)`;
   - the finite approximation exponent approaches
     `6/log_2(81)=0.946394630357...`.
2. **Concatenation algebra.** Every `{17,18}` word of length at most six and
   every nontrivial split: `516` symbolic data comparisons.
3. **Transfer values.** `1,548` exact `Fraction` evaluations at three starting
   heights.
4. **Repeated blocks.** `150` exact checks of the closed repeated-word formula.
5. **Standard words.** Ten Fibonacci standard words, through length `89`, with
   recursively composed and directly expanded transfer data agreeing exactly.

## Interpretation boundary

The finite checks validate the frozen arithmetic and polynomial interfaces.
They do not prove the universal claim files, construct a determinant or Padé
approximant crossing the direct-truncation barrier, establish `2`-adic
irrationality or transcendence, exclude an ordinary stack context, or resolve
the Collatz conjecture.
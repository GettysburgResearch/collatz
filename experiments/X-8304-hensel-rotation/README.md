# X-8304 — Hensel-aligned critical run rotation

Experiment ID: `X-8304`  
Agent: `gpt56-cycle-02`  
Issue: #9  
Classification: exact compressed computation; no counterexample

## Question

Can a critical mechanical run word be repaired so that the ordinary real floor agrees with successively deeper prime-power quotient digits, rather than merely making the numerator vanish modulo proper denominator factors?

## Frozen construction

The experiment uses the critical run word from `L-8304` and 65 disjoint unequal-run transpositions among the first 136 canonical sites.

It proves:

1. all five certified factors `7,191,281,28591,136398329` divide the cycle numerator and denominator;
2. before rotation, the real floor agrees with the quotient-cylinder digits modulo `7` and `191`;
3. quotient digits transport under cyclic rotation by the same exact affine run maps;
4. after `928986` run rotations, the real floor agrees modulo `7`, `191`, and `281` simultaneously;
5. the same rotated rational is still nonintegral and disagrees at `28591` and `136398329`.

This is a three-prime Hensel alignment, not a positive cycle.

## Replay

```bash
python3 -B run.py --check-results results/canonical.json
python3 -B verify.py results/canonical.json
```

`verify.py` imports no author module. It independently rebuilds the five prime-square quotient rows, the directed real value, and all `928986` quotient-transport steps.

## Frozen digest

```text
canonical JSON SHA-256:
a6afbeddf791f5d95f464be331da45f7c528f7edd4cbe34608dd7bb91466e06b
```

## Boundary

The result does not factor the complete denominator, prove the remaining quotient digits, construct an integral cycle, or give an unconditional Collatz counterexample.

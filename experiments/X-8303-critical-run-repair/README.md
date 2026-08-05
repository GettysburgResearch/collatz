# X-8303 — Critical mechanical run repair

Experiment ID: `X-8303`  
Agent: `gpt56-cycle-02`  
Issue: #9  
Classification: exact compressed computation; no counterexample

## Question

Can the critical paired negative-three chart be compressed one Euclidean level further, repaired through the certified PR #45 factor product with macro-run transpositions, and tested at the ordinary quotient level?

## Frozen result

The critical chart word has the exact form

```text
L(1307356254663,1574985702418)
 = phi(L(236838463643,267629447755)),
phi(0)=01111,
phi(1)=011111.
```

The two macro-runs have commutator

```text
C_01-C_10=7*2^16*3^9.
```

A deterministic four-list solver selects 46 disjoint run transpositions and obtains

```text
C_modified=0 mod 1465129870107858983.
```

The same word is rejected twice:

1. its outward-rounded real fixed point has fractional part beginning
   `0.4154867702110835202...`;
2. its prime-power quotient cylinder is incompatible with the sole real integer candidate.

Factor `7` is automatic for every chart word at the frozen length and weight; it is not created by the repair.

## Replay

```bash
g++ -O3 -std=c++17 \
  experiments/X-8303-critical-run-repair/solve.cpp \
  -o /tmp/x8303-solve
/tmp/x8303-solve

python3 -B experiments/X-8303-critical-run-repair/run.py \
  --check-results \
  experiments/X-8303-critical-run-repair/results/canonical.json

python3 -B experiments/X-8303-critical-run-repair/verify.py \
  experiments/X-8303-critical-run-repair/results/canonical.json
```

`verify.py` imports no author module. It reconstructs the original chart product and the run-compressed product independently, replays all five prime-square quotient rows, and independently recomputes the directed interval.

## Frozen digest

```text
canonical JSON SHA-256:
d2a85dbd403b5d3b1a899cc42502d31f3cf7c43c4407cadbd0fa0e90ed31a585
```

## Boundary

This experiment does not factor the complete denominator, solve the prime-square quotient target, construct a positive cycle, produce an infinite ordinary chart path, or disprove Collatz. Its purpose is to replace isolated adjacent repairs by a hierarchical monomial repair alphabet at every Euclidean scale.

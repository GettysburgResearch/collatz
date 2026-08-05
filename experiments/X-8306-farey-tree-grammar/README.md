# X-8306 — Full hierarchical Farey-tree repair grammar

Experiment ID: `X-8306`  
Agent: `gpt56-cycle-02`  
Issue: #9  
Associated claims: `L-8308`, `T-8306`  
Classification: exact compressed computation; no counterexample

## Grammar

The root is the critical lower mechanical run word

```text
L(236,838,463,643 ; 267,629,447,755).
```

Every Christoffel/Farey node is split into its two Farey parents. At every internal occurrence, the recursively repaired children may appear in either order. This permits hierarchical block reversals at every Euclidean scale, far beyond local adjacent swaps.

## Exact compilers

At precision `2^314`, the experiment builds:

1. the exact set of possible affine numerators modulo `2^314`;
2. the directed real convex envelope of every possible fixed point;
3. the corresponding set of ordinary quotient residues.

The real envelope is positive, contains ordinary integers, and lies below `2^314`. None of the exact quotient residues lies in its integer window.

Therefore the full hierarchical grammar contains no integral fixed point.

## Replay

```bash
python3 -B run.py --check-results results/canonical.json
python3 -B verify.py results/canonical.json
```

The verifier uses an iterative bottom-up Farey DAG, while the author implementation uses memoized recursion.

## Boundary

The grammar does not include arbitrary permutations, arbitrary fixed-weight words, or shape-changing replacements. The result is not a proof that positive Collatz cycles do not exist.

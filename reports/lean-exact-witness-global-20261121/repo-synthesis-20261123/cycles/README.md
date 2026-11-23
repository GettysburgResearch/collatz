# Infinite-dictionary descent: author evidence and boundaries

23 November 2026. The [scientific proof](../../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/cycles/INFINITE_DICTIONARY_DESCENT.md) proves ordinary descent for an infinite language of arbitrarily changing long repetitions and defects. Full Collatz remains open.

## Result checked

For a contracting run word with data `(P,Q,C)`, put `d=Q-P`, and for each allowed defect `(R,S,B)` put `E=dB-(S-R)C`. One integer cutoff `K` with

`R P^K + |E| < S Q^K`

for every allowed defect forces the signed ordinary quotient

`h=(d x-C)/Q^K`

to drop by at least one in absolute value at every nonzero macroboundary, and makes zero absorbing. The complete actual future must have all run lengths at least `K`; the final boundary of a finite replay needs its own run lookahead. The integer quotient reaches zero by its initial absolute size. Defect labels, run lengths, and number of macros are unrestricted. A uniform bound on the normalized multiplier and defect error also handles infinite defect families.

The argument settles the variable-run-length dictionary boundary in the previous UC12 corollary. No universal itinerary coverage is supplied. The base word's possible positive integer fixed point is retained, not automatically identified with the standard cycle.

## Formal execution

The final [LatticeDescent.lean](../../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/cycles/LatticeDescent.lean) was compiled with Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, core/Std only:

```
lean -j 1 -DwarningAsError=true LatticeDescent.lean
```

The exact absolute command, compiler output, and successful process result are in [EXECUTION.json](EXECUTION.json); the complete axiom output is also in [lean-strict-audit.log](lean-strict-audit.log). Twenty public declarations are audited. Their axiom union is exactly `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx` or custom research axiom.

The last declaration, `ordinary_word_language_hit`, consumes literal positive shortcut traces with parity and every intermediate endpoint. It proves the explicit all-time boundary equation after the quotient clock. Thus this formal scope includes the ordinary word interface, rather than only an affine numeric model. The cutoff is an explicit arithmetic premise. No proof that arbitrary Collatz itineraries satisfy it is hidden in the module.

The real uniform-family specialization, the explicit all-bounded-defect cutoff `u=10, K=2B`, and the prose cycle consequences are written deductions. They are not counted as additional Lean theorems.

## Finite controls actually executed

[check_lattice_descent.py](../../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/cycles/check_lattice_descent.py) was executed normally and with `-O`; the outputs are byte-identical and preserved in [normal.json](normal.json) and [optimized.json](optimized.json).

The controls include:

- 1,012 complete cutoff words for every bounded binary defect dictionary through length eight;
- 250 actual positive ordinary traces, 750 complete macroedges, and 20,084 literal shortcut steps;
- 1,112 integral paid affine edges, including 50 zero-source edges;
- four boundary controls: strict-cutoff equality, missing terminal lookahead, the legal odd-denominator rational cycle at `11/7`, and damaged ordinary parity.

The rational control has the paid affine fixed quotient `6/7`; it verifies why integer quotient discreteness is load-bearing. The missing-lookahead control is the actual source `1`, run `(10)^2`, defect `1`, endpoint `2`; it verifies why zero absorption cannot be claimed without the next boundary's lattice.

These are finite exact controls, not a bounded census proof of the infinite theorem. The proof is supplied in full separately.

## Frozen science hashes

| File | SHA256 |
|---|---|
| INFINITE_DICTIONARY_DESCENT.md | `40f359ad13850a995ed798bd5c6ae8b3bf2257c9f62991d7a004c8441afa597d` |
| LatticeDescent.lean | `92b4d94ec3d69259fe9604097548b673693bd577ea20faf76c5c8df342b00339` |
| check_lattice_descent.py | `be61f95feb6b167d119868a961a3c07c24f9e3939e4486a19b0286c55ff3a5d7` |

[SOURCES.json](SOURCES.json) records current PR175, PR178, PR180, PR183, and PR185 heads and the exact source files inspected. This was targeted mathematical orientation rather than a blanket new approval of those branches. The new proof does not import their analytic or computational premises.

Repository-integrity validation and publication are coordinated separately by the parent packet. This report does not claim a push, independent review, or gate execution that it did not perform.


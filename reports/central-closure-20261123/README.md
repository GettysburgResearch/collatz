# Published execution record: central Collatz continuation

The exact published research commit
[`e04daab0a0ddd59c80f5d16a51b9943fd5149e6c`](https://github.com/GettysburgResearch/collatz/commit/e04daab0a0ddd59c80f5d16a51b9943fd5149e6c)
was fetched into a fresh, clean, complete checkout and replayed.
Its tree is `95ff707b2c8560760b7af57ab7d4f8dd1e53a75b`; the checkout
contained 736 tracked files. The final report commit adds execution
records only; it changes no mathematical source.

## Outcome

**PASS.** All 18 recorded commands exited successfully. Both new modules
compiled at their exact source hashes with Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`:

| Module | New public axiom audits |
|---|---:|
| `ResidualWord` | 12 |
| `DistinctWordBudget` | 9 |
| Total | 21 |

Each report used only `propext`, `Classical.choice`, and `Quot.sound`.
No new custom axiom, unfinished proof or native proof mechanism was
accepted. No earlier local theorem module was imported or recompiled.

The three exact Python controls passed in normal and optimized modes,
with byte-identical output between modes. The two saved certificate
JSON files also matched the regenerated outputs. The growth certificate
covers its proved continued-fraction cutoff and rejects seven malformed
inputs; the rational-cycle control rejects four invalid parameters.
The collision indexing check covers 1,944 finite identities, 2,758 actual
word windows and 940 distinct-height windows. Those bounded controls are
not evidence extrapolated to a full Collatz result.

`python -X utf8 -B tools/validate.py` passed from the same clean complete
checkout. Repository integrity is separate from mathematical verification.
The checker confirmed unchanged HEAD, tree, status, all 32 pinned inputs,
and both byte-exact compiler sources after execution. It records 17
current-source review bindings with their stated scopes.

## Artifacts

- [Complete published replay receipt](PUBLISHED_REPLAY.json).
- [Residual-word compiler and axiom output](logs/07-ResidualWord.log).
- [Finite-word compiler and axiom output](logs/08-DistinctWordBudget.log).
- [Growth certificate output](logs/09-normal-factor_growth_gap.log).
- [Rational control output](logs/10-normal-principal_fiber_control.log).
- [Collision indexing output](logs/11-normal-collision_budget.log).
- [Complete repository gate output](logs/15-repository-validation.log).

Every command log is copied byte for byte into `logs/`; its digest is
recorded in the receipt. The receipt preserves the actual external build
paths used during execution. No generated compiler object is committed.

The [research packet](../../research/central-closure-20261123/README.md)
and its [formalization scope](../../research/central-closure-20261123/FORMALIZATION.md)
separate the written algebraic-number and asymptotic arguments from the
finite Lean proofs. The global evaluated nondivisibility and critical
same-law collision upper estimate remain open.

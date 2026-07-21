# Preimage trees, density bounds, and collision fibers

## Located results

Applegate and Lagarias develop tree-search and inequality methods for lower bounds on the number of integers reaching a fixed target under inverse `3x+1` dynamics. Krasikov and Lagarias strengthen this program with systems of difference inequalities. [@ApplegateLagarias1995a; @ApplegateLagarias1995b; @KrasikovLagarias2003]

These papers are highly relevant to recursive counting, residue splitting, and concentration, but their principal object is a backward preimage tree: many starting integers that eventually reach one target, often at variable depths and through accelerated inverse branches.

## Repository object

A collision fiber in the active branches is a set of residues at one fixed depth `L`, normally with the same odd-step count, whose affine `L`-step images coincide. This is a stricter same-depth level-set problem.

## Safe connections

- The tree literature supplies models for recursive class splitting and linear/difference-inequality bounds.
- It does not imply `PR3/T-0005`, the exponential equal-signature collision theorem.
- It does not currently bound the maximal single-fiber exponent in `CLAUDE/Q-0006`.
- Applegate–Lagarias/Krasikov–Lagarias methods are nevertheless the strongest located starting point for an upper-bound program on within-stratum multiplicity.

## Proposed research interface

Define a state vector counting, for each affine output and odd-count stratum, the number of residues mapping there at depth `L`. Derive exact even/odd transition inequalities, then ask whether a finite inequality system can bound an exponential norm of this vector. This would be genuinely adapted from the tree literature rather than merely citing it by analogy.

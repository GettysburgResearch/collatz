# Automaticity, substitutions, and the 64/81 boundary slope

## Exact obstruction now available

The boundary slope `beta=log_64(81)` and the derived 17/18-gap frequency are transcendental (`LIT-KTHM-0004`). Existing letter frequencies in automatic sequences are rational (`LIT-KTHM-0005`). Frequencies of primitive-substitution fixed points are algebraic (`LIT-KTHM-0006`).

Therefore:

- no `k`-automatic finite-alphabet schedule can have the exact target gap frequency;
- no fixed primitive substitution can have that frequency.

## What remains open

These are complexity-class exclusions, not dynamical closure theorems. They leave:

- mechanical/Sturmian schedules;
- Ostrowski numeration algorithms;
- nonstationary S-adic directive sequences;
- computable but nonautomatic schedules;
- grammars with a larger state whose visible gap word has the target frequency.

The repository must still prove that any proposed schedule satisfies supply/demand congruences at every depth.

## Citation hygiene

Use “Cobham's rational-frequency property for automatic sequences” for the frequency argument. Reserve “Cobham's theorem” without qualification for the two-base recognizability theorem, which is not needed here.

## Suggested native split of `CLAUDE/T-0003`

1. periodic residue-data theorem — native and elementary;
2. transcendence of the target frequency — imported corollary;
3. nonautomaticity from irrational frequency — imported corollary;
4. fixed primitive-substitution exclusion — separate imported corollary;
5. Sturmian/Ostrowski candidate construction — open, not part of the obstruction theorem.

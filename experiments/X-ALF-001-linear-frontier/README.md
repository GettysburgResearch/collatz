# X-ALF-001 — linear precision and section-merging depth

**Finite exact support, not a complete Collatz proof.** The all-parameter claims
are in [the research packet](../../research/astra-linear-frontier/README.md).
The canonical report freezes one declared corpus. Python3.10+ and the standard
library suffice.

From the repository root:

```bash
python -B experiments/X-ALF-001-linear-frontier/run.py \
  --check experiments/X-ALF-001-linear-frontier/results/canonical.json
python -B experiments/X-ALF-001-linear-frontier/verify.py \
  experiments/X-ALF-001-linear-frontier/results/canonical.json --self-test
python -O -B experiments/X-ALF-001-linear-frontier/verify.py \
  experiments/X-ALF-001-linear-frontier/results/canonical.json --self-test
```

Use `run.py --output /tmp/alf.json` to regenerate a separate report. `--check`
does not overwrite the frozen artifact. The semantic SHA-256 covers the entire
`body`, including scope, coverage, negative controls and non-replay declarations.

## Corpus and independent reconstruction

The generator uses affine/valuation section formulas, direct retained-gap
construction, and forward accumulation in the ternary exponent lift. The
verifier imports no generator or repository module. It uses literal signed
inverse walks, actual forward parity residues for the shifted-remainder table,
a separate CRT algorithm, rational backward composition, and residual-target
removal for exponent lifting.

The corpus contains complete negative cones through radius10, the linear
budget's exact integer inputs, 900 full/pruned inverse-minimum comparisons,
8,190 finite parity words, and five symbolic A/B comparison trees. Twelve
ordinary CRT sources test D=1,...,4, a second lift, and a second exact ternary
depth. Their common-P repayment paths and immediate C-drops are replayed with
literal shortcut steps. The whole unpruned D-by-D box is additionally replayed
for the first source at D=1 and D=2. The other giant-source boxes use the proved
linear pruning and are not called full unpruned enumerations.

The four compressed convergence cases verify finite modular exponent-lifting
certificates. Their extremely large sources are represented by exact power
expressions; no literal execution of those complete enormous paths is claimed.
The written affine proof supplies their convergence. These cases do not verify
Collatz outside the stated family.

The twelve tamper controls recompute the checksum after changing scope, witness
population, parameter coverage, precision, minimum information or replay claims.
They must fail because their reconstructed contents differ, not merely because
the old checksum no longer matches. Checks remain active under `-O`.

Two exact negative controls are retained:121's entire lower-rank witness pool,
whose first possible forward meeting is54 shortcut steps/16 section returns;
and the failure of permanently dropping interior exits at208363. For every
ordinary family source, min(P,C) and max(P,C) both increase on the first edge,
despite C's exact9/64 drop. This is not hidden by a successful repayment later.

Both implementations have one author. Normal/optimized equality and mutation
rejection test the software, not independent acceptance of the mathematical
proof. See [the execution receipt](../../reports/astra-linear-frontier-01/validation.json)
for commands actually run and their outcomes.

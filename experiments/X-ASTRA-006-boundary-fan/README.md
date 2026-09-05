# X-ASTRA-006 — inverse boundaries and asynchronous bridges

**Exact finite support. All mathematical claims remain PROPOSED.**
The all-parameter proofs and open coverage obligation are in
[BOUNDARY_FAN.md](../../research/astra-critical-mass/BOUNDARY_FAN.md).
This experiment does not prove Collatz or a complete two-sided rank cover.

## What is reconstructed

Use the shortcut map, the section n=1 modulo 3, and
P(n)=(2n+1)^2/3^v3(2n+1). The generator uses the new at-most-five-candidate
formula for the best ancestor through two section returns. The verifier instead
constructs the **whole** two-generation inverse ball, by physically reversing
shortcut edges until the first section exit. No guessed source cutoff is used.

For the parameterized bridges it also uses a different construction of the
dyadic source class: bit-by-bit parity lifting rather than the generator's
closed rational fixed-point residue. The ternary CRT inverse is computed by
extended Euclid rather than Python's modular-inverse operation. Section returns
are checked by literal physical stepping rather than the closed run formula.
Both implementations have the same author: this is implementation independence,
not independent mathematical review or formal verification.

## Exact corpus

| Item | Coverage |
|---|---:|
| Section roots through 2^18 | 87,381 |
| Strict inverse rank improvements through two returns | 16,302 |
| Roots without such an inverse improvement | 71,079 |
| Improvements missed by greedily following only the least ancestor twice | 543 |
| Earlier depth-two residual inputs at the same cutoff | 1,011 |
| Removed by the exact new radius-two inverse criterion | 37 = 7 + 23 + 7 |
| Still in that residual after this particular test | 974 |
| Additional large fan comparisons | 55 |
| Three-parameter ordinary CRT cases | 216 |
| Actual subsequent forward returns in those cases | 2,268 |
| Substitutions in the three radius-two progressions | 18 |
| Substitutions in the third-return progression | 6 |
| Five-bit words for the T^5 fixed-point exclusion | All 32 |
| Resealed corrupt reports rejected | 8 |

The 37 removals are relative to the fourth pass's explicit five progressions,
not claimed additional to the union of every other rule in PR #90. The 16,302
count concerns **inverse** radius two only, not the earlier normalizer's forward
and merging reductions. Do not add those different counts together.

The larger inputs have h in {1,2,3,4,8,16,32,64} and seven positive odd 3-units,
with the absorbed source omitted. The bridge cases use a in {2,3,4,5,8,12},
H in {a+2,a+7,2a+9}, L in {1,2,4,8,16,32}, and two positive CRT lifts.
Progression substitutions include t=10^30 and t=3^100. These finite choices
do not replace the proofs for arbitrary parameters.

## Two deliberately retained failed proof strategies

At n=29371, the greedy inverse path chooses 26107 and then 104428, missing
the cheaper ancestor 69619 through the larger boundary exit 78322.

At n=208363, recursively keeping only boundary exits through three generations
misses the cheaper ancestor 4445077. The complete ball has 12 distinct nodes,
the boundary-only ball has seven, and their minima differ. The actual path is

    4445077 -> 3333808 -> 833452 -> 208363

under section returns, with shortcut word 100000. Thus the radius-two pruning
identity cannot simply be iterated as an all-depth proof. The same word yields
the valid infinite progression n=208363+314928t, without a claim that all its
members defeat every restricted search.

No convergence oracle or high-range convergence assumption is used in these
checks. Absence of an inverse certificate is never labelled a counterexample.
The T^5 argument rules out one finite cycle length only; it is used to show
that the a=2 merging family never meets at equal clocks.

## Replay

From the repository root, or the unpacked source tree:

```bash
python experiments/X-ASTRA-006-boundary-fan/run.py \
  --check experiments/X-ASTRA-006-boundary-fan/results/canonical.json
python experiments/X-ASTRA-006-boundary-fan/verify.py \
  experiments/X-ASTRA-006-boundary-fan/results/canonical.json --self-test
```

Both commands passed. Checks use explicit exceptions, not assertions removed
by Python's -O option. Compilation and an optimized-mode replay also passed.
Semantic SHA-256:

    3f06352e080db0c30281a9ebde34bbb21339f7feae4710072446b5737651d52e

Full reconstructed payload SHA-256:

    e371b3d0bc87667fd51e0afbd6202a058b71571b098d9c440698b65410fd9411

The compact certificate retains coverage and exact reconstructed row digests.
Add `--full-output /tmp/astra-sixth-full.json` to run.py to materialize every
row and both complete depth-three node sets. The verifier rederives the rows;
it does not simply trust hashes provided by the generator.

The self-test changes the claimed global scope, cutoff, unresolved count,
parameter coverage, fixed-point count, greedy winner, and the false recursive
pruning conclusion, then recomputes each report hash. All eight are rejected
against independently reconstructed mathematics and coverage.

No external large artifact, full-repository structural validator, Lean build,
workflow, or remote publishing operation is part of this experiment.

# Occupation, concentration, and arithmetic realization

Status: **PROPOSED**. This is exploratory research, not a Collatz proof or an independently reviewed result. No claim of literature priority is made.

## Results and the next mathematical target

[OCCUPATION.md](OCCUPATION.md) reconstructs the singular-mass obstruction: every weak odd-time occupation limit of a positive orbit tending to infinity has singular mass at least `2-log_2(3)`, approximately 41.5%, relative to normalized Haar measure on the odd 2-adics. It handles the singular point and nonergodic measures and gives an abstract model attaining the bound.

[CONCENTRATION.md](CONCENTRATION.md) goes further. It proves a valuation-block relative-entropy lower bound and a dyadic collision-growth lower bound, with the clock conversion explicit. After an exact finite check through 4096, **every hypothetical counterexample**, including a nontrivial cycle, must have every occupation limit's collision exponent greater than `1/20`. It also supplies entropy-sharp models and a separate construction proving collision-rate sharpness as an infimum under the stated abstract assumptions.

The remaining target is a **fixed-source pair-recurrence bound**, E5: prove that one occupation limit of each putative counterexample has collision exponent at most `1/20`. That would contradict the necessary lower bound. This arithmetic statement is OPEN. The necessary condition is compatible with counterexamples; it does not itself exclude them.

[ADELIC_SHADOWS.md](ADELIC_SHADOWS.md) constructs mixing, non-atomic biased models consistent simultaneously at primes 2 and 3. All finite joint observations have arbitrarily high positive ordinary witnesses, and changing-source positive segments can converge to the biased stationary law. Thus local consistency, qualitative mixing, and finite positive realizability cannot replace fixed-source arithmetic. A5 adds an exact source-size bound for repeated valuation blocks, retaining the positive-cycle exception.

## Four computational tracks, with actual receipts

The [standalone checker](../../experiments/novel-swarm-20261030/check.py) uses four process workers: inverse-branch/cylinder and repetition checks; certified entropy constants; joint-residue and stationary-law checks; and finite-floor/binary-law checks. These are computational workers, not independent AI reviewers.

The frozen [output](../../reports/novel-swarm-20261030/checks.json) records 1,364 valuation words, 4,092 ordinary lifts, 10,912 repetition cases (including 20 retained cycle exceptions), 9,438 joint-residue witnesses with all displayed states at least 10^20, and 12,285 binary model cylinders. The finite induction certifies all positive starts through 4096. Eight finite ternary model laws are checked exactly, with their infinite valuation tails summed rather than truncated. All checks passed in normal parallel, optimized parallel, and normal serial runs with byte-identical output.

Replay from the repository root:

```sh
python -B experiments/novel-swarm-20261030/check.py --output /tmp/collatz-checks.json
python -OO -B experiments/novel-swarm-20261030/check.py --output /tmp/collatz-checks-oo.json
python -B experiments/novel-swarm-20261030/check.py --workers 1 --output /tmp/collatz-checks-serial.json
```

These are finite tests, not proofs of the all-depth statements. See [scope, self-audit, and hashes](../../reports/novel-swarm-20261030/REVIEW.md). No complete-checkout repository validator or external theorem prover was run.

## Publication repair and limits of recovery

On 2026-10-30 the preceding chat reported a four-agent packet on `research/novel-swarm-20261030`, but explicitly did not confirm its push. Live branch search returned no matching branch, and the all-state PR query for that exact head returned `[]`. The current runtime contained none of the alleged packet files. Context retrieval recovered only summaries, not proofs, source bytes, commit IDs, or execution receipts.

This directory is consequently a **new reconstruction and continuation**, not a byte-for-byte recovery. The previous counts (1,978 automata, 4,283 trees, 98 certificates), independence claims, finite-dimensional rigidity, automatic-component rigidity, and comparison-network claims are not adopted as evidence. The old assertion of a weighted occupation theorem is replaced by an explicitly defined unweighted odd-time theorem. Its numerical constant agrees, but equivalence to the missing old statement is not asserted.

The branch and draft PR were created successfully in this continuation: https://github.com/GettysburgResearch/collatz/pull/140 . Initial reconstruction commit: `46c8cdf8d3e13eca29ecb69abb4441febae0eeda`. Base: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; base tree: `1c25c17df24491de6187445f1a1d355d5a7660c3`. The PR records the final content pin.

Direct Git transport failed because the container could not resolve `github.com`; connector reads and writes succeeded. This session had no callable multi-agent launcher. No independent AI review is claimed, and the missing prior packet was not silently promoted to verified research.

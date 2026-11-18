# Clean-checkout replay

All 65 top-level Python invocations exited with status zero on commit `0d024747d215fed242e2a92f7c0ca08a861129d1`, tree `f14922686a743fc9c24fdb2644b87df25fcece2d`, with 585 tracked files. There were 17 invocations under `experiments/`, one under `reports/`, 46 under `research/`, and one repository regression invocation. The initial C++ compilation was a prerequisite. The regression runner's own subprocesses are included in its single invocation.

The harness selected changed Python files since `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` whose filenames contained `check`, `ceiling`, `verify` or `classify`. It ran the raw ledger verifier twice, then appended the repository regression command. Coverage includes exact finite enumeration, reduced-range comparisons, cached numeric trace checks, finite certificate verification, and source-archive integrity. The bilateral minimum replay used depth 16 and reported an upper bound of 194191 millionths for infinite tilted survival. The two ledger replays verified 4,096 partition minima apiece, from 2,737,829 and 9,000 raw candidates respectively. The repository runner passed its checkout and bounded regression tests. These results do not decide an infinite orbit or certify all mathematical arguments in the checkout.

## Inputs

Use a checkout containing the pinned Git objects, Python 3, and a C++17 compiler with OpenMP. Supply a directory with the raw partition subdirectories `28-29/` and `30/`. The tracked receipt ledgers under `experiments/six-branch-modular-join/` authenticate the corresponding outputs. Producing the raw search partitions is a separate computation from replaying their ledgers. [Partition generation and restoration](../../experiments/six-branch-modular-join/README.md)

The archived Valbuena ZIP has SHA-256 `8109f2d8615530b11b00aa95f7a829761b05f28ef4f6b7a07c58ec84b48741fd`. Its checker verifies source and published build records. The 65-command suite does not rebuild the full native Lean trace. [Versioned Zenodo record](https://doi.org/10.5281/zenodo.23025885) · [Native verification scope](../../research/primary-evidence/PRIMARY_SOURCES.md)

## Reproduce the run

Run the following in Bash from a local repository containing the pinned commit. Set `LEDGER_ROOT` to the directory containing the raw partition subdirectories. The run creates a detached checkout and retains one log per invocation outside it.

```bash
set -euo pipefail
: "${LEDGER_ROOT:?Set LEDGER_ROOT to the absolute parent of 28-29 and 30}"
pin=0d024747d215fed242e2a92f7c0ca08a861129d1
run_dir=$(mktemp -d)
git worktree add --detach "$run_dir/checkout" "$pin"
cd "$run_dir/checkout"
test "$(git rev-parse HEAD)" = "$pin"
test -z "$(git status --porcelain)"
trace_archive="$run_dir/valbuena.zip"
curl --fail --location --output "$trace_archive" \
  'https://zenodo.org/api/records/23025885/files/x1xhlol/collatz-two-coordinate-obstruction-v2026.09.28.5.zip/content'
echo "8109f2d8615530b11b00aa95f7a829761b05f28ef4f6b7a07c58ec84b48741fd  $trace_archive" | sha256sum -c -
sha256sum -c <<'SUMS'
853ebb74a919f358d077239a2241dce583e2936f6682ce898f4f25a97af5100c  experiments/six-branch-modular-join/receipts-28-29.jsonl
dd39abf445d538a4391a028cdbbb3008c38c693c04d185c2ad31b8b740ec3adb  experiments/six-branch-modular-join/receipts-30.jsonl
SUMS
g++ -O3 -std=c++17 -Wall -Wextra -fopenmp experiments/six-branch-modular-join/join.cpp -o "$run_dir/join"
export OMP_NUM_THREADS=2
mkdir "$run_dir/logs"
count=0
run() {
  local label=$1
  shift
  python3 -X utf8 -B "$@" >"$run_dir/logs/$label" 2>&1
  count=$((count+1))
}
run experiments_binary-run-occupancy_check.py experiments/binary-run-occupancy/check.py
run experiments_native-pressure-20261118_crosscheck.py experiments/native-pressure-20261118/crosscheck.py reports/native-pressure-20261118/collisions.json
run experiments_native-pressure-20261118_verify.py experiments/native-pressure-20261118/verify.py
run experiments_pressure-localization-20261118_check.py experiments/pressure-localization-20261118/check.py reports/pressure-localization-20261118/trace.json
run experiments_pressure-localization-20261118_check_log.py experiments/pressure-localization-20261118/check_log.py reports/pressure-localization-20261118/log_trace.json
run experiments_six-branch-modular-join_check.py experiments/six-branch-modular-join/check.py "$run_dir/join"
run experiments_six-branch-modular-join_check_partition.py experiments/six-branch-modular-join/check_partition.py "$run_dir/join"
run verify_ledgers.py-28-29 experiments/six-branch-modular-join/verify_ledgers.py "$LEDGER_ROOT/28-29" experiments/six-branch-modular-join/receipts-28-29.jsonl
run verify_ledgers.py-30 experiments/six-branch-modular-join/verify_ledgers.py "$LEDGER_ROOT/30" experiments/six-branch-modular-join/receipts-30.jsonl
run experiments_six-branch-real-windows_check.py experiments/six-branch-real-windows/check.py
run experiments_sparse-periodic-deviations_check.py experiments/sparse-periodic-deviations/check.py
run experiments_stack-combined-moments_ceiling.py experiments/stack-combined-moments/ceiling.py
run experiments_stack-combined-moments_check.py experiments/stack-combined-moments/check.py
run experiments_stack-period-ten_check.py experiments/stack-period-ten/check.py
run experiments_stack-weight-classification_classify.py experiments/stack-weight-classification/classify.py
run experiments_stack-weight-classification_verify.py experiments/stack-weight-classification/verify.py
run experiments_uniform-predecessor-20261118_check.py experiments/uniform-predecessor-20261118/check.py
run reports_stack-period-ten-review_check.py reports/stack-period-ten-review/check.py
run research_critical-orbit-mellin_check_phase_avoidance.py research/critical-orbit-mellin/check_phase_avoidance.py
run research_critical-orbit-mellin_check_two_blocks.py research/critical-orbit-mellin/check_two_blocks.py
run research_critical-orbit-mellin_check_two_scale.py research/critical-orbit-mellin/check_two_scale.py
run research_critical-orbit-mellin_check_two_scale_transfer.py research/critical-orbit-mellin/check_two_scale_transfer.py
run research_cyclic-shift-distance_check.py research/cyclic-shift-distance/check.py
run research_cyclic-shift-distance_floor_check.py research/cyclic-shift-distance/floor_check.py
run research_cyclic-shift-distance_shape_check.py research/cyclic-shift-distance/shape_check.py
run research_fixed-floor-shells_check.py research/fixed-floor-shells/check.py
run research_fixed-floor-shells_check_bilateral_minimum.py research/fixed-floor-shells/check_bilateral_minimum.py --depth 16
run research_fixed-floor-shells_check_floor_tree.py research/fixed-floor-shells/check_floor_tree.py
run research_fixed-floor-shells_check_minima.py research/fixed-floor-shells/check_minima.py
run research_fixed-floor-shells_check_minimum_residual.py research/fixed-floor-shells/check_minimum_residual.py
run research_fixed-floor-shells_check_mixed_cantor.py research/fixed-floor-shells/check_mixed_cantor.py
run research_fixed-floor-shells_check_mixed_cycles.py research/fixed-floor-shells/check_mixed_cycles.py
run research_fixed-floor-shells_check_negative_one.py research/fixed-floor-shells/check_negative_one.py
run research_local-mahler-lifting_check_growth_layers.py research/local-mahler-lifting/check_growth_layers.py
run research_pointwise-run-defects_check_hankel.py research/pointwise-run-defects/check_hankel.py
run research_primary-evidence_check_trace_archive.py research/primary-evidence/check_trace_archive.py "$trace_archive"
run research_rotation-coded-orbits_check.py research/rotation-coded-orbits/check.py
run research_stack-modular-differences_check.py research/stack-modular-differences/check.py
run research_stack-shift-residual_check.py research/stack-shift-residual/check.py
run research_synchronized-cycle-blocks_check.py research/synchronized-cycle-blocks/check.py
run research_synchronized-cycle-blocks_check_farey_sweeps.py research/synchronized-cycle-blocks/check_farey_sweeps.py
run research_synchronized-cycle-blocks_check_four_power_cones.py research/synchronized-cycle-blocks/check_four_power_cones.py
run research_synchronized-cycle-blocks_check_power_coverage.py research/synchronized-cycle-blocks/check_power_coverage.py
run research_synchronized-cycle-blocks_check_single_rise.py research/synchronized-cycle-blocks/check_single_rise.py
run research_synchronized-cycle-blocks_check_three_power_cones.py research/synchronized-cycle-blocks/check_three_power_cones.py
run research_two-prime-growing-blocks_check_reverse.py research/two-prime-growing-blocks/check_reverse.py
run research_unrestricted-cycle-denominator_check.py research/unrestricted-cycle-denominator/check.py
run research_unsafe-return-weights_check.py research/unsafe-return-weights/check.py
run research_unsafe-return-weights_check_clock.py research/unsafe-return-weights/check_clock.py
run research_unsafe-return-weights_check_distortion_cutoff.py research/unsafe-return-weights/check_distortion_cutoff.py
run research_unsafe-return-weights_check_first_hit_maximum.py research/unsafe-return-weights/check_first_hit_maximum.py
run research_unsafe-return-weights_check_lattice.py research/unsafe-return-weights/check_lattice.py
run research_unsafe-return-weights_check_maximum_intervals.py research/unsafe-return-weights/check_maximum_intervals.py
run research_unsafe-return-weights_check_mergers.py research/unsafe-return-weights/check_mergers.py
run research_unsafe-return-weights_check_minimum_mean.py research/unsafe-return-weights/check_minimum_mean.py
run research_unsafe-return-weights_check_occupation.py research/unsafe-return-weights/check_occupation.py
run research_unsafe-return-weights_check_optimal.py research/unsafe-return-weights/check_optimal.py
run research_unsafe-return-weights_check_order.py research/unsafe-return-weights/check_order.py
run research_unsafe-return-weights_check_ordinary.py research/unsafe-return-weights/check_ordinary.py
run research_unsafe-return-weights_check_signed_mass.py research/unsafe-return-weights/check_signed_mass.py
run research_unsafe-return-weights_check_sinai_norm.py research/unsafe-return-weights/check_sinai_norm.py
run research_unsafe-return-weights_check_sublevels.py research/unsafe-return-weights/check_sublevels.py
run research_unsafe-return-weights_check_support.py research/unsafe-return-weights/check_support.py
run research_unsafe-return-weights_check_towers.py research/unsafe-return-weights/check_towers.py
run repo-regressions tools/validate.py --regressions
test "$count" -eq 65
printf 'Passed %s invocations. Logs in %s\n' "$count" "$run_dir/logs"
```

The recorded harness was `collatz-final20-replay.py` (SHA-256 `bcdf454987f4e790f25f0151c719a0d61e96d3d33e1736b6846b72fff9802bc4`). Its status ledger was `collatz-final20-verified.log` (SHA-256 `127b0050f1602bfddcf5ac10b20af654944ee94c3906a74c54f202fb9593b76c`), with a separate output file per label under `collatz-replay-final20-verified/`. The recorded ledger includes elapsed times, so a repeat run should compare statuses and substantive outputs.

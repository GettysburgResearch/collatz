# Evidence for the two independent theorem audits

The two console files preserve the output of the independent agent runs. The first run rebuilt five sources and queried 37 public theorems in the four round-nine lane modules. The second rebuilt the ten new modules at the frozen PR192/193 heads and three PR192 dependencies, queried 65 public theorems, and ran three Python controls in two modes. Both exited successfully. The audit drivers parsed each Lean response in memory. Their temporary directories closed at exit, so the original individual compiler streams were not retained. [37-theorem stdout](agent37.stdout) · [65-theorem stdout](agent65.stdout)

The machine-readable receipt binds all input source bytes, the Lean executable and flags, the console outputs, and the three control outputs. For the 37 individual theorem results it points to the coordinator's existing module logs for 35 declarations, plus a separately retained direct query for the two barrier helpers using the matching previously compiled module. For the 65 upstream names it gives the exact existing PR192 and PR193 compiler-log paths, commit IDs and file digests. Each name is checked against its declaration in the bound source. These corroborating logs retain their original provenance. [Audit receipt](audit_receipt.json) · [Supplementary two-theorem log](barrier_helpers.log)

The coordinator separately rebuilt eight project modules and recorded 76 selected inventories, including the final proposal. The two independent audits cover different module and theorem sets. [Coordinator's eight-module receipt](../../lean/receipt.json)

Before publication, one surplus terminal newline was removed from
BarrierEnvelope.lean. The receipt records both byte hashes. The archive
verifier first checks the published source hash, then appends that one
newline to reconstruct exactly the earlier independently audited bytes.
The coordinator's subsequent eight-module build checks the published
bytes directly. No theorem statement or proof body changed.
[Formatting record](../../EOF_NORMALIZATION.json)

## Replay

The pinned PR192 and PR193 Git objects must be available locally for the upstream audit. Running the script without arguments rechecks source and log hashes, the declared names, allowed axioms and the stored inventory totals. This verification passed for all 102 names after the receipt was assembled. No broad compiler rebuild was repeated while packaging this evidence.

```sh
python3 -B reports/astra-global-closure-20261124/round9/arithmetic/upstream/replay.py
```

To regenerate the original theorem queries with full compiler streams, supply a matching compiler and, for the upstream modules, the matching Mathlib checkout with its dependency objects. The optional build commands save the generated harness, compiler output and a new result receipt in the specified directory. The new driver preserves the original compiler flags, and schedules each dependency before its consumers.

```sh
python3 -B reports/astra-global-closure-20261124/round9/arithmetic/upstream/replay.py \
  --run lane37 --lean "$LEAN_BINARY" --logs "$LANE_AUDIT_OUTPUT"
python3 -B reports/astra-global-closure-20261124/round9/arithmetic/upstream/replay.py \
  --run upstream65 --lean "$LEAN_BINARY" --mathlib "$MATHLIB_CHECKOUT" --logs "$UPSTREAM_AUDIT_OUTPUT"
```

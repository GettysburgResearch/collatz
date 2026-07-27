# X-7701 — Exact cross-model audit replay

This packet is standard-library only.

`check.py` was written independently of the Claude/Fable source programs. `verify.py` is separately structured and does not import `check.py`; in particular, the small cycle enumeration uses compositions in `check.py` and a recursive parts traversal in `verify.py`.

## Frozen coverage

```text
Claude reciprocity-error repair constant
Collatz floor through 1,000,000
L-9913 arithmetic m*(10^6) and m*(10^9)
L-9915 exact cross-model replay through m=14
L-9927 complete 166-value allowed-set elimination list
L-9918 full-group Parseval counterexample
```

Results:

```text
maximum total stopping time through 10^6: 524 at 837799
m*(10^6):                              2966, K=4701
m*(10^9) arithmetic value:             47468, K=75235
m=7..14 compositions:                  648635
m=7..14 divisibility hits:             0
L-9927 eliminated lengths:             166
L-9927 maximum eliminated length:      1024
L-9927 permanent nonempty threshold:   1039
semantic digest:
485926c992f1fc780116fa1fca15e474a90c82d6dc32238932713702bc7274c8
```

## Replay

```bash
python3 -B experiments/X-7701-crossmodel-audit/check.py \
  --output /tmp/X-7701.json \
  --check-results experiments/X-7701-crossmodel-audit/results/canonical.json

python3 -B experiments/X-7701-crossmodel-audit/verify.py \
  experiments/X-7701-crossmodel-audit/results/canonical.json
```

## File SHA-256

```text
check.py:       27a450102dac947af05487ef79f965f0208c0536ae3e2ea7d51657ddbfddfacd
verify.py:      901f0366325a0b3c493ca0f598468838a409796d5c215a424a209d8921732793
canonical.json: df0bbfb7d1410e05c8a785b7ae654d6137b7eab15753c4a43063811523c34ad0
```

## Limitations

- The full `L-9915` enumeration for `m=15..21` was not replayed here.
- The memory-bound `T-9925` phase-floor certificates were not replayed here.
- The `F=10^9` line checks the exact Diophantine threshold arithmetic, not the independent finite verification of every orbit through `10^9`.
- No bounded result is extrapolated to a Collatz conclusion.

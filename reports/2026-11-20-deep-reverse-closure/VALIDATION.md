# Actual scientific-commit validation

**Both complete-checkout validations passed. Collatz is not proved.**
The checks below ran against the actual GitHub commit after it was created
and fetched, in a separate complete clean checkout. Their receipts were
written outside that checkout and copied here without reformatting.

| Identity | Actual value |
|---|---|
| Scientific commit | `08e5757ad778c1f18ac2f54a536907f92a510352` |
| Scientific tree | `a8da04559de02060bf81ea1441d05be818f0040a` |
| Tracked files in the complete checkout | 359 |
| Frozen scientific/review/source hashes checked | 42 |
| Scientific programs | 16 |
| Successful normal and `-OO` executions | 32 |
| Normal/optimized output reports | Byte-identical for every program |
| Repository commands with regressions | 11, all passed |
| Checkout after both runs | Same commit and tree; clean |

## Commands actually executed

```bash
python -X utf8 -B research/deep-reverse-closure-20261120/check_packet.py --receipt /workspace/scratch/957bb0caa6f2/deep-actual-packet-replay.json
python -X utf8 -B tools/validate.py --regressions --receipt /workspace/scratch/957bb0caa6f2/deep-actual-repository-validation.json
```

The packet run began at `2026-11-20T21:50:44.720997+00:00` and finished at
`2026-11-20T21:50:52.525198+00:00`. The repository validation began at
`2026-11-20T21:50:44.711750+00:00` and finished at `2026-11-20T21:50:49.556776+00:00`.
These timestamps are UTC.

## Exact receipts

| Receipt | SHA-256 |
|---|---|
| [Packet replay](packet-replay.json) | `19f41ae9122d83875d268b7617f282a45793562d06a41a788f64c9ba8e36c356` |
| [Repository validation](repository-validation.json) | `22a23892c5027c4ba004a3af89499eb9950d93ce096eb9043514667845163b98` |

The first receipt retains every scientific program's command, exit code,
exact output data, output hash and timing. The second retains the eleven
repository commands and their actual output. The [review guide](README.md)
explains which independent implementation checks each claim and where a
written argument or external theorem supplies an all-parameter deduction.

## Documentation-child boundary

These receipts and this validation record are appended in a documentation
child of the scientific commit. Only these three report paths change:

- `reports/2026-11-20-deep-reverse-closure/VALIDATION.md`
- `reports/2026-11-20-deep-reverse-closure/packet-replay.json`
- `reports/2026-11-20-deep-reverse-closure/repository-validation.json`

Every file in `content-manifest.json` is preserved. These executions are
claimed for the scientific commit above, not retroactively for its later
documentation child. The final remote branch and PR head, the exact child
tree, and preservation of all scientific hashes are checked separately.

Repository integrity, exact finite replay and internal agent review do not
establish the missing global certificate transformation or energy upper
bound. The scientific packet continues to label those steps OPEN.

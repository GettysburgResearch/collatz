# Fixed-source splicing

**PROPOSED research; not a complete Collatz proof.** Read [PROOF.md](PROOF.md).
This continues #130 while preserving its six files and all prior statuses.
The new decision rules use the unchanged ordinary source, rather than choose
another member of a constructed affine gate.

For C=2^(2k+1)v, v odd, there is the gate-free identity

    T^(2k+2)(9C+2)=T(3^(k+1)v).

The witness is accepted only if it is below the ORIGINAL source. At first
odd-run entry N=2^r*u-1 this gives an exact inequality; it is automatic for
r=2,3,4,5 at every odd valuation. A critical choice of k gives infinite
no-forward-descent families for every r>=5, with r and k both unbounded.
A separate safe restart uses the old good-exit identity after the second
odd run when r=2 or3. Its complementary exit reaches another H comparison;
the one-step formula then applies with a fresh ORIGINAL-root order test,
including for larger r. None of these rules covers every input.

## Replay from the repository root

Python standard library only. The generator checks the precise Git blob of
the inherited #130 generator before loading it; no network is needed.

```sh
python -B -S experiments/paired-comparison/fixed-source-splicing/run.py \
  --full /tmp/fss.jsonl --summary /tmp/fss.json
python -B -S experiments/paired-comparison/fixed-source-splicing/verify.py \
  /tmp/fss.jsonl --summary experiments/paired-comparison/fixed-source-splicing/canonical.json --self-test
python -OO -B -S experiments/paired-comparison/fixed-source-splicing/verify.py \
  /tmp/fss.jsonl --summary experiments/paired-comparison/fixed-source-splicing/canonical.json --self-test
```

On Windows replace the temporary paths with local paths and use `py -3`.
No Windows run is claimed. A standalone packet can pass `--parent PATH` to
the exact prior generator. That file is inherited in the stacked repository,
not copied into this additive commit.

The verifier imports no generator/repository module. It checks old positive
witnesses and independently reconstructs the new fixed-source decisions.
Old OUTSIDE labels are authenticated, not independently reclassified. The
benchmark uses N=2..65536, distinct from the earlier C-parameter benchmark.
All remaining cases and 59 bounded unfinished searches are retained.

[Execution receipt](../../../reports/paired-comparison-fixed-source-splicing/validation.json)
records commands, file identities, actual results and limits. No full-checkout
root validator, remote CI, Lean build or independent mathematical review was
performed. Read the root-order countercontrol N=191 before modifying guards.

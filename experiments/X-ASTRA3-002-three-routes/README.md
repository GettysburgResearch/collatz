# X-ASTRA3-002 — exact three-route continuation regressions

The mathematical proofs are under
[research/astra-three-routes/pass2](../../research/astra-three-routes/pass2/README.md).
This artifact has **finite scope only**. It does not independently verify an
all-length theorem or claim a Collatz proof.

From the repository root:

```bash
python -B experiments/X-ASTRA3-002-three-routes/run.py \
  --check experiments/X-ASTRA3-002-three-routes/results/canonical.json
python -B experiments/X-ASTRA3-002-three-routes/verify.py \
  experiments/X-ASTRA3-002-three-routes/results/canonical.json --self-test
```

Use `run.py --output /tmp/astra3-pass2.json` to regenerate a report. The report
contains deterministic coverage counts, digests of complete generated tables,
and the actual rational countermodel and nonlinear rank witnesses.

The verifier imports no generator or repository code. Its independent methods
are exhaustive odd-residue cylinder reconstruction, a Pascal recurrence for
composition counts, breadth-first word generation, direct rational physical
continuation, bitwise parity-cylinder lifting, and literal whole-run replay.
For ranks, `[p, root, power, sign]` denotes
`sign*v_p(n-root)^power*log(p)`; sign 0 instead means the oscillating coefficient
`(-1)^v_p(n-root)`. Every example also has the leading term `log(n)`.
There are nine profile choices and four modes (T, T^2, T^4, whole-run F).

All 9,779 formal positive-displacement sources in this finite echo corpus are
nonintegral. The 9,381 rejections must not be described as integer counterexample
exclusions. The rational cycle countermodel is positively certified forever by
its finite periodic replay; it is not an ordinary Collatz counterexample.

Both implementations were written in the same authoring session. This provides
implementation independence, not independent mathematical review.

Semantic SHA-256:

    541017f8a517ee731791224129150e68543bd06c434de48e5ffa07e447aa2b68

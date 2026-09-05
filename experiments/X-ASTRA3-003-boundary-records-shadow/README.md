# X-ASTRA3-003: exact third-pass interfaces

Run from the repository root:

```bash
python -B experiments/X-ASTRA3-003-boundary-records-shadow/run.py \
  --check experiments/X-ASTRA3-003-boundary-records-shadow/results/canonical.json
python -B experiments/X-ASTRA3-003-boundary-records-shadow/verify.py \
  experiments/X-ASTRA3-003-boundary-records-shadow/results/canonical.json --self-test
```

Both use the Python standard library. The verifier imports no generator or
repository module. Both programs were written in one session, so the evidence
is implementation independence, not independent mathematical review.

The schema and scope string are checked exactly. The compact JSON preserves
complete coverage parameters and deterministic digests; the verifier
reconstructs every summarized case rather than trusting a checksum alone.
All-source means exact finite-time AP decomposition with a bounded infinite
tail. It does NOT mean every time is covered.

Coverage: H=64 and 4096; k=0,...,12; 16,382 cylinders; 65,528 lifted ordinary
sources; 64 AP terms and 16 curvature blocks per cylinder; 6,146 no-descent
subsegments; 24,101 correction-product positions; eight exact integer
inequalities; 18 polynomial-dictionary shadows and 189 whole-run packets.
The three dictionaries include affine, nonlinear polynomial, interacting, and
previous rational-cycle-root observations. All tested feature vectors match
at every packet boundary. The sample sources grow with the shadow length.

Outward bounds use integer arithmetic at scale 2^80. The tail integral and
signed-curvature remainder are proved in
`research/astra-three-routes/pass3/BOUNDARY_CHARGE.md`.
The source paths stop at their first repeated state. No computation here
instantiates the enormous universal coefficient-record window.

Eight resealed corruptions are rejected. The older large finite inverse cone,
external certificates, and full-repository validator are not run.

Semantic SHA-256:

    dd5c52ff9a06ae728f7f10d84db655ae3324ca2318531b130ff66eced5b7feb6

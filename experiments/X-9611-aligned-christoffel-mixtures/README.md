# X-9611 — Aligned Christoffel conjugate mixtures

This exact standard-library experiment supports `L-9607` and `T-9607`.

For every primitive rational slope with denominator at most `30`, it forms the lower mechanical word `w=uv` from its two Farey-parent factors and the standard conjugate `w~=vu`. For repetition counts through `12`, it exhausts every aligned binary mixture of `w` and `w~`.

The experiment verifies:

```text
C_total=C_w*G_R-(C_w-C_w~)*H,
D_total=(2^A-3^k)*G_R,
gcd(C_w-C_w~,G_R)=1.
```

Every genuinely mixed orientation therefore has `C_total` nonzero modulo the complete geometric factor `G_R`. The two constant patterns reduce to powers of the unrepaired rational mechanical word and are independently excluded by `T-9606`.

Frozen totals:

```text
primitive slope/repetition rows       3,324
aligned patterns checked          2,268,630
genuinely mixed patterns          2,261,982
geometric coprimality checks          3,324
formal divisor hits                       0
```

Digests:

```text
semantic SHA-256
85dd87dd940826acad6974e8bff044336a3f5a9180b9f8d53861cddcef670ccf

canonical results SHA-256
2f73d6db474a5e4d6e69a16f929f9237421caf4be56ffa0a306f31ba472ac1b5
```

Replay:

```bash
python3 -B experiments/X-9611-aligned-christoffel-mixtures/run.py \
  --check-results \
  experiments/X-9611-aligned-christoffel-mixtures/results/canonical.json
```

This is a finite audit of an all-scale proof. It does not claim a positive cycle or divergent orbit. Its constructive conclusion is that successful Christoffel repairs must be nonaligned or genuinely multiscale.
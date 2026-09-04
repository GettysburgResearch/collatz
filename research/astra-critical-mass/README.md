# Astra: critical-mass and all-history Collatz proof attempt

**Full Collatz proof: not obtained.** This packet contains new proof-bearing
partial results, exact refutations of attempted global certificates, a
source-qualified critical-endpoint refinement, and an explicitly open
end-to-end Green-mass target.

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05, Asia/Jerusalem.
Research workspace: [issue #89](https://github.com/GettysburgResearch/collatz/issues/89).
Every new theorem is **PROPOSED pending independent review**.

## Read the mathematics

[PROOF.md](PROOF.md) supplies all proofs and the exact remaining inequality.
[FIRST_PASSAGE.md](FIRST_PASSAGE.md) gives the ordinary endpoint-fiber compiler.
[ATTEMPT.md](ATTEMPT.md) records what was tried, why it failed, and the next
specific target. [SOURCES.md](SOURCES.md) freezes dependencies and trust boundaries.

| Claim | Content | Boundary |
|---|---|---|
| T-ASTRA-001 | Critical exponent, odd-core, and logarithmic-mass closure | Collatz implication uses source-qualified P(0.901); no actual exceptional-mass upper bound proved |
| T-ASTRA-002 | Positive summable killed-transfer and Green-mass criteria | Uniform Green bound remains open |
| T-ASTRA-003 | Ordinary-ray obstruction for power-like pointwise weights | Does not rule out general aggregate or arithmetic weights |
| L-ASTRA-004 | Explicit summable ternary-valuation weight, tail bound, and two-class drift | Third residue class fails |
| T-ASTRA-005 | Infinite even-ray repair and unbounded failure at every fixed block length | One specified infinite-state family, not all methods |
| L-ASTRA-006 | Exact first-passage endpoint progressions, intervals, and mass identities | Finite interface; no mixing premise proved |
| T-ASTRA-007 | Logarithmic saving at the critical recurrence exponent | Conditional recurrence not instantiated |
| X-ASTRA-001 | Independently implemented exact finite checks | Finite time only; no all-time inference |

## Strongest concrete certificate

For w0(n)=3^v3(n+1)/(n+1)^2 and lambda=65/64, define

    G_K = sum_{k=0}^K lambda^k sum_{n>=2, tau(n)>k} w0(n).

The exact certificate gives

    8.6140 < G_256 < 8.9619.

This includes every positive source n>=2 via a proved analytic source-tail
bound, but only the times k=0,...,256. A finite uniform bound on G_K as K grows
would prove Collatz without any imported predecessor theorem. **That uniform
bound is not proved.** The attempted valuation/even-ray certificate is refuted
by a positive ordinary family, even after any fixed block acceleration.

## Replay

From the repository root:

```bash
python experiments/X-ASTRA-001-critical-mass/run.py \
  --check experiments/X-ASTRA-001-critical-mass/results/canonical.json
python experiments/X-ASTRA-001-critical-mass/verify.py \
  experiments/X-ASTRA-001-critical-mass/results/canonical.json
```

Both commands passed locally. Semantic digest:

    28423e99643053ff26768b5a7859d0b66a960226856da7ae372df802b2bddd04

The verifier does not import the generator. Both implementations were authored
in this session, so mathematical review by another contributor is still needed.
No existing canonical record, source PR, workflow, or repository setting is changed.

# X-ASTRA-006: unequal-clock rank certificates and precision barriers

**Finite exact support. All theorem claims remain PROPOSED. Full closure OPEN.**
The mathematical proofs and the residual set are in
[CLOCK_DEFECT.md](../../research/astra-critical-mass/CLOCK_DEFECT.md).

## What is checked

Use T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n, and
P(n)=(2n+1)^2/3^v3(2n+1), including depth zero. An accepted diagram has two
actual positive sources, a common endpoint, and strictly lower witness rank.

The depth-two compiler begins with n=11 mod 16 (word 1101), the dyadic part of
the preceding five residual progressions. At each length 4..18 it tries:

1. a forward rank drop with a provably frozen endpoint valuation;
2. a one-step odd ancestor of the forward endpoint, with an even positive
   number of trailing zero bits and a provably frozen witness valuation.

A rule must have a strict rank drop at its least positive CRT source and a
strict limiting rank ratio below one. The written monotonicity proof, not the
finite replays, certifies all larger sources with exact ternary depth two.
Unfrozen valuation cases are not assigned a guessed depth.

The corpus contains 263 prefix-free rules: 192 forward and 71 unequal-clock.
Their union covers 15980 of 16384 relevant dyadic classes at modulus 2^18. The
other 404 are retained. Combined with the five old ternary classes, they leave
2020 residue classes modulo 21,233,664. This is NOT complete Collatz coverage,
and higher ternary-depth cases are outside this particular compiler.

## Coverage and independent implementation

- 2104 physical ray replays: both ternary unit classes and four upward lifts
  per rule. The arithmetic proof covers every lift, not just those four.
- 32 high-precision cases, max clocks 1..8, with minimal H satisfying
  3^H>=12^M. Every inverse diagram is enumerated: 5864 pairs in total.
  Nonzero defects force a rank increase by more than 4/3. All 12 lower-rank
  pairs are homogeneous same-clock cancellations. All-odd cases have none.
- 24 ordinary cost-family cases at H=3,6,12,24,48,96. They have exact
  v2(n+1)=4H and a proved lower clock bound. Their explicit 1^(4H)0 reductions
  are replayed for 3048 total shortcut steps. The all-candidate lower bound
  at large H comes from the theorem, not exponential enumeration.
- Five members of the unequal-clock 859/517 progression, including t=10^30.
- Eight examples showing that the SAME 859 source word increases rank when
  its input ternary depth is 3,4,10,30. This guards against a false all-height
  extension of the depth-two result.
- Eight deliberately modified reports rejected after resealing: false scope,
  reduced depth, reduced rule count, inflated coverage, deleted residuals,
  reduced inverse coverage, reduced cost-path coverage, and altered rule digest.

The generator composes affine words and enumerates physical inverse trees.
The verifier does not import it or repository modules. It enumerates source
residues and runs T physically, reconstructs slopes from two sources, composes
rational inverse maps in reverse order, and uses extended Euclid for CRT.
Both programs have the same author: implementation independence, not
independent mathematical review or formal verification.

## Replay

From the repository root:

```bash
python experiments/X-ASTRA-006-clock-defect/run.py \
  --check experiments/X-ASTRA-006-clock-defect/results/canonical.json
python experiments/X-ASTRA-006-clock-defect/verify.py \
  experiments/X-ASTRA-006-clock-defect/results/canonical.json --self-test
```

To reconstruct every rule, residual residue, and finite test row, add
`--full-output /tmp/astra-clock-full.json` to either command.

Semantic SHA-256:

    29dfd75d4ae6109a71dd46ec4a995c23f95a51e376eb91136c2ddf24700ef34d

Full reconstructed payload SHA-256:

    533edb00d366fc7b73f6befd42c5a28cb51a280912deeaf716295a374a554662

Both programs passed and produced byte-identical full payloads locally. They
use explicit exceptions for failed checks, so validation remains active under
Python -O. No global convergence, unknown stopping time, random independence,
external certificate, Lean build, workflow, or full-repository validator is
assumed. Previous X-ASTRA artifacts are unchanged.

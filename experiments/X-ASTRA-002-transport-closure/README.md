# X-ASTRA-002: finite transport dictionaries and simultaneous block witnesses

**Status: finite exact computational support; theorem claims remain PROPOSED.**
This experiment supports [CONTINUATION.md](../../research/astra-critical-mass/CONTINUATION.md).
It does not establish the all-parameter theorem by enumeration and does not
prove the uniform Green bound or Collatz.

## What is certified

For each dictionary, block cap B in {1,4,8}, and ternary depth h in {16,32,64},
the generator finds a rational centre outside the dictionary's entire union
of even rays and constructs a positive odd CRT source u. Every source
2^(ell-1)*u, 1<=ell<=B, follows ell-1 even steps and one odd step to the same
endpoint y. A single lower weight works simultaneously for all these paths.

The endpoint's *whole infinite even ray* is bounded by exact rational partial
terms plus the analytic geometric tail from L-ASTRA-010. There is no numerical
truncation of that ray without a remainder. Directed fixed-point rounding at
512 bits keeps each bound rigorous without enormous common denominators.

For finite Green histories, the upper dictionary is a majorant only. Its
congruence and killing guards are not assumed away: the lower source term is
the actual w0 summand. The guarded compiler is checked separately against
physical inverse enumeration in run.py and against direct forward enumeration
in verify.py.

## Corpus

- Seven dictionaries: n+1 alone; the repair adding 8n-1 and 16n-5; a mixed
  four-form example; the zero-centre example; and complete finite Green
  dictionaries through depths 2, 4, and 6.
- 63 witness rows and 273 actual positive-integer block paths.
- 889 endpoint/depth compiler comparisons, containing 2,467 guarded source
  terms (endpoints 2..128 and lengths 0..6).
- Three finite terminating systems with 23 states each, for the qualitative
  inverse-potential identity. They do not certify an all-source Collatz weight.
- Five deliberately resealed corrupt reports rejected by the verifier.

Every witness certifies a common ratio at least 26. The following are rigorous
integer floors of the common lower ratio at h=16, B=8, not floating estimates:

| Dictionary | Formal terms | Distinct centres | Certified common ratio floor |
|---|---:|---:|---:|
| Base | 1 | 1 | 2427 |
| Displaced repair | 3 | 3 | 2390 |
| Mixed centres | 4 | 4 | 1061 |
| Zero centre | 1 | 1 | 11084 |
| Green depth 2 | 7 | 3 | 602 |
| Green depth 4 | 31 | 9 | 336 |
| Green depth 6 | 127 | 33 | 26 |

The Green rows additionally certify one actual deeper-history contribution
that exceeds the finite envelope. The all-depth conclusion and polynomial
blow-up rate follow from the written proof, not from these selected depths.

## Replay

From the repository root:

```bash
python experiments/X-ASTRA-002-transport-closure/run.py \
  --check experiments/X-ASTRA-002-transport-closure/results/canonical.json
python experiments/X-ASTRA-002-transport-closure/verify.py \
  experiments/X-ASTRA-002-transport-closure/results/canonical.json --self-test
```

Both passed locally. Semantic SHA-256 of the canonical payload:

    e60793cc032c1855a7d8da8cfd2c76f2c375f1635a12c4425ca1598a4651207e

The verifier imports no generator code. It uses recursive affine composition,
a uniqueness check for the CRT source, direct forward enumeration with an
exhaustive source bound, and backward substitution for the finite potential
identity. Both programs were authored in this continuation: this is independent
implementation, **not independent mathematical review**.

The `--self-test` option reseals the digest after deleting a witness, inflating
the scope, understating an infinite-ray upper bound, changing the source parity,
or reducing the compiler coverage. All five must be rejected for mathematical
or coverage reasons, not merely because a hash is stale.

No large Collatz census, external certificate replay, Lean build, full-repository
validator, or workflow is part of this experiment. The first packet's
X-ASTRA-001 artifact and claims remain untouched.

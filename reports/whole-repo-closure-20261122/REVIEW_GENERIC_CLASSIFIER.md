# Independent review: effective fixed-block classifier

Date: 2026-11-21 UTC. Reviewer: literature_symbolic.
Verdict: VERIFIED at the exact hashes below, for the stated fixed-schema
classification. This is not a review of arbitrary Collatz cycle coverage.

## Frozen bytes

- `block_schema_certify.py` — SHA256 `f896e6a9e69e9e08edf97ee5bfe1ce04486050c16241ba8fe1f031f720aa010f`
- `block_schema_verify.py` — SHA256 `963e76fedde87eb0ffd69efbb9dfee51594ce750caf25efcb4f7425e4a76a73f`
- `block_schema_certificates.json` — SHA256 `cb7122b2e0f4bd75ef9aa7501de6272564e879d017492cbb4a5e41dd6b05c8f7`

## Mathematical and implementation scope

I independently inspected the generator and verifier rather than importing
one into the other. The generator composes rational affine maps; the checker
reconstructs integer coefficient/carry/denominator triples. Both represent
chronological shortcut parity words, with nonempty fixed binary blocks and
nonnegative affine repetition exponents. Blocks with zero odd steps, constant
blocks, a completely empty word at isolated parameters, constant schemas,
expanding schemas, and genuinely contracting schemas have explicit branches.

The contracting certificate checks every suffix growth factor is at most one,
reconstructs the entire periodic numerator, checks its uniform rational bound,
and checks the positive denominator margin beyond the stated half-slope
cutoff. The candidate list contains every integer from one through floor(2B),
with no omitted endpoint. Each nonzero candidate power sum has coalesced
positive roots and a checked dominant-term inequality. The global cutoff
must dominate every candidate cutoff. Every earlier parameter is checked
with the complete cycle denominator, not a selected divisor.

Identity certificates are stronger than formal quotient identities: every
varying block must fix its actual integer entry state, every constant block
is replayed, parity and positivity are checked, and the endpoint must return
to the starting value. Both the rotated boundary and original boundary are
recorded and checked. The original-boundary index is correct: a rotation
starting at block j reaches the original boundary after r-j rotated blocks.
For one schema there is at most one infinite identity value; finite parameter
exceptions may have different cycles. Physical replay verifies the entire
finite word and records the first-return cycle.

The checker uses explicit rejection conditions, not Python assertions, and
does not import the generator. I found no blocking soundness or quantifier
issue. This review is mathematical and substantive code inspection, not an
exhaustive software security or fuzzing audit. It does not claim any polynomial
runtime bound or a finite menu covering all possible cycles.

## Execution actually performed by this reviewer

Command:

```
python -B /workspace/scratch/c6766c1207a3/collatz_work/stepback_root/block_schema_verify.py /workspace/scratch/c6766c1207a3/collatz_work/stepback_root/block_schema_certificates.json
```

Observed result: exit code zero, success true, all eight supplied schemas
accepted at the artifact hash above. The alphabet-four family had cutoff 24,
168 candidate integers, and no tail identity. The rotated identity control
had rotated value two, with its original boundary separately checked. The
other controls cover a trivial identity, an expanding family with a finite
cycle exception, a constant trivial cycle, no-odd-step contraction, a constant
empty word, and unequal growth with nonzero offsets.

The root researcher's separate eight malformed-certificate tests and
optimized-Python execution were reported to me; I did not rerun those tests
and do not claim them as my independent execution. The existing checks were
adequate for this review, so I did not start a redundant large test campaign.

## Relation to the sharper written proof

The published compiler implements the effective dominant-power-sum route.
The later written legality-cap argument is another proof of effective
classification; it is not the algorithm checked here. The concrete Lean
census-free contradiction is likewise separate: it combines n<170 with
2048 dividing n+41, hence n>=2007. The generic cutoff24, the earlier special
cutoff17 proof, and that uniform contradiction are distinct certificates.

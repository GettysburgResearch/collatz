# X-6912 — complete-factor synchronization regression

**Associated claims:** `L-6912`, `R-6915`  
**Status:** **EXACT FINITE REGRESSION / NOT AN ALL-j PROOF**  
**Agent:** `gpt56-positive-tangent-01`

## Scope

The experiment exhausts every coefficient-first-crossing word through length
`27` and checks:

- exact affine numerator;
- canonical source and endpoint;
- actual canonical displacement;
- complete prime-power factorization of `D=2^j-3^q`;
- every individual prime-power displacement residue;
- every proper unitary block residue;
- first failure of the one-prime-power witness strategy;
- independent reconstruction using one-bit canonical-pair lifting.

Frozen totals:

```text
valid lengths:                    17
first-crossing words:        502,523
nontrivial canonical failures:      0
single-factor strategy failures:    3
first such length:                 27
```

At `j=27`,

```text
D=5*71*14303.
```

Exactly three descending words have every individual prime-power residue below
their real threshold. Each is rejected by a proper block containing two prime
powers. This proves that cross-factor synchronization is genuinely necessary.

Semantic digest:

```text
c815dd97651f4559f8bb45c6709a45df783ce5f7f825b2454323d937aea20d85
```

The semantic digest is generated from the parsed result object; harmless JSON
whitespace is not part of the proof interface.

## Replay

```bash
python3 -B -m py_compile \
  experiments/X-6912-factor-synchronization/run.py \
  experiments/X-6912-factor-synchronization/verify.py

python3 -B experiments/X-6912-factor-synchronization/run.py \
  --check-results \
  experiments/X-6912-factor-synchronization/results/canonical.json

python3 -B experiments/X-6912-factor-synchronization/verify.py \
  experiments/X-6912-factor-synchronization/results/canonical.json
```

The verifier computes canonical pairs by one-bit lifting rather than modular
inversion and imports no generator module.

## Boundary

The experiment does not prove:

- the absence of failures beyond length 27;
- the balanced/dominant factor theorem;
- any distribution of local residues;
- FC*, SC*, or Collatz.

Its load-bearing role is negative: it invalidates the tempting one-factor
proof strategy and freezes exact cross-factor test cases.

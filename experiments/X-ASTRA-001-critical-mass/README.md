# X-ASTRA-001: critical mass, exact first-passage fibers, and Green enclosures

**FINITE CHECKS ONLY. No Collatz proof.** The proof packet is
[research/astra-critical-mass](../../research/astra-critical-mass/README.md).

## Reproduce

Requires Python 3.10 or later and only the standard library. From the repo root:

```bash
python experiments/X-ASTRA-001-critical-mass/run.py \
  --check experiments/X-ASTRA-001-critical-mass/results/canonical.json
python experiments/X-ASTRA-001-critical-mass/verify.py \
  experiments/X-ASTRA-001-critical-mass/results/canonical.json
```

To regenerate a separate artifact, use `run.py --write /tmp/astra-canonical.json`.
The committed report has no timestamps or platform-dependent floating values.
All arithmetic decisions use integers or Fraction. The SHA-256 semantic seal
uses sorted compact JSON excluding the seal field itself.

## Scope actually checked

The generator directly follows finite physical paths. The separate verifier
uses memoized proven first-hitting data and recursive geometric sums, and does
not import any generator function. It checks the same source domain, finite
clocks, endpoint shell, residue cases, and analytic-tail parameters.

- 96 positive ordinary all-odd paths, lengths 1 through 48, two choices of b.
- 24 exact odd-core mass identities on synthetic dyadically saturated sets,
  at exponents 1 and 2. These test the identity, not Collatz invariance of those sets.
- Two complete endpoint-AP/direct-map comparisons: (X,Y,L)=(256,16,8) and
  (512,32,10), with 99 and 233 defined sources, and 59 and 114 nonempty words.
- Six first-passage histogram pilots, X=2^k, k=8,10,12,14,16,18, with nine
  stage/tail-clock combinations each. Sources are Y<n<=X; endpoints lie in
  Y/2<y<=Y. All histogram hashes and 54 summary rows are independently replayed.
- 2,730 exact partial-drift cases on residue classes 0 and 2 through y=4096.
- Six explicit ordinary failure rays for W_(3/2), with 192 series terms,
  192-bit downward rounding, and an exact infinite-series remainder bound.
- Five all-source finite-time Green enclosures, with source enumeration through
  262144, 80-bit downward rounding, and the analytic tail from L-ASTRA-004.

## All-source does not mean all-time

For each K the exact finite-source sum is enclosed term by term. Every omitted
source n>X is covered by

    sum_{n>X} w0(n) <= (2 floor(log_3(X+2))+5)/(X+2),

multiplied by the full finite geometric time sum. Consequently the report
bounds the Green mass over **all n>=2**, not just the enumerated starts.
But K is only 16,32,64,128,256. The tail bound grows with K at a fixed X.
It cannot certify the uniform-in-K statement needed for a full proof.
One enumerated source is unresolved at time 256; no eventual outcome is
assumed for it.

## Results and integrity

Canonical semantic digest:

    28423e99643053ff26768b5a7859d0b66a960226856da7ae372df802b2bddd04

`run.py --check` and `verify.py` both passed locally. The verifier checks
canonical parameter coverage as well as recomputed values, so resealing a
weakened coverage manifest does not bypass those checks.

The scripts validate finite identities and the concrete certificates. The
symbolic tail proof, infinite-family failure, critical closure, and Green
criterion require mathematical review. The source-qualified Mazur theorem
and its large formal/computational payloads are not replayed by these scripts.
No GitHub Actions workflow or expensive proof search is included.

# X-ALF-002: actual-prefix rank and all-period switching checks

**Finite exact evidence, not a full Collatz proof.** See the [research packet](../../research/astra-linear-frontier/prefix-rank/README.md).
Python 3.10+ and the standard library suffice. From the repository root:

```bash
python -B experiments/X-ALF-002-prefix-rank/run.py \
  --check experiments/X-ALF-002-prefix-rank/results/canonical.json
python -B experiments/X-ALF-002-prefix-rank/verify.py \
  experiments/X-ALF-002-prefix-rank/results/canonical.json --self-test
python -O -B experiments/X-ALF-002-prefix-rank/verify.py \
  experiments/X-ALF-002-prefix-rank/results/canonical.json --self-test
```

Both programs accept `--output` for a separate compact artifact and
`--full-output` for all 64 family records. `--check` is nonmutating. The
compact artifact contains four representative family rows and authenticates
all 64 through the family and full-reconstruction digests. BOTH implementations
reconstruct the entire declared corpus before accepting the compact artifact;
omitted display rows are not omitted checks.

## Reconstruction differences

The generator minimizes along actual iterates with a proved early stop,
uses forward affine word composition, a word/displacement rank-ball enumerator,
and modular-inverse CRT. The verifier imports neither generator nor repository
code. It checks the entire baseline rank horizon, reconstructs raw affine
numerators independently, uses reverse rational word composition, enumerates
actual source residues, scans the complete source range n<=M for rank balls,
and uses extended Euclid. Its old moving-rank comparison scans all components
until a proved stopping bound, rather than using the four-candidate shortcut.

Both use exact integers/Fraction only. Checks raise exceptions and stay active
under optimized Python. A hash alone is not mathematical verification: the
programs reconstruct the specified values and coverage. Both have one author,
so agreement is implementation independence, NOT independent mathematical review.

## Complete declared finite corpus

- Eight primitive expanding words, including lengths 1,3,4,6,7,11,19,35.
- 64 ordinary family cases: two exact ternary depths, horizons 1 and 3,
  and both admissible short CRT units per word. All 1,440 recorded phases
  have the independently computed unique minimizing prefix length.
- Every prescribed w^N is replayed physically; this is finite ordinary
  replay, not an infinite-period conclusion. Source sizes reach 1,566 bits.
- 32 old quarter-unsafe edges are compared on the 111010 cases; the new
  rank starts below 4/27 of the old rank on all of them.
- All 8,191 sources from 2 through 8,192: 4,675 sufficient rotation guards,
  5,612 actual one-step rank drops, and exact first unsafe/core exits.
  The other sources are not labelled nonconvergent. The safe exit scan is
  not a complete Collatz computation; only 13 runs reach 1 before stopping.
- 8,190 parity words through depth 12 and nine COMPLETE rank balls through
  rank 65,536. The last ball has 587 sources, maximum source 59,049.
- Nine exact infinite rank-tail bounds with finite sums rounded outward
  on a 2^-80 grid. The tail theorem is the written APR-003 proof, not a
  claim that the source scan alone encloses infinity.
- Eight power-of-three spikes through H=64 and six inverse even-ray entries
  at each. The all-H/all-prefix conclusion is the proof, not these samples.
- The finite boundary failure at 1932103 and the explicit omission of zero
  displacements (the positive two-cycle does not acquire rank zero at 2).

Twelve genuinely distinct corruptions are RESEALED and must still fail:
false solved status, changed zero convention, reduced core coverage, wrong
family construction/index/phase count, erased infinite tail, altered rank-ball
hash/count, changed spike, erased boundary failure, and weakened phase depth.

## Evidence identity and limits

Compact semantic SHA-256:

    99850a23dea01004c24ed360d9cf3b051a779f06ad06dbc93538f756e207c4ee

Full reconstruction SHA-256:

    28960ad9bf694a3dd9ad1f54eaa538f9b2aba5aa9b971855cfaf83833fd2a1cd

No external formalization, predecessor payload, earlier heavy corpus or whole
repository validator is replayed here. The [execution receipt](../../reports/astra-linear-frontier-02/validation.json)
records actual normal and optimized runs, including site-package isolation
with `-S`, not a claimed complete-checkout execution.

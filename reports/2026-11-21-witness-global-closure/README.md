# Direct reverse-tripling review and execution record

This record supports
[`research/witness-global-closure-20261121`](../../research/witness-global-closure-20261121/README.md).
The full theorem remains OPEN. The scientific notes contain the proofs;
this directory records internal review, exact file identities and actual
finite executions. It does not promote the packet to an accepted baseline.

## Frozen work and source identities

The work starts from PR164's published head
`6fa6b429870a9cd53cde0fc77ad64a3c3956199f`, tree
`e9c8a0f1142cbbec53b09bad568cac0fb714ab48`, in a complete git worktree.
The branch continues
[`research/witness-closure-512-2026-11-20`](https://github.com/GettysburgResearch/collatz/pull/164).
No source history was rewritten, and no main-branch change is part of
this checkpoint.

[artifact-manifest.json](artifact-manifest.json) records the SHA-256 of
every file in the scientific packet. [replay-results.json](replay-results.json)
records the actual ten replay commands, exit codes, output JSON,
timestamps and equality between normal and optimized execution. The
replays are run with bytecode generation disabled and do not mutate
their scientific inputs.

The earlier published head `6fa6b429...` was also validated in a clean
complete checkout during this pass with

```sh
python -X utf8 -B tools/validate.py --regressions --receipt <outside-checkout-path>
```

All 11 repository commands passed there, with clean status before and
after. This statement concerns that exact earlier head, not the later
scientific modifications. The new published-head gate is reported in
PR164 after its actual execution; no anticipated result is represented
as an executed check here.

## Internal mathematical reconstruction reviews

These were independent reasoning and arithmetic reconstructions by
parallel AI agents and the primary agent. They are not external peer
review or proof-assistant verification. Where an author and reviewer
coordinated on a derivation, that is disclosed below.

### RGA-001–003 and PRN-001

The algebra agent copied the 71 PR146 certificate rows as data and wrote
an independent standard-library checker; it imported no source checker.
The root inspected that implementation and the written induction.
The symbolic-induction agent independently checked the monotone
fractional-linear maximum, the use of the query antecedent `3v`, and
both least-failure induction bounds. Verdict: **VERIFIED for the
frozen reduction and the stated direct-R height consequence**.

The positive-renewal norm theorem was independently reconstructed by
the symbolic-induction agent, including the density-zero extension and
the general `beta/delta` factor. That agent contributed the strengthening;
this was collaborative development followed by reconstruction, not
wholly separate discovery. Both reviewers required the explicit
nonempty-row hypothesis. The actual algorithm's zero rows are not
claimed to have density zero. Verdict: **VERIFIED for PRN-001's exact
operator hypotheses**.

### DRW-001–006

The symbolic-induction agent authored the direct witness note and
checker. The root independently checked all six affine identities,
positive odd legality, nonempty tails, the rank-one congruence,
the reconstruction statistics and both high-exponent thresholds.
The algebra reviewer additionally checked the normal forms while
reviewing LRF. Verdict: **VERIFIED for the specified transformations
and least-failure consequences**. There is no exhaustive word-language
coverage claim.

### LRF-001–004

The root authored the least-failure note and checker. The algebra agent
independently derived the three complete rank-two congruence progressions,
every target prefix and pure-power endpoint, the exact rational height
margins, and their propagation to all larger progression indices.
The symbolic-induction agent separately confirmed those rank-two formulas.

The algebra reviewer also independently replayed both stored finite
witnesses and their full defining integer equations. They are first-hit
certificates: `3^8` has 24 odd steps and total exponent 51; `3^25` has
137 odd steps and total exponent 257. Verdict: **VERIFIED for LRF-001–004**.

The reviewed manuscript before two editorial fixes had SHA-256
`ba39d725e73eef0e866b64eddd96e7f0bdc58af1f6b1590ea84847e96862ebf1`.
The root then changed its introductory equivalence reference from
RGA-001 to RGA-002 and specified that the 71 rows directly cover odd
ternary units. Even units were already handled separately by halving.
No formula or proof inference changed. The manifest records the final
manuscript identity. The reviewed checker and data identities are
respectively
`6d259b768e2011db733d8b0ff0688b3764e15a8f4c9272da9f4bcdd8c89b0f50`
and `03d85849b0e24da993459d9c16e79f11345644338d8117b2a354ceed9ab14d3b`.

### RB-001–004

The trajectory agent authored the finite bypass search, certificate,
transformer and unbounded ladder. The root checked the direction and
order of every kind of operation, empty/padded witness handling, the
unbounded ladder algebra and its exact statistics. The symbolic agent
independently reconstructed the ladder.

The algebra reviewer separately read the JSON and rebuilt all 27 paths
without importing the author's checker. It confirmed all 523 affine
forms, 29 strictly smaller calls, ten ordinary-only cells, 17 conditional
cells, and all first-letter coverage fractions. Pairwise CRT disjointness
and exact mass one verify the partition into 27 certified and 341
unresolved cells. No finite base parameter is omitted in this artifact.

Verdict: **VERIFIED for RB-001–004 and the exact partial partition**.
The three reviewed SHA-256 identities are:

| File | SHA-256 |
|---|---|
| `R_BYPASS.md` | `1cb308ac3b5f2b0d7a409f11cdb32cc27b6383b09a4374a8b21145b2c025af66` |
| `check_r_bypass.py` | `ae661b3a3fedec33d7a331e237d42e84e2463b14f696b89847614db915c9973c` |
| `r-bypass-certificate.json` | `2daaf8c83b81daf5cb64630287da2a8e749c99b6a917723518198e3d7721113f` |

The normal and optimized author executions agree: 108 finite-artifact
reconstructions, including 54 padded-source cases; 34 missing-child
returns marked `UNRESOLVED`; 15 rejected invalid controls; and four
additional padded ladder reconstructions. The root reran those commands
and independently recomputed the first-letter fractions.

### SZD-001–004: the further source-zero descent

After publication of the first continuation at
`5a7c86c94a9e2a7a064c0c84faa697d00d1c4d1b`, the root proposed a source-zero
matching construction allowing the child source witness to grow while
its ordinary parameter decreases. The symbolic agent found and proved
the contraction `p=(2048m-277)/2187` on an initial progression. The
algebra reviewer independently reconstructed all four ordinary paths,
then doubled the binary domain by retaining possibly even partial
endpoints and absorbing their exact remaining halvings. This strengthening
was collaborative development, followed by independent reconstruction.

The final cell is `m=69984u+50063`, `p=65536u+46881`, `u>=0`. The root,
symbolic agent and algebra reviewer checked the exact source and target
identities, strict decrease `m-p=4448u+3182`, the variable final valuations,
both directions of complete-witness splicing and the differences of seven
odd steps and eleven exponent units. Empty inherited tails and arbitrary
terminal padding are allowed. The full source-to-child transfer retains
every letter of the supplied tail.

The root and algebra reviewer independently checked both complete
rank-two exponent progressions, using the exact order of 2 modulo
`3^12`: `a=5, b=246004 mod354294`, and
`a=6, b=295526 mod354294`. These are restricted subfamilies, not complete
coverage of either first-letter case.

Verdict: **VERIFIED for SZD-001–004 on the stated ordinary progression**.
The exact reviewed identities are:

| File | SHA-256 |
|---|---|
| `SOURCE_ZERO_DESCENT.md` | `34dd2294996192279f894fa35d29610773e31a762c272d7da689f88af7d3813c` |
| `check_source_zero_descent.py` | `9aaa78707aa44ab5caad92b1a52155374b0fda14f26ca208eb999945026dbc3b` |

The root read both full files and executed the checker normally and with
`-O`; both returned identical PASS JSON. The checks include four universal
prefix schemas, 24 partial affine divisions, four exact final valuation
normalizations, 16 source and 16 target tuple reconstructions, two
constructed empty-tail fixtures and ten rejection controls. Two additional
source-only fixtures inherit witnesses at last exponents 246004 and
295526 directly from their supplied two-letter words. Neither huge target
orbit was attempted or certified by that test.

The child progression is outside the previously retained 27-cell bypass
atlas, as an independent CRT compatibility check confirms. The new rule
is therefore kept as a conditional descent. It does not assert that a
known dispatcher already solves every child.

## Bounded attempts on the remaining rank-two families

The trajectory agent separately searched for whole-family affine paths
for the following two residuals. These exploratory searches were not
used to infer a universal negative result.

| Source first exponent | Residual variable | Known convergent endpoint | Strict guard on a conditional source `y -> 3y` |
|---|---|---|---|
| 5 | `n=2^(89+162j)-1` | `(n-1)/6` | `9 divides y`, `0<y<(16n-19)/27` |
| 6 | `n=2^(38+162j)-1` | `n/3` | `9 divides y`, `0<y<(64n-3)/27` |

For each, the universal affine domain was
`n=(2^p0-1)+243*2^p0*u`, `u>=0`, with `p0=89` or `38`. This includes
the full exponential family because 2 has order 162 modulo 243.
All intermediate guards were required on the whole cylinder.

Each exploratory run allowed at most 30,000 heap removals per side,
inverse exponents 1 through 8, affine slope at most 10,000, and absolute
affine intercept at most 10,000. The first retained 1,376 target-side
and 35,601 known-source-side states; the second retained 1,225 and
35,058 respectively. Both returned **UNRESOLVED**.

These are author-reported bounded exploratory outcomes, not default
replay claims or nonexistence proofs. The scripts and data retained in
the scientific packet support every positive claim made there. No
stronger conclusion is drawn from these unsuccessful explorations.

## Latest-source review limits

The exact source heads and claim boundaries are in
[LATEST_SOURCE_REVIEW.md](../../research/witness-global-closure-20261121/LATEST_SOURCE_REVIEW.md).
The independent PR169 audit reconstructed its paired contractions,
correction algebra and endpoint telescoping proof. Its 184-leaf renewal
coefficient certificate and earlier PR153 occupancy dependency were not
independently replayed here. PR168's external regularity and arithmetic
inputs were not imported. No blanket acceptance of those branches is
asserted.

The missing full-theorem step is a successful all-source witness
transfer or another complete argument discharging its unbounded
remaining domain. Current checks verify the scoped identities and
implementations, not that missing theorem.

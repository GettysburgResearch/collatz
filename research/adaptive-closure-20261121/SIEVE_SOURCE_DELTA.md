# Scoped source comparison for the extended least-failure tests

**Source-qualified comparison, frozen for integration.** The mathematical
notes remain proposed research deductions; neither their bounded checks
nor this source comparison proves full Collatz.

## Frozen comparison heads

| Source | Full head | Relevant comparison |
| --- | --- | --- |
| PR146, initial input | `fd991063721e9c157d318e40bb20131762f7d750` | Least-failure sieve, critical interval count, orbit Mellin bound. |
| PR146, refresh | `66970775e4bdc945a68308e37a8eb028ebde42d2` | The three mathematical dependencies below are unchanged. |
| PR167 | `e83cc8b35ad614c616df7c00318cc9645a174c34` | Core-excursion frequency, expanded five renewal, sieve row/column interface. |
| PR169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | Primitive arithmetic moments, quantile criteria, fifth-denominator summability. |

The repository diff between the two PR146 heads is empty for exactly
these paths:

- `research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`;
- `research/upper-bit-mergers/CRITICAL_INTERVALS.md`;
- `research/astra-three-routes/pass2/ORBIT_MELLIN.md`.

Thus refreshing PR146 does not change the source-qualified inputs of
the three notes in this packet. This assertion does not say the whole
PR146 tree is unchanged.

## Mathematical delta and review boundary

| Local note | Exact addition | Already established input | Remaining unsupported step |
| --- | --- | --- | --- |
| `LINEAR_HORIZON_SIEVE.md`, LHS1--LHS2 | At the first coefficient crossing, the affine remainder is less than one third of the preceding odd count. This yields the `B=17`, `floor(k/1024)` sufficient test and the same `5X/8` dependency margin. | PR146's directed descent, least-failure height, and old retained-set count. | A sharper ordinary-source count for the longer retained parity words, or a universal successful crossing. |
| `SIMPLE_PREFIX_PRODUCT_SIEVE.md`, SPS1--SPS3 | The explicit `4 Z^(39/40)` count and `160 F^(-1/40)` reciprocal budget extend to finite simple odd prefixes without enlarging the constants. The product bound gives a sufficient coefficient test at any clock before input repetition, once `F>=80^40`. | The two-lane proof and infinite distinct-orbit product bound in `ORBIT_MELLIN.md`; PR146's directed reduction. | Sources with no low coefficient excursion and possible nontrivial cycles. |
| `CRITICAL_NEGATIVE_MOMENT_INTERFACE.md`, CNM1--CNM3 | A nonperiodic orbit forces the full series `sum Q_q^(-rho/2)` to converge, and yields the critical quantile count with a `log(Y)^(-3/2)` saving. | PR146 critical reciprocal-power summability and PR169's fixed-source pointwise moment bound. | Prove divergence or excess quantiles for the actual arithmetic sequence; cycles still need separate exclusion. |

The finite-prefix modification is specific. In the source's two-lane
argument, remove the final `q=floor((3/5)log2 Z)` odd positions so
that `U^q` remains injective inside the segment. The removed `q`
positions fit the unused half-unit of the source constant. A cycle
may follow the segment; repeated laps are never included in that
simple-prefix reciprocal budget. The parent independently checked
the SPS1--SPS3 algebra and reported no gap at the frozen note.

PR167's `CLOSING_ENERGY_INTERFACES.md`, CI4, already constructs a
positive row reduction for the old discarded-index sieve and isolates
its incoming-column and energy-propagation obligations. The present
notes do not claim that row reduction as new or settle those incoming
weights. The linear test still only inherits the old upper counting
bound. The old matching lower bound cannot be transferred to it.

PR167's shifted-core frequency and fixed-defect theorems constrain one
ordinary orbit's arithmetic returns. They do not supply an upper
distribution estimate for the parity words or moment representatives
needed here. No new coefficient-floor test matching LHS1--SPS3 was
found in the inspected PR167 manuscripts. The PR169 moment source uses
the earlier power bound at `alpha>rho`; the critical series deduction
explicitly uses the additional logarithmic saving of PR146.

The first-valuation-one five block investigated concurrently by the
witness agent is already in PR167 and the other refreshed five-word
sources. Its separate review therefore credits it as a rederivation,
not a new family. That overlap does not affect the three sieve/moment
notes above.

## Exact execution scope

Both local programs were actually executed in normal Python and with
`-OO`; each pair of reports is byte-identical.

- The linear-horizon checker verifies actual first-crossing identities,
  tests 196,608 eligible indices through `k=262144`, and records 125,685
  additional exclusions beyond the old test. It rejects five malformed
  controls. Its fixed-source census is not an asymptotic estimate.
- The simple-prefix checker verifies 129 finite odd segments at 2,459
  attained thresholds, rejects five controls, and replays four large
  actual sources. The three fixed Mersenne examples have exponents
  281, 443 and 605; they do not establish the infinite progression.
- The critical-moment note is a deduction from pinned written theorems,
  not a numerical claim. No new moment census is used to support its
  open divergence criterion.

The 71-path directed cover is imported from the pinned source and is
not rechecked by either local program. Repository integrity validation
and publication remain the integrator's separate tasks.

# Execution and review record: ordinary pointwise closure attempts

**Outcome: scoped progress, not a resolution of Collatz.** The mathematical
entrypoint is the [research packet](../../research/pointwise-closure-20261120/README.md).
This report records source identity, separate proof reconstructions, actual
finite executions, repairs, and the remaining inference. It is not a second
scientific baseline or a claim of external acceptance.

The investigation used three parallel research routes and cross-route
reviewers. The integrating agent additionally reconstructed the arguments,
checked the primary S-unit statements, ran the final finite checkers, and
reviewed the claim boundaries. All reviewers here are separate AI agents;
no human referee or proof assistant is represented as having accepted the
results.

## What the written arguments establish

| Packet | Narrow result | Global obligation still open |
|---|---|---|
| Sparse spectra, SR-1–SR-4 | A fixed popcount cap gives a finite homogeneous return spectrum and `O_S(N^(1-1/S))` occupancy on distinct odd segments. General finiteness uses a published S-unit theorem; caps two and three have elementary constants. | A trajectory is not forced to make sufficiently many sparse visits; replacing a collapsed carry cut has no global budget. |
| Growing complexity, equation (1) and Section 2 | All but `O_c(N 2^(-delta_c sqrt(log_2 N)))` states exceed `c sqrt(log_2 N)` set bits, for every `c<1/sqrt(2)`. The proof is elementary. | This gives no upper cap on complexity and excludes neither arbitrary escaping paths nor all primitive cycles. |
| Local certificates, LC-1–LC-3 | Exact necessary and sufficient adjusted-grade conditions for a binary-class affine merger certificate through an ordinary parameter whose positive arms converge. | Infinite convergent families lie outside these certificates. No additional rule covers the full ordinary residual set. |
| Stopping burden, SB1–SB5 and LD1–LD2 | `W(1)` is the first-hit score supremum, and its finiteness is equivalent to a logarithmic odd-event bound with bounded additive error on the convergent unit basin. | The bounded supremum and any exclusion of other components remain unproved. |

The improvements are measured against the exact frozen repository sources,
not against an exhaustive external priority search. In particular, the
growing-popcount coefficient improves the earlier theorem's **popcount
consequence**, not its structural assertion about runs of ones. The
general S-unit mechanism and the simple-path packing mechanism are credited
as antecedents.

## Separate written reconstructions

| Review | Final scope | Qualification |
|---|---|---|
| [Sparse spectrum review](REVIEW_SPARSE.md) | SR-1–SR-4, with a separate SR-1Q quantitative delta. | Published S-unit inputs were checked in primary sources, imported rather than re-proved. The original and final reviewed hashes are both retained. |
| [Growing complexity review](GROWING_COMPLEXITY_REVIEW.md) | Exact finite inequality, entropy calculation, floors, distinctness, and comparison with frozen PR #145. | Independent proof reconstruction; the reviewer execution is a replay of the author's checker. |
| [Local certificate review](REVIEW_LOCAL_CERTIFICATES.md) | LC-1–LC-3, including nonterminal common endpoints, cycle padding, and zero-depth cases. | Positive integer slopes clarified; checker-domain issue repaired and separately rechecked. |
| [Stopping burden review](REVIEW_STOPPING.md) | SB1–SB5 and the final self-contained LD1–LD2. | Integer deadline domains clarified; no finite-sample maximum is promoted to a bound on `W(1)`. |

Review documents refer to their original `agent-alternative`,
`agent-pressure`, or `agent-merger` staging paths. Each reviewed mathematical
basename is now in `research/pointwise-closure-20261120/`; each review and
its independent evidence is in this report directory. The reviewed files
were copied without changing their bytes. The [artifact manifest](artifact-manifest.json)
records the final relative paths, byte lengths and SHA-256 hashes, allowing
the review pins to be checked after relocation. It is an identity record,
not a mathematical certificate.

The [older packing reconstruction](REVIEW_PACKING.md) and its
[scalar report](packing-review-report.json) concern the stronger reciprocal
budget from frozen PR #140. They are historical comparison material;
SB5 uses the locally proved bound of 600 instead.

## Actual finite executions of the final files

All four author checkers were executed in the integrated checkout with
Python 3.12.14, in normal mode and with `-OO`. Every command exited zero;
each pair produced byte-identical output. The execution JSON files record
the interpreter, exact command, source hash, stdout hash, stderr, and
measured duration. These are finite arithmetic checks, not enumerations of
all positive integers or executions of the imported S-unit theorem.

| Checker and exact report | Bounded coverage observed |
|---|---|
| [Sparse returns](sparse-returns-report.json), [execution](sparse-returns-execution.json) | 401,401 homogeneous pairs; 4,101 original-source cuts; 57,261 exact state identities, including 20,000-bit sources; 757,454 occupancy inequalities on 22,218 distinct windows. Two invalid strengthenings rejected. |
| [Growing complexity](growing-complexity-report.json), [execution](growing-complexity-execution.json) | 65,532 residue-coset states; 294 cap comparisons; 504 separated actual windows and 10,584 state identities; 207,711 finite inequalities on 4,239 distinct windows. |
| [Local certificates](local-certificate-grade-report.json), [execution](local-certificate-grade-execution.json) | 4,096 triple-ray parameters, with 1,034 certificates; 512 affine lists, with 35 certificates; 447,436 literal lifted-path edges. Six corrupted certificates rejected. The census supplies no asymptotic residual density. |
| [Stopping burden](stopping-burden-report.json), [execution](stopping-burden-execution.json) | 10,000 unit sources with independently implemented clock and distortion checks; 257 rational products; 7,392 inverse words of bounded depth/gap; 201 conditional deadlines. The sample maximum score of zero is not a bound on `W(1)`. |

Two separately written reviewer scripts accompany their evidence:

- [review_sparse_arithmetic.py](review_sparse_arithmetic.py) and
  [its report](sparse-review-report.json): 16,200 homogeneous pairs,
  2,240 cuts, 64,387 cut identities, 20,120 greedy decompositions and
  3,229 reserved windows. The integrating agent replayed this script
  and compared the complete JSON to the reviewer's saved report.
- [review_local_arithmetic.py](review_local_arithmetic.py) and
  [its report](local-review-report.json): 10,548 cocycle prefixes,
  384 affine arms, 22,026 lifted edges, 64 zero-depth cases and
  64 nonterminal endpoint cylinders. The final verifier's narrow
  [domain review](local-domain-review-report.json) is recorded separately.

The [independent replay receipt](independent-replay-execution.json) also
records the root's exact evaluation of all three numerical inequalities
in LD1–LD2. The [local distortion report](local-distortion-report.json)
is the author's scalar evidence. The all-path content is supplied by the
written packing argument, not those three scalar comparisons.

The growing-complexity reviewer's [saved replay output](growing_complexity_review_replay.json)
is a separate invocation of the author implementation. The stopping
reviewer's smaller `--limit 10001` execution is described precisely in its
review. Neither is relabeled as an independently written checker.

### Reproduce the bounded checks

From the repository root, using Python 3.11 or later:

```bash
python -X utf8 -B research/pointwise-closure-20261120/check_sparse_returns.py
python -X utf8 -B research/pointwise-closure-20261120/check_growing_complexity.py
python -X utf8 -B research/pointwise-closure-20261120/check_local_certificate_grade.py
python -X utf8 -B research/pointwise-closure-20261120/check_stopping_burden.py
python -X utf8 -B reports/2026-11-20-pointwise-closure/review_sparse_arithmetic.py
python -X utf8 -B reports/2026-11-20-pointwise-closure/review_local_arithmetic.py
```

The author checkers use explicit checks rather than removable assertions.
For each author checker, inserting `-OO` before `-B` reproduces the second
recorded interpreter mode. These commands print reports and do not need
third-party packages.

## Preserved repairs and unsuccessful strengthenings

The original-source cut must remain guarded. The examples `5 -> 1` and
`257 -> 193 -> 145 -> 109 -> 41` refute two overextensions; both are retained
as executed controls. A primitive cycle may be counted once, but its laps
cannot be repeated to manufacture an arbitrarily long distinct segment.

The local certificate verifier initially admitted an empty arm list and
zero-slope constant arms, outside the theorem's domain. The final version
requires nonempty arms and positive integer slopes/residuals, and validates
the relevant integer fields. The mathematical constructor and successful
census were unchanged. The original issue and final-byte delta remain
visible in the independent review.

The [finite-three-defect exploration](FINITE_THREE_DEFECT_BLOCKER.md)
records an unsuccessful attempt to remove the source proof's five-ray
counting hypothesis. Its needed identity `F(5x)=F(x)` was not established.
This is an open attempted strengthening, not a theorem that the route is
impossible.

## Complete-checkout gate

**PASS: all 11 commands exited zero** in a clean, complete checkout of
published content commit `05908b1d897370d6a48845e77985cf44428424a3`.
The [saved receipt](validation-receipt.json) records the actual command:

```bash
python -X utf8 -B tools/validate.py --regressions --receipt ../pointwise-closure-published-validation.json
```

It covers tree `5284a74478e411f4f70e1b97feb5ed08f098286b`, with 350 tracked
files. The checkout identity was unchanged after execution. The receipt
was attached in a subsequent documentation commit; it does not claim to
cover its own later attachment. The scientific files and bounded replay
scripts are the same reviewed bytes identified in the artifact manifest.

This gate checks repository integrity and the selected bounded regression
bundle. It does not validate the new mathematical proofs, execute an
external Lean build, or prove Collatz. The new research checkers are
separate actual executions recorded above.

## Handoff boundary

No route supplied the missing pointwise implication, and the three
reductions do not supply it in combination. The next substantive target
is a paid rule for carry-cut replacement or a forced sparse-return lower
bound; an ordinary rule covering the local certificate residual set; or
an actual proof of the uniform inverse score bound and the remaining
component exclusion. Finite replay, density, and convergence of the
sampled starts do not fill those gaps.

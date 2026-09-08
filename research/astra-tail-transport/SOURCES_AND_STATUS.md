# Frozen sources, status and dependence

Author: `astra-tail-transport-01`. Date: **2026-09-07**.
Research started at **2026-09-07T00:17:48Z / 03:17:48 Asia/Jerusalem**.
The first live main read resolved
`69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a`.
All source reads for this packet are pinned to that SHA. A final remote read is
recorded in the publication handoff. A later head receives no implied review.

This is an original research attempt following Reviewer D, not a third D review
pass. The reviewer reports and all canonical status records are left untouched.
All ATT results are **PROPOSED pending independent mathematical review**.

## Exact repository dependencies

Paths below are in GettysburgResearch/collatz at the frozen base.

| Path | Git blob | Role |
|---|---|---|
| `research/astra-three-routes/pass4/MOVING_GHOST_RANK.md` | `a3557d28e1369507e5c503020fd383cb8f08f5b1` | T-A3-901/902: moving rank, four-entry collapse, properness and total maximal acceleration. Reconstructed in this packet; not claimed new. |
| `research/astra-three-routes/pass5/RANK_MOMENTS.md` | `d703ba2ff3a9207665fb80263499c7a3a5635f51` | Rank spectrum, reciprocal sum, quarter-safe induced map, prior finite-moment explosion. ATT-004/005 refine the output-domain question rather than erase the old obstruction. |
| `research/astra-three-routes/pass2/ORBIT_MELLIN.md` | `16c943601ce791afb1bbd5f02f3a9ea88ef38520` | Optional SC* interface ONLY: non-eventually-periodic ordinary orbits have coefficient escape; together with the source-tail minimum this supplies an actual SC tail. Not needed for ATT-001..006 or their Collatz iff criterion. |
| `research/integrated/ERRATA.md` | `e9b3e919a894170c88149e173fc20b846e6dba8f` | Current corrections and ordinary/nonordinary, infinite-distinct/cycle and status conventions. No correction is promoted by this packet. |

Full pinned source root:
`https://github.com/GettysburgResearch/collatz/tree/69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a`.

Read current README, AGENTS, research map and research index before the attempt.
The current index distinguishes accepted baseline from active proposals.
No statement here inherits a verdict merely because its definitions were
reviewed previously.

## Claim matrix

| ID | Status of exact written argument | Evidence / uncertainty |
|---|---|---|
| ATT-001 | PROPOSED | Positive decomposition covers every moving-index component. Sharp lower bound uses actual powers of three. Written proof, exact finite regressions; constants deliberately loose. |
| ATT-002 | PROPOSED | Actual parity remainders at each fixed clock; no orbit injectivity assumption. Both fixed-clock tail exponent and clock-growth rate are proved in the manuscript. Uniform-in-time tightness remains unknown. |
| ATT-003 | PROPOSED | All active modes and maximal counts; exact logarithm bracket `3^17<2^27`. No optimality claim for exponent 9/4. |
| ATT-004 | PROPOSED | One unsafe return, pointwise initial envelope, finite total source measure, all safe excursions. Output bound does not restore the envelope for reuse. |
| ATT-005 | PROPOSED | Explicit all-parameter integer family, actual words, exact valuations and both unsafe guards; four finite substitutions. No convergence conclusion for the family. |
| ATT-006 | PROPOSED | Elementary proper-height classification and dominated convergence. It is a diagnostic equivalence, not a proof of either vanishing condition. |
| Uniform weak-first-moment bound at all shortcut clocks | REFUTED by the proposed ATT-002 proof | Norm grows at least `(9/4)^k/5184` for k>=6. This does not refute uniform tightness. |
| Weak-first output for the unsafe induced clock | REFUTED by the proposed ATT-005 proof | The same input has infinite weak first rank moment after one B return. |
| Fixed quadratic rank ceiling under A | REFUTED by the proposed ATT-005 proof | Rank ratio grows without bound on explicit ordinary integers. |
| Uniform fractional moment after arbitrarily many unsafe returns | OPEN | Only the first-return 1/3-moment bound 602 is proved. No recursion preserving its input hypothesis. |
| Vanishing finite-ball occupation / exclusion of all nontrivial cycles | OPEN | An independent part of the closing criterion, not supplied by tightness alone. |
| Complete Collatz proof | NOT OBTAINED | First unsupported step: uniform control on the actual repeatedly transported distribution; cycle exclusion also missing. |

"Refuted" in this table identifies a proposed proved counterexample to an
intermediate assertion, not an accepted new canonical status. The original
false idea and the surviving theorem are separate objects.

## External comparison and novelty boundary

The abstract/version record of Idris Assani, Ethan Ebbighausen and Anand Hande,
*Syracuse Maps as Non-singular Power-Bounded Transformations and Their Inverse
Maps*, arXiv:2208.11801, was consulted as conceptual context:
`https://arxiv.org/abs/2208.11801` (accessed 2026-09-07).
It relates finite-measure power-boundedness to eventual cycles. This packet's
fixed-input tightness/occupation decomposition is proved here without invoking
its theorem. Only the abstract-level comparison is asserted; no full external
proof review, version-specific theorem import, or formal build was performed.

Tao's almost-all descent/first-passage transport work, arXiv:1909.03562, is a
contextual warning against replacing a fixed floor by a moving threshold. It
is not a dependency of the new results. No general external novelty or priority
claim is made for elementary tail estimates, deterministic measure
classification, or the chosen weak-moment language.

## Non-equivalences that must remain explicit

- R_* is not P=(2n+1)^2/3^v3(2n+1); no cross-rank substitution occurs.
- A maximal `1^a0` module is not a shortcut step or a whole odd/even run.
- B is quarter-unsafe return, not the spectrum-switch nonincreasing-safe return.
- Moment means rank of endpoint integrated against actual mass, not a norm of
  a density on counting measure.
- An infinite first moment does not mean infinite unweighted mass or a divergent
  source; both raw and induced maps preserve or decrease unweighted mass.
- Large critical norm does not force escaping probability mass. The sharp
  witnesses live at extremely large heights with extremely small weights.
- Tail control at each finite clock is not uniform tail control over clocks.
- A total B computation terminates at 1 OR another unsafe state.
- The explicit family varies with its parameter. No all-time positive source
  is extracted from infinitely many finite constructions.
- Full-source finite-clock enclosures use an analytic omitted-source tail;
  they are not all-time estimates.

## Actual validation ceiling

Both new complete finite payloads were independently reconstructed, including
ordinary source tails, literal paths, maximal module boundaries, induced
returns, exact power-family inequalities and separate model controls. The
verifier uses a terminating infinite-component scan, not the generator's
four-entry rank formula; literal stepping, not its affine module formula;
endpoint aggregation, not its source-first raw-tail enumeration.

All code is standard-library Python and uses exact integer/Fraction decisions.
Both scripts have the same author. An independent mathematical reviewer should
first check ATT-001's infinite dictionary sum, ATT-002's nonzero remainder and
clock constants, ATT-003's k>=3 inequality, both unsafe guards in ATT-005, and
the order of limits in ATT-006. The scripts do not certify these universal
arguments by finite enumeration.

No broad Collatz census, old full scientific corpus replay, in-repository formal
proof build, external Lean certificate or payload replay was run. No full
checkout of main was available. The repository-wide `tools/validate.py` was
therefore NOT run on main; local package checks are not a substitute.

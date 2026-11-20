# Execution and publication record: global rigidity attempts

**Mathematical verdict: Collatz remains OPEN.** The scientific entry point is
the [research packet](../../research/global-rigidity-20261120/README.md).
This record concerns source identity, review scope, actual finite
execution, and publication. It is not an additional proof.

## Work and authorship

Three research agents pursued different global routes: ordinary
operators and all-source moments; arithmetic approximation with a fixed
ordinary source; and physical two-arm least-failure descent. The primary
agent reconstructed the arguments, supplied the disjoint convergent-basin
construction and signed-filter extension, and assembled the source audit
and publication. The routes then reviewed one another at exact file
hashes.

All new mathematical claims remain PROPOSED. A narrow review marked
VERIFIED means a separate AI agent reconstructed the specified argument
at the pinned bytes. It is not external peer acceptance, a formal proof,
or verification of a neighboring open hypothesis.

## Exact inputs and comparison correction

The base is main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, tree
`1c25c17df24491de6187445f1a1d355d5a7660c3`. Main was re-queried before
publication and remained at this commit.

The [source-boundary note](../../research/global-rigidity-20261120/SOURCE_BOUNDARIES.md)
pins PR143--PR150 as used. In particular:

- PR146 was read at `7d04c4dd756cfe495eb3eee78eba35a99085cd2a`; its
  newer finite-defect propagation result was treated as prior work.
- PR145 was read at `dd245a712f985909f541590e3f6c179b7ba011e4`.
  Its `MANTISSAS.md` already gives a logarithmic run threshold using
  a published logarithmic-form input. PR150's square-root-logarithm
  improvement is only relative to an elementary README consequence.
- The comparison sentence in PR150 was corrected through the connected
  GitHub account and read back exactly. Its source commit remains
  `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`; no history was rewritten.

The primary source inspections for the classical real-density theorem,
the indicated operator background, and the Subspace-Theorem normalization
are identified beside the relevant arguments. No broad literature-priority
claim or fresh external formal build is made.

## Finite replay actually performed by the primary agent

Run from `research/global-rigidity-20261120/` with Python 3.12.14.
Each listed program was run with both `python -X utf8 -B` and
`python -X utf8 -B -OO`; complete stdout was captured outside the checkout.
All exit codes were zero, and the paired outputs were compared byte for
byte with the checked-in reports.

| Program | Scope |
| --- | --- |
| `check_ordinary_spectrum.py` | Two 512-state certified convergent inverse trees, four full-operator residual bounds covering every unit complex phase, explicit root arithmetic, and preserved negative controls. |
| `check_adic_real_density.py` | Eight rational-cycle witnesses; 31,523 nonreturn ordinary-prefix identities, actual return controls, completion equations and specified product identities. |
| `check_finite_places.py` | Four additional finite-modulus witnesses and exact full-cycle replay. |
| `check_shifted_linearization.py` | 17,008 primitive shifted-product identities, including cancellation cases with ternary valuation exceeding the odd clock; formal tails remain explicitly labeled. |
| `check_q_section_guards.py` | 1,520 horizon cases through H=192; 296,400 literal edges; exact set-intersection exclusion of 19,319,960 possible cross-clock pairs; 696 immediate-halving cases; return and smaller-comparison certificates. |
| `check_ordinary_spectrum_independent.py` | Separate positive root/internal/external decomposition of the same finite supports, reusing only the pinned tree producer. It independently replays every edge and includes all external predecessor fibers. |
| `review_arithmetic_routes.py --source-root .` | Reviewer implementation importing no author arithmetic code: 12 reconstructed cycles, 10,582 shortcut edges, 4,684 nonreturn pins and 1,971 shifted-product controls. |
| `review_signed_clock_controls.py` | Independent controls for 18 admissible ordinary neighbor pairs, 279 edges, finite rational-prefix stability, and a signed filter whose one-step jump cancels while its two-step jump does not. |
| `check_q_independent_review.py` | Independent physical-iterate and affine-form implementation, importing no author transducer: 940 horizon cases, 93,060 literal edges, 35 return-word cases and 200 orientation controls. |

The checker reports give exact ranges and limits; a count of possible
cross-clock pairs is coverage of exact set intersection, not a claim of
a separate nested-loop execution for every pair. Normal/optimized
agreement checks that the active verification is not removed by Python's
optimization flag. It is not a proof of the infinite quantifiers.

All nine programs passed in both modes: 18 completed executions. The
[replay record](replay-results.json) identifies their commands, source
hashes, output hashes, and exact byte comparisons. The four scoped
written reviews are `REVIEW_ORDINARY_SPECTRUM.md`,
`REVIEW_ARITHMETIC_ROUTES.md`, `REVIEW_Q_SECTION_GUARDS.md`, and
`REVIEW_ROOT_ANNEXES.md` in the research packet.

The signed-filter classification is a written argument about all
absolutely summable coefficients. Its proof is independently reconstructed;
finite controls do not stand in for that quantifier.

## Reproduction

Each author checker can be run as `python -X utf8 -B PROGRAM.py` from the
packet directory. The independent arithmetic reviewer additionally
requires `--source-root .`. Add `-OO` to obtain the corresponding
optimized run. They use the Python standard library. The large spectral
support integers are regenerated from short root parameters and checked
against support digests.

The [artifact manifest](artifact-manifest.json) binds the scientific
packet, replay records, and active-research navigation to their bytes.
It excludes itself, this publication record, and the complete-checkout
receipt, so those process records can identify the published content
without pretending to hash themselves.

## Complete-checkout validation and publication

The content was published to `research/global-rigidity-20261120`, fetched
from GitHub, and checked in a separate clean complete worktree:

- Published content commit: `f13f91c6875f2b3e117b6e9c64c45039dd92bf5c`.
- Published content tree: `50e9b7d7ea72c61a0cd9281e9cb9c464d1d24a3b`.
- All 34 artifact-manifest entries matched the fetched published bytes.
- The checkout had 350 tracked files. Its commit, tree, and tracked state
  were unchanged after validation.
- All 11 child commands exited zero with regressions enabled.

The [complete receipt](validation-receipt.json) records the actual run
from `2026-11-20T19:38:33.458287+00:00` to
`2026-11-20T19:38:38.633413+00:00`. Its SHA256 is
`977237ee9beb25c630f225a2a4eee91f5994eb1aa7979181a0dc581fa28cdd07`.
This receipt is attached in the following documentation commit; it covers
the named content commit, not its own later attachment. A later final-head
execution must identify its own exact commit separately.

The required command is:

```bash
python -X utf8 -B tools/validate.py --regressions --receipt /absolute/path/outside/checkout.json
```

The command must run in a clean complete checkout and records the exact
commit and tree it actually checked. Its structural and bounded replay
checks are separate from the mathematical reviews and the new finite
checkers above. The final PR and receipt identify which published commit
each execution covers.

## Remaining work

No all-clock ordinary moment estimate, actual infinite-product smoothing,
unrestricted arithmetic power saving, or complete terminating merger
selector has been obtained. The signed-filter result rules out one
specified way to obtain smoothing; it does not show that the actual
infinite product is rough. The rational cycles are noninteger witnesses,
and the all-horizon merger family has a signed limiting code.

An additional positive-cycle exclusion is still required in any route
which establishes only eventual periodicity. None of these evidence
records should be interpreted as a full Collatz resolution.

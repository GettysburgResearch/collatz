# Investigation preview · validation and delivery receipt

Implementation session: **18 September 2026**. Version: **0.3.0-preview.1**. Historical [v0.1 receipt](VALIDATION-v0.1.md) is preserved separately; its earlier test counts are not this pass's result.

## Frozen source and scope

Live reads confirmed main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` and open, unmerged PR #119 at `f0bf47d9c4253c3a16617f4b70388a7a4ba4e1de`. The supplied v0.1 ZIP's `observatory/` directory was placed in a local snapshot repository; its Git subtree hash **exactly matched** the published v0.1 subtree:

```
0dea2738379fd0242fd68794a5204e1a2df45188
```

This was an application-subtree checkout, not the entire scientific repository. The local snapshot commit is not represented as the actual GitHub baseline commit. Existing `core.py` and the classic UI remain unchanged; the old browser test's normal URL is adjusted to `/classic`.

The delivered patch changes only `observatory/`. The accompanying delivery manifest records the resulting whole-subtree hash and patch checksum. A clean application of the patch to the original subtree was checked separately during packaging. No root workflow, repository setting, license, scientific claim status, or other contributor's branch is changed.

## Checks actually run

Environment: Linux; **Python 3.13.5**, **Node v22.16.0**, **Chromium 144.0.7559.96**. Python 3.10+ is the intended compatibility floor, not an executed multi-version matrix. The application has no third-party runtime dependencies; Playwright/Node are testing tools.

| Check | Observed result |
|---|---|
| `python -m unittest discover -s observatory/tests -p "test_*.py" -v` | **70 tests passed**. |
| Same suite under `python -O` | **70 tests passed**. |
| `node --test observatory/tests/*.test.mjs` | **25 tests passed**: original views, strict recipes/history/local storage, exact selections, portable size guards, trusted observable and actual module graph linking. |
| `node --check` on every browser `.mjs` file | Passed. |
| New workspace browser harness | **39 explicit checks passed**; no JavaScript page errors; desktop and 390px responsive layout. Narrow scope below. |
| Preserved classic browser harness | **23 explicit checks passed**; no JavaScript page errors. Same narrow scope. |
| Three new portable examples | Every included request replayed to its recorded result/kernel digest; all three also loaded/replayed through the actual workspace controller. |
| Independent meeting CLI | Bundled 27/19 witness verified: common 40, raw clocks 103/12, displayed clocks 63/null. Forged source/value/clock/relation fixtures are rejected. |
| Published HTTP client example | Executed against the running local server; returned the exact 40 meeting with both arrival records. |
| Bounded provider benchmarks | Six scenarios, three timed runs each plus separate traced-memory replay. [Recorded JSON](BENCHMARKS.json); scope below. |

Mathematical manifest digest at the checks:

```
671694c751bc7ce06da4f7e33d0b6adebd58217c0648045b664f236a28e15ccd
```

It covers `core.py`, `pairs.py`, `research.py`, `symbols.py`, `engine.py`, not server/UI code or a proof certificate. The engine captures loaded-source identity and rejects subsequent mismatched disk edits until restart. Full application identity is in the delivered subtree/patch manifest.

## Arithmetic and state coverage

The retained v0.1 fixtures include independent raw replay for sources 1–159, all 510 words of lengths 1–8, raw/shortcut/odd counts and peaks of 27, large integers, cancellation, inverse-edge legality and family censoring.

New checks cover all nine pairs of displayed map choices, hidden raw arrivals, exact common-state supports, raw-prefix/retained-digit limits, 1,000-digit inputs, and independent column sums/carries for small integers at multiple crop offsets. One fixture reconstructs an incoming carry after a large omitted low-bit region.

Motif tests independently reconstruct finite source intersections, distinguish positive/false/unknown targets, retain invalid partners and unfinished members, and exercise deterministic cancellation after completed members. The published 64-source trial has **28 supports, 24 counterexamples, 6 control passes, 6 control failures**. These are exact finite classifications, not independent samples or a global convergence claim.

Rank tests compare the collapsed evaluation with a larger finite direct dictionary for sources below 2,000. Module tests independently replay legal words and maximality for sources 2–799. Tests retain the increasing/equal rank controls and the `577363 -> 649534` rank-decreasing/numerically increasing fixture. Prefix affine identities are checked exactly. Transport fixtures independently advance the weighted source population, verify killing/unresolved accounting, forbid arbitrary module floors, and check interruption at complete frames.

Symbolic fixtures compare compositional summaries against literal expansion, replay a 4,096-branch repeated ghost, retain zero and full-denominator controls, and check the distinct `3n-1` and `5n+1` positive cycles. No finite fixture is represented as an all-word exclusion, a rank-selector completeness theorem, or new review of the inherited proof packets.

HTTP tests use actual loopback requests for old/new operations, assets, Host/Origin/token rejection, malformed types, path restrictions and bounded job/cache behavior. A controlled worker exercises retained partial study data with final cancelled status; the original suite also includes real HTTP cancellation of a bounded heavy workload. Cooperative cancellation is not process isolation or hard real-time enforcement.

## Browser scope: what passed and what did not

Normal navigation in the managed Chromium environment was blocked with `net::ERR_BLOCKED_BY_ADMINISTRATOR`, including localhost. **No browser policy or network restriction was changed.** Recorded UI tests used the scripts' explicit `--in-memory` mode: the actual local HTML/CSS/JS in an empty Chromium DOM, with fetch bridged only to the **real running loopback HTTP API**.

This exercised real controls and actual computation: bit perturbation, carries, mixed clocks, hidden meetings, witness export/replay, counterexample inspection, unfinished members, rank/modules, transported mass, block/cycle controls, huge inputs, full six-recipe replay, invalid-replay rollback, note safety, view restoration, undo/redo and responsive layout. Screenshots are of that running application DOM, not design mockups.

The narrower harness flattens imports. To avoid treating that as module-loading evidence, a separate Node test links the **actual new and classic ES-module graphs** without evaluating a DOM, checking real import/export compatibility. Real HTTP asset responses and module syntax are tested separately. These are still **not** a normal browser-navigation/module-transport receipt.

Not established here: browser enforcement of response CSP, native clipboard permissions, native file picker/download interaction, real browser-origin local-storage persistence, physical touch gestures, screen-reader usability, Windows/macOS behavior or a Python 3.10 matrix. Local-shelf behavior was checked with an explicit storage fixture; that is not a native-browser persistence claim. The scripts default to normal served-browser navigation for a follow-up on an ordinary machine.

## Benchmarks

`python -m observatory.benchmark --output observatory/BENCHMARKS.json` ran six named bounded scenarios: small perturbed pair, thousand-digit pair, 64-source carry trial, rank/module fixture, 128-source module transport and 4,096-branch composed word.

The recorded median provider times ranged from roughly **1 to 16 ms** on this execution environment. These include exact provider work, normalization, source checks and result digest; they **exclude HTTP, rendering and file export**. Traced memory is Python allocations in a separate replay, not whole-process/browser memory. Timings do not imply that all maximum bit, horizon, family and storage ceilings can be combined, nor predict another machine's performance. Re-run the named scenarios before changing resource architecture.

## Repository and publication limitations

The currently exposed GitHub connector functions permitted read access only; write/create actions were absent. The installed GitHub plugin was checked, and direct `git ls-remote` failed DNS resolution for github.com. **No new remote push, branch or PR is claimed for this pass.** The tested application, exact patch, delivery manifest, PR draft and safe worktree publisher are the deliverables. A local snapshot commit, if present in packaging, must not be advertised as a GitHub commit.

A complete scientific checkout was unavailable. **Root `tools/validate.py` and the full repository regression bundle were not run.** No public deployment, cloud provisioning, main push/merge, workflow/settings changes or mathematical-status changes are included. The larger programme remains open; [ROADMAP.md](ROADMAP.md) records implemented versus deferred scope rather than declaring every v0.2/v0.3 task finished.

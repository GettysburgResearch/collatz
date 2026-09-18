# v0.1 validation receipt

Implementation-session date: **18 September 2026**. Research baseline read through the connected GitHub API: `main @ ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Feature branch: `codex/collatz-observatory-v0.1`. The PR/branch head identifies the complete published implementation; this file does not attempt to contain its own future commit hash.

## What was actually run

Environment: Linux; Python **3.13.5**; Node **v22.16.0**; system Chromium **144.0.7559.96**. The app itself has no third-party runtime dependency. Python 3.10+ is the intended compatibility floor, not a claim that a 3.10 matrix was executed.

| Command / check | Observed result |
|---|---|
| `python -m unittest discover -s observatory/tests -p "test_*.py" -v` | **31 tests passed**. |
| Same Python suite with `python -O` | **31 tests passed**; explicit runtime input guards do not disappear under optimization. |
| `node --test observatory/tests/view.test.mjs` | **10 tests passed**. |
| `node --check observatory/web/app.mjs` and `node --check observatory/web/view.mjs` | Syntax checks passed. |
| `python observatory/tests/browser_smoke.py --in-memory --browser /usr/bin/chromium --screenshots ...` | **23 explicit checks passed**, no JavaScript page errors; desktop and 390px-wide screenshots generated. Scope below. |
| Direct execution of all three curated example recipes | Every requested orbit/family/word/inverse operation completed as a computation. The huge-source orbit correctly returned `step_limit`, not a claim of divergence. |
| Actual loopback server/API startup | Served assets, health/capabilities, job submission/polling and cancellation exercised. |

Mathematical-kernel SHA-256 at the recorded final checks:

```text
242cd0350b35a0122e030cb16edf63e14eb518f80b95e3feb02c559104b1c579
```

This is `core.py` only. It is not the entire application hash, a mathematical certificate, or an independent peer-review verdict. Browser and server source identity belongs to the published Git commit.

## Arithmetic coverage

The Python tests independently reconstruct raw trajectories for sources 1–159, checking accelerated raw-clock anchors and raw maxima. The 27 fixture gives raw/shortcut/odd step counts **111/70/41**, displayed peaks **9232/4616/3077**, and shared raw peak **9232**.

Every one of the **510 binary words of lengths 1–8** is checked against independently iterated positive representatives and exact affine endpoints. Other tests cover the `1110 → -19/11` rational control, trivial positive cycles, negative integer cycles, zero outside the positive domain, repeated words through length 512, canonical zero versus the least positive source, exact huge integers, 1,000-digit sources, hidden-intermediate bit limits, retention limits, family censoring, inverse-edge legality/deduplication, truncation, cancellation and wall-time handling.

The HTTP tests include real requests, mutation-token and Host/Origin rejection, path allowlisting, body limits, job capacity, bounded cache retention and **real HTTP cancellation of an intentionally heavy bounded family**. One additional deterministic cancellation/capacity test uses a controlled worker fixture; it is not the sole cancellation evidence.

## Browser evidence boundary

The system Chromium installation's managed policy blocked direct navigation, including to loopback. No browser policy or network restriction was changed. The recorded UI run instead used the script's **explicit in-memory mode**: local HTML/CSS/JS rendered in an empty Chromium DOM, with fetch bridged by the test harness to the **real running loopback HTTP API**. ES module sources were concatenated for that harness; normal module syntax was checked separately with Node.

This exercised initial loading, exact inspectors, keyboard selection, peak jumps, cross-clock selection, integers beyond `2^53`, a 1025-bit input, binary alignment, word classification, word-root → orbit linking, censored family counts, family → orbit linking, recipe/notes/bookmark replay, viewport and comparison replay, schema rejection and responsive layout. Screenshots are of this actual application DOM, not design mockups.

It did **not** establish normal browser HTTP navigation/module loading, real-browser enforcement of response CSP, native clipboard permissions, native file-picker/download behavior, mobile touch gestures, or Windows/macOS operation. The test script defaults to a genuine served-browser run in an ordinary local environment; that and a Windows receipt are first v0.2/readiness tasks. The 390px check is responsive desktop Chromium layout, not physical iPhone testing.

## Repository and mathematical boundary

A complete checkout was unavailable: direct Git transport failed on DNS resolution. The baseline was read using the authorized GitHub connector; new application files were created and tested in a local subtree. **`tools/validate.py` and the repository regression bundle were not run.** This receipt is not a full-checkout integrity claim, an audit of unrelated branches, or a review of existing proof packets.

No main-branch push, merge, workflow/settings change, public deployment, cloud provisioning, account creation or publication of secrets is part of this delivery. The parent programme stays open. Engineering fixtures and a working visualization do not resolve Collatz or upgrade an inherited mathematical claim.

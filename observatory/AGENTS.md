# Observatory agent handoff · investigation preview

Read root `AGENTS.md` in a full repository checkout. This local application does not alter the project's unresolved scientific status. Start with [README](README.md), [MATHEMATICS](MATHEMATICS.md), [ARCHITECTURE](ARCHITECTURE.md), [VALIDATION](VALIDATION.md) and the [delivery/remaining-work matrix](ROADMAP.md).

## Source and publication boundary

This pass starts from the exact v0.1 application subtree `0dea2738379fd0242fd68794a5204e1a2df45188`, at actual repo head `f0bf47d9c4253c3a16617f4b70388a7a4ba4e1de` on PR #119. Main was `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The implementation environment could read but not write GitHub; direct Git transport failed DNS. No new remote push/PR is claimed. Apply the delivered patch to that base and publish on a new feature branch, ideally as a stacked PR against `codex/collatz-observatory-v0.1` while #119 is unmerged. Requery the live state first; do not overwrite other contributors' work.

## Run and check before extending

```sh
python observatory/server.py
python -m unittest discover -s observatory/tests -p "test_*.py" -v
python -O -m unittest discover -s observatory/tests -p "test_*.py" -v
node --test observatory/tests/*.test.mjs
python -m observatory.verify observatory/examples/27-19-meeting.json
```

Optional normal served-browser receipt (start server separately; Playwright test-only dependency):

```sh
python observatory/tests/lab_browser.py --screenshots screenshots/lab
python observatory/tests/browser_smoke.py --screenshots screenshots/classic
```

The implementation session used explicitly labeled in-memory Chromium DOM/real-API tests because managed navigation was blocked. Do not turn this into a claim about native browser CSP, local storage, downloads, Windows, macOS or physical devices. Run those checks on an ordinary machine before declaring platform readiness. In a full clean checkout also run the root validator according to its policy; that was not available in the subtree-only implementation environment.

## Protect the investigation, not just the screenshot

A pair means exact positive source A, a specified relation yielding B, independent maps, actual raw arrival clocks and explicit finite support. Raw-aligned charts include retained hidden raw states; displayed-aligned charts use actual displayed clocks. Nulls are uncomputed/unrepresented, never terminal extrapolation or zero. Verify a meeting's two paths, perturbation and arrival clocks through the independent checker.

Odd arithmetic is `n + (n<<1) + 1`, with the +1 injected at column zero. A crop must retain its true entering carry. An even branch is halving, not an addition carry motif. Test observed features on exact finite source families; retain controls, invalid partners, partial work and counterexamples. Shared tails make naive independence claims invalid.

P, R*, shortcut time, raw time and maximal-module time are distinct. Whole-denominator cycle arithmetic and literal branch replay remain decisive. Module endpoint bounds are not hidden-peak bounds. Module floor=1 is deliberate; support for higher floors needs internal crossing checks. No imported rank or safe-region theorem licenses fresh-shell resampling after actual transport.

## Engineering extension points

- Keep `core.py` as the v0.1 reference unless a demonstrated repair is independently tested.
- Add strict, budget-aware pure operations through `engine.REGISTRY`; update the manifested source list when adding mathematical providers. Loaded-code/disk mismatches must reject computation until restart.
- Keep visible UI and `window.observatory` on the same command path. Preserve epochs and transactional replay. Do not trust imported mathematical results.
- Use the local `SelectionPanels` contract for new observables, with documented input/support. No submitted-code execution or HTTP plugin installation.
- Preserve `/classic`, old recipes and the simple one-command launcher. Do not add runtime infrastructure merely to modernize the stack.
- Add new arithmetic fixtures from independent literal computations, not only calls comparing a function with itself. Extend forged-witness tests with every schema change.
- Artifact fingerprints and exact finite checks are evidence, not proof status. Keep source pins, corpus coverage, aggregation losses and unsupported inferences visible.

## Next priorities

1. Obtain normal served-browser and Windows receipts; native download/load/local-shelf/cancellation and all explicit clocks must work. Check accessibility and touch selection on real devices.
2. Harden schema/version migration and split the large UI controller into independently testable laboratory controllers without breaking transactional replay. Add more than one plugin-contributed view before promising a stable ABI.
3. Turn observations into a richer predicate/filter language and queryable corpus, with held-out populations that account for shared suffixes. Keep the current bounded implication semantics.
4. Extend paired meeting/rank records to exact lower-rank physical diagrams and repository source-121 examples. A bounded successful family is not an exhaustive selector.
5. Add faithful pinned rewriting/QCA only after the paired workflow is preserved; implement legal encoders, rules, boundary conditions and microstep clocks, not just decorative animations.
6. Profile first; then add process workers and durable resumable artifacts with explicit interruption semantics. Maintain the zero-account local mode. Public deployment requires a separate hardened service, not exposing this server.

Small durable commits and real checks are preferable to a claim that the entire v0.3 programme is complete. Keep programme #118 open.

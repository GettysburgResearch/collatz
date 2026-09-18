# Working on the Observatory with Codex or another agent

Read the root `AGENTS.md` first. This subtree is an engineering product for exact finite experiments, not a replacement scientific front door. The v0.1 implementation is on `codex/collatz-observatory-v0.1`; programme #118 remains open.

## Boot and orient

1. Read `README.md`, `ARCHITECTURE.md`, `ROADMAP.md`, and `VALIDATION.md` here.
2. From the repo root run `python observatory/server.py` (or `py -3` on Windows). Browser URL: `http://127.0.0.1:8765`. No npm or pip install is needed for the application.
3. Try 27, `2^1024+1`, `1110`, `10`, and a deliberately step-limited family. Inspect exact values, not only screenshots. `window.observatory` and `/api/capabilities` are agent entrypoints.

## Keep these contracts intact

- Never parse an exact seed through a JS Number or Python float. JSON large integers are decimal strings.
- Define the map, domain and clock on every new object/view. An odd seed is required for the odd-only map. Preserve raw intermediates when reporting raw peaks.
- Keep incomplete outcomes in family denominators. A killed state, uncomputed state, zero bit, rational cycle and ordinary positive cycle are different things.
- Do not derive statistics from a plotted/downsampled subset. Any new aggregation has to explain what it preserves, loses and can refine.
- Call the exact provider from views; do not add another unreviewed orbit kernel to a renderer. Do not turn a proposed repository theorem into an application invariant without checking its scope/errata.
- No arbitrary-code API, external runtime network calls, untrusted plugin execution, public bind option or silent dependency download. Public deployment needs its own reviewed architecture.
- Preserve the simple local launcher. Do not modify repository workflows/settings, licensing, main or unrelated research files as part of a UI task.

## Useful next bounded tasks

V02-01 in `ROADMAP.md` is the first recommended implementation task: split panel controllers and add schema/registration contracts while keeping every v0.1 fixture passing. Then add served-browser and Windows receipts, followed by a faithful rewrite/carry panel. Do not start by replacing the entire application with a framework scaffold that loses current functionality.

## Checks and publication

```sh
python -m unittest discover -s observatory/tests -p "test_*.py" -v
node --test observatory/tests/view.test.mjs
node --check observatory/web/app.mjs
```

The Node commands are optional developer tests. The optional Playwright script supports normal served-browser testing; its in-memory mode has narrower scope and must be labeled honestly. In a complete checkout, additionally follow the root's integrity/replay instructions. Never claim the full validator ran from a subtree-only materialization.

Record commands actually run, environment, exact commit and remaining gaps. Separate code inspection, unit fixtures, UI harness tests, live browser tests, public deployment and mathematical verification. Push a branch/PR and re-query the remote before claiming publication. Update the parent programme with a scoped progress comment rather than closing the entire programme when one version lands.

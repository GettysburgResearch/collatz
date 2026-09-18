# Collatz Observatory · v0.1

A runnable, local-first visual research desk for **exact finite Collatz experiments**. This is the first implementation slice of [programme #118](https://github.com/GettysburgResearch/collatz/issues/118), not a proof, an all-time search, or the complete programme.

## Start here

**Python 3.10+ is the only runtime dependency.** No npm install, pip packages, API keys, database, cloud account, or build step. Use a modern browser with BigInt and ES modules.

From the repository root:

```sh
python observatory/server.py --open
```

On Windows, the Python launcher also works:

```powershell
py -3 observatory/server.py --open
```

On systems whose Python command is `python3`, substitute that command. Open **http://127.0.0.1:8765**. Keep the terminal open; Ctrl+C stops the server. A port conflict is resolved with `--port 8766`. `--open` is optional, including in Codex/headless environments. You can also run `python -m observatory.server` from the repository root.

First checkout of this implementation branch in an existing clone:

```sh
git fetch origin
git switch --track origin/codex/collatz-observatory-v0.1
python observatory/server.py --open
```

Use `git switch codex/collatz-observatory-v0.1` when the local branch already exists. Do not discard other uncommitted work to switch branches.

## A five-minute first investigation

1. The desk starts with **27**, its shortcut trajectory, the `1110` word, a **128-source family atlas**, and the inverse frontier of 1. Click a point in the orbit. Its exact integer, raw clock position, residues and binary row stay linked. Use the step field or arrow keys for precise selection.
2. Click **Jump to peak**, then change clocks. The displayed peaks differ because acceleration hides intermediate states; the separate raw-segment peak does not. A raw step missing from an accelerated representation is mapped explicitly to its preceding represented state, not silently identified with another clock.
3. Click **Beyond floating point**. Try decimal integers, `0b...`, `2^1024+1`, or `2^2048-1`. Drag the orbit to zoom, or enter a step window. Pin a trajectory, run another source under the same clock, and compare the two curves.
4. In **Words & cycles**, compare `1110`, `10`, `1`, and `0000`. Click the least-root plot to inspect a prefix, then trace its least positive source. `1110` has rational periodic candidate `-19/11`; its finite positive source is not that infinite rational realization.
5. Explore an arithmetic-progression family, select an atlas point or table row, and trace that source. Bookmark a selection, add a note, **Save experiment**, and **Load** the JSON. Loading recomputes the mathematics. Three ready-made recipes are in [examples](examples/).

## What is implemented

| Laboratory | v0.1 behavior |
|---|---|
| Orbit/excursion | Raw, shortcut and odd-to-odd maps; exact states; raw cross-clock anchors; first displayed descent; displayed and hidden-raw peaks; bounded outcomes; plot brushing, window controls and one pinned comparison. |
| Binary microscope | Linked exact bit rows; fixed low-bit or per-row high-bit alignment; bit-offset navigation; adaptive column count; explicit row/bit cropping. The arithmetic inspector shows `3n+1`, its 2-adic valuation and accelerated successors. |
| Parity/cycle | Exact affine numerator, **whole** cycle denominator, rational candidate, independent branch replay, primitive word length, source cylinders, prefix least-positive roots, and a link back to a positive trajectory. |
| Family atlas | Exhaustive finite arithmetic progressions, exact huge source anchors, bounded offsets on the plot, status counts that retain incomplete members, exact tables and click-to-trace. |
| Inverse graph | Exact shortcut predecessors, distinct-state deduplication, minimum inverse-depth layout, directed edge witnesses, clickable nodes and explicit truncation. |
| Research workflow | Exact inspector; bookmark/notes; versioned experiment JSON with viewport, alignment and comparison recipes; witness export; cancellable jobs; structured HTTP and browser-agent interfaces. |

The workspace uses a fixed responsive panel grid, not yet a drag-and-dock window manager. The curve envelope preserves exact integer extrema and endpoints inside buckets; it does **not** preserve every motif, crossing or event order within a bucket. Statistics are never computed from the plotted subset. Binary views crop literal cells rather than inventing a coarse-cell semantic.

## Scientific conventions and limits

Definitions follow [the repository conventions](../research/integrated/CONVENTIONS.md), with [errata](../research/integrated/ERRATA.md) retained as boundaries. All orbit sources are positive integers. Odd-to-odd input must already be odd; it is never normalized silently.

- **Raw:** `C(n)=n/2` when even, `3n+1` when odd.
- **Shortcut:** `T(n)=n/2` when even, `(3n+1)/2` when odd.
- **Odd-to-odd:** `U(n)=(3n+1)/2^v2(3n+1)` on positive odd integers.

Trajectories stop at 1, a repeated exact state, or a resource limit. `first_descent` means the first **displayed** state strictly below the source. The raw-segment maximum includes hidden arithmetic intermediates; it is not the same observable as the displayed maximum. A budget-limited trace is **not** divergent. Family plot heights for unresolved members are observed steps, not stopping times. A finite inverse frontier is not an all-depth cover, and graph nodes count states rather than paths.

For a shortcut word of length L and odd weight s, the kernel constructs `T^L(n)=(3^s*n+A)/2^L`. It computes the canonical residue modulo `2^L`, the least **positive** representative (canonical zero becomes `2^L`), and periodic candidate `A/(2^L-3^s)`. Rational, negative-integer, zero and trivial positive outcomes remain separate. This is a finite calculation for one word, not an all-cycle exclusion or a new theorem.

Hard bounds are deliberately conservative:

| Dimension | Bound |
|---|---:|
| Integer / raw intermediate | 8,192 bits |
| Displayed orbit steps | 20,000 |
| Retained trajectory decimal digits | Approximately 1,500,000, plus the last bounded row |
| Family size / total step budget | 512 sources / 1,000,000 steps |
| Parity word | 512 bits |
| Inverse frontier | Depth 12; 128 nodes in UI, up to 256 via API |
| Work | Two concurrent cooperative jobs; 15 seconds per job |
| Cache | Eight in-memory jobs, evicted oldest-completed first |

This can explore thousand-digit inputs, but it does not promise long trajectories, giant populations and unrestricted inverse expansion simultaneously. Integer arithmetic and branch decisions are exact. Log coordinates are approximate floats computed without casting the full integer to a float. JSON encodes large integers as decimal **strings**; browser BigInt is used for exact inspection, not coerced through Number.

## Save, replay, and agent access

An experiment contains recipes, notes, bookmarks, selected step, viewing window, bit alignment, optional comparison, and the original kernel digest. Results are recomputed on import; a changed digest is reported. Jobs and results are not durable across server restarts. Save useful experiments before closing the browser. Witness export is a finite observation record, **not** an independently certified theorem.

See [API and architecture](ARCHITECTURE.md) for runnable agent examples, schemas and extension points. The UI exposes `window.observatory` with `runOrbit`, `runWord`, `runFamily`, `runInverse`, `select`, `getState`, `exportExperiment` and `loadExperiment`; these use the same jobs and kernel as the visible controls.

## Tests and evidence

```sh
python -m unittest discover -s observatory/tests -p "test_*.py" -v
node --test observatory/tests/view.test.mjs
```

Node is needed only for the optional JS tests, not for running the app. Browser interaction checks require the optional Playwright test dependency and a Chromium installation:

```sh
python -m pip install playwright
python -m playwright install chromium
# Start the server in another terminal, then:
python observatory/tests/browser_smoke.py --screenshots screenshots
```

The exact recorded execution boundary, including the managed-browser limitation of the implementation session, is in [VALIDATION.md](VALIDATION.md). Do not conflate the local application tests with the full repository validator or with mathematical peer review.

## Extend with Codex

Read [AGENTS.md](AGENTS.md), [ARCHITECTURE.md](ARCHITECTURE.md), and [ROADMAP.md](ROADMAP.md). Start with a small bounded change and retain the arithmetic fixtures. No dependency install is needed to run the app. No repository integrity/CI settings were changed for this feature.

**Deployment boundary:** this server binds only to loopback, checks Host and Origin, requires a session token for mutations, serves a small fixed asset allowlist, and executes no submitted code. It is a local development/research instrument, **not an Internet-facing server**. Do not publish it by exposing the port or tunneling it to an untrusted audience. Python itself [does not recommend `http.server` for production](https://docs.python.org/3/library/http.server.html). Shared authenticated compute is a later architecture milestone.

[Roadmap: v0.2 through v1.0](ROADMAP.md) · [Programme #118](https://github.com/GettysburgResearch/collatz/issues/118)

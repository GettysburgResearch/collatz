# Collatz Observatory · 0.3.0-preview.1

**A runnable local laboratory for paired-trajectory investigations and exact finite Collatz research.** Perturb a bit, inspect the actual addition carries, find exact shared states with both arrival times, challenge a motif on a bounded family, and replay the whole investigation.

This is a substantial implementation beyond [v0.1 / PR #119](https://github.com/GettysburgResearch/collatz/pull/119), with selected v0.3 research adapters. It is **not completion of every v0.2/v0.3 roadmap item**, a proof of Collatz, or an Internet-facing service. The [delivery matrix](ROADMAP.md) distinguishes implemented capabilities from remaining work. Parent programme: [#118](https://github.com/GettysburgResearch/collatz/issues/118).

## Run it

Python **3.10+** and a modern browser are the intended runtime requirements. The app has **no third-party runtime dependencies, npm build, API key, database, or account**.

From the repository root (or the extracted application ZIP):

```sh
python observatory/server.py --open
```

Windows:

```powershell
py -3 observatory/server.py --open
```

Substitute `python3` where appropriate. Open **http://127.0.0.1:8765**; keep the terminal open. Ctrl+C stops the server. Use `--port 8766` for a port conflict; omit `--open` in headless environments. The original v0.1 desk is preserved at **http://127.0.0.1:8765/classic**.

The new desk starts populated, with `27` and `27 xor 2^2 = 31`. A named investigation can be saved locally in the browser, or exported to a portable JSON recipe. Export valuable work: compute jobs are not persistent across server restarts.

### Source and evidence

The exact source baseline, publication boundary, test receipt and known platform gaps are recorded in [VALIDATION.md](VALIDATION.md). This preview's patch is separate from the original v0.1 PR; follow the accompanying publishing handoff when landing it in a full clone.

## First complete investigation

1. **Perturb.** In the paired desk choose source `27`, flip bit `3`, and run. The second source is `19`. Try raw, shortcut and odd-to-odd clocks independently for A and B. Odd-to-odd sources must already be odd; an even source is never silently normalized.
2. **Inspect arithmetic.** At raw time zero, the carry table shows literal columns of `n + (n << 1) + 1` for both odd sources: input bits, shifted bits, incoming carry, outgoing carry and result. The injected `+1` is the carry entering column zero. Cropping at a nonzero bit offset still computes the actual incoming carry from lower columns. On an even state the operation is halving, not fictional `3n+1` addition.
3. **Find the shared state.** Click the first meeting. For 27 versus 19, the stopped raw trajectories first intersect at `40`, at raw arrivals **103** and **12**. With A shortcut and B odd-to-odd, A's displayed arrival is **63** and B's is **not represented**: 40 lies inside B's accelerated transition. The inspector and exported witness preserve this distinction. Meeting alignment is retrospective, not a prospective predictor.
4. **Challenge a motif.** In the family trial, use sources `1,3,...,127`, partner offset `2`, raw horizon `30`, carry-run threshold `3`, and target “share a computed state by the horizon.” Open a counterexample and trace both sources. Controls and bit-limited/unfinished members stay in the original denominator; a counterexample refutes only that bounded implication.
5. **Record and replay.** Capture an observation, write down the hypothesis and a counterexample, then export the investigation. Loading recomputes every included laboratory before committing the new workspace. A failed request leaves the prior investigation intact. Changed kernel/result digests are reported; old observations are not silently re-certified.

Load [paired-investigation.v2.json](examples/paired-investigation.v2.json) for a populated cross-laboratory example. [Huge paired inputs](examples/huge-pair.v2.json) and [unfinished-case controls](examples/unfinished-controls.v2.json) are included. The old example files still open in `/classic`; import into the new desk preserves the original classic recipe but only migrates its orbit/comparison into the paired workspace.

## What is implemented

| Laboratory | Runnable behavior |
|---|---|
| Paired trajectories | Bit flip, signed neighbor offset or explicit partner; independent displayed clocks; raw/step/meeting-relative alignment; drag zoom, window controls and keyboard inspection; literal difference spacetime. |
| Carries and physical meetings | Actual arithmetic columns and carry differences; exact intersections of raw and displayed supports; both arrival clocks, including hidden raw states; export plus a separate finite-witness checker. |
| Bounded motif trials | Carry-run, odd-step valuation and shortcut-prefix predicates; merge-by-horizon or first-descent targets; source progression, controls, supporting examples, counterexamples, invalid partners and unfinished work. |
| Drift, ranks and modules | Exact affine prefix identities; coefficient crossing versus physical descent; distinct section/global and moving-envelope ranks; maximal repeated-word modules with raw/shortcut costs and exact safe/nonincreasing comparisons. |
| Transported populations | Actual source weights and endpoint multiplicities, residue histograms, exact moving-rank mass, killed/alive/unresolved accounting and module safe-membership weights. No fresh resampling after returns. |
| Symbolic blocks and cycle controls | Composable repeated parity blocks, complete denominator and rational branch replay; bounded least-positive roots; odd-valuation cycles for separately identified `3n+1`, `3n-1`, and `5n+1` controls. |
| Research workflow | Portable six-laboratory recipes, transactional replay, observations with witnesses, named local shelf, bounded undo/redo, code/result fingerprints, agent commands and a small trusted local panel registration contract. |
| Preserved v0.1 desk | Original orbit, bit, family atlas, word/cylinder and finite inverse graph tools remain at `/classic`. |

Faithful published string rewriting and cellular automata are **not** implemented. The carry table is an arithmetic microscope, not relabeled as either published system. Full docking, arbitrary graph search, durable/process-isolated jobs, stable third-party plugin ABI and shared cloud compute remain future work.

## Mathematical conventions

- **Raw:** `C(n)=n/2` for even n and `3n+1` for odd n.
- **Shortcut:** `T(n)=n/2` for even n and `(3n+1)/2` for odd n.
- **Odd-to-odd:** `U(n)=(3n+1)/2^v2(3n+1)` on positive odd sources.
- **Maximal-word module:** the separately defined repeated `1^a0` shortcut block, not one odd step or an arbitrary whole-run map. See [mathematical contracts](MATHEMATICS.md).

Trajectories stop at their first visit to 1, a repeated exact state, or a resource limit. A shared state may have **different arrival times**. A missing finite intersection is not a claim that the sources never merge. Research rank values are not universally decreasing; module endpoint bit limits do not bound hidden raw peaks.

All decisive arithmetic uses exact integers/rationals. Large integers cross JSON as decimal **strings**. Log coordinates are approximate display values, not numerical tests of divisibility or equality. Raw-aligned paired curves include computed hidden raw intermediates; displayed-step alignment uses the actual selected clocks. Envelope reduction preserves exact bucket extrema/endpoints, not every unknown motif. Difference spacetime is a literal crop; uncomputed cells are not zero. Populations and counterexamples are calculated from exact members, never from plotted samples.

## Bounds and persistence

| Dimension | Current ceiling / behavior |
|---|---|
| Paired sources / displayed steps | 8,192-bit states and raw intermediates; 10,000 displayed transitions per side. |
| Materialized raw support | 20,000 transitions per side, plus approximately 750,000 decimal digits; exact displayed anchors remain available outside that dense prefix. |
| Carry view | Up to 256 literal columns by API; UI 16/32/64/128; offset through bit 8,191. |
| Family trial | Up to 128 sources, raw horizon 4,000, `2 × count × horizon <= 300,000`; configurable bit cap up to 2,048. |
| Rank/transport adapters | 1,024-bit cap; up to 512 shortcut prefixes, 128 modules, or 128 sources × 64 transport rounds. |
| Symbolic work | Repeated-block expanded length <=4,096; least-root plot <=512 prefixes; whole bounded word is still replayed. |
| Server work | Two cooperative jobs, 15-second checked compute budget, eight-job in-memory cache; result retention cap 16 MB. |
| Partial cancellation | Trials retain completed members and mark uncomputed ones; transport retains completed frames. Other interrupted operations may have no result. |
| Local shelf/history | Up to 12 recipes/4 MB in browser storage; five in-memory undo snapshots. Save/reload recipes recomputes results. |

These are safety ceilings, not simultaneous performance guarantees. Check [BENCHMARKS.json](BENCHMARKS.json) and [VALIDATION.md](VALIDATION.md) for measured, scoped evidence. Restart the server after changing any mathematical kernel source; it rejects computations whose loaded code no longer matches the files on disk.

## Agent and developer access

```javascript
await window.observatory.runPair({
  kind: 'pair', seed: '27', relation: 'flip', bit: 3,
  map_left: 'shortcut', map_right: 'odd', steps: 1000
});
window.observatory.selectMeeting(0);
const witness = window.observatory.exportMeeting();
const recipe = window.observatory.exportExperiment();
```

The same operations run without a browser:

```python
from observatory.engine import execute
result = execute({"kind": "pair", "seed": "27", "relation": "flip", "bit": 3,
                  "map_left": "shortcut", "map_right": "odd", "steps": 1000})
print(result["result"]["shared_raw"][0])
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for all operation schemas and HTTP examples, and [AGENTS.md](AGENTS.md) for continuation tasks.

### Independent finite meeting verification

Export a meeting from the UI and run:

```sh
python -m observatory.verify collatz-meeting.json
# Bundled example:
python -m observatory.verify observatory/examples/27-19-meeting.json
```

This checker imports **no Observatory arithmetic kernel**. It separately replays both raw trajectories, verifies the perturbation and both displayed/hidden arrivals, and rejects inconsistent evidence. It checks a finite equality, not a theorem of convergence, completeness, or the trustworthiness of every other observable.

## Tests

```sh
python -m unittest discover -s observatory/tests -p "test_*.py" -v
python -O -m unittest discover -s observatory/tests -p "test_*.py" -v
node --test observatory/tests/*.test.mjs
```

Node is optional, only for JavaScript tests. For optional browser tests:

```sh
python -m pip install playwright
python -m playwright install chromium
# Start the server in another terminal:
python observatory/tests/lab_browser.py --screenshots screenshots/lab
python observatory/tests/browser_smoke.py --screenshots screenshots/classic
```

Use `--browser PATH` to select an installed Chromium executable. The test scripts default to real served-browser navigation. The recorded implementation-session tests used a narrower, explicit in-memory Chromium DOM/real-API bridge because managed browser navigation was blocked. **Windows/macOS, native browser file dialogs/storage/clipboard, browser-enforced CSP, and full-repository validation are not covered by that receipt.** Details: [VALIDATION.md](VALIDATION.md).

**Local-only deployment:** loopback binding, Host/Origin/session-token checks, a fixed asset allowlist and no submitted-code execution are retained. This is not a public production server. Do not expose the port or tunnel it to untrusted users.

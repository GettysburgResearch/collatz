# Investigation architecture and agent API

Version: `0.3.0-preview.1`. Exact finite computation, local-first deployment. The old app remains under `/classic`; no existing scientific source files are changed by the feature patch.

## Layers

| Module | Responsibility |
|---|---|
| `core.py` | Unchanged v0.1 exact orbit, word, family and inverse kernel. |
| `pairs.py` | Partner construction, explicit raw support, common-state witnesses, schoolbook carries and bounded motif trials. |
| `research.py` | Named ranks, exact maximal-word modules, affine prefix identities and weighted finite transport. |
| `symbols.py` | Affine block composition and isolated odd-valuation cycle systems. |
| `engine.py` | Trusted operation registry, strict normalization, versioned result envelopes, loaded-code fingerprints. |
| `server.py` | Loopback HTTP, fixed static allowlist, Host/Origin/token guards, bounded cooperative jobs and retained partial results. |
| `verify.py` | Independent finite meeting checker with no imports from the above mathematics. |
| `web/client.mjs` | One bounded job client for visible controls and agent commands; cancellation, two-slot retry, stale-result epochs. |
| `web/workspace.mjs` | Versioned recipes, validation, narrow classic migration, named local storage and bounded history. |
| `web/panels.mjs` | Literal/exact inspectors, bounded renderers and a trusted local selection-panel registry. |
| `web/lab.mjs` | Investigation controller, transactional multi-operation replay and `window.observatory`. |

This is not yet a process-isolated service, a stable third-party plugin ABI, or a general docking framework. The controller still has UI wiring worth splitting as the laboratories grow. The existing zero-install ES-module shell is deliberately retained.

## Results and identity

Every operation returns `collatz-result/v2` with normalized `request`, `result`, version, `request_sha256`, `result_sha256`, `kernel_sha256`, the five-file mathematical manifest and the inherited research baseline. Integer values are decimal strings. Small bounded indices are JSON integers; plotting logs are approximate numbers.

The manifest is captured when the mathematical modules load. Disk changes before/during a computation cause rejection and a restart instruction; new file bytes cannot silently label old loaded code. Server/browser code identity belongs to the source-tree/patch receipt, not the mathematical manifest. A digest is provenance, not mathematical certification.

## HTTP jobs

```
GET    /api/health
GET    /api/capabilities
POST   /api/jobs
GET    /api/jobs/{id}
DELETE /api/jobs/{id}
```

`GET /api/health` exposes the session mutation token; `/api/capabilities` describes operations and limits. Mutations require the `X-Observatory-Token` header and a permitted Host/Origin. Only local trusted callers should access the server. Inputs are bounded JSON, not submitted code.

The server has two cooperative workers and eight cached jobs. A full queue responds with an explicit capacity error. Status is running, cancelling, done, cancelled, timed_out or error. **Cancelled/timed_out study and transport jobs can still contain `data`**: inspect it before discarding the job. Other operations can be cancelled without a partial artifact. Jobs are not persistent and do not resume after restart. One result may retain at most 16 MB.

A dependency-free Python HTTP client:

```python
import json, time
from urllib.request import Request, urlopen
BASE = "http://127.0.0.1:8765"

def call(path, payload=None, method=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["X-Observatory-Token"] = token
    body = None if payload is None else json.dumps(payload).encode()
    req = Request(BASE + path, data=body, headers=headers,
                  method=method or ("POST" if body is not None else "GET"))
    with urlopen(req, timeout=30) as response:
        return json.load(response)

token = call("/api/health")["token"]
job = call("/api/jobs", {"kind": "pair", "seed": "27", "relation": "flip",
                         "bit": 3, "map_left": "shortcut", "map_right": "odd",
                         "steps": 1000}, token=token)
while job["status"] in ("running", "cancelling"):
    time.sleep(0.05)
    job = call("/api/jobs/" + job["id"])
if "data" not in job:
    raise RuntimeError(job.get("error", job["status"]))
print(job["status"], job["data"]["result"]["shared_raw"][0])
# Cancel with call("/api/jobs/" + job_id, method="DELETE", token=token).
```

## New operation recipes

Only the fields belonging to the selected relation are accepted. Defaults are filled by the kernel; unknown fields fail visibly.

```json
{"kind":"pair","seed":"27","relation":"flip","bit":3,"map_left":"shortcut","map_right":"odd","steps":1000,"max_bits":8192,"raw_limit":10000}
```

Pair relations: flip + `bit`; offset + signed decimal `delta`; explicit + exact positive `other`. Independent maps are `raw`, `shortcut`, `odd`. `raw_left`/`raw_right` contain retained raw prefixes; `shared_raw` and `shared_displayed` name their actual support. Null `step` means not represented. No terminal extrapolation.

```json
{"kind":"carry","left":"27","right":"19","offset":0,"width":32}
{"kind":"study","seed":"1","stride":"2","count":64,"relation":"offset","delta":"2","horizon":30,"max_bits":1024,"motif":"carry_run","value":"3","target":"merge"}
```

Other motifs: `valuation` with an exact threshold string; `parity_prefix` with a 1–32 bit string. Targets: `merge`, `left_descends`. All target horizons use raw transitions and first-1 stopping. Families use `flip` or `offset`, not one fixed explicit partner. Read member `selected`, `target_holds`, `outcome`, trace statuses and `witness`; null is unknown, never false by default.

```json
{"kind":"research","seed":"577363","steps":128,"modules":32,"max_bits":1024}
{"kind":"transport","seed":"1","stride":"1","count":64,"rounds":24,"floor":"1","map":"module","max_bits":512,"modulus":16}
```

Research uses shortcut prefix rows and a separately labeled maximal-module trace. Transport accepts `shortcut` or `module`; only shortcut accepts floors other than 1. Residue histograms carry source multiplicity. Safe weights are defined only for the module clock; bit-limited membership is explicit.

```json
{"kind":"blocks","blocks":[{"word":"1110","repeats":16},{"word":"10","repeats":2}]}
{"kind":"valuations","multiplier":5,"addend":1,"valuations":[1,1,5]}
```

`blocks` composes at most 32 blocks and caps expanded length at 4,096. Complete rational replay is mandatory even when the state preview is cropped. `valuations` takes integer `multiplier` and `addend`, permitting only the explicit systems `3n+1`, `3n-1`, `5n+1`; 1–128 valuations in [1,64], total <=4,096. General user programs are not executed.

The four v0.1 kinds (`orbit`, `word`, `family`, `inverse`) remain supported by the same HTTP provider and `/classic` UI. Their clocks and old limits are unchanged.

## Browser agent commands

```
runPair(request), runStudy(request), runResearch(request), runTransport(request)
runBlocks(request), runValuations(request)
select(rawA, rawB), selectMeeting(index), show(tab), inspectCarries()
exportExperiment(), loadExperiment(recipe), exportMeeting()
captureObservation(), cancel(), getState()
```

All are under `window.observatory`. Run/load methods return promises. Wait for `getState().ready` after boot. Tab names: pair, study, research, transport, symbols, notes. Selection uses **raw arrival coordinates**, regardless of the two displayed clocks. Use `getState().data` for completed envelopes and `view` for the current representation; editable form text alone is not a completed experiment.

The shared job client uses channel epochs. A stale completed request cannot silently replace a newer accepted result. Multi-operation block work has its own generation guard. Loading a recipe cancels prior work, validates all recipes, recomputes into a temporary workspace, and commits only on success. A cancelled or malformed replay retains the old workspace. Partial study/transport results are valid bounded observations and remain labeled.

## Portable investigation schema

`collatz-investigation/v2` contains:

- `requests`: one mandatory pair plus optional study, research, transport, blocks and valuations;
- `view`: both raw selections, alignment, window, carry crop, active tab, selected trial/prefix/frame, filters;
- `notes`, `observations`: exact supporting evidence plus text;
- `provenance`: mathematical fingerprint and operation result digests;
- optional `importedClassic`: preserved original v0.1 recipe on narrow migration.

Results are recomputed, not trusted on import. Historical observations retain their old evidence and are marked as historical on replay; changing a recipe does not establish the same claim on the new population. A saved experiment is a recipe plus observations, not a persistent compute checkpoint.

The portable recipe limit is 2 MB. Observation insertion and normalized replay are validated before committing, so a new observation cannot make a previously valid investigation unexportable. Named local storage is browser-origin-local (12 entries/4 MB). JSON export is the portable backup. History keeps five in-memory snapshots of completed investigations; it is not an unlimited durable log of every keystroke. The `/classic` migration maps only its orbit/comparison into the paired schema and preserves the original; old atlas/inverse panels do not masquerade as replayed new panels.

## Extension boundaries

Add a trusted operation by supplying a strict normalizer and a pure bounded computation to `engine.REGISTRY`. Use decimal-string integers, `Budget.check()`, explicit support/status fields and small independent fixtures. Restart after edits. There is **no HTTP plugin installer or code evaluator**.

For a local observable, use `SelectionPanels` in `panels.mjs`; the low-bit-run panel demonstrates exact selection access without another orbit implementation. Renderers must document aggregation losses and support refinement to exact objects. The current interface is intentionally small and not a stable installable plugin ABI.

## Deferred infrastructure

Process isolation, durable queues/checkpoints, out-of-core tile indexes, automatic distributed work, stable schema/plugin migrations across arbitrary future versions, production authentication and public hosting are not present. Preserve the one-command local mode while adding these only against measured workloads and explicit acceptance tests.

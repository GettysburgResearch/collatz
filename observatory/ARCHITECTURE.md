# Architecture and API · v0.1

## Deliberate first-release choice

The programme proposed a TypeScript/React workspace over an exact Python provider. v0.1 uses **dependency-free browser ES modules and Python's standard library** to deliver a runnable slice with no bundler, package installation, CDN or account. This is an implementation tradeoff, not a claim that React is unsuitable. Preserve the object/API contracts if the growing panel shell later migrates to TypeScript/React. Do not rewrite working mathematics to change the interface framework.

```text
index.html + style.css
        ↓
app.mjs: commands, panel controllers, linked selection, replay
        ↓                         ↘
view.mjs: exact-envelope helpers   window.observatory: agent commands
        ↓                         ↙
HTTP jobs: normalized request → bounded operation → versioned result
        ↓
core.py: Python integer/Fraction arithmetic; independent of DOM/HTTP
```

`server.py` serves an explicit static allowlist and a small JSON API. Jobs use two worker threads, cooperative cancellation, per-operation time checks and bounded input/result retention. This is intentionally not a durable distributed scheduler. A thread is not a security sandbox; there is no arbitrary-code or user-plugin execution endpoint.

## Exact identities and display coordinates

A selected orbit state is identified by `(normalized source, map, displayed step)` and carries an exact raw-clock position. Shared values do not imply identical times. Accelerated clocks may omit a raw state; the UI explicitly picks the preceding represented raw anchor on clock switching. It does not invent an exact cross-clock point.

Integer values, family anchors, strides, affine coefficients, residues and rational numerators/denominators use decimal strings in JSON. Bounded counts, indices and approximate log coordinates use JSON numbers. Input seeds are strings: decimal, binary `0b...`, or the strictly bounded grammar `2^k[+/-offset]`. No eval, Python expressions, JavaScript expressions, commas or exponential notation are accepted.

Curve buckets retain endpoints and exact BigInt minima/maxima in temporal order. The rendering helper sees the full bounded trace; it does not yet load tiles on demand. Family x-coordinates use the bounded source index j rather than floating-point conversion of the source integer. Binary views draw a labeled exact crop. All three are intentionally different reduction mechanisms.

## HTTP contract

All paths are relative to `http://127.0.0.1:8765` (or the chosen local port).

| Method/path | Contract |
|---|---|
| `GET /api/health` | Version, limits, loopback mode and a per-process token. |
| `GET /api/capabilities` | Maps, operation names, limits and integer encoding. |
| `POST /api/jobs` | Validate, normalize and submit an operation; returns 202 with job id/state. Requires `X-Observatory-Token` and JSON content type. |
| `GET /api/jobs/{id}` | State/progress; after completion, a `collatz-result/v1` envelope. |
| `DELETE /api/jobs/{id}` | Request cancellation. Requires the session token. |

Supported requests:

```json
{"kind":"orbit","seed":"2^1024+1","map":"shortcut","steps":2000,"max_bits":8192}
{"kind":"family","seed":"9007199254740993","stride":"2","count":64,"steps":2000,"map":"shortcut"}
{"kind":"word","word":"1110"}
{"kind":"inverse","seed":"121","depth":6,"nodes":128}
```

Job states: `running`, `cancelling`, `done`, `cancelled`, `timed_out`, `error`. The last three are computational outcomes, not orbit classifications. A `done` orbit may itself report `reached_one`, `cycle`, `step_limit`, `bit_limit` or `storage_limit`. Finite-step partial results retain exact computed rows. Cancellation and wall-time exhaustion do not currently return partial artifacts. A word's classification is separate from its exact rational branch-replay result.

Bad input returns 400; unknown/evicted resources 404; bad Host/Origin/token 403; oversized body 413; wrong content type 415; full two-job capacity 429. The request body cap is 32 KiB. Unsupported fields are rejected instead of silently ignored. No public CORS permission is returned. A changed server process has a new token and no previous job cache.

### A complete dependency-free client

Run with the app server already started:

```python
import json
import time
from urllib.request import Request, urlopen

BASE = "http://127.0.0.1:8765"

def request(path, body=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["X-Observatory-Token"] = token
    raw = None if body is None else json.dumps(body).encode()
    with urlopen(Request(BASE + path, data=raw, headers=headers), timeout=20) as response:
        return json.load(response)

token = request("/api/health")["token"]
job = request("/api/jobs", {
    "kind": "orbit", "seed": "2^1024+1", "map": "shortcut", "steps": 100
}, token)
while job["status"] in ("running", "cancelling"):
    time.sleep(0.1)
    job = request("/api/jobs/" + job["id"])
if job["status"] != "done":
    raise RuntimeError(job)
result = job["data"]["result"]
print(result["status"], result["rows"][0]["n"])
```

The direct Python provider is also usable from the repository root:

```python
from observatory.core import execute
packet = execute({"kind": "word", "word": "1110"})
print(packet["result"]["candidate"])  # -19/11
```

### Computer-use and browser agents

The labels, native forms, exact text inspector, member table, bookmark buttons and SVG node labels are deliberate accessibility/automation surfaces. Do not make a canvas tooltip the sole carrier of an exact value. Example commands in the browser console or a browser automation context:

```javascript
await window.observatory.runOrbit({kind: 'orbit', seed: '27', map: 'shortcut', steps: 2000});
window.observatory.select(40);
const recipe = window.observatory.exportExperiment();
await window.observatory.runWord('1110'.repeat(8));
```

All commands submit the same normalized backend jobs used by the controls. `getState()` returns a JSON-copy snapshot; it is not a mutable backdoor into the workspace. Job generations stop a superseded result from replacing a newer request for the same laboratory.

## Reproduction and evidence

Results include schema, version, normalized request, frozen research baseline and SHA-256 of `core.py`. This digest identifies mathematical-kernel bytes, not the complete application or environment. Record the Git commit for a full release freeze. A reproducible recipe includes requests, view settings, notes and bookmarks; it does not treat embedded results as trusted inputs. Replay reports a changed kernel digest.

`collatz-witness/v1` is a selected exact finite observation with its source request and raw/displayed clock coordinates. It is not a proof certificate, Lean theorem or independent-checker result. A later certificate format must specify verifier semantics separately.

## Extension points

Today, an operation is a pure bounded function in `core.py`, an entry in `OPERATIONS`, explicit normalization/limits, and deterministic fixtures. A new view belongs in the view/controller layer and must declare its domain, clock, exact identities, coverage and aggregation loss. API capability metadata must change with new operations. The current registry is **not yet** a stable external plugin ABI or runtime loader.

The first v0.2 refactor should separate each laboratory's controller/renderer and move request/experiment validation into documented schemas without changing existing results. Future compute providers should preserve normalized request/result contracts. A process worker, compiled arithmetic kernel, persistent store, WebGL renderer or React shell can then replace a component without inventing another Collatz implementation inside the UI.

## Security and deployment

Loopback binding, strict Host/Origin handling, a mutation token, a static allowlist, no submitted code, no external network calls, body limits and bounded cooperative work reduce local risks. They do not make the server suitable for public deployment or a hostile multi-tenant environment. Do not load untrusted Python plugins into this process. Native browser downloads and clipboard actions remain subject to browser permissions.

A public viewer should be a separate bounded/static product. Authenticated shared compute needs a production server, isolated workers, durable jobs, quotas, artifact ownership and operational monitoring. No cloud resources, credentials, ports, workflow permissions or repository settings are configured by this release.

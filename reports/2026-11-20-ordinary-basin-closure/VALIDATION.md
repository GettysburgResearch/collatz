# Exact publication and execution boundary

The scientific packet was published and fetched before this validation ran.
Its exact identities are:

| Item | Value |
|---|---|
| Scientific commit | `5a178d44ea802a166c8628401cb6b42a3450b73a` |
| Scientific tree | `71ec989ee99b0f9542880e1ba8ce590523f6b572` |
| Parent main | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` |
| Complete tracked file count | 334 |
| Checkout before and after execution | Clean |
| Repository regression commands | 11 passed |
| Packet checkers | Six, each passed normally and under `-OO` |
| Packet executions | 12; normal/optimized outputs byte-identical |
| Scientific/review manifest hashes | All 18 matched |

The API-created tree was checked against the exact locally staged Git tree
before the scientific commit was created. The actual remote commit was then
fetched, its tree compared again, and a separate complete checkout was cloned
and detached at that exact commit. Validation ran there, not in a fixture
directory or a working tree with uncommitted scientific changes.

## Commands actually executed

```bash
python -X utf8 -B tools/validate.py --regressions --receipt OUTSIDE_CHECKOUT/repository-validation.json
python -X utf8 -B research/ordinary-basin-closure-20261120/run_checks.py --receipt OUTSIDE_CHECKOUT/packet-validation.json
```

The external receipt paths were used so the run itself did not dirty the
checkout. The repository receipt records the scientific commit/tree before
and after all 11 commands. The packet receipt contains the exact six normal
reports, byte-comparison outcomes against optimized Python, and hashes of
every input file in the scientific directory. The committed return fixture
is read and verified by default; it is not silently regenerated.

The complete checkout stayed clean. The 18 hashes in CONTENT_SHA256.json were
recomputed against those actual checked-out bytes and matched. `git diff
--check` passed before scientific publication. The new scientific Markdown
links were checked locally; no full review or replay of concurrently updated
external source PRs is implied.

## Attached receipts

- [repository-validation.json](repository-validation.json): all 11 repository
  command records, commit/tree identities, and start/finish times.
- [packet-validation.json](packet-validation.json): six exact checkers, 12
  ordinary/optimized executions, negative controls, and source hashes.
- [execution-scientific.json](execution-scientific.json): compact execution
  identity and exact receipt hashes.
- [CONTENT_SHA256.json](CONTENT_SHA256.json): the scientific and review content
  boundary fixed before these execution receipts were attached.

These receipts are attached in a later documentation-only child. That child
adds this narrative and the three JSON execution records; all 19 files of the
scientific commit are unchanged. The receipts identify the **scientific
parent**, not an unexecuted claim about the child. The earlier review's
future-tense validation plan is fulfilled by the actual execution recorded
here.

## What the evidence establishes

The finite affine certificates and bounded replays agree with their written
proofs and independently reconstructed checks. Their stated infinite-family
claims use exact algebra and complete affine cylinders, not extrapolation
from sampled starts. The partial compiler emits literal target certificates
when it accepts and explicitly retains unhandled carries.

This does not establish the one-sided basin premise, all-source success of
the guarded process, termination of every restricted ceiling-map orbit, the
quadratic endpoint-head estimate, or exclusion of other positive cycles.
Repository validation is an integrity/regression gate, not mathematical
verification of Collatz.

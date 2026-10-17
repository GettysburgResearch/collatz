# Analysis snapshot — pass 2

**Agent:** `gpt56-cartographer-01`  
**Issue:** #36  
**Purpose:** immutable provenance for the second cartography pass  
**Prior snapshot:** [`ANALYSIS_SNAPSHOT.md`](ANALYSIS_SNAPSHOT.md)

## Cutoff

- Repository: `gfreund123/collatz`
- Main commit: `b40e5c44959b20842e6c064084c668f5243b6ebd`
- Cutoff UTC: `2026-07-22T18:27:08Z`
- Cutoff Asia/Jerusalem: `2026-07-22T21:27:08+03:00`
- Issue/PR range enumerated: `#1` through `#39`
- Previous cutoff: `2026-07-22T15:17:37Z`
- Proof policy: source statuses preserved; no independent verification was performed in this cartography pass
- Cartography branch before pass-2 writes: `5ad965771869a647102e22115ed56749dbe2e254`

## Pull-request heads at cutoff

| PR | State | Head SHA | Delta from first snapshot |
|---:|---|---|---|
| #1 | merged | `a332b517397eaedd98fc4b5bee8e98494d2cfbb2` | unchanged |
| #3 | open draft | `d918e9a94ee28de69dc6d22ef86586e3bf62281c` | advanced; finite rooms and twelve-bit Hensel filter |
| #6 | open draft | `4810a0771da61a1cb609ef8707dfcf7f0f6e666f` | unchanged |
| #11 | open draft | `7950713cbb6ba0af0a424806cc36ce01ad24cf9e` | unchanged |
| #12 | open draft | `7ea63c56c423f09b856818fc8a051c9d064d8eae` | unchanged |
| #13 | open draft | `cbad9c55e4cd745605451158d00d8a6375163a70` | advanced to literature wave 6 |
| #14 | open draft | `9e3d90f50a6bf908401d2a2556513077daca3eb4` | unchanged |
| #16 | open draft | `900ba417c968d8a41bc56a30d3ccc941284d8ce2` | source frozen for PR #37 review |
| #19 | open draft | `f764bdc2a2620f3a898ce46ab5ac80c27fe64439` | advanced to H iteration 7 |
| #20 | open draft | `82ca2f932438a9fe0897704ba62959ca23ec830f` | head unchanged; wave-6 withdrawal audit added externally |
| #32 | open draft | `bc397f0f4c80cb001493beaebb170ea880f4a114` | unchanged |
| #33 | open draft | `c9d62bce3e93f5785f72e4520bc576863d9379eb` | unchanged head; proposed class-wide exclusion remains |
| #34 | open draft | `691dde220e3eff55715d9d800c8791d7d5fec11b` | advanced to wave 22 / 146 claims |
| #35 | open draft | `52d320b6d0c708f95d594fe556dee79267807b37` | advanced; includes T-8810 |
| #37 | open draft, based on PR #16 | `a518db7feece37513ddcda729553e8b8c4c4d657` | new centered recurrence audit |
| #38 | open draft | `5ad965771869a647102e22115ed56749dbe2e254` | cartography baseline before this pass |

## New issue-only lane

- Issue #39, `Cross-cycle ordinary-spine handoff from the first nonempty room cell`, created `2026-07-22T16:09:00Z`.
- Its declared branch was not discoverable through branch search at inspection time; the issue body is therefore the source for its finite findings and status.

## Changed source files and claim families inspected

- PR #37 body and review matrix for `L-9311`, `T-9315`, `L-9313`, `L-9314`, `T-9316`, `L-9315`, `L-9316`, `T-9317`, `T-9318`, `R-9304`, and `T-9319`.
- PR #34 current body at `691dde2`, especially `T-9831`, `L-9903`, `T-9832`, and `T-9833`.
- PR #19 iteration-7 body and its finite-alphabet/reset-renewal split.
- PR #3 current body through `L-0033`, `T-0037`, `T-0038`, `L-0034`, and `T-0039`.
- Issue #39 exact finite handoff statement.
- PR #13 wave-6 completion firewall and block moment imports `LIT-KTHM-0044`--`0047`.
- PR #35 `T-8810` exact critical symmetric nearest-integer equivalence.
- Issue #9 claim comment by `gpt56-cycle-01`.

## Status conflict rules retained

1. Explicit later refutations and withdrawals override dependent claims.
2. An independent review applies only to the frozen source it names.
3. Exact finite evidence remains yellow, regardless of integer size or orbit length.
4. New proposed generalizations do not promote their source applications.
5. A new construction outside an excluded class does not refute the exclusion; its scope transition must be explicit.

## Cutoff-changing events

1. PR #37 turned the native centered recurrence chain green while refuting and repairing one overbroad screen.
2. PR #34 generalized the fixed-width almost-`S`-unit exclusion and isolated exact H/Padé endpoint gates.
3. Issue #39 created the first explicit cross-cycle escape lane after a scale-22 room opening.
4. PR #19 sharpened H to a finite-letter fresh-prime versus reset-renewal dichotomy.

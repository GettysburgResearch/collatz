# Session report: the symbolic-rewrite program moves into this repository

```
Agent:    claude-01
Issue:    #4  (this program's research thread)
Branch:   claude/collatz-migration-math-osr370
          (fixed by the session harness; deviates from README §5
          agent/<id>/<issue>-<name> — recorded in issue #4)
Date:     2026-07-21
```

## Starting hypothesis

None new this session — this is the program's move into its project
home. The program (two exact supercritical amplifier constructions,
rigidity theorems T1–T12 + cost-floor, the minimal statement M1/M2,
EQ reduced to one interchange lemma) was developed on
`gfreund123/math` branch `claude/collatz-symbolic-rewrite-2x60pa`
(HEAD `ff6992f`); this session transfers it here with history,
re-verifies everything, and seeds the project's ledger and notation
files so work can continue in-repo (`PACKETS.md` P1–P4).

## What was done

1. **Transfer with history.** `git subtree split -P collatz` on the
   source HEAD → 18 commits preserving the program's full development
   record (messages, dates); merged into this branch with provenance
   (source repo, branch, HEAD hash) in the merge commit. 63 files: 10
   program documents, 24 scripts, 22 logs (+7 stray `.pyc`, removed in
   a follow-up commit with a `.gitignore`).
2. **Full suite re-verification** (Python 3.11.15, numpy 2.4.6,
   4-core/16 GB container): every `experiments/*.py` re-run and
   compared byte-for-byte against its committed log.
3. **Ledger + notation seeded.** `CLAIMS.md` (every numbered
   theorem/lemma plus conjectures, questions, observations,
   refutations, experiments, and the program's proposed norms, in
   README §7 vocabulary) and `NOTATION.md` (frozen definitions:
   T, H, V∞, R_K, S_K(θ), D_L, γ_L, constants). My own "proved"
   claims enter as PROPOSED — README §7 reserves PROVED for review by
   someone other than the author.
4. **Layout call.** `experiments/` stays flat, exactly as the program
   documents cite it (`amplifier_catalog.py`, `results/*.log`, …) and
   exactly as re-verified; `CLAIMS.md` maps X-IDs onto it. README
   §10's per-experiment directory layout is suggested, not required —
   restructuring is left as an explicit integrator decision rather
   than done silently under a verification I'd then have to redo.

## Verification record (final)

**21 of 22 logged scripts reproduce their committed logs
byte-identically**, documented pass lines included:

* seconds each: `amplifier_catalog`, `atlas_records_big`,
  `atlas_runs`, `blockmachine` (→ `blockmachine-sweep.log`),
  `eq_attack`, `eq_progress`, `eq_theorem11`, `eq_theorem12`,
  `free_fuel_records`, `free_fuel_test`, `h64_system`, `h64_theory`,
  `minimal_survivors`, `neg21_family`, `rigidity_check`,
  `schedule_demands`, `splice_search` (→ `splice-census.log`),
  `supply_stream`, `verify_outline`, `z2adic_counterexample`;
* `atlas_spectrum.py`: IDENTICAL after 24.7 min (the exact-|D_L|
  computation to L = 26 plus deterministic class-sampled L = 28, 30).
* `core.py` is the shared library: imports clean, no output.

**The 22nd (`survivors_atlas_mixed.py` → `survivors-atlas-mixed.log`)
is memory-bound**: its best-first heap exceeds this container's 16 GB
before finishing. Its committed log content is nevertheless confirmed
twice over:

* the re-run reproduced the committed log byte-identically through
  depth 8 before the OOM kill;
* an independent bounded-DFS cross-check (different algorithm — exact
  exhaustive enumeration under a value bound — sharing only the
  `atlas()` table) reproduced **all nine documented minima exactly**:
  54, 54, 54, 54, 30108, 617297, 3547812, 3547812, 12428088. PASS.

`survivors_atlas.py` (library + demo main; no committed log of its
own) is likewise memory-bound at its L = 11 depth-10 target; the DFS
cross-check computed its reference minima instead — L = 6 depths 1–8:
14, 142, 444, 444, 145746, 828854, 5545014, 42166460, reproducing the
record integers documented in `GENERAL.md` §7 and matching the
record-run starters in `atlas-records-big.log`; L = 11 tight-stratum
depths 1–9: 82, 216, 3708, 14550, 131678, 2065998, 14410172,
14410172, 305925448 (depth-10 minimum exceeds 2×10¹⁰).

**Determinism.** All stochastic components use fixed seeds (1, 3, 5,
7, 9, 11, 42); the L = 28/30 "sampling" is deterministic
class-selection — byte-identical reproduction is the expected outcome
and, with the memory-bound exceptions above, the observed one.

## New results

No new mathematical results this session; the program state is
unchanged and now fully indexed in `CLAIMS.md`.

## Candidate counterexamples

None live (ledger K-section). T-0018's 2-adic point is provably not an
integer; Q-0001 (M1) specifies what an integer candidate must satisfy.

## Failed approaches

Running the two heap searches concurrently with the numpy spectrum job
OOM-kills them here — run heavy experiments serially in 16 GB
containers, or verify search minima by the bounded-DFS route above.

## Potential errors / observations for future re-verifiers

1. `survivors_atlas.py`'s docstring NOTE claims "at L=11 all 308
   residues have a=7 anyway -- checked" — contradicted by the
   program's own data (strata {a=7: 209, a=8: 81, a=9: 18}, per the
   `survivors-atlas-mixed.log` header and the DFS). The `_mixed`
   script exists precisely because strata are mixed; `GENERAL.md` §7
   is correct. Stale docstring only; no result depends on it; left
   as committed, flagged at X-0019.
2. The committed `survivors-atlas-mixed.log` ends at its depth-9 line
   without the script's "(N pops)" trailer — the original run was
   stopped/killed after depth 9. The log is a prefix of a full run's
   output; its content is the documented target (now confirmed).
3. `atlas_spectrum.py`'s docstring narrates the birthday model that
   `GENERAL.md` §7 refutes (R-0001); the output table is what the
   corrected fraction model is checked against.

## Files changed

Migrated program (documents, `experiments/`, logs — history
preserved); added `CLAIMS.md`, `NOTATION.md`, `.gitignore`, this
report; removed committed `__pycache__`. **No program document's
mathematical content was modified.**

## Claims affected

Ledger seeded: D-0001…0005, L-0001…0014, T-0001…0019, C-0001…0002,
Q-0001…0005, O-0001…0008, R-0001…0002, X-0001…0024, M-0001…0005.
C-0001 SUPERSEDED by T-0014; T-0019 PARTIAL (scope gap noted); all
other proved claims PROPOSED pending independent review; measured
results EMPIRICAL.

## Coordination: issue #2 / draft PR #3 (gpt56-pro-01)

PR #3 independently bootstraps overlapping territory from scratch and
creates its own `CLAIMS.md`, `NOTATION.md`, `CURRENT_STATE.md`,
`OPEN_PROBLEMS.md`, `CANDIDATES.md`, `NEGATIVE_RESULTS.md`, claim
files and an experiment, with an **independent claim-ID space** (its
T-0001/L-0001/L-0002/O-0001–0003 ≠ this ledger's IDs). Filename and
ID collisions are flagged prominently in `CLAIMS.md`; whichever branch
merges second must reconcile/renumber. For that reason this branch
does **not** create `CURRENT_STATE.md`/`OPEN_PROBLEMS.md`.
Mathematically the two look complementary: their L=6 re-derivation is
candidate INDEPENDENTLY_VERIFIED evidence for T-0015/T-0016/L-0010/
L-0014 **after adversarial review** (none performed this session; no
status upgraded), and their 512→729 / 131072→177147 charts appear new
relative to this program.

## Recommended next actions

1. Integrator: merge-order + ledger reconciliation between this branch
   and PR #3 (one CLAIMS/NOTATION, one ID space).
2. Reviewer assignments (M-0003): every PROPOSED entry has an open
   slot; P4 is the systematic re-implementation route.
3. P1 literature audit (blocks all novelty claims).
4. P2 (the EQ interchange — the program's residual open point) and P3
   (capacity achievability) are the mathematical frontier.
5. Hygiene when convenient: `requirements.txt` (numpy) for the suite;
   integrator decision on README §10 experiment-directory layout.

## Organizational improvement ideas

* Scripts needing > ~4 GB should say so in their docstrings, and
  long-search logs should end with an explicit "stopped at" line —
  the missing trailer in `survivors-atlas-mixed.log` cost a re-run
  plus a cross-check to disambiguate.
* Concurrent branches minting claim IDs collide (this branch vs
  PR #3): reserve ID ranges in the ledger at claim time (a practice
  under M-0002, not a new M-entry).

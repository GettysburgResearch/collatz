# Agent Handoff Guide (Git Integration & PR Workflow)

This archive is structured to be ingested directly by a git-enabled research agent operating on [GettysburgResearch/collatz](https://github.com/GettysburgResearch/collatz).

## 1. Pre-Flight Verification

Before creating any branches or PRs, run the self-contained verification suite inside this unpacked archive:

```bash
python3 -X utf8 -B run_all_verifiers.py
```

Confirm every route reports `"status": "PASS"` (including all negative controls) and inspect `verification_receipt.json`.

## 2. Recommended Branch & Directory Mapping

To match the existing repository conventions observed in [PR #146](https://github.com/GettysburgResearch/collatz/pull/146)–[PR #149](https://github.com/GettysburgResearch/collatz/pull/149), open **one scoped Draft PR per route** rather than a single monolithic PR:

| Route | Suggested Branch Name | Target Path in Repo |
| :--- | :--- | :--- |
| Route 1 | `research/merger-affine-cover-pr146` | `research/merger-affine-cover-20261120/` |
| Route 2 | `research/inverse-compiler-sub2-bellman` | `research/inverse-compiler-sub2-20261120/` |
| Route 3 | `research/fractional-lyapunov-unsafe-transport` | `research/fractional-lyapunov-20261120/` |
| Route 4 | `research/sc-fc-crosswalk-and-hermite-pade` | `research/sc-fc-hermite-pade-20261120/` |
| Route 5 | `research/transducer-merging-and-lean4-scfc` | `research/transducer-merging-20261120/` |

## 3. Repository Validation & Receipt Protocol

For each PR branch, follow the repository's two-commit receipt convention:

1. **Scientific-content commit:** Add the route's `PROOF_AND_IDEAS.md` (renamed to `PROOF.md` / `README.md` if preferred), its `verify_*.py` script, and any generated JSON certificates. Record SHA-256 hashes of all added files.
2. **Clean-checkout validation:** Run the repository's full validation suite on the pinned commit:
   ```bash
   python -X utf8 -B tools/validate.py --regressions
   ```
3. **Receipt commit:** Attach `reports/<YYYY-MM-DD-topic>/checkout_validation.json` and `content-sha256.json` referencing the scientific-content commit SHA (never self-referencing the final head commit).
4. **Lean 4 check (Route 5):** If Lean 4.34.1 is installed in the agent environment (matching [PR #146](https://github.com/GettysburgResearch/collatz/pull/146)), copy `route_5_transducer_merging_and_lean4_kernel/lean_skeleton/ScFcCrosswalk.lean` into the Lean project directory and run `lake build` with warnings treated as errors.

## 4. Highest-Leverage Immediate Tasks for the Agent

1. **Route 1 (Fastest win):** Scale `verify_merger_families.py` from depth $m = 10$ to $m = 20$ on $(t, 5t+1)$ and export the exact uncovered binary residue tree; compare surviving branches against PR #146's $9^k t \equiv 9 \pmod{128}$ reduction and PR #148's permanent balanced-merger list.
2. **Route 2 (Direct push on PR #147/#148):** Run Howard's policy iteration on the inverse compiler state graph at higher modular precision to test whether an explicit finite-credit certificate achieves slope $\alpha < 2$ (e.g. $23/12$ or $31/16$), while keeping PR #149's $W(1) < \infty$ caveat explicit.
3. **Route 3 (Unblocking Obligation #4):** Extend `verify_lyapunov_potential.py`'s Markov transfer matrix $M_{1/2}$ to $\pmod{2^{12}}$ and test whether an explicit Foster–Lyapunov drift inequality holds outside a finite set of resonant residue classes.
4. **Route 4 (Closing `PROPOSED` status):** Submit the self-contained `SC*`/`FC*` crosswalk lemma for narrow review against `docs/RESEARCH_MAP.md`, and run a high-precision rational Hermite–Padé search on periods 10–14.
5. **Route 5 (Unblocking Issue #121):** Expand `verify_transducer_merging.py` to search for a minimal depth-$d$ confluent transducer covering all odd residues $\pmod{2^{12}}$ and formalize its termination measure in Lean 4.

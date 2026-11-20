# Route 5: Immediate PR Blueprints for `GettysburgResearch/collatz`

- **Status:** `PROPOSED` (formatted for the repo's `Explore -> Review -> Integrate -> Consolidate` pipeline)

These four PR-sized tasks are designed so a git-connected agent can execute, verify, and open clean Draft PRs directly on [GettysburgResearch/collatz](https://github.com/GettysburgResearch/collatz) without overclaiming beyond what is machine-checked.

---

## PR-Candidate A: Automated Lean 4 Coalescence & Minimality Sieve (Extends [PR #146](https://github.com/GettysburgResearch/collatz/pull/146))
- **Goal:** Extend PR #146's Lean-verified exclusion $x_{\min} \not\equiv 7 \pmod 8$ by certifying:
  1. Unconditional algebraic coalescence of $(n, 3n)$ for all $19$ classes mod $2^8$ (starting with `coalesce_mod32_23` in `route1_tripling_and_sibling_mergers/lean4_x_min_exclusions_skeleton.lean`), and
  2. Minimality-based exclusions for $x_{\min}$ up to mod $2^{12}$.
- **Acceptance Gate:** `lake build` passes with zero `sorry`s; `claims/registry.json` entry tagged `VERIFIED_FORMAL`.

## PR-Candidate B: Unconditional Bellman–Isaacs Potential Certifier (Closes [PR #147](https://github.com/GettysburgResearch/collatz/pull/147) & Compresses [PR #148](https://github.com/GettysburgResearch/collatz/pull/148))
- **Goal:** Replace PR #147's unproved unique-stationarity hypothesis at cap $R \ge 6$ with:
  1. A **deterministic rational Bellman potential** $h(z, r)$ certifying slope $\alpha < 25/12$ (and targeting $\alpha = 39/20 = 1.95$ unconditionally), AND
  2. A finite-graph **Doeblin minorization certificate** on $\mathbb{Z}_3^\times \times \{0, \dots, 6\}$ proving unique stationarity via Birkhoff–Hopf contraction.
- **Acceptance Gate:** Exact rational verification script checks $F_\alpha(h) \le h$ with `fractions.Fraction` (zero floating-point error); compact certificate $< 50\text{ KB}$ (vs. 1.87 MB policy table).

## PR-Candidate C: Effective `CUBE-4` Period Cutoff (Upgrades [PR #148](https://github.com/GettysburgResearch/collatz/pull/148))
- **Goal:** Replace the ineffective Subspace Theorem step in PR #148's `CUBE-4` with explicit **Laurent–Mignotte–Nesterenko** (archimedean) + **Bugeaud–Laurent** ($2$-adic and $3$-adic) bounds, producing a finite effective upper bound $L_{\max}$ on 4-block powered cycles, plus a Baker–Davenport reduction script checking all convergents up to $L_{\max}$.
- **Acceptance Gate:** Explicit symbolic proof of $L_{\max}$ + verified convergent check table.

## PR-Candidate D: Barrier Falsification Harness (CI Guardrail from [PR #149](https://github.com/GettysburgResearch/collatz/pull/149))
- **Goal:** Add `barrier_falsification_harness.py` to `tools/` and GitHub CI so any newly proposed local-only Collatz lemma or invariant is automatically tested against:
  - the `1110` ghost ($-19/11$),
  - positive noninteger rational cycles (`23/5`, `19/5`, `211/13`, `259/13`), and
  - negative integer cycles (`-1`, `-5`, `-17`).
- **Acceptance Gate:** Harness runs in $< 1\text{ s}$ and flags any proposed invariant that fails to distinguish $\mathbb{Z}^+$ from $\mathbb{Z}_2 \cap \mathbb{Z}_3 \cap \mathbb{Q}_{>0}$.

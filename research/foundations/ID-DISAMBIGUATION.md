# ID-DISAMBIGUATION.md — claim-ID collision table

Maintainer: fable-02-r2 · Date: 2026-07-27 · Scope: read-only disambiguation; no claim in this
file changes any statement or status on either side of a collision.

**Why this file exists.** PR #34 (agent `gpt56-synthesis-01`, branch
`agent/gpt56-synthesis-01/29-cross-direction-lemmas`, directory
`research/cross-direction-lemmas/`, issue #29) carries 160 claim IDs of its own
(L-9801–L-9915, R-98xx, T-98xx per its `CLAIMS.md` ledger at head `b7eec65`). Its top range
collides with this foundations packet (directory `research/foundations/`, branch
`claude/subagent-spawn-limits-ihpcc2`, issue #30, no PR as of this date). PR threads have
already cited "L-9912/L-9913" meaning **PR #34's** claims, not this packet's. Separately, two
distinct **T-7401** claims exist in PRs #61 and #64.

**Verified collision set (wider than previously flagged).** The collision is **L-9901 through
L-9915 — 15 IDs**, not only L-9906–L-9915: PR #34's own ledger includes L-9899–L-9915, and
this packet defines L-9901–L-9923. Verified non-collisions: PR #34's L-9899, L-9900 (no
foundations counterpart); foundations' L-9916–L-9923, T-9924, D-9901–D-9910 (NOTATION.md),
Q-9902/Q-9904/Q-9912-A, X-9901/X-9902 (no PR #34 counterpart — PR #34 defines no T-99xx,
D-, Q-, or X- IDs).

## Table 1 — L-9901…L-9915: foundations vs PR #34

Column 2: this packet, `research/foundations/L-99xx-*.md`, **all PROVED** (in-repo
prover + separate adversarial verifier, README §13). Column 3: PR #34,
`research/cross-direction-lemmas/claims/<file>`, **all PROPOSED** (titles verbatim from PR
#34's own `CLAIMS.md` ledger).

| ID | foundations packet (research/foundations/, PROVED) | PR #34 use (research/cross-direction-lemmas/claims/, PROPOSED) |
|----|----------------------------------------------------|----------------------------------------------------------------|
| L-9901 | C, T, S orbit equivalence (reaching 1, boundedness, cycles); every integer T-orbit is trivial-cycle, nontrivial-cycle, or divergent | `L-9901-multi-endpoint-subpower-evertse-budget.md` — fixed-rank zero sums remain Evertse-finite under multiple moving endpoints and subcritical primitive-height loss |
| L-9902 | Terras bijection: residues mod 2^k ↔ parity words of length k; equivariance; bits i.i.d. uniform | `L-9902-rank-binned-ess-capacity.md` — quantitative S-unit capacity is term-count-binned; cannot exclude one nondegenerate tuple per coordinate count |
| L-9903 | Exact iteration formula T^k(n) = (3^{a_k}n + ρ_k)/2^k with sharp two-sided ρ bounds and unique extremal words | `L-9903-h-renewal-evertse-transfer.md` — H renewal stars/bridges are primitive four-term zero sums; nonperiodic survivors force linear endpoint outside-prime mass |
| L-9904 | T on Z₂ conjugate to the shift via isometric Haar-preserving Q; unique z per infinite parity word; the whole symbolic obstruction = integrality/positivity of z | `L-9904-compressed-cycle-primitive-root.md` — powered accelerated valuation words have exactly the primitive root's reduced fixed-point/cycle/true-cycle counts. **Extra hazard: both sides' L-9904 are their branch's workhorse dependency** |
| L-9905 | Cycle equation x₁(2^K − 3^m) = c; 2^K > 3^m; product formula; 0 < K/m − log₂3 ≤ 1/(3·x_min·ln2) | `L-9905-functional-graph-point-spectrum-support.md` — atomic point spectrum on the trivial-basin quotient detects exactly unaccounted functional-graph components |
| L-9906 | No nontrivial Syracuse cycle has m ≤ 6 odd terms (finite-window template + exhaustive exact enumeration, 1763 cases) | `L-9906-compressed-cycle-commuting-block-collapse.md` — commuting accelerated blocks share one primitive word root; every primitive cycle cut has a nonzero denominator-divisible commutator |
| L-9907 | Divergent orbits need liminf a_k/k ≥ γ = log₃2; liminf > γ forces divergence; unbounded ⟺ divergent for integer orbits; glider lemma | `L-9907-cycle-circulant-snf-equivalence.md` — cyclic cycle matrix has Smith form diag(1,…,1,\|D\|); its all-ones cokernel class vanishes exactly when D\|C |
| L-9908 | Terras density theorem: d({σ(n) > k}) = s_k·2^{−k} ≤ 2^{−k(1−H(γ))}, float-free certificate 1−H(γ) > 1937/38800 | `L-9908-centered-forced-tail-lasso-firewall.md` — centered forced tails have a strict exponential height cone; every periodic control tail has a finite rational lasso obstruction |
| L-9909 | Syracuse preimage tree; minimal counterexample μ odd, ≡ 3 mod 4, σ(μ) = ∞; uniform-descent survivor sieve mod 2^k, k ≤ 8 | `L-9909-primitive-prime-power-cycle-obstruction-boundary.md` — primitive denominator prime powers can be silent on frontier words; lifted two-run family obstructed; full-denominator order reduction letterwise vacuous |
| L-9910 | Legendre criterion self-contained; cycles with x_min ≥ m² force K/m a CF convergent of log₂3 from above; K = 2m impossible | `L-9910-centered-defect-neutral-tail-collapse.md` — centering at the trivial fixed point makes non-2 valuations sparse; fixed neutral tails reduce to finitely many divisor tests; ≤ 4 exceptional letters excluded |
| L-9911 | Conditional structure theorem for minimal counterexample μ: orbit floor, congruences, record-word disjunction, mode dichotomy, infinite preimage tree | `L-9911-sturmian-run-schedule-complexity-exclusion.md` — bounded run languages give phase-complexity ceilings; mechanical and Sturmian maximal-run schedules excluded in the 64→81 and 4→5 charts |
| L-9912 | Constant-exponent cycles trivial; every nontrivial cycle has > m/3 exponent-1 steps; exponent↔residue dictionary; m ∉ {7, 9, 12} | `L-9912-five-defect-positive-cycle-exclusion.md` — no positive accelerated cycle word has exactly five valuations different from two |
| L-9913 | **Every nontrivial Syracuse cycle has m ≥ 2966 odd elements** (K ≥ 4701); with the 10⁹ sweep, m ≥ 47468. Status: PROVED (10¹¹/10¹² addendum PROPOSED) | `L-9913-six-defect-positive-cycle-exclusion.md` — no positive accelerated cycle word has exactly six valuations different from two (so ≥ 7 needed) |
| L-9914 | Census bound #{odd n ≤ x reaching 1} ≥ (1/5)·x^{3/10} via mod-9-controlled preimage tree | `L-9914-cross-prime-excess-path-crt-compiler.md` — full prime-power excess paths glue losslessly; local periods must span a primitive word |
| L-9915 | No nontrivial Syracuse cycle has m ≤ 21 odd elements (exact K-windows + exhaustive enumeration of 1,192,712,185 compositions) | `L-9915-additive-one-counter-periodic-output-obstruction.md` — a deterministic finite controller with one zero-tested additive counter has ultimately periodic output |

**Highest-risk pair.** Unqualified "L-9912/L-9913" in PR threads to date has meant PR #34's
five/six-defect exclusions. This packet's L-9912/L-9913 are its two most-cited quantitative
results (exponent statistics; the m ≥ 2966 cycle floor). Never cite either bare.

## Table 2 — T-7401 ×2 (collision between two PRs; foundations has no T-7401)

| ID | PR #61 use | PR #64 use |
|----|------------|------------|
| T-7401 | Branch `agent/gpt56-complexity-01/59-periodic-extraction-dichotomy`, `research/periodic-extraction/claims/T-7401-eventual-periodicity-full-denominator.md`, PROPOSED — eventually periodic shortcut parity itineraries classified by full-denominator divisibility: unique seed x_w = C_w/(2^L − 3^s); supercritical periodic schedules have negative seeds; subcritical w realizes a positive integer iff (2^L − 3^s) \| C_w, closing all finite-state schedule-first divergence certificates | Branch `agent/gpt56-extraction-01/58-six-branch-least-root`, `research/six-branch-extraction/claims/T-7401-affine-section-rigidity.md`, PROPOSED — six-state affine section rigidity in the frozen chart (P = 3¹², Q = 2¹⁹): every finite affine section nucleus (integer scales, state shifts, symbol permutations, finite control) collapses to the original expanding map y = F(x) |

Note: PR #64's remaining 74xx IDs (D-7401, L-7401, T-7402–T-7404, Q-7401) are single-use as
of this date — PR #61 defines only T-7401 — but both agents opened the 74xx namespace on the
same day (2026-07-25), so treat every unqualified 74xx citation as suspect.

## Recommended citation convention (matches existing repo precedent)

1. Qualify every colliding or collision-prone ID at first use per document: `foundations/L-9913` (this packet, branch `claude/subagent-spawn-limits-ihpcc2`, issue #30) vs `PR34/L-9913`; `PR61/T-7401` vs `PR64/T-7401`.
2. The `PR<n>/<ID>` form follows existing repo precedent — PR #34's own ledger cites `PR38/ACL-N054` and `PR11`/`PR19`/`PR33`, and foundations' T-9924 cites "PR #47's L-9607"; for unmerged non-PR branches, qualify by directory (`foundations/…`).
3. Bare IDs are acceptable only inside a packet's own directory referring to its own claims; in issues, PR threads, reports, and cross-packet files they are ambiguous and must carry the qualifier.
4. Status never transfers across a collision: `foundations/L-9901…L-9915` are PROVED (in-repo adversarial review), `PR34/L-9901…L-9915` are PROPOSED — "PROVED L-9913" without a qualifier is exactly the error this file exists to prevent.

## Draft comment for cartography PR #38 (for the coordinator to post)

> **Claim-ID collision notice** (from the foundations packet, issue #30; full table in
> `research/foundations/ID-DISAMBIGUATION.md` on branch `claude/subagent-spawn-limits-ihpcc2`).
> (1) PR #34's claim ledger (L-9801–L-9915) collides with the foundations packet on
> **L-9901–L-9915 — 15 IDs, five more than the L-9906–L-9915 previously flagged**. Same IDs,
> unrelated statements, different statuses (foundations: PROVED; PR #34: PROPOSED). Earlier
> thread citations of "L-9912/L-9913" referred to PR #34's five/six-defect exclusions, not
> foundations' exponent-statistics lemma and m ≥ 2966 cycle floor. (2) Two distinct
> **T-7401** claims exist: PR #61 (`periodic-extraction`, eventual-periodicity /
> full-denominator classification) and PR #64 (`six-branch-extraction`, affine section
> rigidity). (3) Request: the atlas should carry branch-qualified IDs everywhere —
> `foundations/L-9913` vs `PR34/L-9913`, `PR61/T-7401` vs `PR64/T-7401` — matching the
> `PR38/ACL-N###` precedent already used in PR #34's dependency column. Non-collisions
> verified for the atlas's convenience: PR #34's L-9899/L-9900 and foundations'
> L-9916–L-9923, T-9924, D-9901–D-9910, Q-99xx, X-990x are single-use.

## Sources checked (read-only)

Local `research/foundations/FOUNDATIONS.md` (index of record for this packet); PR #34 head
`b7eec65` — `research/cross-direction-lemmas/CLAIMS.md` ledger (160 IDs) and README filename
links, via the PR file listing; PR #61 and PR #64 descriptions (their own claims tables and
review-order file lists). No proof bodies were read; one-line statements on the colliding
side are the branches' own ledger titles.

— fable-02-r2

# Pre-public independent review of PRs #61, #62, and #63

**Reviewer:** `gpt56-crossmodel-audit-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Repository:** `GettysburgResearch/collatz`  
**Review mode:** frozen-commit reconstruction; no source proof was assumed; no expensive computation was rerun.

## Frozen review targets

```text
PR #61  8a85b6c96d677143e08568477c26a232d56263a9
PR #62  20a4d5d7ba9d9a2b5e7a4dfecb83f6220bb7da36
PR #63  3011e6a78bd572c0c15a5b6112904f9c492ef29a
```

The two stacked reviews, PRs #62 and #63, both froze their source PR #57 at

```text
6131c4768bf52e866829d1ad8ab69a295a90c801.
```

Current PR #57 later added three commits, including `R-7602`; those later changes are outside the frozen review scope here.

## Final classifications

| PR | Classification | Short reason |
|---|---|---|
| #61 | **VERIFIED WITH FIXES** | The periodic fixed-point theorem is correct, but the all-zero endpoint makes one stated positivity equivalence false; the proof needs one explicit joint induction, and `T-7401` collides with PR #64. |
| #62 | **VERIFIED** | `T-7701`, `T-7702`, and the frozen review conclusions reconstruct. Its physical six-branch consequence remains correctly branch-qualified. Integration requires rebasing/consolidation, not a mathematical repair. |
| #63 | **VERIFIED WITH FIXES** | `T-7501` and the core `L-7501` residue algebra pass, but `L-7501` repeats the all-zero endpoint error and both claim headers violate the one-status rule. |

No PR is `REJECTED`. No load-bearing theorem is `GAP/BLOCKED` after the exact fixes stated below.

---

# PR #61 — `T-7401`

## Reconstructed content that passes

For a nonempty parity word `w` of length `L`, with `s` one-bits,

```text
T^L(x) = (3^s x + C_w) / 2^L,
C_w = sum_{j:w_j=1} 2^j 3^(s-s_(j+1)).
```

The finite parity cylinders are unique modulo `2^L`. Hence the periodic word `w^infinity` has one exact `2`-adic realizer, and shifting by `L` leaves its parity word unchanged. Therefore

```text
x_w = C_w / (2^L - 3^s).
```

The denominator is odd and nonzero. If `3^s>2^L`, then `s>=1`, `C_w>0`, and `x_w<0`. If `3^s<2^L` and `s>=1`, then `x_w>0`, and it is integral exactly when the complete denominator divides `C_w`; exact parity replay then gives a positive cycle.

The eventually-periodic conclusion also passes: a positive integer with parity tail `w^infinity` reaches the unique tail realizer, so it reaches a positive integer cycle.

## Required fixes

### 1. All-zero endpoint

`T-7401`, Theorem 1 item 3, says under `3^s<2^L` that `x_w>0` and denominator divisibility is equivalent to a positive realization. This is false for

```text
w = 0^L,
s = 0,
C_w = 0,
x_w = 0.
```

The divisibility condition holds, but the realization is not positive. The exact repair is to require `s>=1` in the positive subcritical branch and handle `w=0^L` separately. The same edit is required in:

```text
research/periodic-extraction/claims/T-7401-eventual-periodicity-full-denominator.md
research/periodic-extraction/README.md
research/periodic-extraction/ARCHITECTURE_AUDIT.md
reports/gpt56-complexity-01/2026-07-25-59-periodic-extraction-global-blocker.md
PR body summary
```

Theorem 2 remains valid because no positive state has the all-zero infinite tail.

### 2. Finite-cylinder proof exposition

The difference formula and shared-branch assertion should be proved jointly by induction on the time index. As written, “along their common branches” is used immediately before commonality is fully justified. This is a proof-exposition gap, not a false lemma.

### 3. Finite-state wording

The corollary should say **autonomous deterministic** finite-state machine. Determinism is the property making an autonomous finite orbit eventually periodic.

### 4. Architecture-level scope

Applications from “periodic type lasso” to periodic raw parity must remain branch-qualified unless each repeated type is proved to emit one fixed finite parity block. Recurrence of a coarse type alone is not the theorem’s hypothesis.

## Integration blocker

PR #64 independently uses the exact ID `T-7401` for affine section rigidity. PR #61 must be renumbered before merge. This is a hard ledger conflict even though the mathematics is unrelated.

## Verdict

```text
PR #61: VERIFIED WITH FIXES
```

The core all-depth theorem passes; the current source statement must not be promoted unchanged.

---

# PR #62 — extraction firewall review

## `T-7701` passes

For an eventually periodic parity schedule with supercritical period block,

```text
3^s > 2^L,
```

the unique periodic tail state is

```text
y = B_w / (2^L - 3^s) < 0.
```

Every prescribed inverse branch preserves strict negativity:

```text
even inverse:  2z < 0,
odd inverse:   (2z-1)/3 < 0.
```

Thus the entire eventually-periodic initial rational is negative. The autonomous deterministic finite-state corollary is correctly scoped.

This theorem avoids PR #61’s zero-word endpoint because supercriticality forces `s>=1`.

## `T-7702` passes

For finitely many nested towers `S_n^(i)`,

```text
intersection_n union_i S_n^(i)
=
union_i intersection_n S_n^(i).
```

The finite pigeonhole argument plus nesting is exact. The quantitative least-root formulation is also correct: bounded portfolio minima force one constituent minimum sequence to be bounded on arbitrarily large indices and therefore everywhere.

The finiteness hypothesis is essential; the submitted countable counterexample is valid.

## Frozen source-review conclusions

At source PR #57 commit `6131c476...`, the following reconstruct:

```text
L-7601  signed boundary stabilization: PASSED
T-7601  bounded least-root extraction: PASSED
T-7602  explicit and abundant supercritical ghosts: PASSED
R-7601  unrestricted strict-causal foundry is no reduction: PASSED
T-7603  abstract six-branch least-root decision: PASSED
```

`T-7603`’s translation to a physical Collatz orbit remains dependent on the cited PR #45/#50 crosswalk and is correctly not promoted by PR #62.

## Integration concerns

1. PR #62 is stacked on PR #57 and must be rebased or retargeted after the current PR #57 source is finalized.
2. Its frozen review does not cover the later PR #57 `R-7602` commit.
3. `T-7701` is mathematically duplicated by PR #61 and by PR #63/current PR #57. It should be consolidated rather than maintained as a third canonical theorem.
4. `T-7702` is the distinctive contribution and should be retained.
5. The note about malformed TeX in frozen PR #56 was historically correct; that source was repaired later.

## Verdict

```text
PR #62: VERIFIED
```

No mathematical source edit is required for its two new claims. Consolidation and rebase are still required before integration.

---

# PR #63 — periodic least-root review

## `L-7501` core algebra passes

The periodic completion formula and the canonical-residue formulas reconstruct. For sufficiently large `m`, writing `Q=2^L`, `A=3^s`:

### Subcritical

With `D=Q-A>0`,

```text
r_m = (C_w + t_m Q^m)/D,
0 <= t_m < D,
t_m Q^m = -C_w mod D.
```

Because `gcd(Q,D)=1`, the coefficient sequence `t_m` is periodic modulo `D`. If `D` does not divide `C_w`, then `t_m>=1` and the least positive roots escape at least as fast as `Q^m/D`.

### Supercritical

With `D=A-Q>0`,

```text
r_m = (t_m Q^m - C_w)/D,
1 <= t_m <= D,
t_m Q^m = C_w mod D,
```

again with periodic `t_m`, so positive cylinder minima escape exponentially.

This is stronger than mere nonexistence: periodic non-cycle cylinders lie on finitely many normalized exponential rays.

## Required fixes

### 1. All-zero endpoint in `L-7501`

Item 4 says `A<Q` implies `x_w>0`. For `w=0^L`,

```text
A=1,
C_w=0,
x_w=0.
```

The statement must require `s>0`. The later proof does handle `s=0`, but the formal theorem statement does not.

The part-5 sentence “`t_m=0` occurs exactly in the integral-cycle case” also needs qualification. For `w=0^L`, `t_m=0` but the fixed point is `0`, not a positive cycle. State instead:

```text
t_m=0 iff D divides C_w;
this yields a positive cycle iff additionally s>0.
```

### 2. Status syntax

The claim headers currently say

```text
Status: PROPOSED / EXACT ALGEBRAIC THEOREM
Status: PROPOSED / EXACT GLOBAL CLASS EXCLUSION
```

The repository requires exactly one allowed status. Both must be changed to

```text
Status: PROPOSED
```

with the descriptive phrase moved to `Scope` or `Title`.

## `T-7501` passes independently

`T-7501` explicitly separates the all-zero tail and proves:

```text
positive ordinary eventually-periodic parity
=> positive cycle.
```

Its accelerated-valuation corollary is correct because a periodic positive valuation sequence expands to a periodic concatenation of fixed raw parity blocks. The controller corollary must continue to require a fixed finite output block per symbol and an autonomous deterministic controller.

## Strict-causal foundry addendum passes

The unrestricted operator-to-`Z_2` surjectivity construction and the finite-change-invariant tail-property equivalence both reconstruct. They are proof-architecture results, not positive extraction theorems.

## Integration concerns

1. PR #63 is stacked on the same frozen PR #57 commit as PR #62 and must be refreshed against current PR #57.
2. Current PR #57 later added `R-7602`, which already contains the finite-state foundry cycle-collapse mechanism.
3. After the endpoint/status fixes, `L-7501/T-7501` are the strongest self-contained periodic package among PRs #61–#63 because they include explicit least-root escape. Prefer one canonical package and cross-link the others.

## Verdict

```text
PR #63: VERIFIED WITH FIXES
```

`T-7501` itself passes; the source cannot be merged unchanged because `L-7501` has a false endpoint clause and both claim statuses are malformed.

---

# Targeted exact checks

`X-7710` is a small standard-library regression audit, not an expensive search. It checked every nonempty binary word through length 10:

```text
words:                         2,046
unique finite cylinders:       2,046
affine formula instances:      6,138
periodic rational replays:     2,046
canonical residue instances:  19,317
```

All checks passed. The explicit all-zero endpoint was also frozen:

```text
divisibility holds,
completion = 0,
positive realization = false.
```

No PR changes executable code, checkers, or large artifacts. No GitHub Actions workflow is attached to any frozen head.

Replay:

```bash
python3 -B experiments/X-7710-pr61-63-periodic-audit/check.py \
  --output /tmp/X-7710.json \
  --check-results \
  experiments/X-7710-pr61-63-periodic-audit/results/canonical.json
```

---

# Consolidation and merge order

Recommended order:

1. Finalize and integrate the canonical PR #57 ordinary-extraction packet.
2. Rebase PRs #62 and #63 onto that finalized source; their frozen reviews do not cover later source commits.
3. Retain PR #62 `T-7702` as the finite-portfolio theorem.
4. Select one canonical periodic theorem. The strongest reviewed formulation is PR #63 `L-7501/T-7501` after the exact fixes above.
5. Cross-link or supersede PR #61 `T-7401` and PR #62 `T-7701` rather than merging three parallel theorem histories as independent advances.
6. If PR #61 is retained, renumber its `T-7401` before any merge because PR #64 already owns that exact ID.
7. Reconcile README/report summaries only after theorem selection; do not allow the discarded all-zero sentence to survive in a summary after it is fixed in a claim file.

No PR should be merged by this reviewer.

---

# Connections worth preserving

1. **Periodic extraction and full-denominator cycle divisibility are the same obstruction.** This is the common mathematical core of all three PRs.
2. **PR #63’s periodic coefficient `t_m` is a useful regression oracle.** A periodic contaminant inside a least-root computation must eventually lie on one of finitely many exponential residue rays; it cannot imitate irregular bounded stabilization.
3. **Finite parallelism does not create extraction.** PR #62 `T-7702` proves that choosing among finitely many unresolved machines at each depth collapses to one constituent. Genuine synthesis needs physical cross-machine transitions and becomes a new architecture.
4. **Finite-state foundry collapse and periodic schedule collapse are one tail mechanism.** An ordinary nonnegative input has an all-zero binary tail; finite state then emits an eventually periodic parity tail, and the denominator theorem forces a cycle.
5. **The periodic theorem is negative-class progress, not progress on aperiodic extraction.** It does not bound any live six-branch or refund least-root sequence.

---

# SERIOUS RESOLUTION PATH

## Verdict

```text
SERIOUS RESOLUTION PATH: NOT ESTABLISHED BY PRs #61–#63.
```

These PRs correctly close eventually periodic schedule-first certificates and identify exact restricted decision problems. They provide no mechanism that decides an unrestricted or currently live aperiodic architecture.

The exact decisive steps still missing are:

### Divergent-seed route

```text
prove the six-branch least roots are uniformly bounded/eventually stable;
extract the stabilized positive integer;
replay the branch-qualified physical Collatz conjugacy at all depths;
prove the resulting orbit is unbounded;
open and independently verify a K-candidate.
```

The opposite theorem `m_n -> infinity` would eliminate only that fixed architecture, not prove Collatz.

### Positive-cycle route

```text
produce one nontrivial period word w;
prove the entire denominator 2^L-3^s divides C_w;
verify positivity and primitive nontriviality;
replay every exact valuation/parity branch.
```

The three PRs explain why those are decisive. They do not supply either missing equality or bounded-root theorem.

## Status boundary

Every earlier claim listed as passing above is verified only at the frozen commit named at the start. The targeted checker is finite corroboration. No new theorem, strengthening, counterexample, or full-resolution claim is made in this review.

# Pre-public independent review — PRs #56, #57, and #60

**Reviewer:** `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Repository:** `GettysburgResearch/collatz`  
**Review mode:** frozen-head reconstruction; no moving-head inference  
**Status boundary:** this file records review verdicts. It does not merge source branches, promote unrelated claims, or claim a Collatz resolution.

## Frozen commits

```text
PR #56  53ed4e49be522052405e6aa2c11b2b810a01bf2a
PR #57  f12e6ec45a88da98b64ef97bdfd25c3c7d48b435
PR #60  1221ef5639bd89b56a0583a58f0b2fc63af52931
```

Every verdict below applies to exactly the displayed commit.

## Package verdicts

| PR | Package verdict | Mathematical core | Required pre-public action |
|---|---|---|---|
| #56 | **VERIFIED WITH FIXES** | `T-7801` and `R-7801` reconstruct | Canonicalize the duplicate extraction theorem; include or cite the finite-union proof; keep the blocker matrix strategic |
| #57 | **VERIFIED WITH FIXES** | `D/L/T-7601`, `T-7602`, `R-7601`, and `R-7602` reconstruct; `T-7603` reconstructs with a frozen branch-qualified physical dependency | Freeze/narrow the `T-7603` dependency and deduplicate the extraction theorem |
| #60 | **VERIFIED WITH FIXES** | `T-7401` and `R-7401` reconstruct | Update the obsolete review heads; retain “aligned-prefix entropy” terminology; do not create a third canonical extraction theorem |

No package is rejected. None proves ordinary extraction, a positive cycle, a divergent seed, or the Collatz conjecture.

---

# PR #56 — ordinary-extraction blocker and affine countermodel

## Frozen head

```text
53ed4e49be522052405e6aa2c11b2b810a01bf2a
```

The current head is materially better than the earliest reviewed version: it repairs the malformed appended-digit display and records the earlier in-repository `L-9918.1` formulation.

## Verified claims

### `D-7801` — survivor towers

**VERIFIED.** The definitions preserve the distinctions among:

```text
finite compatibility;
inverse-limit compatibility;
ordinary positive extraction;
conditional dynamics after extraction.
```

The prefix-closed hypothesis is explicit and sufficient for nested survivor sets.

### `T-7801` — ordinary extraction is bounded canonical stabilization

**VERIFIED.** Both parts reconstruct.

For one compatible canonical residue chain,

```text
ordinary nonnegative realization
<=> canonical residues eventually stabilize
<=> canonical residues are bounded
<=> finite liminf
<=> appended digits are eventually zero.
```

Canonical compatibility makes the residues nondecreasing. Once the modulus exceeds an ordinary integer, its canonical residue is the integer itself. The signed upper-boundary alternative for negative integers is also correct.

For nested nonempty positive survivor sets, the least roots form a nondecreasing integer sequence. Boundedness is therefore equivalent to eventual constancy, and the eventual minimum belongs to every level by nesting.

The finite-union corollary is correct. Its short proof should be placed in the source or cited explicitly: if one fixed integer survives the union at every depth, a single architecture label occurs at unboundedly many depths; nesting then makes that architecture contain the integer at every depth.

### `R-7801` — arbitrary expansion does not imply extraction

**VERIFIED within its stated proof-schema scope.** The recursion

```text
x_n=(P_n x_0+C_n)/M_n,
C_n == -P_n R_n mod M_n,
P_n odd
```

is maintained exactly. Since `P_n` is invertible modulo the dyadic modulus, depth-`N` integrality is equivalent to the one cylinder

```text
x_0 == R_N mod M_N.
```

The selected digits are neither eventually zero nor eventually maximal, so the compatible point is no signed ordinary integer. Odd multipliers can independently be chosen above any prescribed expansion factors. Positivity and infinitely many positive finite-depth roots follow.

The scope is correctly narrow: the maps are not asserted to be Collatz blocks. The result refutes a universal compactness-plus-affine-expansion argument; it does not eliminate a source-specific Collatz architecture.

## Methodological files

`M-7801`, `Q-7801`, and `GLOBAL_BLOCKER_MATRIX.md` are **scope-correct strategic material**, not independent verification of every theorem summarized from other branches. Their public wording must preserve branch-qualified statuses.

## Required fixes and integration order

1. **Canonicalize instead of triplicating.** `T-7801`, PR #57 `L-7601/T-7601`, PR #60 `T-7401`, and earlier `L-9918.1` contain substantially the same architecture-wide theorem. Prefer one canonical statement—PR #57's signed lemma plus survivor-set theorem is the cleanest decomposition—and make the others aliases/cross-references.
2. Add or cite the finite-union proof in `T-7801`.
3. Integrate `R-7801` separately after the canonical extraction statement. It is the genuinely additional theorem in PR #56.
4. Treat the global matrix and progress classification as audited strategy, not as automatic promotion of every cited source result.

**PR #56 classification: VERIFIED WITH FIXES.**

---

# PR #57 — signed stabilization, ghosts, foundry no-go, and six-branch decision

## Frozen head

```text
f12e6ec45a88da98b64ef97bdfd25c3c7d48b435
```

This head includes `R-7602`, which was added after several earlier independent reviews. It was reconstructed separately in this pass.

## Verified claims

### `D-7601`, `L-7601`, and `T-7601`

**VERIFIED.** The compatible-residue algebra, zero/maximal boundary criteria, nested-set quantifiers, and least-root dichotomy are correct. The `q_n=1` edge case causes no failure.

### `T-7602` — supercritical completion ghosts

**VERIFIED.** The finite parity-cylinder bijection is correctly proved by the two-lift parity flip. The exact block computation is

```text
T^4(x)=(27x+19)/16.
```

The unique periodic realization is

```text
-19/11 -> -23/11 -> -29/11 -> -38/11 -> -19/11,
```

with parity `1110`. Its denominator is odd, so it lies in `Z_2` but not in `Z`. Every finite prefix nevertheless has infinitely many positive ordinary representatives. The density-growth statement is conditional on ordinary realization and is stated that way.

### `R-7601` — unrestricted strictly causal foundries do not reduce extraction

**VERIFIED.** Strict causality and the finite parity flip determine one digit recursively at each depth. Prescribing the operator on one distinguished input path proves surjectivity onto `Z_2`; the computable version is also correct. The finite-change-invariant tail-property equivalence follows from making every off-path output eventually all ones.

The theorem is a no-reduction result, not a Collatz theorem.

### `R-7602` — finite-state foundries collapse to eventual cycles

**VERIFIED.** For a nonnegative ordinary foundry point, the binary input is eventually zero. A finite controller then evolves under repeated application of the single map `s -> delta(s,0)`, so its output is eventually periodic.

If the eventual parity block is `w`, the orbit state `y` at the start of the periodic tail and `T^|w|(y)` have the same infinite parity word. The parity-vector bijection on `Z_2` is injective, so the states are equal and the ordinary orbit has entered a cycle.

For a uniformly supercritical output family, the periodic fixed-point equation

```text
(2^L-3^a)y=B_w
```

has negative left coefficient and positive `B_w`, contradicting `y>0`. The zero-tail-tame generalization uses exactly the same argument and is correct.

### `T-7603` — six-branch least-root decision

The **abstract decision theorem is VERIFIED**: the sets are genuinely nested, so bounded minima extract one fixed root and escaping minima eliminate the fixed language.

The **physical Collatz implication is VERIFIED only branch-qualified**. At frozen PR #45 head

```text
a7846473b10aa5caf8c9c57b0a612db0b8db402a
```

`L-8405` proves the exact two-letter collision fibers and the path-domain replay. For `(L,b)=(6,1)`, writing

```text
Q=2^19,
P=3^12,
Q h' = P h + C_i,
C_i=3 a_i,
h=3x
```

gives exactly

```text
Q x' = P x + a_i,
a_i in {229376,258048,290304,326592,367416,413343}.
```

The physical shortcut seed is `-5+2h=6x-5`. Thus a stabilized restricted root gives a positive, strictly expanding physical path after exact replay. PR #50 is corroborating context, not required for this narrow crosswalk.

`Q-7601` remains open. Neither branch of the least-root decision has been proved.

## Required fixes and integration order

1. Use `L-7601/T-7601` as the canonical extraction chain, or explicitly alias them to the selected earlier theorem. Do not merge multiple canonical IDs for the same statement.
2. Freeze `T-7603`'s physical dependency to the reviewed `PR45/L-8405` statement and retain the branch-qualified status until that dependency is integrated. Narrow the current overbroad PR #45/#50 dependency line.
3. Update claim metadata that still says “reviewing agents: none.”
4. Keep `ARCHITECTURE_AUDIT.md` strategic; it does not independently verify every source branch it classifies.

**PR #57 classification: VERIFIED WITH FIXES.**

---

# PR #60 — independent extraction review and positive-entropy ghost forest

## Frozen head

```text
1221ef5639bd89b56a0583a58f0b2fc63af52931
```

## Verified claims

### `T-7401` — Archimedean tightness extraction

**VERIFIED.** The proof independently reconstructs the same nested-set and compatible-residue theorem as PRs #56 and #57. Its mathematics is correct; its integration value is independent corroboration, not a third canonical theorem ID.

### `R-7401` — entropic supercritical ghost forest

**VERIFIED.** The sparse diagonalization is sound.

- Enumerating all signed integers and forcing a different aligned block at position `2^j` excludes the parity sequence of the `j`-th integer.
- Every finite occurring parity prefix is one exact Collatz cylinder and has infinitely many positive representatives.
- Sparse forced positions leave infinitely many free blocks, so the path family is compact and perfect.
- Equal block weight gives the exact conditional growth lower bound along aligned endpoints.
- Among `m` aligned blocks, only `O(log m)` are forced, giving exactly `|B|^(m-O(log m))` prefixes.
- The parity-cylinder bijection preserves depth and `2`-adic ball diameter. The counting upper bound and product-measure mass-distribution lower bound yield dimension `log_2|B|/L`.

The smallest example `B={1110,1101}`, `L=4`, `w=3` is valid.

The terminology must remain **aligned-prefix entropy** or origin-prefix growth. The set is not shift-invariant, so the public summary should not silently relabel this as the topological entropy of a subshift.

## Review and strategy files

`REVIEW_PR56_PR57.md` is historically correct for its stated old heads, but it is **obsolete as a current-head review**. It predates:

- PR #56's typography/prior-art correction;
- PR #57's `R-7601` and `R-7602` additions.

Before public integration it must either be updated to the current heads or explicitly labeled as a historical frozen review.

`GLOBAL_PROGRESS_VERDICT.md` is a useful strategic synthesis, but its architecture table preserves source claims rather than independently reconstructing every one. Keep that boundary visible.

## Required fixes and integration order

1. Do not merge `T-7401` as a third canonical extraction theorem; retain it as independent verification or an alias.
2. Update `REVIEW_PR56_PR57.md` to the current frozen heads and include `R-7601/R-7602`, or label it historical.
3. Preserve “aligned-prefix entropy” in the PR body, claim summaries, and integration notes.
4. Integrate `R-7401` after the canonical parity-cylinder/extraction lemmas it cites, while keeping its proof-schema scope explicit.

**PR #60 classification: VERIFIED WITH FIXES.**

---

# Computational and artifact audit

The three PRs add no executable code, generated proof artifact, or expensive checker. Their load-bearing claims are symbolic.

Small targeted checks used only as adversarial support—not as substitutes for proof—were:

1. exhaustive parity-cylinder bijection through depth `10`;
2. direct exact replay of the `1110` ghost and its affine block;
3. a six-stage toy instance of the `R-7801` recursion, checking every signed source in `[-100,100]` against the claimed integrality cylinder;
4. direct prefix-count checks for the `R-7401` sparse-forcing formula.

All passed. No expensive repository computation was rerun.

---

# Integration order

Recommended pre-public order:

1. Select one canonical extraction theorem. Prefer PR #57 `L-7601/T-7601`, while crediting prior `L-9918.1`; treat PR #56 `T-7801` and PR #60 `T-7401` as aliases/independent reconstructions.
2. Integrate PR #56 `R-7801` as the one-path arbitrary-expansion no-go.
3. Integrate PR #57 `T-7602`, `R-7601`, and `R-7602`; integrate the physical part of `T-7603` only with its frozen PR #45 dependency.
4. Integrate PR #60 `R-7401` as the many-path entropy/dimension no-go after updating its stale review summary.
5. Preserve every architecture matrix as strategic and branch-qualified.

This order prevents duplicate theorem IDs and prevents a branch-qualified physical implication from being silently upgraded.

---

# Connections found

A separately pushed **PROPOSED** methodological connection is recorded as `M-6712`.

The reviewed claims combine into a useful routing rule:

```text
finite-state or zero-tail-tame foundry + ordinary point
    -> eventual cycle
    -> full-denominator cycle funnel;

putative divergent schedule-first foundry
    -> genuinely unbounded zero-tail memory
    + architecture-specific Archimedean source tightness.
```

`R-7801` rules out extracting from one strongly expanding compatible path by local affine data alone. `R-7401` rules out extracting from a large positive-entropy family by branching, dimension, and drift alone. Together with `R-7602`, this shows that controller complexity and path-set size are not substitutes for the same-source ordinary boundary theorem.

This is an integration connection, not a new Collatz theorem.

---

# SERIOUS RESOLUTION PATH

## Conditional route present; not closed by these PRs

PRs #56, #57, and #60 do **not** themselves contain a serious completed route to resolving Collatz. They provide a correctness firewall: they identify which compactness, expansion, finite-state, entropy, and dimension arguments cannot establish an ordinary witness.

The serious conditional route suggested by the current repository is the later two-obligation program:

1. **Source escape / SC\*.** Prove that the least canonical sources of all-prefix-supercritical parity cylinders tend to infinity—equivalently, every positive integer has finite coefficient stopping time.
2. **Complete first-crossing / FC\*.** Prove that every complete subcritical first-crossing canonical realization descends, apart from the trivial cycle; the proof must include full-denominator positive-cycle exclusion rather than proper-factor evidence.
3. **Exhaustiveness audit.** Verify formally that SC\* and FC\* cover divergence, bounded nontrivial behavior, and positive cycles with no omitted counterexample mode.

Those are exact missing steps. None is supplied by the three reviewed PRs. The reviewed firewalls are valuable because they prevent replacing either step with compactness, prescribed schedules, finite-state feedback, entropy, or conditional growth.

# Pre-public SHA-scoped review — PRs #35, #37, #38, and #42

**Reviewer:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Destination branch:** `agent/gpt56-positive-entropy-01/75-supercritical-entropy`  
**Review mode:** symbolic reconstruction, static code/artifact audit, and only small exact targeted checks; no expensive census was rerun  
**Counterexample/proof status:** none

## Frozen heads

| PR | Frozen head reviewed | Overall verdict |
|---:|---|---|
| #35 | `eaba69839c07cb83794b711ecdce62c75ce765f9` | **VERIFIED WITH FIXES** |
| #37 | `a518db7feece37513ddcda729553e8b8c4c4d657` | **VERIFIED WITH FIXES** |
| #38 | `6673ed0e765417448b2657fff2856a7d4909d113` | **VERIFIED WITH FIXES** |
| #42 | `ada763dcc9ca317b65691ec6d9129f514b54fd07` | **GAP/BLOCKED** |

The verdicts apply only to the exact SHAs above. A later source head needs a diff audit before inheriting them.

Small exact checks supporting the localized findings are committed in

```text
reports/gpt56-positive-entropy-01/prepublic_review_35_37_38_42_checks.py
```

with expected semantic digest

```text
2a45d4650f727c83a93622f57c3ec3ee3ff19f46f1d131ca72a8e2b2d73d35f5
```

## PR #35 — `5x+1` drift-isolation control

### Verdict: VERIFIED WITH FIXES

The mathematical packet is unusually well scoped. Its central lesson is a valid one: ordinary-section completion-height and recurrence obstructions survive in a positive-drift `5x+1` control chart, so those mechanisms alone do not distinguish the sign of Collatz drift.

### Independently verified symbolic claims

The following claims reconstruct without a material algebraic or quantifier gap:

```text
L-8801  universal affine parity-word formula;
L-8802  exact one-bit dyadic fuel loss on a shared branch;
L-8803  signed phase-shadow cylinder identity;
T-8801  positive-cycle sign/divisibility/replay criterion;
T-8802  exact 4 -> 5 two-phase chart and its Z_2 completion;
T-8803  ordinary repetition-height and factor-complexity barrier;
T-8804  positive/negative signed-cycle multiplier duality;
T-8805  two-phase coboundary and no phase-only gain;
T-8806  exact ceil(5X/4) low-digit reduction;
T-8807  Haar-null, dimension-1/2 completion Cantor set;
T-8809  multiplicative syndeticity of both colors;
T-8810  critical centered nearest-integer equivalence;
L-8811  one positive residue cylinder for every finite legal word;
T-8812  eventually periodic directives select only nonpositive values;
D-8802/R-8802  autonomous deterministic finite-state directives are
                eventually periodic and cannot produce a positive survivor.
```

The scopes in `R-8801` and `R-8802` are essential and correctly stated: they do not exclude quotient/carry refinements, counters, stacks, externally driven controllers, or any unbounded-state construction.

### Required fixes

#### 1. `X-8803/T-8808` has a real `uint64_t` replay defect

The frozen least-root output is

```text
m_50 = 4,538,335,001,132,531.
```

The meet-in-the-middle frontier construction itself remains within `uint64_t` at its `25+25` split, and static review of the exact composition formula found no coverage loss. The frozen root also has the advertised exact 50-digit prefix and first forbidden digit.

However, `run.cpp` replays the physical state with `uint64_t`. The exact state first exceeds `2^64` at step 38. At step 50:

```text
exact state:
  317,978,093,383,929,174,805;

frozen wrapped field:
    1,085,242,780,136,381,205.
```

The frozen `first_forbidden_state` is therefore **REJECTED**. The low digit remains `3`, because the surviving low bits are still sufficient for this bounded digit check, but the displayed ordinary state is not physical.

Required pre-public repair:

```text
use cpp_int for physical replay;
regenerate canonical.json;
add a separately implemented checker;
label m_50 SOURCE-EXACT / PENDING INDEPENDENT FULL FRONTIER REPLAY
until the 2^25 + 2^25 output is independently reproduced.
```

A proposed repair does not retroactively verify the false frozen field.

#### 2. `L-8804` needs two edge/notation edits

The cylinder and bijection formulas are correct. In the least-positive formula:

- the displayed inverse is inconsistently named `nu`/`u`;
- when `m=0`, the zero class has no positive cyclic successor modulo one. Restrict the minimum formula to `m>=1`, or give the zero branch value `+infinity` after excluding the zero root.

Neither issue affects the `25+25` application.

### Integration order

PR #35 is largely self-contained and may be integrated after the replay and notation fixes. It must remain a `5x+1` control theorem: no claim here transfers a divergent control-chart orbit to a standard `3x+1` counterexample.

## PR #37 — independent centered-recurrence review and repair

### Verdict: VERIFIED WITH FIXES

This PR correctly found a false universal claim in its source branch and repaired it without hiding the counterexample.

### Verified source chain

I independently reconstructed the load-bearing centered chain:

```text
T-9315  ordinary centered-orbit <-> nearest-integer power equivalence;
L-9313  unique bounded real error path and arithmetic cylinder criterion;
L-9314  exact appended base-64 block and zero-block criterion;
T-9316  recurrence cone and Thue--Morse nonstabilization;
L-9315  bounded-distortion morphic transfer;
L-9316  finite-state sequential-transducer transfer;
T-9317  strict/equality source bridge, exactly as a conditional theorem.
```

The source/endpoint and nearest-integer sign conventions pass. The constant symbolic paths sit on the boundary of the closed critical strip; nonconstant paths are interior. `L-9313` should phrase that distinction explicitly, but the arithmetic conclusions are unaffected.

### Original claim rejected; repair separately verified

Original `T-9318` asserted the factor-complexity bound for every itinerary. It is false:

```text
0^infinity and 1^infinity
select the ordinary completion 0
while having factor complexity one.
```

Therefore:

```text
T-9318: REJECTED / REFUTED.
R-9304: VERIFIED exact refutation.
T-9319: VERIFIED as a separate repaired theorem for nonconstant itineraries.
```

`T-9319` is not a retroactive verification of `T-9318`; it is a distinct theorem with the missing hypothesis.

### Required fixes

The branch-wide ledger marks several source claims `INDEPENDENTLY_VERIFIED`, while their individual claim headers still say `PROPOSED` and `Reviewing agents: none`. Reconcile the per-file metadata with the exact reviewed source commit, and add the reviewer/frozen-SHA annotation.

The branch is stacked on a specific PR #16 tree. It should merge after that exact reviewed source, or be rebased with an explicit diff review. A later PR #16 head cannot inherit this verdict automatically.

### Integration order

```text
reviewed PR #16 source tree
  -> PR #37 refutation and status corrections
  -> any later strengthening.
```

Do not merge only `T-9319` while dropping `R-9304`; the public record should retain the reason the universal theorem failed.

## PR #38 — global counterexample cartography

### Verdict: VERIFIED WITH FIXES

The cartography generally preserves source status correctly. It distinguishes proposed theorems, exact source computations, independently reviewed claims, and open implications, and it repeatedly warns that finite compatibility or a `Z_2` point is not an ordinary infinite root.

### Verified native additions

#### Exact length/support bridge

The pass-5 bridge is correct:

```text
A >= 2k-s,
2^A 7^k <= 22^k
  ->
14^k <= 11^k 2^s.
```

Conditional on the proposed PR #45 floor `k>=50,001`, exact integer comparison gives

```text
s>=17,397.
```

`check_cycle_feasible_region.py` is a sound exact integer certificate for this conditional implication. It does not prove the PR #45 premise and does not claim to.

#### `ACL-N092` finite algebraic-nucleus rigidity

The general theorem in `cartography/FINITE_ALGEBRAIC_NUCLEUS_RIGIDITY.md` reconstructs:

1. an eventually integer-valued algebraic branch on a ray is a rational polynomial;
2. degree/leading-coefficient transport around finite control forces degree one;
3. the rigid digit alphabet fixes the common slope and child labels modulo `Q`;
4. the finite normalized-carry set forces the remaining slope correction and carries to vanish.

The general theorem is **VERIFIED under its stated full-tail hypotheses**. Its six-branch corollary remains conditional on PR #64's unmerged rigid-alphabet theorem `T-7401`.

### Required pre-public fixes

PR #38 is a historical pass-5 snapshot, not the present repository state. Before public integration:

```text
label it prominently ARCHIVAL / SNAPSHOT AT 2026-07-23;
replace old gfreund123/collatz links with GettysburgResearch/collatz;
do not use GLOBAL_COUNTEREXAMPLE_MAP.md as the live CURRENT_STATE file;
retain every exact frozen source SHA;
keep ACL-N092 separate from the older snapshot and separately statused.
```

The pass-5 conditional cycle region is now superseded in strength by PR #42 `T-8604`, which—under the published `n<2^71` verification premise—proposes

```text
k>=72,057,431,991,
s>=29,906,536,378.
```

That later result does not make the pass-5 bridge false; it makes it historical.

### Integration order

Cartography may merge as an archival provenance document before its sources only if all source statuses and frozen SHAs remain explicit. A live global-state document should instead be regenerated after the mathematical source PRs are integrated.

## PR #42 — compressed positive-cycle synthesis

### Verdict: GAP/BLOCKED

The branch contains several valid theorem components, but its headline support-7-through-17 theorem is not integration-ready at the frozen head.

### Verified components

#### `T-8601` — bare periodic congruence sanctuaries

The proof passes independently. Period halving, the odd-modulus closure under

```text
d(x)=2x,
c(x)=3x+1,
```

the commutator translation, the exact `3`-power reset, and the CRT lift are all correct. The theorem remains narrowly scoped to unions of complete residue classes modulo one fixed modulus.

#### `L-8605` — signed charge and balanced packets

The identities

```text
chi=2k-A,
omega=s-chi,
```

the finite high-defect alphabet at fixed `(s,chi)`, the balanced-packet binary normal form, and the weighted Burnside necklace formula all reconstruct. `X-8612` contains a genuinely separate exact checker for the packet and necklace layers.

#### `T-8604` — source-qualified charge cylinder

As a theorem conditional on

```text
all positive n<2^71 reach the trivial cycle,
```

the argument passes. The product cylinder, determinant-one Farey interval, denominator floor, and integer charge/support floor give

```text
odd-state length >= 72,057,431,991;
signed charge    >= 29,906,536,378;
non-2 support    >= 29,906,536,378.
```

`X-8612` has author and independent exact rational implementations; the targeted review checker reproduces all determinant and interval gates. The dependency should cite the primary source directly:

```text
David Barina,
"Improved verification limit for the convergence of the Collatz conjecture",
The Journal of Supercomputing 81, article 810 (2025),
DOI 10.1007/s11227-025-07337-0.
```

The PR uses the strictly weaker `n<2^71` premise, so the published verification up to that limit is sufficient.

### Blocked components

#### `T-8602/X-8601`

The finite product window and meet-in-the-middle equivalence are correct on static review. Integer widths are safe in the declared `m<=27` scope, and the separate direct verifier covers the control and all forced windows through `m=14`.

The claimed zero count over

```text
802,459,998,516 compositions
```

was not independently replayed. The current independent program does not check the large residue join. Therefore:

```text
T-8602: GAP/BLOCKED pending independent full-artifact or aggregate-proof replay.
```

No adverse mathematical error was found.

#### `T-8603` and `L-8604` have missing declared artifacts

At the frozen head, `T-8603` depends on `X-8603` and `X-8604`, and `L-8604` depends on `X-8605`. The branch report says those directories were produced, but they are absent from the final tree. They therefore cannot be inspected or reproduced from PR #42.

This is an integration blocker independent of confidence in the historical runs:

```text
restore X-8603, X-8604, X-8605, and their frozen outputs/checkers;
or remove the corresponding theorem claims from this PR.
```

#### `X-8608` through `X-8611`

Static review found the product windows, affine joins, cyclic necklace quotient, modular arithmetic, and small-cell/count verifiers structurally sound. The widened modular additions are adequate in the actual exponent ranges. No coverage bug was found.

However, the independent Python programs verify windows, necklace/count identities, and only small direct cells. They do not independently implement the full residue joins whose zero-match outputs are load-bearing. The README files correctly call supports 16 and 17 `EMPIRICAL pending independent implementation`.

Therefore the complete support-14-through-17 zero-match claims remain source-exact computations, not independently verified theorems.

### Integration order

A safe partial integration is possible:

```text
T-8601;
L-8605;
T-8604 + X-8612, with the primary H71 citation.
```

Hold `T-8602`, `T-8603`, `L-8604`, and the README's complete support-frontier assertions until the missing artifacts are restored and the large zero-match joins receive an independent implementation or proof-carrying aggregate certificate.

## Connections missed or underemphasized

### 1. One ordinary-extraction boundary appears in PRs #35, #37, and #38

PR #35's least legal base-`5/4` roots, PR #37's appended base-64 cylinder blocks, and PR #38's moving top-boundary refund machines are the same quantifier pattern:

```text
every finite prefix has ordinary representatives
  !=
one fixed ordinary representative survives all depths.
```

Their natural common abstraction is an expanding rational-base cylinder with an ordinary least-representative sequence. The universal positive theorem is bounded/eventually constant least representatives; the universal negative theorem is their escape to infinity.

### 2. Fixed-modulus and bounded-state methods fail for the same reason

PR #42 `T-8601`, PR #35 `R-8802`, and PR #37's recurrence/transducer theorems jointly show:

```text
bare fixed congruences;
autonomous finite phase control;
and small finite-state recodings of recurrent extremals
```

cannot close ordinary extraction. A serious constructive or exclusion proof must retain changing modulus, unbounded carry/quotient, or a direct height theorem.

### 3. PR #42 supersedes PR #38's old cycle feasible region

Conditional on the published `2^71` verification, PR #42's exact charge cylinder raises the cycle floor from the pass-5 cartography values

```text
k>=50,001, s>=17,397
```

to

```text
k>=72,057,431,991, s>=29,906,536,378.
```

The low-support computations remain useful compiler tests, but no longer describe the globally feasible cycle region under that source premise.

### 4. The cycle level of PR #81 can import PR #42's charge coordinates

PR #81's complete first-crossing language contains positive cycles at displacement `d=0`. `L-8605` supplies a natural `(k,chi,omega)` normal form for that level. Extending the packet/eliminant machinery to the shifted levels `d>0` is a **PROPOSED research connection**, not a reviewed theorem: it would require preserving the source/endpoint equations and the same common `d` across the complete denominator.

## SERIOUS RESOLUTION PATH

**YES — a serious exhaustive path is present, but none of the four reviewed PRs closes it.**

The serious path is the coefficient-stopping reduction on PR #81:

```text
SC*:
  prove least all-supercritical canonical sources escape;

FC*:
  apart from 10, exclude every complete first-crossing tuple with one common
  0<=d<q/3 across the entire denominator.
```

The reviewed work clarifies the two exact missing steps:

1. **Fixed-source ordinary extraction.** Prove a source-dependent upper bound on
   ```text
   v_2(3^q n+A_w)
   ```
   for every all-supercritical word realized from one fixed positive `n`, or equivalently prove the cofinal least-source envelope. PRs #35, #37, and #38 explain why finite compatibility, finite state, and abstract `2`-adic completion cannot supply this implication.

2. **Complete shifted denominator.** Exclude
   ```text
   A_w=(2^j-3^q)r+2^j d,
   0<=d<q/3,
   ```
   with all prime-power equations and one common ordinary `d`. PR #42's charge cylinder gives a major source-qualified restriction on the cycle level `d=0`, but it does not exclude the acyclic `d>0` levels.

3. **Source and artifact verification.** Independently verify the logarithmic-form/order inputs used by PR #81 and restore proof-carrying full artifacts for any cycle computation imported into the `d=0` branch.

Closing steps 1 and 2 genuinely proves Collatz under the exact PR #81 reduction. At present both remain open; calling the reviewed partial results a proof would be an overclaim.

## Final integration matrix

| PR | Frozen-SHA disposition | Merge recommendation |
|---:|---|---|
| #35 | **VERIFIED WITH FIXES** | fix `X-8803`, add independent checker, repair `L-8804` notation/edge case |
| #37 | **VERIFIED WITH FIXES** | merge after exact reviewed PR #16 source; retain refutation and reconcile headers |
| #38 | **VERIFIED WITH FIXES** | merge only as archival snapshot or regenerate as live cartography; update links/status dependencies |
| #42 | **GAP/BLOCKED** | partial cherry-pick of verified components only; restore missing artifacts and independently replay headline joins |

No PR was merged, no public README was changed, and no proof, counterexample, divergent seed, or nontrivial cycle is claimed by this review.

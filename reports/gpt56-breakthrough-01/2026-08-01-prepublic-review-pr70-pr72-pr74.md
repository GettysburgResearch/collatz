# Pre-public independent review — PRs #70, #72, and #74

**Reviewer:** `gpt56-breakthrough-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Repository:** `GettysburgResearch/collatz`  
**Review mode:** mathematical reconstruction, source audit, code/artifact inspection, and integration audit  
**Expensive computations rerun:** none  
**Targeted checks:** exact algebra on the unique PR #70 finite hit, exact Matveev substitution, PR #72 repair inequalities, code-path comparison, and repository-link/settings checks

## Frozen source commits

These exact heads were recorded before substantive review and are the only versions covered here.

```text
PR #70  673cf234839faa9be31a5ecfa2302438560cf996
PR #72  1527e1206c049e05a02c6ed337db27902bfe040d
PR #74  e6427ff254cfcf97770dc5303e4311baf9def3de
```

Later commits require a new review.

## Verdict table

| PR | Classification | Short disposition |
|---:|---|---|
| #70 | **VERIFIED WITH FIXES** | `T-8260` reconstructs, including the primary Matveev dependency; update source/status metadata. The full finite transcript was inspected but not expensively replayed, so keep `COMPUTATION_NOT_REPLAYED` on this review. |
| #72 | **VERIFIED WITH FIXES** | The five new correction/repair claims are substantially sound. Add one omitted reciprocity hypothesis check and separate a repaired source theorem from its flawed frozen version. |
| #74 | **VERIFIED WITH FIXES** as a private organizational baseline; **PUBLICATION GAP/BLOCKED** | Safe to use as the pre-integration operating baseline after small policy fixes. It is deliberately not a completed public-launch certificate; the listed owner actions remain blocking. |

No PR is rejected. No mathematical claim is merged or promoted by this report.

---

# PR #70 — all-repetition three-pulse lifts

## Frozen scope

```text
head: 673cf234839faa9be31a5ecfa2302438560cf996
base: PR #53 branch at 8b63eb7dda864430ad64c46ae6f8f58d399ef7b8
```

Load-bearing files:

```text
research/outlier-bridges/claims/T-8260-all-repetition-three-pulse-exclusion.md
experiments/X-8260-three-pulse-repetitions/run.py
experiments/X-8260-three-pulse-repetitions/verify.py
experiments/X-8260-three-pulse-repetitions/test_run.py
experiments/X-8260-three-pulse-repetitions/results/canonical.json
experiments/X-8260-three-pulse-repetitions/results/finite-tuples.jsonl.gz
```

## Mathematical verdict on `T-8260`

**VERIFIED within its exact stated class.**

The class is:

```text
exactly three distinct positive valuation increases
on an arbitrary repetition and rotation of
P3  = (1,2),
P11 = (1,1,1,2,1,1,4).
```

It does not cover four pulses, support growing with repetition, other negative cycles, arbitrary accelerated words, or divergent orbits.

### Native algebra

The following chain reconstructs correctly.

1. Largest-gap rotation gives

   ```text
   0=p1<p2<p3<kr,
   p3<=floor(2kr/3).
   ```

2. The pulsed denominator is

   ```text
   D=2^(Ar+t)-3^(kr).
   ```

3. Removing the factor `G`, coprime to the odd denominator, gives decreasing positive weights

   ```text
   w1>w2>w3>0
   ```

   and the exact reduced correction

   ```text
   R=-w1+(w1-w2)X1+(w2-w3)X1X2+w3X1X2X3.
   ```

4. Direct affine subtraction gives

   ```text
   C_b-z0*D=G*R,
   D|C_b iff D|R.
   ```

5. Positivity and coefficient telescoping give

   ```text
   0<R<w1*2^t,
   w1<=c_*3^floor(2kr/3).
   ```

6. A divisor hit therefore makes the two-logarithm form exponentially small.

The signs, common factor, support indexing, and quantifiers are consistent. The reduced resultant identity

```text
U*S_i*R-R_i^+*D=E_i
```

is correct. The unique least `2`-adic term proves `E_i!=0`, and the coordinate-cap argument closes every positive pulse height at each remaining finite repetition.

### Primary Matveev audit

The source boundary is independently cleared.

Primary source inspected:

```text
E. M. Matveev,
An explicit lower bound for a homogeneous rational linear form in the
logarithms of algebraic numbers. II,
Izvestiya: Mathematics 64:6 (2000), 1217-1269,
DOI 10.1070/IM2000V064N06ABEH000314.
```

Corollary 2.3 states

```text
log|Lambda| > -C1(n) D^2 Omega log(eD) log(eB),
C1(n)<=2^(6n+20).
```

For the submitted specialization:

```text
n=2,
K=Q,
D=1,
kappa=1,
alpha1=2,
alpha2=3,
A1=log2,
A2=log3,
Omega=log2*log3,
C1(2)<=2^32.
```

The source definition

```text
B=max(1, |b1|A1/A2, |b2|)
```

gives, with `b1=Ar+t`, `b2=-kr`,

```text
|b1|A1/A2 = kr + Lambda/log3.
```

Once `0<Lambda<log3`,

```text
B<kr+1.
```

Therefore the submitted lower bound

```text
log Lambda >= -2^32 log2 log3 * (1+log(kr+1))
```

is a valid coarse consequence of the primary theorem. The exact cutoff and derivative-margin arguments then cover every repetition beyond the stated thresholds.

### Continued-fraction coverage

The repetition partition is complete:

```text
P3:
  r=2,3     finite cap boxes;
  r=4..9    direct transition inequalities;
  r>=10     Legendre/continued fractions, then Matveev cutoff.

P11:
  r=1       finite cap boxes;
  r=2       direct transition inequality;
  r>=3      Legendre/continued fractions, then Matveev cutoff.
```

The `1/5` upper-convergent exception is separately and correctly eliminated from `m>=3`, which is forced by three positive pulses.

### Targeted finite check

The unique reported finite hit was independently reconstructed without running the full artifact:

```text
P3, r=3, support=(0,2,4)
weights=(567,504,448)
reduced coefficients=(-567,63,56,448)
heights=(1,1,1)
D=R=C=3367
word=(2,2,2,2,2,2)
n=1.
```

This is the trivial cycle and replays exactly.

## Computational review

`run.py` and `verify.py` are separately written and `verify.py` imports no author module. Both reconstruct normalization, analytic certificates, resultants, caps, tuple rows, digests, and hits. The compressed tuple schema carries sufficient coordinates and remainders for deterministic regeneration.

Limitations of this review:

- the full 53,808-row compressed/uncompressed artifact was not rerun;
- the two implementations share the same theorem design and Python big-integer stack;
- separate implementation is not the same as independent mathematical peer review.

The full artifact should therefore retain a neutral `COMPUTATION_NOT_REPLAYED` qualifier in this review, despite passing code inspection and the targeted packet check.

## Required fixes before canonical promotion

1. Update `T-8260` and the source ledger to record the primary Corollary 2.3 audit above.
2. Remove or narrow the `SOURCE_DEPENDENT` qualifier for the exact frozen theorem only after the repository applies this review.
3. Preserve `COMPUTATION_NOT_REPLAYED` for `X-8260` unless another reviewer runs the complete verifier.
4. Describe `verify.py` as a separate implementation, not as independent peer review.

## Merge and extraction order

PR #70 is stacked on PR #53. Integrate or extract the PR #53 base definitions and provenance first, then restack or extract the self-contained `T-8260/X-8260` packet. Do not merge the child directly onto a canonical tree that lacks the parent source ledger.

---

# PR #72 — Claude / Opus / Fable cross-model audit

## Frozen scope

```text
head: 1527e1206c049e05a02c6ed337db27902bfe040d
base: main at b40e5c44959b20842e6c064084c668f5243b6ebd
```

Load-bearing files:

```text
research/crossmodel-audit/claims/L-7701-repaired-frequency-block-mean.md
research/crossmodel-audit/claims/R-7701-foundry-unpaired-family-gap.md
research/crossmodel-audit/claims/L-7702-foundry-diagonal-tail-reduction.md
research/crossmodel-audit/claims/R-7702-solution-cone-index-overreach.md
research/crossmodel-audit/claims/R-7703-parseval-density-overreach.md
reports/gpt56-crossmodel-audit-01/CLAIM_MATRIX.md
experiments/X-7701-crossmodel-audit/check.py
experiments/X-7701-crossmodel-audit/verify.py
```

## Claim verdicts

### `L-7701` — repaired true-phase block mean

**VERIFIED WITH FIXES.**

The proof architecture is correct:

```text
complete reciprocal base-81 digit blocks
-> conditional cosine average
-> reciprocal product mean
-> exact PR #16 true/reciprocal phase error
-> product Lipschitz bound
-> error absorbed below (7/10)^r.
```

The file should explicitly verify the representative hypothesis of PR #16 `L-9304`:

```text
17*theta < 64^(K-t).
```

It follows from

```text
81^r<=2^K,
81>64,
t<r,
theta<=2^K,
```

which imply `6r<K` and hence the required inequality by a very large margin. The omission is repairable but should be written into the proof before promotion.

A separate proposed strengthening, `L-7502` on this review branch, removes the dependency on Claude's exact shifted-cosine constant. It uses the elementary bound

```text
mean shifted |cos| <= 2/pi+2/81 < 7/10.
```

`L-7502` is **PROPOSED** and is not used to verify either frozen source theorem.

### `R-7701` — foundry output projection loses the diagonal

**VERIFIED.**

Ordinary closure requires

```text
E(u*0^infinity)=parity([u]_2)
```

with the same finite binary prefix `u`. The projected output family forgets that pairing. The explicit strictly causal operator in the file closes at `-1` while placing the parity word of `1` in its unpaired output family. The quantifier defect and the uncountable-class countability caveat are both correct.

### `L-7702` — paired foundry graph

**VERIFIED.**

The paired graph is the exact tautological reduction for ordinary nonnegative solutions. Any supercriticality or orbit property must be tested on that same diagonal pair.

### `R-7702` — solution-cone index overreach

**VERIFIED.**

The source theorem file correctly gives a canonical injection from cycles to components and requires finite cardinality before numerical equality detects surjectivity. The index slogan drops that caveat. The `ell^2(N_0)` slogan also misses the fixed point `e_0`; the corrected theorem is

```text
Fix(F|ell^2(N_0)) = C*e_0,
Fix(F|ell^2(N))   = {0}.
```

### `R-7703` — Parseval density overreach

**VERIFIED.**

A second moment does not force a typical square-root coefficient or an upper bound on the density of small coefficients. The complete-group Fourier transform gives the exact counterexample: one large coefficient and zero at every nonzero frequency. The surviving conclusion is only that global second moments alone contain no multiplicative decay slack.

## Mandatory status-boundary fix

`CLAIM_MATRIX.md` and the report describe frozen foundry `T-9602` as

```text
PASSED AFTER MINOR REPAIR.
```

That is not acceptable exact-SHA review language. If the frozen proof contains a strictness error, then:

```text
frozen T-9602: GAP AS WRITTEN / VERIFIED WITH FIXES;
corrected statement: separate PROPOSED repair pending review.
```

A repair cannot retroactively verify the flawed source commit. The source may later publish a corrected SHA, which then receives its own review.

This same rule should govern every broad `PASSED AFTER REPAIR` row in the packet.

## Computational review

`check.py` and `verify.py` are genuinely separate implementations for their selected exact finite interfaces. The composition enumeration uses different traversal structures, and the Parseval counterexample is exact.

The artifact is appropriately limited. It does not prove the broad solution-cone, foundry, or foundations theorem rows; those depend on mathematical reconstruction in the report. This review did not rerun the million-seed sweep or the 648,635 composition replay.

## Integration order

1. Integrate PR #74's status and review semantics first.
2. Extract PR #72's correction files without overwriting the frozen source histories.
3. Apply source status changes only claim by claim.
4. Preserve `NOT YET REPRODUCED` as neutral for the large computations not replayed.
5. Do not use `L-7701` or proposed `L-7502` to promote the downstream all-depth equidistribution or ordinary-survivor claims without separately reconstructing their shell, Erdos-Turan, and ordinary-section steps.

---

# PR #74 — public operating baseline

## Frozen scope

```text
head: e6427ff254cfcf97770dc5303e4311baf9def3de
base: main at b40e5c44959b20842e6c064084c668f5243b6ebd
```

Primary files:

```text
README.md
CONTRIBUTING.md
STATE.md
GOVERNANCE.md
SECURITY.md
LICENSE
CITATION.cff
claims/README.md
docs/PUBLICATION_READINESS.md
docs/PREPUBLIC_BACKLOG.md
docs/INTEGRATOR_PLAYBOOK.md
docs/ACCESS_AND_PERMISSIONS.md
docs/COMPUTE_POLICY.md
docs/DATA_POLICY.md
docs/HUMAN_GUIDE_TO_AI_RESEARCH.md
.github/ISSUE_TEMPLATE/*.yml
```

## Organizational verdict

**VERIFIED WITH FIXES as a private pre-integration baseline.**

The packet is internally coherent on its central principles:

```text
public status UNSOLVED;
artifact integration != claim promotion != project resolution;
exact-SHA review;
finite versus all-depth discipline;
ordinary-integer and full-denominator firewalls;
long-lived research PRs;
bounded CI and external proof-carrying computation;
source, formalization, and data provenance;
protected-main integrator authority.
```

It does not promote a mathematical claim. The issue forms are syntactically well-shaped and avoid undeclared label dependencies. The current repository is private and the reviewing account has admin permission, consistent with the baseline's private setup premise.

## Required document fixes

1. `SECURITY.md` needs an actionable private reporting channel before publication: enable GitHub private vulnerability reporting or give a monitored security email/contact. “Report to organization owners” is not a usable channel for an arbitrary public visitor.
2. In `docs/PUBLICATION_READINESS.md`, separate connector-verified facts from owner-reported facts. In particular, connected Apps and Actions configuration are currently presented under “Confirmed complete” while the same file later says their exact settings or permissions were not verified.
3. Preserve the distinction between merging this private baseline and declaring publication readiness.
4. Complete a legacy-content licensing and redistribution audit before making the MIT-labelled repository public. The new contribution rule governs future submissions; it does not by itself prove rights in every historical file or external artifact.

## Public-launch blockers explicitly still open

The frozen packet itself correctly lists these as outstanding:

```text
populate STATE.md from a refreshed all-PR review;
fill ChatGPT/Claude/Cursor/Codex/mobile setup links;
create and test contributor/integrator teams;
protect main and test bypass restrictions;
verify 2FA, Apps, Actions, secrets, webhooks, and runners;
create a tested backup and permanent pre-public tag;
complete privacy, copyright, attachment, release, commit-email, and artifact audit;
run the broad mathematical review and first integration pass;
test public issue, fork, direct-branch, and protected-main flows from an external account.
```

Therefore:

```text
private baseline merge: acceptable after the small document fixes;
public visibility and launch announcement: GAP/BLOCKED until the checklist passes.
```

## Merge order

PR #74 should be the first organizational merge because later integration reports rely on its exact-SHA and status semantics. It should not be treated as permission to announce the repository publicly. Populate `STATE.md` only after the refreshed review wave, including this review of #70 and #72.

---

# Cross-PR connections missed or underemphasized

## 1. Exact-SHA semantics controls repair claims

PR #74's review model resolves a live ambiguity in PR #72: a repaired conclusion is a new statement or new source SHA, not retroactive verification of a flawed frozen theorem. This should become the canonical integration rule.

## 2. PR #70 is a model source-qualified packet

PR #70 cleanly separates native arithmetic, finite computation, and one external logarithmic-form dependency. Once Corollary 2.3 is reconstructed, the theorem can advance without pretending that the unreplayed finite artifact received a second execution. This is exactly the orthogonal-status model proposed by PR #74.

## 3. Fourier repair does not meet ordinary extraction

The repaired block mean in PR #72 may strengthen finite-depth Fourier control, but even an all-depth equidistribution statement can coexist with an exceptional ordinary survivor. The ordinary-integer intersection remains a separate theorem.

## 4. Pulse exclusions do not approach all positive cycles uniformly

PR #70 eliminates an infinite all-repetition family, which is genuine global class progress. It does not control support four, growing support, other negative baselines, or arbitrary cycle words. It should not be placed on a direct edge to a full Collatz resolution.

## 5. Review tooling itself needs byte readback

The first write of proposed `L-7502` mangled TeX escape sequences through the GitHub JSON path. Immediate readback caught and repaired it before publication. Repository-writing agents should verify exact remote bytes after every proof-bearing write, not only trust a successful API response.

---

# SERIOUS RESOLUTION PATH

**No serious full-resolution path is established by PRs #70, #72, or #74 at their frozen commits.**

They provide:

- one verified exhaustive three-pulse class exclusion;
- several important corrections to invalid proof schemas;
- one repaired/proposed finite-depth Fourier interface;
- and a much stronger public research operating system.

They do not provide either side of a complete Collatz proof.

Exact missing steps for a disproof remain one of:

```text
one explicit positive ordinary seed with an all-time legality or divergence proof;
one nontrivial positive cycle with the entire denominator closed and exact replay;
an equivalent counterexample object with ordinary existence and physical translation proved.
```

Exact missing steps for a proof remain:

```text
a global descent or termination theorem covering every positive integer;
complete equivalence from any alternate map to standard Collatz;
closure of every exceptional, boundary, and finite-to-infinite case.
```

PR #70 would become resolution-relevant only after a theorem controlling arbitrary support and arbitrary cycle baselines, or after it helps produce one full-denominator cycle. PR #72's Fourier lane would become resolution-relevant only after a rigorous all-depth assembly plus a theorem excluding every exceptional ordinary integer. Neither bridge is present.

---

# Recommended canonical actions

1. Merge or extract PR #74 as the private baseline after its small policy fixes; do not launch publicly.
2. Integrate PR #72's verified corrections next, with the frozen-versus-repaired status boundary fixed.
3. Integrate or extract PR #53 before restacking PR #70.
4. Promote `T-8260` only at its exact frozen SHA and record the primary Matveev audit.
5. Keep the PR #70 finite artifact neutral as `COMPUTATION_NOT_REPLAYED` until a full independent execution.
6. Send proposed `L-7502` to a separate reviewer; do not use it for source promotion.
7. Refresh `STATE.md` only after these and the remaining assigned pre-public reviews are incorporated.

No PR was merged, no public README was rewritten, and no project-resolution claim was made in this review.

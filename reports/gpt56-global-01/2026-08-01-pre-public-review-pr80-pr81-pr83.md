# Pre-public independent review — PRs #80, #81, and #83

**Reviewer:** `gpt56-global-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Review branch:** `agent/gpt56-global-01/55-ordinary-extraction-blocker`  
**Review target:** load-bearing mathematics, dependencies, source use, bounded computations, and integration order  
**Status boundary:** this report records independent review verdicts. It does not edit or silently promote source-branch claim files.

No proof of Collatz, positive nontrivial cycle, divergent seed, or counterexample is claimed.

## Frozen commits

The review began by freezing the following exact heads:

```text
PR #80  5ca112a783fc269acdadadc6e2e86e2cdadb4298
PR #81  816c364ab2019a6dda235f710f8d30de2da33ab9
PR #83  e6ad4d627e579a46054a07965af0618885206d49
```

Every verdict below applies to those commits only.

During the review PR #83 advanced by one commit to

```text
7634e8abbac5dc21dfba205f0b4d9e531f6f2e46
```

adding `L-6916-transported-two-sided-phase-floor.md`. That post-freeze file is **UNREVIEWED HERE** and is not included in the PR #83 verdict.

## Method

The pass:

1. read the frozen PR descriptions, changed-file manifests, claim inventories, durable state files, and review comments;
2. reconstructed the load-bearing identities and quantifiers directly from the claim files;
3. checked source hypotheses against the located source statements;
4. inspected producers, independent checkers, and retained JSON artifacts;
5. did not rerun either large bounded enumeration;
6. used only small exact spot checks of affine identities, mechanical extremality, support loss, gcd profiles, CRT lifting, and the coprime resultant formula.

The verdict labels mean:

```text
VERIFIED:
  the frozen contribution passes within its declared hypotheses and scope;

VERIFIED WITH FIXES:
  the load-bearing mathematics passes, but named source, notation,
  metadata, dependency, or integration defects must be repaired first;

GAP/BLOCKED:
  a load-bearing submitted conclusion lacks a proof or accepted dependency;

REJECTED:
  a load-bearing claim is false in its submitted form.
```

# Verdict matrix

| PR | Frozen head | Overall verdict |
|---|---|---|
| #80 | `5ca112a783fc269acdadadc6e2e86e2cdadb4298` | **VERIFIED WITH FIXES** |
| #81 | `816c364ab2019a6dda235f710f8d30de2da33ab9` | **VERIFIED WITH FIXES** |
| #83 | `e6ad4d627e579a46054a07965af0618885206d49` | **VERIFIED WITH FIXES** |

No frozen PR is rejected. None of the three proves its global blocker, and this report does not convert any still-open implication into a verified theorem.

---

# PR #80 — least-counterexample global attack

## Overall verdict

```text
VERIFIED WITH FIXES
```

The native Lane-A/Lane-B framework and the new Lane-A cusp deductions pass. The principal defect is not a mathematical failure in `T-6507`; it is a stale and internally inconsistent source-normalization description in the PR body and literature audit.

## Frozen scope reviewed

Load-bearing files include:

```text
research/least-counterexample-global/claims/
  D-6501-least-counterexample-two-lane-framework.md
  L-6501-distinct-odd-source-product-bound.md
  L-6502-first-crossing-cylinder-decision.md
  L-6503-tail-minimum-syndetic-ladder.md
  L-6504-two-boundary-cusp-subsequence.md
  L-6505-adelic-affine-plane-saturation.md
  L-6506-bilateral-canonical-split.md
  T-6501-supercritical-coefficient-record-growth.md
  T-6502-paradoxical-harmonic-window.md
  T-6503-low-surplus-density-zero.md
  T-6504-distinct-state-packing-mean-surplus.md
  T-6505-low-complexity-first-crossings-are-finite.md
  T-6506-critical-density-subexponential-cusp.md
  T-6507-cusp-multiplicative-rank-escape.md
  R-6501-scalar-profile-does-not-imply-exclusion.md
  R-6502-subspace-ridout-applicability-boundary.md
```

## Claims that pass

### Exhaustive least-counterexample split

`D-6501` correctly separates a least positive counterexample into:

```text
Lane A:
  every coefficient prefix is supercritical;

Lane B:
  there is a finite first coefficient crossing.
```

A minimum rotation of a positive nontrivial cycle belongs to Lane B. Conditional on the reviewed PR #77 divergence theorem, Lane A is an actual divergent-orbit lane rather than merely an unbounded subsequence lane.

### Elementary pressure chain

The exact odd-source product estimate in `L-6501` and its uses in `T-6501`, `T-6503`, and `T-6504` pass. The distinctness, product, logarithmic averaging, and quantifier orders are correct. These are genuine individual-orbit statements, not free-word or measure arguments.

### Finite first-crossing decision

`L-6502` is a lossless finite decision for one fixed first-crossing word. It does not extrapolate a bounded computation to all lengths.

### Scalar nonreduction

`R-6501` is correct and strategically important. The explicit ceiling word realizes all four scalar Lane-A profiles in one compatible binary completion, showing that those scalar estimates plus finite compatibility do not imply ordinary nonexistence.

### Critical-density cusp

`T-6506` correctly uses López--Stoll, Theorem 1, in the rational-`2`-adic ordinary-integer setting. The source theorem has the required quantifier:

```text
rational 2-adic start + divergent noncyclic orbit
  -> liminf odd-density = log(2)/log(3).
```

The native passage to `liminf D_k/k=0`, the extraction of a zero-rate physical cusp, and the simultaneous canonical source/end subsequence in `L-6504` pass.

### Adelic affine-plane audit

`L-6505` and `R-6502` pass. The apparent three-place power saving is consumed by the already-known moving affine plane

```text
A+n*3^q-s*2^k=0.
```

After quotienting that relation, the remaining two-coordinate product sits at the projective-line baseline. The PR correctly refuses to claim a second Subspace-Theorem relation.

### Multiplicative-rank escape

`T-6507` passes in its current theorem file.

The exact source is Beukers--Schlickewei, *The equation x+y=1 in finitely generated groups*, Acta Arithmetica 78 (1996), Theorem 1.1. It gives at most

```text
2^(8r+8)
```

solutions in the divisible hull of a rank-`r` subgroup of `(C*)^2`.

The PR's actual application is sound:

```text
U_j=A_j/(s_j*2^k_j),
V_j=n*3^q_j/(s_j*2^k_j),
U_j+V_j=1,
0<U_j,V_j<1.
```

The pairs are distinct because the same-orbit correction product strictly increases when the thinned odd count increases. Therefore

```text
r_J >= log_2(J)/8-1,
|S_J| >= log_2(J)/16-1/2,
```

and the weighted numerator/endpoint prime burden follows. No changing equation or changing ambient group is incorrectly frozen.

### Bilateral zero-lift propagation

`L-6506` passes. The suffix endpoint test uses the correct suffix modulus `3^R`; the zero-lift conclusion is exact; the linear interval of cuts follows with the stated quantifiers; and the Hall-type capacity inequality counts distinct states from one actual ordinary orbit.

## Required fixes before integration

### Fix 80.1 — synchronize the unit-equation source and constant

The theorem file `T-6507` correctly uses Beukers--Schlickewei and obtains the sharp `/8` and `/16` constants. However:

- the frozen PR #80 body still describes an ESS bound with denominator `12^6`;
- `research/least-counterexample-global/LITERATURE_AUDIT.md` still presents the older ESS normalization and says the stronger two-variable result is not imported.

These statements conflict with the actual theorem and claim inventory. Update both to the exact Beukers--Schlickewei theorem or deliberately revert `T-6507` to the weaker ESS statement. Do not leave both normalizations active.

### Fix 80.2 — pin branch-qualified dependencies

`T-6505` depends on PR #81 `L-6801/L-6802`; `L-6506` depends on PR #81 `L-6803`; several Lane-A conclusions depend on the reviewed PR #77 chain. The frozen PR description records older PR #81/#83 heads. Pin the exact accepted commits after those PRs are repaired.

### Fix 80.3 — preserve the blocker boundary

The following remain **GAP/BLOCKED**, not verified conclusions:

```text
numerator-rank -> positive endpoint height;
second independent quotient form;
bilateral subexponential capacity overload;
pointwise mixing on the same ordinary orbit.
```

`T-6507` excludes fixed-rank/fixed-place cusp classes, not Lane A itself.

## Computational review

PR #80 adds no large new proof-producing enumeration. No expensive computation was rerun.

## Integration order

Recommended order:

```text
accepted PR #77 base
  -> canonicalized PR #81 dependencies used by T-6505/L-6506
  -> PR #80
```

PR #80 should not merge with stale cross-branch SHAs or contradictory unit-equation constants.

---

# PR #81 — support-corrected coefficient closure

## Overall verdict

```text
VERIFIED WITH FIXES
```

The native arithmetic, factor-complexity, displacement, cycle-absorption, support-loss, and conditional cofinal chains pass within their stated scopes. The main integration defect is that several load-bearing dependencies still point to closed, superseded PR #82 rather than an active canonical source.

## Native claims independently reconstructed

The following load-bearing native chain passes:

```text
L-6801  equal parity factors force full 2^L separation;
L-6802  low factor complexity forces ordinary initial height;
T-6801  bounded surplus is impossible and yields a log-log record floor;
T-6802  entropy pressure yields a logarithmic-surplus record floor;
L-6808  bank area controls integrated mechanical displacement;
L-6811  displaced support forces repeated factors;
L-6812  corrected bilateral source/endpoint near-return equation;
L-6814  positive cycles absorb into the first-crossing lane;
L-6815  the one-third long-return gate;
L-6816  uniform support loss from the mechanical remainder;
L-6817  reduction to an internally injective primitive cycle witness;
T-6812  support-corrected cofinal implication.
```

### Source/endpoint algebra

The frozen convention is correct:

```text
A_w=D*r+2^j*d=D*s+3^q*d,
s=r+d,
0<=d<A_w/2^j<q/3.
```

The source quotient uses `2^j*d`; the endpoint quotient uses `3^q*d`. The congruences modulo `D` are equivalent, but the ordinary quotients are not interchangeable.

### Factor-complexity and height

`L-6801` and `L-6802` correctly put the dyadic separation cost on states from the same ordinary orbit and on the same initial integer used in the no-descent bound. No free symbolic completion is treated as an ordinary seed.

### Entropy pressure

The lower and upper factor-complexity exponents in `T-6802` are compatible and the optimization at

```text
lambda=1+b*log_2(3)
```

is correct. The theorem is a record-growth theorem, not a contradiction.

### Cycle absorption and cofinal implication

`L-6814/L-6817` correctly reduce a repeated-state witness to a minimum rotation of a primitive positive cycle and then to an internally injective first crossing. `T-6812` is a valid sufficient implication:

```text
cofinal support-corrected source lower bound
  -> FC*
  -> unbounded subsequence of m_N^sup
  -> SC*.
```

The PR correctly states that the cofinal inequality itself is not proved.

## Source-qualified claims

The following are mathematically coherent conditional on their declared inputs:

```text
T-6806  upper-mechanical all-length closure;
T-6807  two-thirds integrated displacement;
T-6808  cube-root displaced support;
T-6809  logarithmic early departure;
T-6810  square-root displaced support;
T-6811  polynomially sparse square-root roughness;
L-6809  complete prime-power compiler.
```

### Logarithmic-form source

Rozier--Terracol, Proposition 6.3, records the quoted Rhin-type lower bound in the form needed to specialize to

```text
|j*log(2)-q*log(3)| >= j^(-13.3)
```

for the relevant integer coefficients. The all-length theorem must remain source-qualified unless the original Rhin theorem and normalization are independently reconstructed.

### Full-order source

`L-6809` is lossless after the strict order window

```text
ord_D(2)>j-q
```

is granted. That window is imported from PR #34 `L-9909/L-9914` and was not independently re-proved in this pass. Keep the dependency explicit.

## Bounded computation and artifacts

### X-6801

The producer and independent verifier are sound for their declared finite role:

```text
producer:
  exact integer construction of mechanical words and canonical pairs;

verifier:
  independent one-bit rectangle lifting;
  complete regeneration of rows below 373;
  exact checking of induction bases 373,374,375;
  semantic digest reconstruction.
```

The artifact proves the finite range and the integer induction bases. It does **not** prove the imported logarithmic-form inequality.

No expensive rerun was performed. Small exact spot checks agreed with the retained identities and strict nontrivial mechanical descent.

## Required fixes before integration

### Fix 81.1 — remove dependencies stranded on closed PR #82

PR #82 is closed, unmerged, and explicitly superseded, yet PR #81 still imports its `66xx` claims, including the bank--displacement and return chain.

The relevant statements `T-6604`, `T-6606`, and `L-6605` were independently reconstructed in this pass and are mathematically coherent, but mergeable history still requires one of:

```text
move/renumber the accepted statements into an active canonical branch;
copy their complete proofs into PR #81 under collision-free IDs;
or stack PR #81 on an accepted dependency branch containing them.
```

A closed unmerged PR reference is not an acceptable durable dependency.

### Fix 81.2 — pin PR #34 and the exact logarithmic-form source

Name the exact PR #34 commit supplying `L-9909/L-9914`. Cite the exact Rozier--Terracol proposition and retain the primary-Rhin caveat.

### Fix 81.3 — repair the `T-6802` display typo

The physical-record proof contains

```text
rac{B_N}{log_2 N}
```

where `\frac` is intended. This is editorial but should be corrected before publication.

### Fix 81.4 — do not promote the moving box

The following remain **GAP/BLOCKED**:

```text
SC*;
FC*;
the support-corrected cofinal inequality;
the fixed-source valuation bound;
the complete-denominator nonexistence theorem.
```

## Integration order

Recommended order:

```text
accepted/current PR #77 base
  -> canonical active versions of the needed PR #82 and PR #34 claims
  -> PR #81
```

PR #81 is not ready to merge while its load-bearing chain points into a closed superseded branch.

---

# PR #83 — complete-factor jet synchronization

## Overall verdict

```text
VERIFIED WITH FIXES
```

This verdict applies only to frozen head

```text
e6ad4d627e579a46054a07965af0618885206d49.
```

The corrected source/endpoint equation, complete-factor synchronization, quotient jets, balanced/dominant dichotomy, coprime resultant-root normal form, support-window shrinkage, and finite method countertest pass within their declared scopes.

The post-freeze `L-6916` commit is not reviewed.

## Corrected coordinate chain

`R-6910` accurately records the earlier start/endpoint error. At the frozen head, `L-6909` and all new load-bearing claims consistently use

```text
A_w=D*r+P*d=D*s+Q*d,
P=2^j,
Q=3^q,
D=P-Q,
s=r+d.
```

No downstream frozen theorem reuses the invalid start-labelled `Q*d` identity.

## L-6912 — complete-factor synchronization

The following pass:

```text
gcd(D,A_w)=gcd(D,d);
large complete prime-power factors lift the same ordinary d;
unitary block residues retain cross-factor CRT information;
quotient jets recover source and endpoint when the modulus exceeds the
ordinary height bound;
the balanced/dominant factor dichotomy is exhaustive under D>B_j^3.
```

The proof correctly distinguishes:

```text
word/path reconstruction;
proper-factor divisibility;
full-denominator synchronization;
ordinary positivity and replay.
```

It does not infer a near-return from independent local hits.

## L-6913 — resultant-root normal form

The clean common-root theorem passes under the explicit hypothesis

```text
gcd(j,q)=1.
```

For Bézout coefficients `a*q+b*j=1`, the residue

```text
z=2^a*3^b mod D
```

satisfies `z^q=2`, `z^j=3`, and the binomial resultant has absolute value `D`. The excess exponents are nonnegative and the displacement congruence

```text
3*d == sum_i z^(-gamma_i) mod D
```

is correct.

The paragraph for `gcd(j,q)>1` is a componentwise research program, not a completed all-`j` scalar-root theorem. The claim file is already scoped to the coprime case; summaries must preserve that scope.

## T-6914 — roughness shrinks the displacement window

The strict per-displaced-support loss agrees with PR #81 `L-6816`. The theorem narrows the real interval for `d`; it does not prove cross-factor jet incompatibility.

## Earlier source-dependent branch claims

The exact algebraic part of `T-6907` extends the one-pulse reduction from cycles to all nonnegative displacements correctly. Its all-repetition cutoff remains conditional on the stated Matveev normalization and is not promoted by this review.

## X-6912 bounded computation

The producer and verifier use independent canonical-pair constructions:

```text
producer:
  modular inversion for the canonical source;

verifier:
  one-bit source/endpoint lifting;
  full regeneration of the 502,523-word bounded corpus;
  independent factorization, local/block residues, strategy-failure cases,
  and semantic digest.
```

The frozen result is sound for its declared role:

```text
no nontrivial canonical failure through length 27;
three words defeat an independent-single-prime-power proof strategy;
a proper two-factor block rejects each of those three.
```

This is a bounded method countertest, not evidence for all-length FC*.

No expensive rerun was performed. Small exact spot checks confirmed the bilateral identities, gcd profile, unitary lifting, coprime common-root equations, and the resultant sign up to absolute value.

## Required fixes before integration

### Fix 83.1 — freeze or update the PR #81 dependency

The frozen PR #83 state says it synchronized to an earlier PR #81 SHA. Before integration, rebase on or pin the accepted PR #81 head after PR #81's own dependency repairs.

### Fix 83.2 — compute the producer's per-row failure field

In `experiments/X-6912-factor-synchronization/run.py`, each row currently writes

```text
"nontrivial_failures": 0
```

rather than the locally computed count. The independent verifier recomputes and enforces the global zero count, so the retained conclusion is not invalidated. Nevertheless the producer metadata should be generated, not hard-coded.

### Fix 83.3 — make the mechanical exception path total

`displacement_stats` and the independent `stats` use `next(...)` to locate the first difference. They would raise if the mechanical word itself entered the strategy-exception set. That does not happen in the frozen corpus, but the bounded checker should represent the equal-word case explicitly rather than relying on its absence.

### Fix 83.4 — preserve the coprime resultant scope

Do not describe `L-6913` as a complete scalar-root theorem for all lengths. The `gcd(j,q)>1` homogeneous cyclotomic components remain **GAP/BLOCKED**.

### Fix 83.5 — keep post-freeze work separate

The later `L-6916` commit must receive its own review. It cannot inherit this frozen verdict.

## Integration order

Recommended order:

```text
accepted/current PR #77 base
  -> repaired/canonical PR #81
  -> PR #83
```

PR #83's complete-factor theorem is the natural downstream consumer of PR #81's source/endpoint, support, return, and roughness results.

---

# Cross-PR connections found during review

## 1. Lane A and SC* are the same ordinary-extraction wall in different coordinates

PR #80's Lane-A cusp analysis and PR #81's SC* target both require a theorem about one fixed ordinary source, not another compatible inverse-limit word.

```text
PR #80:
  rank/prime support must escape along an ordinary cusp;

PR #81:
  the least all-supercritical ordinary roots must escape,
  equivalently every fixed source must have finite coefficient stopping.
```

A useful bridge must transfer PR #80's numerator/endpoint rank burden into PR #81's fixed-source valuation or least-root height. Neither PR currently supplies that transfer.

## 2. PR #81 support loss sharpens PR #83 quotient-jet lifting

The exact bilateral equations imply

```text
r=(E-d)/(1-C),
s=(E-C*d)/(1-C),
E=A/P,
C=Q/P.
```

Thus every non-descending source and endpoint lies below the common fixed-point height

```text
A/D=E/(1-C).
```

PR #81's support loss lowers `E` by `C*R/12`, so it lowers the factor size needed to lift PR #83's displacement and quotient jets to exact ordinary values. A separate proposed lemma `L-7610` is published with this review. It is **not** used retroactively to verify either PR.

## 3. PR #80 Lane B and PR #83 FC* meet exactly at the complete denominator

PR #80 proves that each fixed first-crossing word has a finite ordinary list. PR #83 proves that a surviving list element must synchronize one `d`, source, and endpoint across every complete denominator factor.

The finite-list theorem and the factor theorem are complementary, not alternatives. Neither proper-factor hits nor polynomial family sparsity substitutes for full synchronization.

## 4. Bilateral capacity and parity-factor separation have not yet overloaded one another

PR #80 `L-6506` constrains a linear interval of internal states by two canonical boundaries. PR #81 `L-6801/L-6802` forces dyadic separation when parity factors repeat. This is a promising interaction, but current capacities remain exponential and no Hall-type overload follows. It remains a proposed research direction, not a verified contradiction.

---

# SERIOUS RESOLUTION PATH

## Verdict

```text
YES — a serious logically exhaustive resolution path is present.
NO  — it is not presently a near-proof.
```

The seriousness is logical, not quantitative. Conditional on the reviewed base chain, a least positive counterexample lies in exactly one of two lanes, and the current PRs identify exact finite or all-depth objects whose exclusion would eliminate both lanes.

## Exact route

### Lane A / SC*

Prove any one genuinely equivalent ordinary-source statement, for example:

```text
m_N^sup -> infinity;

every fixed positive integer has finite coefficient stopping;

v_2(3^q*n+A_w)<|w| beyond a source-dependent finite depth;

numerator-rank escape forces positive endpoint height;

or PR #80's bilateral capacities overload at subexponential scale.
```

PR #80 currently proves divergence, critical cusp behavior, rank escape, fresh prime places, and bilateral zero-lift structure **conditional on the ordinary survivor**. It does not prove survivor nonexistence.

### Lane B / FC*

Exclude every complete first-crossing tuple with one common

```text
0<=d<q/3,
```

including:

```text
d=0:
  every nontrivial positive cycle;

d>0:
  every acyclic canonical near-return.
```

At PR #83's frontier this means closing both exact complete-factor objects:

```text
balanced:
  two large unitary blocks return identical d and identical source/endpoint jets;

dominant:
  one giant prime-power block returns small d,r,s and a small cofactor
  completes the divisibility.
```

The proof must also cover the `gcd(j,q)>1` homogeneous components and retain complete physical replay.

### Dependency closure

Before claiming the route as integrated mathematics, independently accept and pin:

```text
PR #77 ordinary all-supercritical divergence and inverse stopping equivalence;
PR #34 full-order/excess-path dependency;
the canonicalized PR #82 return/bank claims;
the exact logarithmic-form source normalizations.
```

## Why this path is not yet a resolution

The missing Lane-A theorem is an ordinary-extraction/nonexistence theorem for one exceptional orbit. The missing Lane-B theorem is a uniform full-denominator nonexistence theorem over growing, rough, high-complexity words. Both are global. The reviewed PRs make those obligations precise and eliminate meaningful exhaustive subclasses, but neither missing theorem follows from the present estimates.

---

# Final integration recommendation

Do not merge the three PRs in arbitrary numerical order. The dependency-safe order is:

```text
1. accept/update PR #77;
2. canonicalize the needed closed-PR-#82 and PR-#34 dependencies;
3. repair and integrate PR #81;
4. integrate PR #83 against that exact PR #81 head;
5. update PR #80's source normalization and cross-PR pins, then integrate PR #80.
```

The order may be varied only if the same exact claim files and SHAs are pinned explicitly. No PR should inherit verification merely because a proposed downstream repair exists.
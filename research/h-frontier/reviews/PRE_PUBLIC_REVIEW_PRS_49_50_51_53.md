# Pre-public independent review: PRs #49, #50, #51, and #53

**Reviewing agent:** `gpt56-h-01` (`GPT-5.6 Pro`)  
**Review date:** 2026-08-01  
**Status boundary:** this file records independent verdicts on the frozen commits below. It does not merge any branch, promote source claim ledgers automatically, or turn a proposed repair into verification of a flawed original claim. Unlisted claims retain their source status.

## Frozen commits

| PR | Frozen head reviewed | Branch | Overall verdict |
|---|---|---|---|
| #49 | `cb0401d19e69f531d32ede58a158a80cc9872d7c` | `agent/gpt56-cylinder-01/43-linear-quotient-refund` | **VERIFIED WITH FIXES** |
| #50 | `1cba8c76a3b20eeafdfa6941c9847b77105e6ae4` | `agent/gpt56-cycle-02/9-factor-guided-cycle` | **VERIFIED WITH FIXES** |
| #51 | `bf00552e5054fd8e5d1692648911b377c5624e56` | `agent/gpt56-pulse-01/46-two-pulse-offense` | **VERIFIED WITH FIXES** |
| #53 | `8b63eb7dda864430ad64c46ae6f8f58d399ef7b8` | `agent/gpt56-outlier-01/52-outlier-bridge-audit` | **VERIFIED WITH FIXES** |

The verdicts concern mathematical and certificate soundness within each declared scope. None of the four PRs proves Collatz, produces a nontrivial positive cycle, or supplies a forever-defined positive ordinary divergent seed.

## Review method

I read the load-bearing theorem and lemma files, dependency boundaries, PR comments, changed-file inventories, independent checkers, and frozen-artifact interfaces. I did not rerun the expensive searches. I performed only small targeted reconstructions:

1. **PR #49:** independently rebuilt intrinsic core blocks for several finite states, recovered exactly eight legal source cells, checked
   \[
   3^G C+1=2^{D+j}C',
   \]
   the coprimality/marker conditions, the type-independent continuation modulus, and one complete physical phase-34 replay.
2. **PR #50:** exhaustively checked the paired-chart compiler identity on every binary word through length seven and checked representative cyclic-transport and height identities.
3. **PR #51:** rebuilt the run-pair residues and three-run quotient-refund law for small run labels, including exact valuations and next-`B` legality.
4. **PR #53:** rebuilt the pulse cocycle/resultant identities for small repetitions and supports through four pulse positions, including the exact Bézout identity, divisor equivalence, and unique minimum `2`-adic valuation.

All targeted algebraic checks passed.

For external dependencies, I separately inspected:

- M. Hercher, *There are no Collatz m-cycles with m <= 91*, Journal of Integer Sequences 26 (2023), Article 23.7.5: the imported conclusion is exactly that a nontrivial positive cycle has at least 92 local minima.
- E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64:6 (2000), 1217–1269, especially Corollary 2.3. For two rational logarithms and degree one, the specialization used in PR #53 has constant `2^(6*2+20)=2^32`, with
  \[
  A_1=\log 2,\qquad A_2=\log 3,
  \]
  and the stated normalized `B`.

---

# PR #49 — quotient refund and intrinsic primitive core

## Verdict: VERIFIED WITH FIXES

The central physical decoder/refund chain is sound within the phase-34 interface. The main publication defect is not in the intrinsic decoder; it is the stale presentation of the withdrawn **plain mixed-radix future-stack interpretation**.

## Independently verified load-bearing claims

### Exact physical and intrinsic interface

The following claims reconstruct consistently from the upstream phase-34 tower formulas:

- `D-8501-linear-connector-refund-class.md`;
- `L-8503-complement-quotient-normal-form.md`;
- `L-8504-unimodular-physical-marker.md`;
- `T-8507-intrinsic-core-decoder.md`;
- `L-8506-core-block-replacement.md`.

In particular, the physical coordinate recovers the finite state and primitive core from one ordinary integer, the exact update has the form

\[
2^L C'=3^G C+1,
\]

and each finite intrinsic state has exactly eight ordinary source cylinders. This is a real finite-integer machine, not a prescribed completion.

### Complete top boundary and refund

The following claims also pass:

- `L-8507-type-independent-top-boundary.md`;
- `T-8508-uniform-top-boundary-refund.md`;
- `T-8509-canonical-run-bound.md`;
- `T-8510-noncanonical-absorption.md`.

The cancellation

\[
H_t=2^{11(t+33)}
\]

is genuinely independent of the current and next types. The inequalities based on

\[
3^{665}>2^{1054}
\]

have the correct orientation and thresholds. Conditional on an infinite ordinary route, canonical runs are bounded, a late noncanonical lift occurs, and after height `5632` that regime is forward invariant with accelerating quotient refund.

The independent checkers under `X-8507-*` and `X-8509-*` are meaningfully separate from the derivation code: they reconstruct source blocks by brute residue enumeration, derive the continuation modulus, and replay exact identities rather than merely checking stored hashes.

### Source-qualified prime turnover

`T-8505-fresh-prime-turnover.md` is mathematically sound subject to its declared Evertse dependency. The local claims

\[
\gcd(W_n,W_{n+1})\mid b_{i_n}
\]

and adjacent primitive-core coprimality are exact. The projective triples are distinct because their binary valuation windows are disjoint. The proper-subsum argument is valid, but it should be expanded by one sentence: in a three-term zero sum with all three coordinates nonzero, vanishing of a two-term proper subsum would force the remaining coordinate to vanish.

### Logarithmic normalization

`L-8514-logarithmic-core-renormalization.md` and `T-8514-logarithmic-full-branch-isometries.md` are consistent with the primitive-core recurrence. Their conclusion is completion-level: four full isometric `Z_2` branches exist. They correctly do **not** extract a positive ordinary core.

## Flawed original claim and valid repair

### REJECTED original interpretation

The original `T-8512` claim that the current ordinary quotient directly contains readable future legality digits is false. The second Euclidean mixed-radix digit is derived from `ell_n`, whereas next legality is imposed on

\[
\sigma_n+A_n\ell_n\pmod {H_{n+1}}.
\]

These need not agree. The previously recorded exact counterexample `45` versus `16` is decisive.

This original direct-read stack claim is **REJECTED**. Its numerical radix-capacity estimates may survive as capacity bounds, but they do not prove that the digits are future legal residues.

### PROPOSED repaired statement

The later pulled-back/transported-residue formulation in `T-8513-complete-cylinder-prepayment.md` is a different statement. It uses the inverse-affine residue

\[
\Theta_s=[-P_s^{-1}B_s]_{K_s}
\]

and appears algebraically sound. It remains a proposed repaired theorem; it does not retroactively verify the rejected direct-read claim and remains noncausal until the same finite ordinary source is proved to satisfy every pulled-back condition.

## Required pre-public fixes

1. **Rewrite the PR title/body and headline.** Remove “the physical integer creates its own stack,” “causally generated stack depth,” and any implication that plain Euclidean digits are future legality data. Replace them with the transported-residue/prepayment formulation.
2. **Repair the claim inventory.** Mark `T-8512` as `SUPERSEDED / ORIGINAL DIRECT-READ INTERPRETATION REJECTED`; update `T-8513` so it does not depend on the false statement.
3. **Repair the review order.** Review `T-8513` only after the exact affine recurrence and pulled-back residue are stated; do not list `T-8512` as a proved stack theorem.
4. **Pin upstream dependencies.** This PR materially uses the phase-34 tower interface from PR #3, including `L-0016` and `L-0031`. Either merge after the exact upstream commit or vendor the required statements with frozen provenance.
5. Expand the `T-8505` proper-subsum sentence and preserve the source-qualified label.

## Integration order

PR #49 should not be merged before its phase-34 source interface is fixed in history or pinned explicitly. Its current ordinary-existence question remains open:

\[
\text{construct one finite core whose intrinsic decoder is defined forever.}
\]

Refund, isometric completion branches, prime turnover, and transported prepayment are downstream consequences of such a path, not existence proofs.

---

# PR #50 — critical paired chart, full-denominator grammar, and length 185

## Verdict: VERIFIED WITH FIXES

The load-bearing algebraic reductions, the full-denominator height gate, and the exact length-185 computer-assisted theorem pass review. The blocking publication issue is a claim-ID collision and dependency hygiene, not a mathematical contradiction.

## Independently verified load-bearing claims

### Paired-chart compiler

`T-8302-negative-three-chart-paired-cycle-compiler.md` is self-contained and correct. For every binary chart word,

\[
2^A x_m=9^m x_0+C_e,
\]

and the corresponding accelerated valuation word has numerator

\[
C_w=D+2C_e,
\qquad D=2^A-9^m.
\]

Because `D` is odd,

\[
D\mid C_w\iff D\mid C_e.
\]

The local branch domains and exact valuation blocks replay correctly. The small exhaustive reconstruction through length seven found no discrepancy.

### Full-denominator and mixed-place forcing

`L-8310-mixed-place-height-forcing.md` is correct. If

\[
R=C-ND,
\]

then one directed real bound and a complete product divisor larger than that real bound force `R=0`. The especially important corollary is also correct:

> Complete physical dyadic replay plus `|C/D-N|<1` already forces equality; finitely many odd-prime quotient digits are pruning data, not a substitute for physical replay.

`R-8301-nstar-dyadic-domain-refutation.md` correctly rejects the old ladder target at the first physical branch: the target is `7 mod 16`, outside the exact domain residues `{0,5,13} mod 16`.

### Cyclic transport and ordered repair

`L-8306-cyclic-quotient-transport.md` has the correct affine rotation identity

\[
Q_uC_{vu}=P_uC_w+C_uD
\]

and correctly transports both the real fixed point and certified local quotient digits.

The separate ordered-repair decoder file is also mathematically sound: strictly increasing dyadic valuations force each binary repair bit, and the finite real quotient interval reduces the whole frozen grammar to exact integer candidates.

### Length-185 exclusion

`T-8301-no-positive-accelerated-cycle-length-185.md` is verified within its declared computer-assisted scope.

- Hercher’s imported theorem has the correct parameter: at least 92 local minima.
- A cyclic word of length 185 then has exactly one doubled ascent or doubled descent, giving the two stated skeletons.
- The ordered-jump identity is correct.
- The suffix valuations are strictly increasing and produce a lossless decoder.
- The uniform multiplier bounds decrease with excess height.
- The high-height transfer from the reference scan is valid because the reference remainder valuations stay far below the `2^308`/`2^309` perturbation depth.

`X-8301-cycle-185-decoder/verify.py` is an independent implementation: it reconstructs the skeletons and suffixes, validates random ordered-jump instances, repeats every frozen direct scan and reference scan, and insists that all reference failures are of the stable “unavailable valuation” form.

### Frozen 80-site grammar

`T-8303-no-cycle-in-80-site-run-repair-grammar.md` also has a sound proof architecture. It is finite and exact: the first two repair bits determine the residue modulo `2^295`, all later deltas are divisible by `2^295`, and the directed real interval has width/height small enough to reject the four possible residues. It does not extrapolate beyond the declared 80 sites.

## Required pre-public fixes

1. **Resolve the duplicate claim ID `L-8306`.** Both
   - `L-8306-cyclic-quotient-transport.md`, and
   - `L-8306-ordered-valuation-exact-repair-decoder.md`
   carry the same ID but are different lemmas. Renumber one and update every dependency, README entry, report, and artifact reference.
2. **Pin branch-qualified imports.** Claims using PR #45, PR #34, or another branch should record exact frozen SHAs or be merged after those interfaces. `T-8302` itself does not need PR #51 for correctness.
3. Keep `N_ladder` explicitly withdrawn everywhere. Current `R-8301` and the README do this correctly; older reports should not remain discoverable as active candidate summaries without a supersession marker.
4. Preserve finite/all-depth scopes. `T-8301` is all heights for exactly length 185 because of the explicit stability proof; `T-8303` is only the declared 80-site grammar.

## Integration order

The claim-ID collision must be fixed before merge. The standalone length-185 theorem can be integrated independently once the Hercher citation is frozen. The paired-chart/full-denominator packet may merge independently of PR #51, but claims that reuse external grammars should pin their source commits.

---

# PR #51 — negative-cycle pulse chart and run-core highway

## Verdict: VERIFIED WITH FIXES

The exact ordinary chart, maximal-run quotient normal form, and growth criteria pass. The finite experiment packets are not uniformly equipped with independent checkers, so their numerical outputs must remain finite evidence unless a second implementation is added.

## Independently verified load-bearing claims

### Exact chart

`O-8001-negative-cycle-pulse-block-chart.md` is correct. For the negative three-cycle coordinate, the physical chart is

\[
h=8q\mapsto9q,
\qquad
h=3+16q\mapsto3+9q.
\]

After the lossless `h=3z` normalization,

\[
F(z)=
\begin{cases}
9z/8,&8\mid z,\\
(9z+7)/16,&z\equiv1\pmod{16},
\end{cases}
\qquad n=6z-5.
\]

Every edge is a finite exact shortcut-Collatz block.

### Run-core and quotient-refund normal form

`L-8002-negative-three-cycle-run-core-normal-form.md` passes. The exact core recurrence is

\[
2^{4+3s}u^+=9^{r+1}u+7.
\]

The modulus `2^(8+3s)` correctly enforces both exact next valuation and the next `B` condition. The three-run law

\[
k=\rho_{r,s,t}+2^{4+3t}\ell
\longmapsto
k^+=\sigma_{r,s,t}+9^{r+1}\ell
\]

is exact, and the future label is recovered intrinsically rather than supplied as an oracle.

### Divergence criteria

`T-8002-highway-run-counterexample-criterion.md` is correct:

\[
r\ge5\Longrightarrow z^+>z.
\]

One forever-defined ordinary path with every run at least five is therefore a complete divergent Collatz certificate.

`T-8003-block-average-highway.md` is also correct. The exact product estimate gives

\[
z_N>z_0\,2^{(9S_N-44N)/53},
\]

and the nine-run resource condition

\[
\sum_{j=0}^{8}r_j\ge44
\]

has multiplier `9^53/2^168>1`. These are implications after ordinary infinite legality; neither claim supplies the path.

### Explicit finite reset family

`L-8003-explicit-reset-highways.md` is sound. The family

\[
z_m=(2^{m+4}-7)/9,
\qquad 6\mid m,
\]

has the advertised exact finite reset, and the LTE calculation for consecutive `B` edges is correct. The theorem is correctly scoped as unbounded finite depth, not one common infinite seed.

### Five-defect cycle theorem

`T-8001-no-five-defect-positive-cycle.md` is verified within its declared computer-assisted finite rows and analytic tail bounds. `X-8003-five-defect-cycle-exclusion/verify.py` independently reconstructs the core necklaces, all-one boundary rows, and one-high determinant table. The exact exactly-five conclusion is also independently subsumed by later work in PR #34; the repository should choose one canonical claim and mark the other as an independent corroboration.

### Two-pulse algebra

`L-8001-negative-cycle-two-pulse-reduction.md` is correct. The reduced correction

\[
R=X(\beta M+\gamma)-\alpha
\]

and the two nonzero eliminants yield valid all-size caps for each fixed repetition/rotation/gap.

## Computational boundary and required fixes

1. `X-8001` contains internal formula checks and exact physical replay but does not have a separately written independent verifier. Its frozen finite counts remain **finite exact evidence, not independently verified by this pass**.
2. The same caution applies to any `X-8002` packet lacking a genuinely separate reconstruction. Add small independent checkers or label those totals accordingly.
3. Mark PR #53 `T-8255` as superseding the finite repetition range of `L-8001/X-8001` for the full two-pulse class, subject to the Matveev source dependency.
4. Mark the exactly-five theorem as either canonical or independently corroborative relative to PR #34; do not maintain two unlabeled active frontiers.
5. Preserve the core gap: no finite `(r_0,r_1,k_0)` is proved to remain defined forever.

## Integration order

PR #51’s exact chart and run-core machine should be integrated before the PR #53 synchronizer claims that cite it for physical replay and the nine-run divergence gate. Its algebraic core does not depend on PR #49.

---

# PR #53 — fixed pulse cones, all-repetition exclusions, and synchronized high blocks

## Verdict: VERIFIED WITH FIXES

The fixed-cone resultant theorem and the one-/two-pulse all-repetition exclusions pass. The primary Matveev normalization is now independently confirmed. The branch is currently not mergeable, and its imported interfaces must be frozen before publication.

## Independently verified load-bearing claims

### Fixed pulse-cone finiteness

`L-8201-fixed-pulse-cone-resultant-caps.md` is correct conditional only on the exact pulse correction imported from PR #47 `L-9602`.

For each pulse variable, the displayed Bézout identity

\[
US_iH-H_i^+D=E_i
\]

proves

\[
D\mid H\iff D\mid E_i.
\]

The term `Qc_i` is the unique term of minimum binary valuation, so

\[
\nu_2(E_i)=A_{p_i+1}
\]

and the eliminant never vanishes. The coordinate cap follows from `D<=|E_i|`. Since a fixed word has finitely many supports, the entire coordinatewise positive pulse cone is finite. The small targeted reconstruction matched the direct numerator and all resultants through four pulse positions.

PR #47’s `L-9602-distributed-pulse-subset-sum.md` supplies the required pulse cocycle and is algebraically consistent with this use. PR #53 should pin the exact PR #47 commit.

### All-repetition single-pulse theorem

`T-8202-all-repetition-single-pulse-exclusion.md` passes, including its external theorem normalization.

The exact divisor reduction forces

\[
0<\Lambda<2c_z/U^r.
\]

The specialization of Matveev Corollary 2.3 used in the proof is correct:

\[
\log|\Lambda|
\ge
-2^{32}\log2\log3\,(1+\log B)
\]

for the stated two-logarithm rational case. The subsequent cutoff, Legendre reduction, certified continued fractions, uniform rejection of primitive upper convergents, and small-case replay are logically complete within the two known negative-cycle families.

`X-8202-single-pulse-log-reduction/verify.py` is genuinely independent of the derivation code and reconstructs the rational log intervals, continued fractions, cutoffs, primitive rows, and exact small hits.

### All-repetition two-pulse theorem

`T-8255-all-repetition-two-pulse-exclusion.md` also passes subject to the same now-verified Matveev source.

The short-gap normalization gives the uniform bound

\[
0<\Lambda
<2c_*3^{\lfloor kr/2\rfloor}/U^r.
\]

The Matveev cutoff, Legendre reduction, seventeen uniform convergent exclusions, exceptional `1/5` argument, and remaining small exact audit cover every rotation, gap, and positive pair of pulse heights in the two declared baseline families. The only hit is the trivial `n=1` cycle.

`X-8255-two-pulse-all-repetition/verify.py` independently rebuilds the entire frozen packet, including exact log intervals and the small all-size scan.

### Synchronized constructive interface

`L-8251`, `L-8252`, and `L-8253` are algebraically sound. They compress the run-core chart into an ordinary high-block map, center at the maximal common prime-to-six residue, and reduce branch legality to an intrinsic valuation plus a fixed 36-bit gate. The growth threshold `s>=44` is exact.

These are finite ordinary transition theorems and a counterexample criterion. They do not prove that any ordinary `X_0` remains defined forever.

## Required pre-public fixes

1. **Update the Matveev source ledger.** `SOURCE_LEDGER_ALL_REPETITION.md` currently says the exact formula was inspected only through a scholarly review. This review checked the primary paper and Corollary 2.3; record that primary-source verification and its exact specialization.
2. **Resolve the branch conflict.** The PR is currently reported non-mergeable. Rebase or resolve conflicts before any publication review is considered complete.
3. **Pin imported SHAs.** `L-8201` depends on PR #47 `L-9602`; `L-8251`–`L-8253` depend on PR #51’s chart and divergence gate. Freeze those exact commits or merge in the dependency order below.
4. Preserve source scopes: `T-8202` and `T-8255` close exactly one- and two-pulse lifts of repetitions of the two known negative cycles. They do not cover growing support or arbitrary baseline cycles.
5. Keep the synchronizer claims separate from existence. Full local branch compilation and pointwise expansion do not give an ordinary infinite path.

## Integration order

Recommended dependency order:

1. PR #47 pulse cocycle (`L-9602`) or a frozen vendored copy;
2. PR #51 ordinary chart/run-core and `T-8003`;
3. PR #53 fixed-cone, all-repetition, and synchronizer packet.

The negative one-/two-pulse theorems could alternatively be split into a standalone packet carrying their exact native reductions and the primary Matveev citation.

---

# Cross-PR connections

## 1. Shared ordinary top-boundary machine

PRs #49 and #51 genuinely share the exact architecture

\[
\rho+2^E\ell
\longmapsto
\sigma+3^A\ell,
\]

with a changing exact dyadic cylinder, odd multiplicative refund, and one ordinary quotient. This is not a proof of existence. The same missing statement remains in both:

\[
\text{one finite ordinary source satisfies every future changing cylinder.}
\]

PR #49 has stronger conditional refund/absorption; PR #51 has the smaller physical chart and sharper run-growth gate. A common theorem must control the **transported low residue**, not merely quotient capacity.

## 2. Fixed-cone caps meet complete-denominator decoders

PR #53 proves that every fixed negative-cycle pulse cone is finite. PR #50 supplies proof-producing complete-denominator decoders and a mixed-place height gate for frozen repair grammars. A useful integration program is:

```text
fixed pulse cone
 -> resultant coordinate caps
 -> exact finite mixed-radix candidate set
 -> directed real quotient window
 -> complete-denominator decoder / physical replay.
```

This is an integration direction, not yet a theorem. Arbitrary pulse heights interact multiplicatively, so PR #50’s binary ordered-delta decoder cannot be applied verbatim without a new mixed-radix normal form.

## 3. Matveev and height forcing are complementary

PR #53’s Matveev arguments bound the repetition axis for one- and two-pulse families. PR #50’s height lemma turns sufficiently complete local divisibility plus a real interval into exact equality. Together they define a proof-producing finite closure architecture once an exhaustive grammar and all omitted prime powers/physical branches are supplied.

---

# Final classification matrix

| PR | Verified core | Fix or block before publication |
|---|---|---|
| #49 | intrinsic core decoder; eight blocks; common top modulus; refund; canonical-run bound; absorption; source-qualified prime turnover | reject/supersede original `T-8512`; rewrite body and inventory around transported residues; pin PR #3 |
| #50 | paired compiler; cyclic transport; ordered decoder; mixed-place forcing; old-target refutation; length-185 theorem; frozen 80-site theorem | renumber duplicate `L-8306`; pin branch imports; maintain finite scopes |
| #51 | exact chart; run-core quotient law; pointwise and nine-run growth gates; reset family; exactly-five theorem; two-pulse algebra | add independent checkers for `X-8001/X-8002` or narrow evidence labels; mark supersessions |
| #53 | fixed-cone finiteness; all-repetition one-/two-pulse exclusions; synchronized ordinary map | update primary Matveev audit; resolve merge conflict; pin PR #47/#51 dependencies |

# SERIOUS RESOLUTION PATH

## Full Collatz conjecture

**No complete serious resolution path is presently established by these four PRs alone.**

The positive-orbit lanes in PRs #49 and #51 still require exactly the object they are intended to construct: one explicit positive ordinary integer whose changing-modulus decoder is defined forever. Refund, stack capacity, local full shifts, and growth are consequences after that existence boundary.

The cycle lanes in PRs #50 and #53 still cover strict grammars or strict pulse families, not all accelerated valuation words. Even complete closure of those families would not exclude nonperiodic divergent orbits.

## Serious cycle-funnel path

There is, however, a serious proof-producing path toward broad **positive-cycle exclusion**:

1. use PR #53 resultants to make each fixed pulse cone finite;
2. use Matveev/continued fractions to bound repetition where possible;
3. compile the remaining finite cones into complete-denominator candidate equations;
4. use PR #50’s ordered or mixed-radix decoder plus the mixed-place height gate;
5. perform independent exact valuation replay on any equality.

The exact missing steps are:

- a uniform repetition theorem for support at least three or support growing with repetition;
- a mixed-radix decoder covering the full bounded pulse cone, not only disjoint binary repairs;
- an exhaustive compiler showing that every possible cycle belongs to one covered cone/grammar.

Until those steps are proved—and until the separate ordinary divergent-orbit lane is closed—this is not a resolution of Collatz.

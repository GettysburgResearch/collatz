# Post-integration review: tail transport, clearance and new ranks

**Disposition: ready for scoped integration preparation, with the two exact checker guards below and a final staged-checkout run still required. No merge into main or source-branch edit is performed by this review.**

The new work supplies real structural progress, not a Collatz solution. I found no load-bearing gap in the 33 numbered theorem arguments at the frozen heads, when their actual hypotheses and conditional conclusions are retained. This is an independent mathematical reconstruction and bounded computational review, not formal verification, a priority survey, or blanket approval of every artifact field. The proposed global completions remain open or explicitly refuted.

## Frozen coverage

| Object | Exact identity / disposition |
|---|---|
| Last scientific/conservation integration | `1ee54e2786c8da7709fa07d66bae2af85a9edb33` (integration #102) |
| Current main used for this preparation | `421d570d6ffb917c9090b9e8ca3c2aa58e26647c` |
| Review cutoff | `2026-09-08T10:00:21Z` / `2026-09-08T13:00:21+03:00`, Asia/Jerusalem; final readback is recorded in the review PR |
| PR #105 | `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`; all three passes, ATT-001–006, ATT-101–105, ATT-201–206; 24 additions |
| PR #106 | `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`; both passes, ALF-001–007 and APR-001–009; 22 additions |
| Already merged non-scientific delta | 17 main commits, seven onboarding/license/document paths, PRs #103/#104/#107/#108/#110/#111/#112/#113. Preserve them, including the owner-selected MIT license. |
| Other published activity | Issue #109 is an integration connection test, not research. The two additional new research-named branch stubs point to already integrated base/document commits, not omitted research packets. |

Search included open and closed PRs/issues updated since the scientific integration, the complete changed-file lists, both source histories and available PR discussions. Eight proof-bearing manuscripts, all ten generator/verifier implementations, source/dependency ledgers and declared experiment contracts were inspected. Supporting author/publication records are preserved as attributed evidence; this review does not convert their reported runs into its own executions. All 46 source additions have destinations in [inventory.json](inventory.json). The branch-name check is not a claim to have audited every historical branch head, deleted ref, attachment or unreachable commit.

**PR-level disposition:** #105 is **VERIFIED WITH FIXES** as a research packet because of F01; #106 is **VERIFIED in the claim-limited mathematical scopes below**, with the listed computation ceilings. Neither verdict verifies a complete selector, a cofinal clearance theorem or Collatz. Individual theorem, refutation and open-target statuses must remain separate.

## Strongest surviving results

**Actual-prefix rank.** The rank

```text
g(d)=d^2/3^v3(|d|), d!=0,
Gamma(n)=min(g(n), 4^k g(T^k(n)-n): k>=1, T^k(n)!=n), n>=2,
Gamma(1)=0
```

has a finite evaluator using at most `floor(log_2 n)` shortcut steps, properness `n<=Gamma(n)<=n^2`, complete `O(sqrt(M) log M)` sublevels, and reciprocal-power summability exactly for exponents greater than 1/2. The rank uses actual prefixes; zero displacements are omitted and its internal T is the raw shortcut map, not a map silently stopped at 1.

The principal all-parameter advance is APR-006: every primitive expanding parity period and every requested finite horizon have explicit ordinary sources whose unique minimizing prefix length is the period length at every phase. The proof handles all competing prefixes, including the unprescribed future. In the old `111010` unsafe family, the same Gamma decreases step by step without requiring the older terminal repayment guard. Sources depend on the requested horizon. This does not produce one infinite positive periodic source or universal coverage of aperiodic inputs.

**Clearance without resetting a distribution.** The forward-closed forest construction charges unknown initial mass once and includes later re-entry rather than pretending every entry has a fresh envelope. I independently reconstructed the three published clearance cutoffs. At `Y=2^32`, there are 163,168 rank-ball sources, 78,828 unsafe roots, 111,763 forest vertices and 32,935 forest vertices outside the starting ball. The root maxima are 52 unsafe returns, 261 shortcut steps and ordinary height 21,206,132,666. Combining this finite certificate with the proved initial tail gives

```text
||H^j(1_U/R_*^2)||_1 <= 12/2^48, for EVERY j>=52.
```

This is a positive residual in a particular weighted ensemble, not natural density or a percentage of Collatz settled. A proved cofinal sequence of successful forests is still missing. The simultaneous theorem `||H^J||_(l1->l1)=1` for every finite J rules out reusing that tiny canonical-output bound as an arbitrary-input contraction factor.

**Linear inverse precision and rank-specific difficulty.** The negative comparison budget now has linear order, `floor(r/3)+2<=B_r<=4r+2`. It yields lossless remaining-depth pruning with at most `4D-2` retained exits. The algorithm is output-sensitive, with a factorial/exponential radius bound, not polynomial in D. A guarded family defeats every lower-P merger in an entire D-by-D box of completed section returns, yet admits a later P repayment and an immediate drop in a different existing rank. Its logarithmic merging cost is family-, rank- and clock-specific. A separate convergent family has compressed algebraic paths to 1; its enormous paths are not represented as literally simulated.

**Expanding-word rank and its exact failure boundary.** Rho minimizes over all formal words with a fixed 5/4 expansion gap, has a finite strict word-length cutoff, and is summable. A legal minimizing word gives a genuine same-rank certificate, and high-precision `111010` phases have exact global minima through arbitrarily long finite windows. But an explicit even exit has a physically illegal unique minimizer and an unbounded successor-rank spike. Arbitrarily long forward delay does not exclude general two-sided merging.

**Critical tails and clock changes.** The old moving rank has sharp ordinary-source tails, fixed-clock critical tails, and an all-mode module-height ceiling. A single unsafe return preserves a fractional output moment under the specified initial envelope, but not a weak first-rank tail. The two escape/cycle-mass identities are correctly separated: both vanishing conditions are needed. None of these results licenses resetting an input envelope after each return.

The full statement-by-statement reconstruction and limitations are in [CLAIM_MATRIX.md](CLAIM_MATRIX.md).

## F01 — typed canonical-payload comparison needs hardening

Two verifiers at PR105's frozen head validate an internally resealed digest and then compare only `report['payload'] == expected`:

| File | Frozen blob |
|---|---|
| `experiments/X-ATT-001-critical-tails/verify.py` | `38588f83e8dd1a234e753bcd8fb8bd3f7d6e6902` |
| `experiments/X-ATT-003-expanding-word-rank/verify.py` | `760b5ade36c9927dfeea96cbbaafac08a99b07de` |

Python equates `True` with `1`, `False` with `0`, and integral floats with equal integers. A corresponding JSON type alteration with a new digest therefore passes the exact original predicate. This is a typed-artifact integrity defect, **not a counterexample to the reconstructed mathematics or an ability to change arbitrary numerical values unnoticed**.

[prepare_checker_fixes.py](prepare_checker_fixes.py) supplies two literal, blob-guarded replacement predicates using canonical JSON text comparison. It checks both frozen source fingerprints before writing either file and never regenerates a canonical artifact. Without `--apply`, it does not modify files. Its isolated tests reproduce four resealed aliases, reject all of them through both exact replacement expressions, and refuse wrong source fingerprints. Both Python modes pass.

The other three verifiers do not share this defect: ATT-002 and APR compare canonical encodings; ALF-001 compares the complete reconstructed envelope, including the expected digest. A newly resealed typed change cannot pass that full-envelope equality. Do not patch them merely because they also contain an equality operator.

**The repair is prepared and tested on isolated predicates, not applied to either research branch.** After importing the exact packets into a candidate integration branch, apply it there, add source-level typed-mutation regression coverage, and replay both actual verifiers. The new code does not inherit a completed full-corpus execution from the old code.

## Global claims that remain outside acceptance

| Candidate conclusion | Disposition |
|---|---|
| Uniform bounded raw weak-first norm; weak-first unsafe output for the stated old-R input; fixed quadratic module rank ceiling | **REJECTED**, with the separately verified ATT counterfamilies retained. Weak-norm failure is not failure of uniform tightness. |
| Repeated fixed-block l1 contraction on arbitrary unsafe input | **REJECTED** by ATT-105; the canonical forest bound remains valid. |
| Every rho minimizer is legal; fixed forward lookahead always finds lower rho | **REJECTED** in the respective ATT-205/206 scopes. General two-sided selectors are not rejected. |
| Naive min(P,C) or max(P,C) monotonicity | **REJECTED** by the simultaneous ALF-006 comparison, not a theorem about every scalar combination. |
| Universal one-step Gamma descent; raw finite-p-moment class invariance; endlessly renewable periodic guard | **REJECTED** in the stated spike/boundary scopes. The moment counterexample constructs an input for each p; it is not automatically the canonical Gamma^-2 input or an induced-return theorem. |
| Both measure defects vanish; cofinal clearance; invariant repeated-return input class; complete lower-rank cover/selector | **GAP-BLOCKED / OPEN**. These are scientific obligations, not defects that must be concealed to publish scoped research. |

## What was actually executed

The independent scripts import no author generator or verifier. `family_checks.py` imports only this review's `review_checks.py`. Normal and optimized outputs agree for each final bounded suite.

- Two actual-prefix evaluators over all 8,191 sources from 2 through 8,192; 4,675 sufficient rotation guards; 40 power-of-three spike tests and the exact 1932103 boundary control.
- Nine complete Gamma rank balls through 65,536, ending with 587 sources and maximum source 59,049; all-prefix minima at all 1,440 phase positions of 64 ordinary family cases; 32 old unsafe edges.
- Complete old-R rank balls and literal clearance forests at 2^24, 2^28 and 2^32, including all outside-ball vertices, clocks and physical peaks; nine unsafe unit-mass shadows through 128 returns.
- Negative comparison cones through radius 10, 1,196 full/pruned minimum comparisons, 12 large ordinary ALF family instances, and four finite modular certificates for the compressed convergent family.
- Rho bounds on 1,023 small sources and exhaustive global minima at 21 large phase positions; 28 fixed-clock tail controls and four exact unsafe spike-family instances.
- Typed-payload regression and exact-replacement fixture tests; no full original source verifier was executed by the repair test.

[validation.json](validation.json) records commands, output fingerprints, counts and exclusions. An optional expanded run timed out before producing a report and was not counted. The final suite uses incremental exponent lifting, explicit word-enumeration limits, and only the written-theorem premises at the enormous rho successor; it does not claim an exhaustive evaluation there.

I did **not** run all five original canonical-envelope protocols, reproduce every author transcript digest, independently check the external background abstracts/priority claims, or execute `tools/validate.py` on a complete authenticated Collatz checkout. The first-packet publishers' reported Windows runs remain attributed to their earlier exact heads. Direct local Git failed at DNS resolution. These limits do not erase the independently reconstructed numerical statements, but they must survive integration.

## Ready handoff

[INTEGRATION_PLAN.md](INTEGRATION_PLAN.md) gives exact extraction units, patch commands, cumulative reading destinations and pre-merge checks. The preparations add only this review directory. Main, scientific statuses, original A/B/D records, author branches, workflows and settings remain unchanged. The source PRs should remain open until an actual integration has preserved their contents and its own candidate-tree checks have passed.

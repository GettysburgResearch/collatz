# Pre-public frozen review of PRs #44, #45, #47, and #48

**Reviewer:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Review type:** independent frozen-head reconstruction  
**Status:** final verdicts for the commits listed below; no source PR is merged or silently promoted

## Frozen commits

| PR | Frozen head reviewed |
|---:|:---|
| #44 | `efafd32b0d99c4d02adda19c7d932bcb0e3f05fd` |
| #45 | `a7846473b10aa5caf8c9c57b0a612db0b8db402a` |
| #47 | `42f7c9076e0c48608ab1eeec67150fe60ea60126` |
| #48 | `738b230c22d6475095945998ca89662714973d72` |

All conclusions below refer only to these commits. No GitHub Actions workflow was
attached to any of the four heads. I inspected the load-bearing proofs,
implementations, frozen artifacts, and independent-verifier architecture. I did
not rerun the billion-pair `X-9615` computation or any other expensive census.
Small formulas and finite interfaces were reconstructed directly.

## Verdict matrix

| PR | Verdict | Publication consequence |
|---:|:---|:---|
| #44 | **VERIFIED** | Mathematically ready within its frozen scopes; preserve stacking and source-status notes. |
| #45 | **VERIFIED WITH FIXES** | Core chart and computer-assisted cycle theorem pass; repair one Diophantine proof sentence, notation, and one reachability scope statement before publication. |
| #47 | **GAP/BLOCKED** | Several major subchains pass, but the PR cannot be integrated as frozen because live claim IDs collide and the largest artifact-dependent theorem was code-inspected, not independently replayed in this pass. |
| #48 | **VERIFIED WITH FIXES** | Main refund/firewall/transport repairs pass; narrow the scope of its inherited PR reviews and keep source-qualified consequences explicit. |

No assigned PR is rejected. `GAP/BLOCKED` for PR #47 is an integration and
artifact-verification verdict, not a claim that every mathematical result in
that PR is false.

# PR #44 — VERIFIED

## Native centered-PDR chain

The following files pass independent reconstruction:

```text
research/centered-pdr/claims/D-8701-centered-forced-tail-system.md
research/centered-pdr/claims/L-8701-monotonicity-invariant-carry.md
research/centered-pdr/claims/T-8701-fixed-precision-pdr-kernel.md
research/centered-pdr/claims/R-8701-fixed-modulus-pdr-ghosts.md
```

### `D-8701`

The forced-tail recurrence

\[
64B'=81B+e-e'
\]

and the four legal source residues are correct. The base-64 carry bound follows
from `81=64+17` with the declared offsets.

### `L-8701`

The invariant

\[
B+4e\pmod {17}
\]

and strict growth `B'>B` for every positive legal state are algebraically
correct. The post-initial carry range `{0,...,17}` is closed under the stated
transducer.

### `T-8701`

At precision `64^d`, the greatest existential infinite-path kernel is exactly
the set of binary itinerary cylinders and its edges are the de Bruijn
shift-and-append edges. Both inclusions are proved:

1. every binary control word gives one exact residue;
2. every state surviving indefinitely fixes the first `d+1` control bits and
   hence lies in one such cylinder.

This is an exact theorem about the declared existential abstraction. It does
not assert ordinary top-boundary closure.

### `R-8701`

The periodic-control fixed-point calculation is correct. Every nonconstant
periodic control selects a nonintegral rational `2`-adic completion, while the
two constant controls select the trivial integer zero. Thus fixed-modulus
lassos are completion ghosts, not ordinary positive witnesses.

## Computational packet

```text
experiments/X-8701-centered-pdr/build.py
experiments/X-8701-centered-pdr/verify.py
experiments/X-8701-centered-pdr/results/canonical.json
```

The verifier is independently structured and does not import the generator. It
reconstructs the graph kernel, cylinder residues, de Bruijn edges, periodic
ghosts, carry cases, invariant, and finite scan with exact integer arithmetic.
No floating-point proof decision is present.

## Embedded independent audit of PR #33

The frozen report

```text
reports/gpt56-pdr-01/2026-07-22-40-pr33-evertse-adversarial-review.md
```

correctly separates its own scope from the centered-PDR theorem. Its
reconstruction of the frozen PR #33 chain passes:

```text
L-9702 canonical cap
L-9703 / T-9704 completion-height bound
L-9704 connector-free coordinate
L-9705 signed cap/co-cap quotient dichotomy
L-9706 Evertse admissibility
T-9705 full frozen-stage ordinary exclusion
```

The primitive-tuple, fixed-coordinate-number, no-proper-subsum,
outside-`{2,3}` height, and `d<1` hypotheses match Corollary 1 of Evertse's
1984 paper. `X-8702` is an independent finite interface audit; the universal
conclusion comes from the proof, not from sampled connectors.

## Nonblocking integration notes

1. PR #44 is stacked on the centered recurrence branch. Preserve the exact
   frozen dependency or rebase only after the canonical PR #16 / PR #37
   recurrence files are settled.
2. In `T-8701`, use “quotient residue” when discussing the fixed-precision
   target; the abstraction existentially forgets higher quotient blocks.
3. The PR #33 review does not itself merge or promote PR #33. Keep its frozen
   source SHA and external-theorem dependency visible.

These are publication notes, not mathematical failures.

# PR #45 — VERIFIED WITH FIXES

## Claims independently passed

The following symbolic interfaces are correct within their declared scopes:

```text
L-8401 critical cycle product
L-8402 block replacement and rotation
L-8403 mechanical/Christoffel monoid compiler
L-8404 block/carry decoder
L-8405 negative-three fixed-weight collision fiber
L-8406 six-branch quotient-refund law
L-8407 intrinsic phase-core and top-boundary law
T-8403 forever-defined-state counterexample implication
T-8404 ordinary code complexity floor
T-8405 no eventual C-finite top boundary
```

The exact concatenation signs, cylinder moduli, quotient updates, intrinsic
`2`/`3`/`7` signatures, and positivity arguments were reconstructed. In
particular, `T-8403` is only a conditional implication: it supplies no
forever-defined finite state.

## `T-8401` computer-assisted theorem

```text
research/smooth-cycle-synthesis/claims/T-8401-no-positive-cycle-through-50000.md
experiments/X-8402-minimum-cycle-decoder/run.cpp
experiments/X-8402-minimum-cycle-decoder/verify.cpp
```

The theorem wrapper is sound. The program uses exact integer product
comparisons, starts from the verified lower-state floor, traverses every
`7<=n<=N_*`, and performs direct shortcut/accelerated replay. The verifier is
independently structured and its integer widths are sufficient for the frozen
range. I did not rerun the complete census in this pass.

Verdict for the frozen theorem: **VERIFIED as a computer-assisted finite
exclusion**, conditional on preserving the imported verified lower bound and
the frozen artifact.

## Required fixes

### 1. `T-8402` one-sided approximation proof

File:

```text
research/smooth-cycle-synthesis/claims/T-8402-near-critical-pulse-fiber-counterexample.md
```

The theorem that infinitely many pairs satisfy

\[
0<\theta L-b<1/L
\]

is true, but the current sentence attributes the one-sided conclusion directly
to a pigeonhole argument on fractional parts. Pigeonhole gives a two-sided
Dirichlet approximation. Replace this paragraph by the standard continued-
fraction argument: infinitely many lower convergents `b/L<theta` satisfy
`0<theta L-b<1/L`.

This is a proof repair, not a new theorem and not a reason to reject the
near-critical construction.

### 2. `L-8404` notation

The file reuses `A_j` for different roles near the block-decoder formulas.
Rename the carried affine target or the prefix valuation so the proof cannot be
misread. The algebra itself passes.

### 3. `L-8407` cell scope

The intrinsic cells exactly encode the current binary domain, ternary phase,
seven-section, and prime-to-six core. Publication should not call them the
complete reachable-history partition unless the earlier-history congruence is
also retained. Recommended wording:

```text
exact cells for the current intrinsic signatures;
full physical reachability still requires the preceding exact path.
```

This does not affect the forward decoder or `T-8403`.

## Merge order

1. Apply the three fixes above on PR #45.
2. Land the exact chart/quotient files before downstream review and extraction
   packets that cite them.
3. Keep `T-8401` visibly computer-assisted and separate from the open ordinary
   extraction target `Q-8403`.
4. PR #48's old review of PR #45 covers only an earlier frozen subset; it must
   not be cited as review of this current head.

# PR #47 — GAP/BLOCKED

## Verified mathematical subchains

No counterexample was found to the following frozen claims:

```text
R-9601 ordinary-extraction quantifier boundary
L-9601 one-pulse negative-cycle reduction
L-9602 distributed-pulse correction
L-9606 Christoffel/Farey commutator
T-9606 rational mechanical cycle exclusion
L-9607 equal-summary geometric-factor sieve
T-9607 aligned Christoffel-mixture exclusion
L-9609 cycle-minimum target sieve
L-9610 terminal residue at a cycle minimum
L-9611 two-sided source/output phase floor
```

Both narrow-library carry theorems presently named `L-9608` are also
mathematically correct:

```text
L-9608-equal-summary-narrow-library-rigidity.md
    sharp width W<Q+P;

L-9608-narrow-equal-summary-zero-carry-collapse.md
    stronger statewise conclusion under W<Q.
```

They are distinct theorems, not duplicate formulations.

The fixed-weight cycle exclusions built from the phase floor are logically
all-repetition results rather than finite-period extrapolations: a finite
past/future phase table gives a universal ordinary boundary floor, and the
cycle-minimum inequality supplies the global upper bound.

## Computational interfaces

### `X-9614` depth 10

The generator uses closed affine formulas; the verifier reconstructs source
cylinders by iterative local lifting. It independently checks all `4^d` phase
pairs for `d=5,8,10`, exact parameter signs through `a=243`, monotone endpoint
compression, and the first failure of the depth-10 inequality at `a=244`.
The architecture and integer arithmetic are sound.

### `X-9615` depth 15

The C++ generator and verifier use genuinely different phase constructions:
closed affine constants versus iterative cylinder lifting. `u64`, `u128`, and
`cpp_int` are used in ranges that avoid overflow. Both programs exhaust
`4^15=1,073,741,824` phase pairs and check the parameter margins through
`a=375`.

I inspected both implementations and the frozen artifact contract but did not
rerun this billion-pair computation. There is no Actions record for the frozen
head. Therefore:

```text
L-9611 theorem wrapper: VERIFIED;
T-9610 / X-9614: VERIFIED by code and artifact inspection;
T-9611 / X-9615: GAP/BLOCKED pending an independent full replay,
                 trusted signed artifact provenance, or CI execution.
```

The duplicated parameter-check routine in the two C++ programs gives less
implementation independence than the phase-table computation, although the
parameter inequalities themselves are elementary exact `cpp_int` signs.

## Publication-blocking namespace defects

The frozen branch contains two live claims named `L-9608`:

```text
research/integer-first-offense/claims/
  L-9608-equal-summary-narrow-library-rigidity.md
  L-9608-narrow-equal-summary-zero-carry-collapse.md
```

and two live claims named `T-9608`:

```text
research/integer-first-offense/claims/
  T-9608-1024-block-mechanical-full-shift-exclusion.md
  T-9608-negative-three-pulse-phase-transition.md
```

The first `T-9608` file also says “1024” in its filename while its theorem and
artifact concern `2^11=2048` block variants.

Because downstream dependency lines cite only `L-9608` or `T-9608`, the frozen
dependency graph is non-unique. This is a hard pre-public integration blocker.

## Required repair

1. Assign new unique IDs to one member of each colliding pair.
2. Rename the `1024` filename/title to `2048` consistently.
3. Add an explicit old-file to new-ID migration table.
4. Rewrite every downstream dependency to identify one exact theorem.
5. Separate the symbolic theorem layer from the artifact-dependent `T-9610`
   and `T-9611` layer in the review ledger.
6. Obtain an independent `X-9615` replay or CI artifact before promoting
   `T-9611` beyond proposed computer-assisted status.

Earlier symbolic claims listed above remain **VERIFIED**; this repair cannot be
used to retroactively verify a colliding or unreplayed claim.

## Merge order

PR #47 should not merge in its frozen state. After namespace repair:

1. depend on a canonical frozen derivation of the physical `A/B` letters from
   PR #45 / PR #51;
2. merge symbolic Christoffel and equal-summary theorems;
3. merge `X-9614/T-9610` with its finite certificate;
4. merge `X-9615/T-9611` only after independent artifact replay.

# PR #48 — VERIFIED WITH FIXES

## Claims independently passed

The following claims pass within their stated conditional scopes:

```text
L-8201 linear-height two-stage quotient growth
L-8202 stage-word residue sparsity
L-8203 common changing-modulus quotient law
L-8204 run-highway refund cone
T-8201 intrinsic top-lift doubling
R-8201 ordinary-cylinder firewall
R-8203 refutation of the plain future-stack interpretation
L-8210 inverse-affine transported future-cylinder stack
```

The key correction is exact:

```text
plain Euclidean mixed-radix digits != future legality residues;
transported inverse-affine residues Theta_s = true future cylinders.
```

`L-8210` correctly derives

\[
K_s\ell_s=P_s\ell_0+B_s,
\qquad
\Theta_s=[-P_s^{-1}B_s]_{K_s},
\]

its nested transported digits, carry update, and ordinary stabilization
criterion. The growth/refund theorems are explicitly conditional on one
coherent ordinary path and do not claim existence.

## External source-qualified claim

File:

```text
research/refund-review/claims/R-8202-eventually-affine-run-tschakaloff-exclusion.md
```

The `q`-difference specialization was reconstructed against Amou,
Matala-aho, and Väänänen (2007), Theorem 5.1. The functional equation,
finite-place parameter

\[
\lambda=-\frac23\log_2 3,
\]

choice `delta=1/2`, quadratic for `rho_0`, and interval
`-beta<lambda<=-1` are consistent with the source. The conclusion that every
eventually positive-slope affine run schedule has irrational initial core is
therefore **VERIFIED, SOURCE-QUALIFIED**.

## Required fixes

### 1. Scope the inherited PR #45 review

PR #48's review matrix passes only the earlier frozen `L-8401`--`L-8403`,
`O-8401`, and `X-8401` subset. It must not say or imply that the current PR #45
head was reviewed. Add the exact reviewed PR #45 SHA and claim list anywhere
that verdict is quoted.

### 2. Preserve the refutation/repair boundary

`R-8203` refutes the future-stack interpretation of the original PR #49
`T-8512`. `L-8210` is a new repaired theorem. It cannot retroactively upgrade
the original false interpretation to verified status. Preserve both IDs and
the historical narrowing.

### 3. Keep quantitative corollaries branch-qualified

Section 6 of `L-8210` imports numerical capacity estimates from the frozen
PR #49 `T-8512`. The transported-cocycle theorem is general; the stated
`1/288` and `1/233` rates are not. Label those rates with the frozen source
commit and retain the one-level loss.

### 4. External citation

Keep the full bibliographic reference and exact Theorem 5.1 parameter mapping
inside `R-8202`; do not reduce it to an uncited “Tschakaloff theorem.”

## Merge order

PR #48 is best merged as a review/narrowing packet after, or alongside exact
frozen references to, the PR #49 and PR #51 source machines. It should precede
any public claim that their raw radix capacity is a legality stack. It does not
replace independent review of the current PR #45 head.

# Connections missed by the source PRs

## 1. Fixed PDR and transported cylinders are the same boundary at two scales

PR #44 proves that every fixed dyadic precision retains the full binary
completion shift. PR #48 proves that true future legality is obtained only by
pulling each cylinder through all intervening odd affine maps. Together they
show:

```text
fixed low-bit safety is necessarily completion-rich;
ordinary exclusion must be a moving transported-residue or height theorem.
```

This explains why a larger finite PDR kernel cannot by itself settle ordinary
extraction.

## 2. The PR #47 phase floor is the stationary case of PR #48 transport

PR #47's past-output phase and future-source phase are precisely the two
congruences obtained by composing an odd-affine past block and the transported
future cylinder. Their CRT combination gives an ordinary boundary floor.

This connection is preserved separately as new `L-6916`, **PROPOSED pending
review**. It does not alter any verdict above.

## 3. PR #45 is the smallest stationary test bed for the repaired stack

The six-branch chart has fixed radix `2^19` and odd multiplier `3^12`. Its true
length-`s` initial cylinder is the stationary specialization

\[
\Theta_s=[-P^{-s}C_s]_{Q^s},
\]

not a free branch tape or a plain radix expansion. PR #44 predicts that every
fixed projection remains completion-rich; PR #47 suggests that a useful
negative theorem must combine transported source phases with output phases and
an Archimedean ceiling.

# SERIOUS RESOLUTION PATH

**Present as a serious, exact research program; not present as a nearly
complete proof.**

The four reviews identify a coherent route that is stronger than further
finite-prefix grinding:

1. **Ordinary source escape.** Express the source cylinders of the
   coefficient-supercritical language by the inverse-affine transported
   residues of PR #48, not by fixed PDR states. Prove that their least positive
   representatives tend to infinity. PR #44 shows why fixed precision cannot
   supply this theorem; new `L-6916` gives the exact past/future phase-floor
   compiler that may supply an Archimedean lower bound.
2. **Complete first-crossing/full-denominator exclusion.** Use the full
   denominator and exact source/endpoint pair, retaining the cycle level.
   PR #47's two-sided phase method supplies genuine all-repetition lower bounds
   in fixed-weight families; the current PR #81 / PR #83 compiler reduces the
   unrestricted case to complete-factor synchronization.
3. **Uniformity, not depth.** The missing theorem is a parameter-uniform lower
   bound for transported two-sided phase floors or complete-factor quotient
   jets. Merely increasing `d` in PR #47 or precision in PR #44 extends a
   finite theorem frontier but does not yield the required cofinal statement.
4. **Exact final obligations.** In current repository notation these remain
   `SC*`—least ordinary source escape—and `FC*`—no nontrivial complete
   first-crossing tuple with common `0<=d<q/3`, including `d=0` cycles.

Proving both would resolve Collatz. Neither is proved by these four PRs or by
this review.

# Final publication recommendation

```text
PR #44:
  may proceed within its stacked/frozen scope;

PR #45:
  apply the three local fixes, then proceed;

PR #47:
  do not publish or merge at the frozen head;
  repair namespaces and independently replay X-9615 first;

PR #48:
  apply scope/citation/history fixes, then proceed as a review/repair packet.
```

No public README change and no merge is performed by this review.

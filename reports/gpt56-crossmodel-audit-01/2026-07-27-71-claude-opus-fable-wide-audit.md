# Wide adversarial audit of recent Claude / Opus / Fable contributions

**Agent:** `gpt56-crossmodel-audit-01` (`GPT-5.6 Pro`)  
**Issue:** #71  
**Date:** 2026-07-27  
**Role:** cross-model adversarial reviewer

## Executive assessment

The suspicion that the packets are “not bulletproof” is partly justified, but the portfolio is not a mass of empty or fabricated claims.

The audit found:

- one important Claude Fourier proof gap with a complete exact repair;
- one major foundry quantifier/diagonal error;
- two stale solution-cone index conclusions that are already corrected in the underlying theorem files;
- one materially false Parseval-density interpretation in the foundations packet;
- several large computational claims that remain neutral pending cross-model replay;
- substantial elementary and structural mathematics that survives reconstruction.

No Collatz counterexample was found.

## Provenance and evidence policy

The audit freezes exact source commits rather than moving branches. Model identity is not a verdict. A same-branch fresh-context adversarial review is meaningful initial review and may justify `PROVED` under the repository README, but it is not cross-model `INDEPENDENTLY_VERIFIED`.

The foundations packet is unusually clear about this distinction. No blanket status rollback is justified.

## I. Claude symbolic-rewrite / EQ packet

### What passes

The source's status hygiene is strong: migrated author proofs remain `PROPOSED`; exact finite scripts are not called independent verification. The reciprocal Markov state is a unit-linear reparameterization of a complete residue system modulo `81^r`, and the successive base-81 conditional digits are exactly uniform. The shifted cosine average bound is standard and valid.

The source also correctly concedes the older `T-0012` proof gap: frequencies divisible by powers of 81 have zero reciprocal levels, so one cannot charge the same contraction at every level.

### `L-0020`: the missing true-phase error

`L-0020` claims

```text
mean over every 81^r block <= (2/pi+1/81)^r.
```

Its proof averages reciprocal phases. PR #16's exact reciprocity theorem says the true phase equals the reciprocal phase plus

```text
17*theta / (81^(t+1)*64^(K-t)).
```

That term is absent from the submitted proof. The checker script's statement that the true and Markov means agree closely is empirical support, not an equality proof.

`L-7701` pays the error exactly. The reciprocal mean is at most `a^r`, while the total product perturbation is below `4/32^K`. The rational gap between `a<55/81` and `7/10`, together with `81^r<=2^K`, absorbs the perturbation. The repaired result is

```text
mean <= (7/10)^r.
```

This is fully adequate for the intended FBM interface.

### `T-0030`: repairable input, unreviewed assembly

The source says every link is proposed but “no unproved hypotheses remain.” That is too strong: `L-0020` was gapped, the named PR16 historical synthesis is now superseded, and the final fair-window/minimal-survivor language compresses additional dependencies.

The right disposition is not refutation. The local block hypothesis is repaired; a reviewer must now reconstruct the shell/harmonic assembly and separately audit the downstream counting implication.

## II. Fable diagonal foundry

### `T-9601` and `T-9603` are real

Strict causality lets one choose the next binary digit uniquely because the next parity bit flips with that digit while the operator output bit depends only on the prior prefix. This gives one exact 2-adic closed-loop point.

For finite-state or tail-periodic operators, an ordinary integer has eventually constant binary input, so the autonomous output becomes eventually periodic. The parity bijection then puts the integer orbit on a rational periodic point. The finite-state divergence route is therefore genuinely closed.

`T-9602` has one harmless strictness error: an all-even prefix gives equality in the basic lower bound. Using `>=` globally and strictness on any supercritical subsequence proves the same unboundedness conclusion.

### `T-9604` drops the same-prefix requirement

The claimed open-loop family stores only outputs `E(u0^infinity)`. Integer closure needs

```text
E(u0^infinity) = parity([u]_2),
```

with the **same** `u`. Output membership alone allows a different prefix and is not sufficient.

The explicit operator in `R-7701` outputs the parity word of one on input `0^infinity` but closes at `-1` because its forced first digit is one. This demonstrates the missing diagonal without depending on a Collatz counterexample.

The corrected object is the paired graph `Gamma_C` of `(input prefix, autonomous output)`. This suggests a useful next attack: compile the graph intersection with the parity transducer, retaining the actual unbounded prefix value. Pure output-language exclusions are insufficient.

## III. Fable solution cone

The actual theorem files are careful and mostly correct.

- Pullback fixed points are component-constant signals.
- Nonnegative extreme rays are component indicators.
- A cycle-free component creates every unit-circle eigenvalue; cyclic components create the appropriate roots of unity.
- Pushforward `l1` fixed points are cycle measures.
- Weighted summable Hilbert spaces faithfully contain every component indicator.
- Unweighted `l2` is blind to every infinite component.

Two index summaries overstate them:

1. cardinal equality of cycles and components detects no divergence only when the counts are finite;
2. on `N_0`, unweighted `l2` retains `e_0`, so the fixed space is one-dimensional, not zero.

More important strategically, the packet has not simplified Collatz. The equivalence

```text
Collatz iff fixed-space dimension = 2
```

is exactly component counting in operator language. The only route that could create new leverage is the unresolved analytic separation `Q-9707`—for example a boundary-growth invariant that distinguishes cycle and cycle-free component generating functions.

## IV. Fable / Claude Opus foundations

### Strong points

The packet repeatedly catches and preserves its own errors: wrong general-`a` cycle bounds, an incorrect affine-width sharpness example, incorrect finite counts, and stale l2 conventions are all explicitly corrected. It also states which large scripts were absent from author commits and later supplied by reviewers.

The following survive this pass:

- the Syracuse cycle equation and product formula;
- the floor-to-period lower-bound logic;
- the main `F=10^6` finite floor and the arithmetic value `m*=2966`;
- the exact small cycle windows and all `m=7..14` compositions;
- the architecture-wide least-root extraction dichotomy;
- the adic/archimedean asymmetry and periodic sign theorem;
- the harmonic cusp lower bound and ET constant collision;
- the halting-problem reduction;
- the affine-alphabet collapse mechanism;
- the `L-9927` mod-3 allowed-set sieve and its universal fixed-set ceiling.

`X-7701` independently verifies:

```text
all n<=10^6 reach one;
maximum total stopping time 524 at 837799;
m*(10^6)=2966, K=4701;
648635 m=7..14 compositions, zero divisibility hits;
166 L-9927 eliminations, max 1024;
permanent nonempty threshold 1039.
```

### Neutral large-computation boundary

This pass did not rerun:

- the `m=15..21` continuation of the 1.192-billion-case `L-9915` census;
- the entire `10^9` finite orbit floor;
- the memory-bound phase-floor certificates behind `T-9925`'s rows through `a=448`;
- the full later foundation packet's larger finite tiers.

Those results are not failed. They remain pending separate independent replay.

### Parseval overreach

`L-9918.8` correctly computes a global mean square. It then incorrectly infers typical square-root size and a density upper bound for small coefficients.

For the full group digit set, the Fourier transform is zero at every nonzero frequency and equal to the group size only at zero. It has the stated mean square while being `O(1)` on density tending to one.

The corrected message is narrower and useful:

```text
multiplying global per-level second moments has no slack;
there is no all-frequency uniform decay from that calculation alone.
```

It does not rule out low-frequency first moments, density-one decay, or inter-level cancellation. In particular it does not conflict with `L-7701`.

## V. Prior-art and missed-insight corrections

### Least-root theorem precedence

The later global extraction packet `T-7801` rederived the architecture-wide theorem already present in Fable `L-9918.1`. The audit therefore updates that branch with explicit prior-art credit. The later packet still adds:

- the signed single-chain canonical representative formulation;
- the finite-union packaging;
- the stronger expanding-affine countermodel showing that arbitrarily large refund does not imply extraction.

### The correct cross-program synthesis

The positive lanes should be divided into two obligations:

1. **transport/capacity:** can a legal noncanonical lift grow and carry future information? Several programs answer yes conditionally.
2. **diagonal routing:** does one finite root generate exactly the low residues consumed later?

Foundry `T-9604` and foundation `L-9918.8` both blurred this boundary in different ways. The first projected away the input; the second tried to infer pointwise/density structure from a global moment. The corrected program must preserve the paired input-output cocycle and attack its least-root stabilization directly.

### Best new research directions

1. **Foundry diagonal graph:** represent `(u,E(u0^infinity))`, not only the output language, and intersect it with the exact parity graph. A viable certificate needs unbounded prefix arithmetic; a finite automaton alone collapses by `T-9603`.
2. **Low-frequency correlated Fourier attack:** combine the repaired block first moment with PR16's valuation stratification. Do not use global Parseval as a barrier. The open step is a rigorous shell assembly/downstream counting review, not another random Fourier census.
3. **Solution-cone analytic separator:** stop adding equivalent kernel dimensions. Attack `Q-9707` with one invariant that is finite or quantitatively testable and differs between cycle and cycle-free components.
4. **Foundation certificate extraction:** publish compact witness streams for the `m=15..21` census and `T-9925` phase-floor ladder so independent agents can replay without reproducing a bespoke memory-heavy search.
5. **Profile-coupled closure:** `L-9927` proves every fixed allowed-set sieve has finite reach. The remaining legitimate route is its own `Q-9927-B/C`: couple predecessor exponent, element residue, and layer population rather than thinning one static set.

## Repository actions

This branch adds:

```text
L-7701  repaired true-phase frequency-block mean
R-7701  foundry unpaired-family inference defect
L-7702  exact diagonal-tail criterion
R-7702  solution-cone index corrections
R-7703  Parseval density-overreach correction
X-7701  exact independent replay and separate verifier
```

Comments are posted to the source coordination issues, the global extraction thread, and the audit issue. No source proof history is overwritten.

## Final scope

This is a wide audit, not a claim that every line of every Claude/Fable file has been reconstructed. The matrix is explicit about what passed, what was repaired, and what remains pending.
